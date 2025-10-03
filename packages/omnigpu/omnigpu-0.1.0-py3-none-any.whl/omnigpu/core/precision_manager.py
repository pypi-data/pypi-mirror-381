"""Precision handling across different devices."""
import torch
from typing import Dict, Set, Optional, List, Tuple, Any
import warnings
import logging
from contextlib import contextmanager

from .device_manager import get_device_manager

logger = logging.getLogger(__name__)


class PrecisionPolicy:
    """Precision policy enumeration."""
    AUTO = "auto"
    HIGHEST = "highest"
    FASTEST = "fastest"
    MIXED = "mixed"


class PrecisionManager:
    """Manages precision handling across devices."""
    
    def __init__(self):
        self.device_manager = get_device_manager()
        self.device_precision_support: Dict[str, Dict[str, bool]] = {}
        self.precision_policy = PrecisionPolicy.AUTO
        self.mixed_precision_enabled = False
        self._amp_context = None
        
    def detect_precision_support(self, device: str) -> Dict[str, bool]:
        """Detect supported precisions for device.
        
        Args:
            device: Device to test
            
        Returns:
            Dict mapping precision names to support status
        """
        # Check cache first
        if device in self.device_precision_support:
            return self.device_precision_support[device]
            
        support_map = {}
        device_obj = torch.device(device)
        
        # Define precisions to test
        precisions = [
            ('float16', torch.float16),
            ('bfloat16', torch.bfloat16), 
            ('float32', torch.float32),
            ('float64', torch.float64),
            ('int8', torch.int8),
            ('int16', torch.int16),
            ('int32', torch.int32),
            ('int64', torch.int64),
            ('complex64', torch.complex64),
            ('complex128', torch.complex128),
        ]
        
        for dtype_name, torch_dtype in precisions:
            try:
                # Test by creating small tensor and performing operation
                test_tensor = torch.ones(2, 2, dtype=torch_dtype, device=device_obj)
                result = torch.matmul(test_tensor, test_tensor)
                
                # Additional test for mixed precision ops
                if dtype_name in ['float16', 'bfloat16']:
                    # Test common mixed precision operations
                    _ = torch.nn.functional.linear(test_tensor, test_tensor)
                    
                support_map[dtype_name] = True
                logger.debug(f"{device} supports {dtype_name}")
                
            except Exception as e:
                support_map[dtype_name] = False
                logger.debug(f"{device} does not support {dtype_name}: {e}")
                
        # Cache results
        self.device_precision_support[device] = support_map
        
        # Log summary
        supported = [k for k, v in support_map.items() if v]
        logger.info(f"Device {device} supports precisions: {supported}")
        
        return support_map
        
    def get_supported_precisions(self, device: str) -> Set[torch.dtype]:
        """Get set of supported precisions for device.
        
        Args:
            device: Device to query
            
        Returns:
            Set of supported torch dtypes
        """
        if device not in self.device_precision_support:
            self.detect_precision_support(device)
            
        support_map = self.device_precision_support[device]
        
        # Map string names to torch dtypes
        dtype_map = {
            'float16': torch.float16,
            'bfloat16': torch.bfloat16,
            'float32': torch.float32,
            'float64': torch.float64,
            'int8': torch.int8,
            'int16': torch.int16,
            'int32': torch.int32,
            'int64': torch.int64,
            'complex64': torch.complex64,
            'complex128': torch.complex128,
        }
        
        return {dtype_map[name] for name, supported in support_map.items() if supported}
        
    def auto_convert_precision(self, tensor: torch.Tensor, target_device: str) -> torch.Tensor:
        """Automatically convert tensor precision for compatibility.
        
        Args:
            tensor: Input tensor
            target_device: Target device
            
        Returns:
            Tensor with compatible precision
        """
        original_dtype = tensor.dtype
        supported_precisions = self.get_supported_precisions(target_device)
        
        # If original precision is supported, no conversion needed
        if original_dtype in supported_precisions:
            return tensor
            
        # Define precision fallback chains
        fallback_chains = {
            torch.bfloat16: [torch.float16, torch.float32],
            torch.float64: [torch.float32, torch.float16],
            torch.complex128: [torch.complex64, torch.float32],
            torch.int64: [torch.int32, torch.int16],
        }
        
        # Try fallback chain
        if original_dtype in fallback_chains:
            for fallback_dtype in fallback_chains[original_dtype]:
                if fallback_dtype in supported_precisions:
                    warnings.warn(
                        f"Converting tensor from {original_dtype} to {fallback_dtype} for {target_device} compatibility",
                        UserWarning
                    )
                    return tensor.to(dtype=fallback_dtype)
                    
        # Default fallback based on tensor type
        if tensor.is_floating_point():
            # Float types default to float32
            if torch.float32 in supported_precisions:
                warnings.warn(
                    f"Converting tensor from {original_dtype} to float32 for {target_device} compatibility",
                    UserWarning
                )
                return tensor.to(dtype=torch.float32)
                
        elif tensor.dtype.is_complex:
            # Complex types try complex64 then float32
            if torch.complex64 in supported_precisions:
                warnings.warn(
                    f"Converting tensor from {original_dtype} to complex64 for {target_device} compatibility",
                    UserWarning
                )
                return tensor.to(dtype=torch.complex64)
            elif torch.float32 in supported_precisions:
                warnings.warn(
                    f"Converting complex tensor to float32 for {target_device} compatibility (losing imaginary part)",
                    UserWarning
                )
                return tensor.real.to(dtype=torch.float32)
                
        else:
            # Integer types default to int32
            if torch.int32 in supported_precisions:
                warnings.warn(
                    f"Converting tensor from {original_dtype} to int32 for {target_device} compatibility",
                    UserWarning
                )
                return tensor.to(dtype=torch.int32)
                
        # Last resort: convert to float32 (should be universally supported)
        warnings.warn(
            f"No compatible precision found for {original_dtype} on {target_device}, using float32",
            UserWarning
        )
        return tensor.to(dtype=torch.float32)
        
    def get_optimal_precision(self, device: str, policy: Optional[str] = None) -> torch.dtype:
        """Get optimal precision for device based on policy.
        
        Args:
            device: Target device
            policy: Precision policy (auto, highest, fastest, mixed)
            
        Returns:
            Optimal torch dtype
        """
        if policy is None:
            policy = self.precision_policy
            
        supported = self.get_supported_precisions(device)
        device_type = device.split(':')[0]
        
        if policy == PrecisionPolicy.AUTO:
            # Auto: balance between speed and accuracy
            if device_type == 'cuda':
                # Prefer float16 for modern GPUs
                if torch.float16 in supported:
                    return torch.float16
                elif torch.float32 in supported:
                    return torch.float32
                    
            elif device_type == 'mps':
                # MPS works well with float32
                if torch.float32 in supported:
                    return torch.float32
                elif torch.float16 in supported:
                    return torch.float16
                    
            else:  # CPU
                # CPU usually faster with float32
                return torch.float32
                
        elif policy == PrecisionPolicy.HIGHEST:
            # Highest: prioritize accuracy
            precision_order = [
                torch.float64, torch.complex128,
                torch.float32, torch.complex64,
                torch.float16, torch.bfloat16
            ]
            for dtype in precision_order:
                if dtype in supported:
                    return dtype
                    
        elif policy == PrecisionPolicy.FASTEST:
            # Fastest: prioritize speed
            if device_type in ['cuda', 'mps']:
                precision_order = [
                    torch.float16, torch.bfloat16,
                    torch.float32, torch.float64
                ]
            else:  # CPU
                precision_order = [
                    torch.float32, torch.float16,
                    torch.bfloat16, torch.float64
                ]
                
            for dtype in precision_order:
                if dtype in supported:
                    return dtype
                    
        elif policy == PrecisionPolicy.MIXED:
            # Mixed precision: return base type, actual mixing handled by AMP
            return torch.float32
            
        # Default fallback
        return torch.float32
        
    @contextmanager
    def mixed_precision_context(self, device: Optional[str] = None, enabled: bool = True):
        """Context manager for mixed precision computation.
        
        Args:
            device: Target device, or None for current
            enabled: Whether to enable mixed precision
        """
        if device is None:
            device = str(self.device_manager.get_current_device())
            
        device_type = device.split(':')[0]
        
        if not enabled:
            yield
            return
            
        # Check if mixed precision is supported
        supported = self.get_supported_precisions(device)
        if torch.float16 not in supported and torch.bfloat16 not in supported:
            warnings.warn(f"Mixed precision not supported on {device}, using float32")
            yield
            return
            
        # Set up appropriate autocast context
        if device_type == 'cuda':
            dtype = torch.float16 if torch.float16 in supported else torch.bfloat16
            with torch.cuda.amp.autocast(dtype=dtype):
                yield
                
        elif device_type == 'mps':
            # MPS autocast support
            if hasattr(torch, 'autocast'):
                with torch.autocast(device_type='mps', dtype=torch.float16):
                    yield
            else:
                # Fallback for older PyTorch versions
                yield
                
        else:  # CPU
            if hasattr(torch, 'autocast'):
                with torch.autocast(device_type='cpu', dtype=torch.bfloat16):
                    yield
            else:
                yield
                
    def convert_model_precision(self, model: torch.nn.Module, target_dtype: torch.dtype) -> torch.nn.Module:
        """Convert model to target precision.
        
        Args:
            model: PyTorch model
            target_dtype: Target dtype
            
        Returns:
            Model converted to target precision
        """
        # Convert parameters
        model = model.to(dtype=target_dtype)
        
        # Log conversion
        param_count = sum(p.numel() for p in model.parameters())
        logger.info(f"Converted model ({param_count:,} parameters) to {target_dtype}")
        
        return model
        
    def get_precision_info(self, tensor: torch.Tensor) -> Dict[str, Any]:
        """Get precision information about a tensor.
        
        Args:
            tensor: Input tensor
            
        Returns:
            Dict with precision information
        """
        dtype = tensor.dtype
        
        info = {
            'dtype': str(dtype),
            'bits': self._get_dtype_bits(dtype),
            'is_floating': tensor.is_floating_point(),
            'is_complex': tensor.is_complex(),
            'device': str(tensor.device),
            'memory_bytes': tensor.element_size() * tensor.numel()
        }
        
        # Add device-specific info
        if tensor.is_cuda:
            info['supports_tensor_cores'] = self._supports_tensor_cores(tensor)
            
        return info
        
    def _get_dtype_bits(self, dtype: torch.dtype) -> int:
        """Get number of bits for dtype."""
        dtype_bits = {
            torch.float16: 16,
            torch.bfloat16: 16,
            torch.float32: 32,
            torch.float64: 64,
            torch.int8: 8,
            torch.int16: 16,
            torch.int32: 32,
            torch.int64: 64,
            torch.complex64: 64,
            torch.complex128: 128,
        }
        return dtype_bits.get(dtype, 0)
        
    def _supports_tensor_cores(self, tensor: torch.Tensor) -> bool:
        """Check if tensor operation can use tensor cores."""
        if not tensor.is_cuda:
            return False
            
        # Tensor cores require specific dtypes
        if tensor.dtype not in [torch.float16, torch.bfloat16]:
            return False
            
        # Check compute capability
        device_idx = tensor.device.index or 0
        props = torch.cuda.get_device_properties(device_idx)
        
        # Tensor cores available on compute capability 7.0+
        return props.major >= 7
        
    def set_precision_policy(self, policy: str) -> None:
        """Set global precision policy.
        
        Args:
            policy: One of 'auto', 'highest', 'fastest', 'mixed'
        """
        valid_policies = [
            PrecisionPolicy.AUTO,
            PrecisionPolicy.HIGHEST,
            PrecisionPolicy.FASTEST,
            PrecisionPolicy.MIXED
        ]
        
        if policy not in valid_policies:
            raise ValueError(f"Invalid precision policy: {policy}. Must be one of {valid_policies}")
            
        self.precision_policy = policy
        logger.info(f"Precision policy set to: {policy}")


# Global precision manager instance
_global_precision_manager = None


def get_precision_manager() -> PrecisionManager:
    """Get global precision manager instance."""
    global _global_precision_manager
    if _global_precision_manager is None:
        _global_precision_manager = PrecisionManager()
    return _global_precision_manager