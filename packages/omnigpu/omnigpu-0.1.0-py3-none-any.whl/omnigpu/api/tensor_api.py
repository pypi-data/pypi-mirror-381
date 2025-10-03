"""Tensor operations API for OmniGPU.

Provides device-agnostic tensor creation and manipulation functions
that automatically handle device selection, memory management, and
precision compatibility across different GPU backends.
"""
import logging
import torch
from typing import Optional, Union, Tuple, List, Any
import functools

from ..core.device_manager import get_device_manager
from ..core.memory_manager import get_memory_manager
from ..core.precision_manager import get_precision_manager
from ..core.error_handler import get_error_handler, FallbackStrategy


def _log_tensor_fallback(op_name: str, size, target_device, dtype, error: Exception) -> None:
    """Emit structured telemetry when tensor creation falls back to CPU."""
    device_str = str(target_device)
    dtype_str = str(dtype) if dtype is not None else 'inferred'
    strategy = None

    try:
        strategy = get_error_handler().handle_device_error(op_name, device_str, error)
    except Exception as handler_error:  # pragma: no cover - defensive logging
        logger.exception(
            "Failed to record tensor fallback",  # keep context for diagnostics
            extra={
                'event': 'tensor_fallback_telemetry_error',
                'operation': op_name,
                'requested_device': device_str,
                'tensor_size': size,
                'dtype': dtype_str,
                'handler_error': str(handler_error),
            },
        )

    payload = {
        'event': 'tensor_creation_fallback',
        'operation': op_name,
        'requested_device': device_str,
        'tensor_size': size,
        'dtype': dtype_str,
        'strategy': strategy.value if isinstance(strategy, FallbackStrategy) else 'unknown',
        'error_type': type(error).__name__,
    }

    logger.error("Tensor creation fallback triggered", extra=payload)


logger = logging.getLogger("omnigpu.tensor_api")


def auto_device() -> torch.device:
    """Returns the best available device automatically.
    
    Selects devices in order of preference:
    1. CUDA (if available)
    2. MPS (if available on Apple Silicon)
    3. CPU (always available)
    
    Returns:
        torch.device: The selected device
    """
    return get_device_manager().select_best_device()


def zeros(*size, dtype=None, device=None, requires_grad=False) -> torch.Tensor:
    """Create tensor of zeros on optimal device.
    
    Args:
        size: Tensor dimensions
        dtype: Data type (default: torch.float32)
        device: Target device (default: auto_device())
        requires_grad: Whether to track gradients
        
    Returns:
        torch.Tensor: Created tensor
    """
    if device is None:
        device = auto_device()
    else:
        device = torch.device(device)
        
    if dtype is None:
        dtype = torch.float32
        
    # Handle precision compatibility
    precision_manager = get_precision_manager()
    dtype = precision_manager.auto_convert_precision(
        torch.zeros(1, dtype=dtype), str(device)
    ).dtype
    
    try:
        return torch.zeros(*size, dtype=dtype, device=device, requires_grad=requires_grad)
    except Exception as e:
        import warnings
        warnings.warn(f"Failed to create zeros tensor on {device}, falling back to CPU: {e}")
        _log_tensor_fallback("tensor_api.zeros", size, device, dtype, e)
        return torch.zeros(*size, dtype=dtype, device='cpu', requires_grad=requires_grad)


def ones(*size, dtype=None, device=None, requires_grad=False) -> torch.Tensor:
    """Create tensor of ones on optimal device.
    
    Args:
        size: Tensor dimensions
        dtype: Data type (default: torch.float32)
        device: Target device (default: auto_device())
        requires_grad: Whether to track gradients
        
    Returns:
        torch.Tensor: Created tensor
    """
    if device is None:
        device = auto_device()
    else:
        device = torch.device(device)
        
    if dtype is None:
        dtype = torch.float32
        
    # Handle precision compatibility
    precision_manager = get_precision_manager()
    dtype = precision_manager.auto_convert_precision(
        torch.ones(1, dtype=dtype), str(device)
    ).dtype
    
    try:
        return torch.ones(*size, dtype=dtype, device=device, requires_grad=requires_grad)
    except Exception as e:
        import warnings
        warnings.warn(f"Failed to create ones tensor on {device}, falling back to CPU: {e}")
        _log_tensor_fallback("tensor_api.ones", size, device, dtype, e)
        return torch.ones(*size, dtype=dtype, device='cpu', requires_grad=requires_grad)


def randn(*size, dtype=None, device=None, requires_grad=False) -> torch.Tensor:
    """Create tensor with random normal distribution on optimal device.
    
    Creates a tensor filled with random numbers from a normal distribution
    with mean 0 and variance 1 (standard normal distribution).
    
    Args:
        size: Size of the output tensor (can be variable number of arguments)
        dtype: Desired data type (default: torch.float32)
        device: Target device (default: auto-selected best device)
        requires_grad: If True, gradient computation is enabled
        
    Returns:
        torch.Tensor: Tensor filled with random normal values
        
    Example:
        >>> x = ugpu.randn(3, 4)  # 3x4 tensor on best device
        >>> y = ugpu.randn(100, 100, device='cpu')  # Force CPU
    """
    if device is None:
        device = auto_device()
    else:
        device = torch.device(device)
        
    if dtype is None:
        dtype = torch.float32
        
    # Handle precision compatibility
    precision_manager = get_precision_manager()
    base = torch.randn(*size, dtype=dtype, device='cpu', requires_grad=requires_grad)
    base = precision_manager.auto_convert_precision(base, str(device))
    
    try:
        return base.to(device, non_blocking=False)
    except Exception as e:
        import warnings
        warnings.warn(f"Failed to move randn tensor to {device}, keeping on CPU: {e}")
        _log_tensor_fallback("tensor_api.randn", size, device, dtype, e)
        return base


def tensor(data, dtype=None, device=None, requires_grad=False) -> torch.Tensor:
    """Create tensor from data on optimal device.
    
    Args:
        data: Input data
        dtype: Data type (default: inferred)
        device: Target device (default: auto_device())
        requires_grad: Whether to track gradients
        
    Returns:
        torch.Tensor: Created tensor
    """
    if device is None:
        device = auto_device()
    else:
        device = torch.device(device)
        
    # Create tensor on CPU first to infer dtype if needed
    cpu_tensor = torch.tensor(data, dtype=dtype)
    
    # Handle precision compatibility
    precision_manager = get_precision_manager()
    cpu_tensor = precision_manager.auto_convert_precision(cpu_tensor, str(device))
    
    # Move to target device - simplified without error handler for now
    try:
        return cpu_tensor.to(device=device, non_blocking=False).requires_grad_(requires_grad)
    except Exception as e:
        # Fallback to CPU if device transfer fails
        import warnings
        warnings.warn(f"Failed to create tensor on {device}, falling back to CPU: {e}")
        _log_tensor_fallback("tensor_api.tensor", cpu_tensor.shape, device, cpu_tensor.dtype, e)
        return cpu_tensor.requires_grad_(requires_grad)


def to_device(obj, device=None):
    """Move tensor/model to device, handles nested structures.
    
    Args:
        obj: Tensor, model, or nested structure
        device: Target device (default: auto_device())
        
    Returns:
        Object moved to target device
    """
    if device is None:
        device = auto_device()
    else:
        device = torch.device(device)
        
    error_handler = get_error_handler()
    
    def _move_to_device(item):
        if isinstance(item, torch.Tensor):
            # Handle precision compatibility
            precision_manager = get_precision_manager()
            item = precision_manager.auto_convert_precision(item, str(device))
            
            try:
                return item.to(device, non_blocking=False)
            except Exception as e:
                import warnings
                warnings.warn(f"Failed to move tensor to {device}, keeping on {item.device}: {e}")
                return item
            
        elif isinstance(item, torch.nn.Module):
            try:
                return item.to(device)
            except Exception as e:
                import warnings
                warnings.warn(f"Failed to move module to {device}: {e}")
                return item
            
        elif isinstance(item, (list, tuple)):
            return type(item)(_move_to_device(elem) for elem in item)
            
        elif isinstance(item, dict):
            return {k: _move_to_device(v) for k, v in item.items()}
            
        else:
            return item
            
    return _move_to_device(obj)


def get_tensor_device(tensor) -> torch.device:
    """Get tensor device as a torch.device instance.
    
    Args:
        tensor: Input tensor
        
    Returns:
        torch.device describing where the tensor lives
    """
    if not isinstance(tensor, torch.Tensor):
        raise TypeError(f"Expected torch.Tensor, got {type(tensor)}")
        
    return tensor.device


def is_gpu_tensor(tensor) -> bool:
    """Check if tensor is on GPU.
    
    Args:
        tensor: Input tensor
        
    Returns:
        True if tensor is on GPU (CUDA or MPS)
    """
    if not isinstance(tensor, torch.Tensor):
        raise TypeError(f"Expected torch.Tensor, got {type(tensor)}")
        
    device_str = str(tensor.device)
    return device_str.startswith(('cuda', 'mps'))


def empty_cache() -> None:
    """Clear memory cache on all available devices."""
    memory_manager = get_memory_manager()
    memory_manager.empty_cache()


def get_device_info(device: str = None) -> dict:
    """Get device information and capabilities.
    
    Args:
        device: Device string, or None for current device
        
    Returns:
        Dict containing device information
    """
    device_manager = get_device_manager()
    
    if device is None:
        device = str(device_manager.get_current_device())
        
    info = device_manager.get_device_info(device)
    
    return {
        'device': device,
        'name': info.device.name,
        'type': info.device.type,
        'memory_total_gb': info.memory_info.total / (1024**3),
        'memory_available_gb': info.memory_info.available / (1024**3),
        'memory_allocated_gb': info.memory_info.allocated / (1024**3),
        'memory_utilization': info.memory_info.utilization,
        'compute_capability': info.compute_capability,
        'features': info.features
    }


def available_devices() -> List[str]:
    """Get list of available devices.
    
    Returns:
        List of device strings like ['cuda:0', 'cuda:1', 'mps:0', 'cpu:0']
    """
    return get_device_manager().available_devices()


def gpu_available() -> bool:
    """Check if any GPU is available.
    
    Returns:
        True if CUDA or MPS available, False otherwise
    """
    return get_device_manager().gpu_available()


def set_device_preference(devices: List[str]) -> None:
    """Set device preference order.
    
    Args:
        devices: List of device preferences in order
    """
    get_device_manager().set_device_preference(devices)
