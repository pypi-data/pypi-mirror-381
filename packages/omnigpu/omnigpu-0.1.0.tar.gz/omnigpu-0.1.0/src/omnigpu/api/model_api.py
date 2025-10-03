"""Model operations API."""
import torch
import torch.nn as nn
from typing import Optional, Union, Callable, Dict, Any, List
import warnings
import logging

from ..core.device_manager import get_device_manager
from ..core.memory_manager import get_memory_manager
from ..core.precision_manager import get_precision_manager
from ..core.error_handler import get_error_handler

logger = logging.getLogger(__name__)


def load_model(model_path_or_callable: Union[str, Callable], 
               device: Optional[str] = None) -> torch.nn.Module:
    """Load model and place on optimal device.
    
    Args:
        model_path_or_callable: Path to model or model constructor
        device: Target device (default: auto_device())
        
    Returns:
        torch.nn.Module: Loaded model on target device
    """
    device_manager = get_device_manager()
    error_handler = get_error_handler()
    
    if device is None:
        device = device_manager.select_best_device()
    else:
        device = torch.device(device)
        
    @error_handler.safe_operation(operation_name='load_model')
    def _load():
        if isinstance(model_path_or_callable, str):
            # Load from file
            if model_path_or_callable in ['resnet18', 'resnet50', 'vgg16']:
                # Handle torchvision models
                import torchvision.models as models
                model_fn = getattr(models, model_path_or_callable)
                model = model_fn(pretrained=False)
            else:
                # Load custom model
                model = torch.load(model_path_or_callable, map_location='cpu')
                
        elif callable(model_path_or_callable):
            # Call constructor
            model = model_path_or_callable()
        else:
            raise ValueError(f"Invalid model input: {type(model_path_or_callable)}")
            
        # Move to device
        model = model.to(device)
        logger.info(f"Loaded model on {device}")
        
        return model
        
    return _load()


def save_model(model: torch.nn.Module, path: str) -> None:
    """Save model with device-agnostic format.
    
    Args:
        model: Model to save
        path: Save path
    """
    error_handler = get_error_handler()
    
    @error_handler.safe_operation(operation_name='save_model')
    def _save():
        # Move to CPU for saving to ensure compatibility
        cpu_state = model.cpu().state_dict()
        
        # Save with metadata
        save_dict = {
            'state_dict': cpu_state,
            'model_class': model.__class__.__name__,
            'omnigpu_version': '0.1'
        }
        
        torch.save(save_dict, path)
        logger.info(f"Saved model to {path}")
        
    _save()


def optimize_model(model: torch.nn.Module, 
                  optimization_level: str = 'auto') -> torch.nn.Module:
    """Apply device-specific optimizations.
    
    Args:
        model: Model to optimize
        optimization_level: 'auto', 'aggressive', 'conservative'
        
    Returns:
        torch.nn.Module: Optimized model
    """
    device = next(model.parameters()).device
    device_type = str(device).split(':')[0]
    
    if optimization_level == 'auto':
        # Auto-detect based on device
        if device_type == 'cuda':
            optimization_level = 'aggressive'
        else:
            optimization_level = 'conservative'
            
    logger.info(f"Optimizing model with level: {optimization_level}")
    
    if optimization_level == 'aggressive':
        # Apply aggressive optimizations
        if device_type == 'cuda':
            # Enable cudnn benchmarking
            torch.backends.cudnn.benchmark = True
            
            # Try to compile model if available (PyTorch 2.0+)
            if hasattr(torch, 'compile'):
                try:
                    model = torch.compile(model, mode='max-autotune')
                    logger.info("Applied torch.compile optimization")
                except Exception as e:
                    logger.warning(f"torch.compile failed: {e}")
                    
        # Apply memory format optimization
        if hasattr(model, 'to'):
            try:
                model = model.to(memory_format=torch.channels_last)
                logger.info("Applied channels_last memory format")
            except:
                pass
                
    elif optimization_level == 'conservative':
        # Conservative optimizations
        if device_type == 'cuda':
            torch.backends.cudnn.benchmark = False
            torch.backends.cudnn.deterministic = True
            
    # Optimize memory layout
    memory_manager = get_memory_manager()
    for name, param in model.named_parameters():
        if not param.is_contiguous():
            param.data = param.data.contiguous()
            
    return model


def wrap_model(model: torch.nn.Module) -> torch.nn.Module:
    """Wrap existing model with universal GPU capabilities.
    
    Args:
        model: Existing PyTorch model
        
    Returns:
        torch.nn.Module: Wrapped model with ugpu features
    """
    
    class UniversalGPUWrapper(nn.Module):
        """Wrapper that adds universal GPU capabilities to models."""
        
        def __init__(self, wrapped_model):
            super().__init__()
            self.wrapped_model = wrapped_model
            self.device_manager = get_device_manager()
            self.error_handler = get_error_handler()
            self.precision_manager = get_precision_manager()
            
        def forward(self, *args, **kwargs):
            # Ensure inputs are on same device as model
            device = next(self.parameters()).device
            
            def move_to_device(x):
                if isinstance(x, torch.Tensor):
                    # Handle precision compatibility
                    x = self.precision_manager.auto_convert_precision(x, str(device))
                    return x.to(device)
                elif isinstance(x, (list, tuple)):
                    return type(x)(move_to_device(item) for item in x)
                elif isinstance(x, dict):
                    return {k: move_to_device(v) for k, v in x.items()}
                return x
                
            args = move_to_device(args)
            kwargs = move_to_device(kwargs)
            
            # Forward with error handling
            @self.error_handler.safe_operation(operation_name='model_forward')
            def _forward():
                return self.wrapped_model(*args, **kwargs)
                
            return _forward()
            
        def to(self, *args, **kwargs):
            """Override to() to handle device moves safely."""
            # Let parent handle the move
            result = super().to(*args, **kwargs)
            
            # Extract device if provided
            device = None
            for arg in args:
                if isinstance(arg, (str, torch.device)):
                    device = str(arg)
                    break
                    
            if device:
                # Check device compatibility
                available = self.device_manager.available_devices()
                if not any(device.startswith(d.split(':')[0]) for d in available):
                    warnings.warn(f"Device {device} may not be available, model may fallback")
                    
            return result
            
        def cuda(self, device=None):
            """Override cuda() to handle non-CUDA systems."""
            if not torch.cuda.is_available():
                # Fallback to best available device
                device = self.device_manager.select_best_device()
                warnings.warn(f"CUDA not available, using {device}")
                return self.to(device)
            return super().cuda(device)
            
        def __getattr__(self, name):
            """Delegate attribute access to wrapped model."""
            try:
                return super().__getattr__(name)
            except AttributeError:
                return getattr(self.wrapped_model, name)
                
    # Create wrapped model
    wrapped = UniversalGPUWrapper(model)
    
    # Copy model's device
    if next(model.parameters(), None) is not None:
        wrapped = wrapped.to(next(model.parameters()).device)
        
    logger.info(f"Wrapped model with universal GPU capabilities")
    
    return wrapped


def distribute_model(model: torch.nn.Module, 
                    strategy: str = 'auto',
                    devices: Optional[List[str]] = None) -> torch.nn.Module:
    """Distribute model across multiple devices.
    
    Args:
        model: PyTorch model to distribute
        strategy: Distribution strategy ('auto', 'data_parallel')
        devices: List of devices to use (default: all available GPUs)
        
    Returns:
        Distributed model
    """
    device_manager = get_device_manager()
    
    if devices is None:
        # Get all GPU devices
        all_devices = device_manager.available_devices()
        devices = [d for d in all_devices if d.startswith(('cuda', 'mps'))]
        
    if len(devices) <= 1:
        warnings.warn("Not enough devices for distribution, returning original model")
        return model
        
    if strategy == 'auto':
        # Auto-select strategy based on devices
        if all(d.startswith('cuda') for d in devices):
            strategy = 'data_parallel'
        else:
            warnings.warn("Mixed device types not fully supported for distribution")
            return model
            
    logger.info(f"Distributing model across {devices} with strategy: {strategy}")
    
    if strategy == 'data_parallel':
        # Use DataParallel for CUDA devices
        device_ids = [int(d.split(':')[1]) if ':' in d else 0 for d in devices]
        model = model.cuda(device_ids[0])
        model = nn.DataParallel(model, device_ids=device_ids)
        logger.info(f"Applied DataParallel distribution")
        
    return model


def get_model_info(model: torch.nn.Module) -> Dict[str, Any]:
    """Get information about a model.
    
    Args:
        model: PyTorch model
        
    Returns:
        Dict with model information
    """
    # Count parameters
    total_params = sum(p.numel() for p in model.parameters())
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    
    # Get device
    device = next(model.parameters()).device if next(model.parameters(), None) is not None else 'cpu'
    
    # Get memory usage
    if str(device).startswith(('cuda', 'mps')):
        param_memory = sum(p.numel() * p.element_size() for p in model.parameters())
        buffer_memory = sum(b.numel() * b.element_size() for b in model.buffers())
    else:
        param_memory = 0
        buffer_memory = 0
        
    # Get precision info
    dtypes = {str(p.dtype) for p in model.parameters()}
    
    return {
        'name': model.__class__.__name__,
        'total_parameters': total_params,
        'trainable_parameters': trainable_params,
        'device': str(device),
        'parameter_memory_mb': param_memory / (1024**2),
        'buffer_memory_mb': buffer_memory / (1024**2),
        'precision_types': list(dtypes),
        'is_distributed': isinstance(model, (nn.DataParallel, nn.parallel.DistributedDataParallel))
    }