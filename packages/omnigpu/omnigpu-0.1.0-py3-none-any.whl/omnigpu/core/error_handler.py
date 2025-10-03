"""Error handling and fallback mechanisms."""
import torch
import warnings
import logging
from typing import Optional, Callable, Any, Dict, List
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
import functools
import traceback

from .device_manager import get_device_manager
from .memory_manager import get_memory_manager

logger = logging.getLogger(__name__)


class FallbackStrategy(Enum):
    """Fallback strategies for error handling."""
    RETRY_AFTER_CLEANUP = "retry_after_cleanup"
    FALLBACK_TO_CPU = "fallback_to_cpu"
    SELECT_ALTERNATIVE_DEVICE = "select_alternative_device"
    RAISE_ERROR = "raise_error"
    REDUCE_PRECISION = "reduce_precision"
    REDUCE_BATCH_SIZE = "reduce_batch_size"


@dataclass
class ErrorInfo:
    """Information about an error."""
    operation: str
    device: str
    error_type: str
    message: str
    timestamp: datetime
    traceback: Optional[str] = None
    recovery_attempted: bool = False
    recovery_successful: bool = False


class ErrorHandler:
    """Handles errors and implements fallback strategies."""
    
    def __init__(self):
        self.fallback_enabled = True
        self.error_history: List[ErrorInfo] = []
        self.device_manager = get_device_manager()
        self.memory_manager = get_memory_manager()
        self.max_retries = 3
        self.error_on_fallback = False
        
    def handle_device_error(self, operation: str, device: str, error: Exception) -> FallbackStrategy:
        """Handle device-related errors.
        
        Args:
            operation: Operation that failed
            device: Device where error occurred
            error: The exception
            
        Returns:
            FallbackStrategy to use
        """
        # Log error information
        error_info = ErrorInfo(
            operation=operation,
            device=device,
            error_type=type(error).__name__,
            message=str(error),
            timestamp=datetime.now(),
            traceback=traceback.format_exc()
        )
        self.error_history.append(error_info)
        
        # Determine error type and strategy
        error_str = str(error).lower()
        
        if 'out of memory' in error_str or 'oom' in error_str:
            return self._handle_oom_error(operation, device, error)
        elif 'not supported' in error_str or 'not implemented' in error_str:
            return self._handle_unsupported_operation(operation, device, error)
        elif 'device' in error_str and ('not found' in error_str or 'not available' in error_str):
            return self._handle_device_unavailable(operation, device, error)
        elif 'dtype' in error_str or 'type' in error_str:
            return self._handle_dtype_error(operation, device, error)
        else:
            return self._handle_generic_device_error(operation, device, error)
            
    def _handle_oom_error(self, operation: str, device: str, error: Exception) -> FallbackStrategy:
        """Handle out of memory errors.
        
        Strategy:
        1. Clear device cache
        2. Try operation again
        3. If still fails, try reducing batch size
        4. If still fails, fallback to CPU
        """
        logger.warning(f"Out of memory on {device} during {operation}")
        
        if not self.fallback_enabled:
            if self.error_on_fallback:
                raise error
            return FallbackStrategy.RAISE_ERROR
            
        # First attempt: clear cache
        self.memory_manager.empty_cache(device)
        logger.info(f"Cleared cache on {device}, suggesting retry")
        
        # Check if this is a repeated OOM
        recent_ooms = [
            e for e in self.error_history[-5:]
            if e.device == device and 'memory' in e.message.lower()
        ]
        
        if len(recent_ooms) >= 2:
            # Multiple OOMs, try more aggressive strategy
            if device != 'cpu':
                logger.warning(f"Repeated OOM on {device}, suggesting CPU fallback")
                return FallbackStrategy.FALLBACK_TO_CPU
            else:
                # Even CPU is OOM, suggest batch size reduction
                return FallbackStrategy.REDUCE_BATCH_SIZE
                
        return FallbackStrategy.RETRY_AFTER_CLEANUP
        
    def _handle_unsupported_operation(self, operation: str, device: str, error: Exception) -> FallbackStrategy:
        """Handle operations not supported on device."""
        logger.warning(f"Operation {operation} not supported on {device}")
        
        if not self.fallback_enabled:
            if self.error_on_fallback:
                raise error
            return FallbackStrategy.RAISE_ERROR
            
        # Try CPU as it supports most operations
        if device != 'cpu':
            logger.info(f"Falling back to CPU for {operation}")
            return FallbackStrategy.FALLBACK_TO_CPU
        else:
            # Operation not even supported on CPU
            raise RuntimeError(f"Operation {operation} not supported on any available device") from error
            
    def _handle_device_unavailable(self, operation: str, device: str, error: Exception) -> FallbackStrategy:
        """Handle device not available errors."""
        logger.warning(f"Device {device} not available for {operation}")
        
        if not self.fallback_enabled:
            if self.error_on_fallback:
                raise error
            return FallbackStrategy.RAISE_ERROR
            
        # Find alternative device
        return FallbackStrategy.SELECT_ALTERNATIVE_DEVICE
        
    def _handle_dtype_error(self, operation: str, device: str, error: Exception) -> FallbackStrategy:
        """Handle dtype-related errors."""
        logger.warning(f"Dtype error on {device} during {operation}: {error}")
        
        if not self.fallback_enabled:
            if self.error_on_fallback:
                raise error
            return FallbackStrategy.RAISE_ERROR
            
        # Try reducing precision
        return FallbackStrategy.REDUCE_PRECISION
        
    def _handle_generic_device_error(self, operation: str, device: str, error: Exception) -> FallbackStrategy:
        """Handle generic device errors."""
        logger.error(f"Device error on {device} during {operation}: {error}")
        
        if not self.fallback_enabled:
            if self.error_on_fallback:
                raise error
            return FallbackStrategy.RAISE_ERROR
            
        # Try alternative device first
        if device != 'cpu':
            return FallbackStrategy.SELECT_ALTERNATIVE_DEVICE
        else:
            # Already on CPU, can't fallback further
            raise error
            
    def with_fallback(self, func: Callable, *args, device: Optional[str] = None, 
                     operation_name: Optional[str] = None, **kwargs) -> Any:
        """Execute function with automatic error handling and fallback.
        
        Args:
            func: Function to execute
            *args: Function arguments
            device: Device to run on
            operation_name: Name of operation for logging
            **kwargs: Function keyword arguments
            
        Returns:
            Function result
        """
        if device is None:
            device = str(self.device_manager.get_current_device())
            
        if operation_name is None:
            operation_name = func.__name__
            
        retries = 0
        last_error = None
        
        while retries < self.max_retries:
            try:
                # Attempt operation
                return func(*args, **kwargs)
                
            except (RuntimeError, torch.cuda.OutOfMemoryError) as e:
                last_error = e
                
                # Get fallback strategy
                strategy = self.handle_device_error(operation_name, device, e)
                
                if strategy == FallbackStrategy.RETRY_AFTER_CLEANUP:
                    retries += 1
                    logger.info(f"Retrying {operation_name} after cleanup (attempt {retries}/{self.max_retries})")
                    continue
                    
                elif strategy == FallbackStrategy.FALLBACK_TO_CPU:
                    logger.info(f"Falling back to CPU for {operation_name}")
                    # Move inputs to CPU and retry
                    cpu_args = self._move_to_device(args, 'cpu')
                    cpu_kwargs = self._move_to_device(kwargs, 'cpu')
                    return func(*cpu_args, **cpu_kwargs)
                    
                elif strategy == FallbackStrategy.SELECT_ALTERNATIVE_DEVICE:
                    # Find alternative device
                    alt_device = self._find_alternative_device(device)
                    if alt_device:
                        logger.info(f"Trying alternative device {alt_device} for {operation_name}")
                        alt_args = self._move_to_device(args, alt_device)
                        alt_kwargs = self._move_to_device(kwargs, alt_device)
                        return func(*alt_args, **alt_kwargs)
                    else:
                        raise RuntimeError(f"No alternative device available for {operation_name}") from e
                        
                elif strategy == FallbackStrategy.REDUCE_PRECISION:
                    # This would need to be handled by the caller
                    logger.warning(f"Precision reduction suggested for {operation_name}")
                    raise e
                    
                elif strategy == FallbackStrategy.REDUCE_BATCH_SIZE:
                    # This would need to be handled by the caller
                    logger.warning(f"Batch size reduction suggested for {operation_name}")
                    raise e
                    
                else:  # RAISE_ERROR
                    raise e
                    
            except Exception as e:
                # Non-device errors, re-raise
                logger.error(f"Non-recoverable error in {operation_name}: {e}")
                raise
                
        # Max retries exceeded
        if last_error:
            raise RuntimeError(f"Failed after {self.max_retries} retries: {last_error}") from last_error
            
    def _move_to_device(self, obj: Any, device: str) -> Any:
        """Recursively move tensors to device."""
        if isinstance(obj, torch.Tensor):
            return obj.to(device)
        elif isinstance(obj, torch.nn.Module):
            return obj.to(device)
        elif isinstance(obj, (list, tuple)):
            return type(obj)(self._move_to_device(item, device) for item in obj)
        elif isinstance(obj, dict):
            return {k: self._move_to_device(v, device) for k, v in obj.items()}
        else:
            return obj
            
    def _find_alternative_device(self, failed_device: str) -> Optional[str]:
        """Find alternative device when one fails."""
        available = self.device_manager.available_devices()
        
        # Remove failed device
        alternatives = [d for d in available if d != failed_device]
        
        if not alternatives:
            return None
            
        # Prefer GPU over CPU
        gpu_devices = [d for d in alternatives if d.startswith(('cuda', 'mps'))]
        if gpu_devices:
            return gpu_devices[0]
            
        # Fallback to CPU
        cpu_devices = [d for d in alternatives if d.startswith('cpu')]
        if cpu_devices:
            return cpu_devices[0]
            
        return alternatives[0] if alternatives else None
        
    def safe_operation(self, operation_name: str = None):
        """Decorator for safe operation execution with fallback.
        
        Args:
            operation_name: Optional operation name for logging
        """
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                op_name = operation_name or func.__name__
                return self.with_fallback(func, *args, operation_name=op_name, **kwargs)
            return wrapper
        return decorator
        
    def get_error_summary(self) -> Dict[str, Any]:
        """Get summary of errors.
        
        Returns:
            Dict with error statistics
        """
        if not self.error_history:
            return {
                'total_errors': 0,
                'errors_by_type': {},
                'errors_by_device': {},
                'recovery_success_rate': 0.0
            }
            
        # Count errors by type
        errors_by_type = {}
        errors_by_device = {}
        recovery_attempts = 0
        recovery_successes = 0
        
        for error in self.error_history:
            # By type
            if error.error_type not in errors_by_type:
                errors_by_type[error.error_type] = 0
            errors_by_type[error.error_type] += 1
            
            # By device
            if error.device not in errors_by_device:
                errors_by_device[error.device] = 0
            errors_by_device[error.device] += 1
            
            # Recovery stats
            if error.recovery_attempted:
                recovery_attempts += 1
                if error.recovery_successful:
                    recovery_successes += 1
                    
        recovery_rate = (recovery_successes / recovery_attempts * 100) if recovery_attempts > 0 else 0.0
        
        return {
            'total_errors': len(self.error_history),
            'errors_by_type': errors_by_type,
            'errors_by_device': errors_by_device,
            'recovery_attempts': recovery_attempts,
            'recovery_successes': recovery_successes,
            'recovery_success_rate': recovery_rate,
            'recent_errors': [
                {
                    'operation': e.operation,
                    'device': e.device,
                    'error': e.error_type,
                    'message': e.message,
                    'time': e.timestamp.isoformat()
                }
                for e in self.error_history[-10:]  # Last 10 errors
            ]
        }
        
    def clear_error_history(self) -> None:
        """Clear error history."""
        self.error_history.clear()
        logger.info("Error history cleared")
        
    def set_fallback_enabled(self, enabled: bool) -> None:
        """Enable or disable automatic fallback.
        
        Args:
            enabled: Whether to enable fallback
        """
        self.fallback_enabled = enabled
        logger.info(f"Fallback {'enabled' if enabled else 'disabled'}")
        
    def set_error_on_fallback(self, enabled: bool) -> None:
        """Set whether to raise error when fallback would occur.
        
        Args:
            enabled: Whether to raise error on fallback
        """
        self.error_on_fallback = enabled
        logger.info(f"Error on fallback {'enabled' if enabled else 'disabled'}")


# Global error handler instance
_global_error_handler = None


def get_error_handler() -> ErrorHandler:
    """Get global error handler instance."""
    global _global_error_handler
    if _global_error_handler is None:
        _global_error_handler = ErrorHandler()
    return _global_error_handler