"""
Production Hardening for OmniGPU
Ensures operations never crash - always fall back gracefully.
"""

import functools
import logging
import traceback
import warnings
from typing import Callable, Any, Optional, Dict, List
import torch
import time
import psutil
import os

logger = logging.getLogger(__name__)


class OmniGPUError(Exception):
    """User-friendly error with suggestions."""
    
    def __init__(self, operation: str, original_error: Exception, 
                 suggestion: Optional[str] = None, fallback_used: bool = False):
        self.operation = operation
        self.original_error = original_error
        self.suggestion = suggestion or self._generate_suggestion(original_error)
        self.fallback_used = fallback_used
        
        # Check environment variables
        debug_mode = os.environ.get('OMNIGPU_DEBUG', '0') == '1'
        quiet_mode = os.environ.get('OMNIGPU_QUIET', '0') == '1'
        
        if quiet_mode:
            msg = f"OmniGPU: {operation} using CPU fallback"
        elif debug_mode:
            msg = f"""
OmniGPU Error Details:
=====================
Operation: {operation}
Error Type: {type(original_error).__name__}
Error Message: {str(original_error)}
Fallback Used: {'Yes' if fallback_used else 'No'}
Suggestion: {self.suggestion}

Stack Trace:
{traceback.format_exc()}

To suppress this message: export OMNIGPU_QUIET=1
"""
        else:
            msg = f"""
Operation '{operation}' failed on MPS.
Reason: {str(original_error)}
Suggestion: {self.suggestion}
{"Falling back to CPU (this may be slower)." if fallback_used else "No fallback available."}

To debug: export OMNIGPU_DEBUG=1
To suppress: export OMNIGPU_QUIET=1
"""
        super().__init__(msg.strip())
    
    def _generate_suggestion(self, error: Exception) -> str:
        """Generate helpful suggestions based on error type."""
        error_msg = str(error).lower()
        
        if "out of memory" in error_msg:
            return "Try reducing batch size or use gradient checkpointing"
        elif "not implemented" in error_msg:
            return "This operation doesn't have MPS support yet. CPU fallback will be used"
        elif "dimension" in error_msg or "size" in error_msg:
            return "Check tensor dimensions. MPS may have different size constraints than CUDA"
        elif "dtype" in error_msg:
            return "Try converting to float32. MPS has limited dtype support"
        else:
            return "This is likely an MPS limitation. Report at github.com/omnigpu/issues"


class SafeOperation:
    """Decorator that makes any operation safe with automatic fallback."""
    
    def __init__(self, op_name: Optional[str] = None, 
                 fallback: Optional[Callable] = None,
                 track_stats: bool = True):
        self.op_name = op_name
        self.fallback = fallback
        self.track_stats = track_stats
        self.stats = {
            'success_count': 0,
            'fallback_count': 0,
            'failure_count': 0,
            'total_time': 0.0,
            'fallback_time': 0.0
        }
    
    def __call__(self, func: Callable) -> Callable:
        op_name = self.op_name or func.__name__
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            
            try:
                # Try the original operation
                result = func(*args, **kwargs)
                
                if self.track_stats:
                    self.stats['success_count'] += 1
                    self.stats['total_time'] += time.time() - start_time
                
                return result
                
            except Exception as e:
                # Log the error
                logger.warning(f"{op_name} failed: {e}")
                
                # Try fallback if available
                if self.fallback:
                    try:
                        fallback_start = time.time()
                        result = self.fallback(*args, **kwargs)
                        
                        if self.track_stats:
                            self.stats['fallback_count'] += 1
                            self.stats['fallback_time'] += time.time() - fallback_start
                            self.stats['total_time'] += time.time() - start_time
                        
                        # Warn user about fallback (respecting quiet mode)
                        if os.environ.get('OMNIGPU_QUIET', '0') != '1':
                            warnings.warn(
                                f"{op_name} using CPU fallback (may be slower)",
                                category=RuntimeWarning,
                                stacklevel=2
                            )
                        
                        return result
                        
                    except Exception as fallback_error:
                        logger.error(f"Fallback also failed for {op_name}: {fallback_error}")
                        if self.track_stats:
                            self.stats['failure_count'] += 1
                        
                        # Raise user-friendly error
                        raise OmniGPUError(
                            op_name, 
                            e, 
                            fallback_used=True
                        ) from fallback_error
                else:
                    if self.track_stats:
                        self.stats['failure_count'] += 1
                    
                    # No fallback available
                    raise OmniGPUError(
                        op_name,
                        e,
                        fallback_used=False
                    ) from e
        
        # Attach stats for monitoring
        wrapper.omnigpu_stats = self.stats
        wrapper.omnigpu_op_name = op_name
        
        return wrapper
    
    @classmethod
    def get_stats(cls, func: Callable) -> Optional[Dict[str, Any]]:
        """Get statistics for a wrapped function."""
        return getattr(func, 'omnigpu_stats', None)


class ResourceGuard:
    """Prevents memory exhaustion and resource issues."""
    
    def __init__(self, 
                 max_memory_percent: float = 90.0,
                 max_tensor_size_gb: float = 10.0,
                 check_interval: int = 100):
        self.max_memory_percent = max_memory_percent
        self.max_tensor_size_gb = max_tensor_size_gb
        self.check_interval = check_interval
        self.operation_count = 0
    
    def check_memory(self):
        """Check if we're running low on memory."""
        if torch.backends.mps.is_available():
            # MPS doesn't provide good memory stats yet
            # Use system memory as proxy
            memory_percent = psutil.virtual_memory().percent
            
            if memory_percent > self.max_memory_percent:
                logger.warning(f"High memory usage: {memory_percent:.1f}%")
                # Force garbage collection
                import gc
                gc.collect()
                
                # Check again
                memory_percent = psutil.virtual_memory().percent
                if memory_percent > self.max_memory_percent:
                    raise MemoryError(
                        f"System memory usage too high: {memory_percent:.1f}%. "
                        f"Maximum allowed: {self.max_memory_percent}%"
                    )
    
    def check_tensor_size(self, *tensors):
        """Check if tensors are too large."""
        for tensor in tensors:
            if not isinstance(tensor, torch.Tensor):
                continue
                
            size_gb = tensor.element_size() * tensor.nelement() / (1024**3)
            if size_gb > self.max_tensor_size_gb:
                raise ValueError(
                    f"Tensor too large: {size_gb:.2f}GB. "
                    f"Maximum allowed: {self.max_tensor_size_gb}GB. "
                    f"Consider using gradient checkpointing or smaller batch sizes."
                )
    
    def guard(self, func: Callable) -> Callable:
        """Decorator to add resource guards to a function."""
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Periodic memory check
            self.operation_count += 1
            if self.operation_count % self.check_interval == 0:
                self.check_memory()
            
            # Check tensor sizes
            self.check_tensor_size(*[a for a in args if isinstance(a, torch.Tensor)])
            
            return func(*args, **kwargs)
        
        return wrapper


class GlobalErrorHandler:
    """Global error handling and recovery system."""
    
    def __init__(self):
        self.error_counts = {}
        self.error_threshold = 10
        self.disabled_operations = set()
    
    def handle_error(self, op_name: str, error: Exception):
        """Track errors and disable operations that fail too often."""
        self.error_counts[op_name] = self.error_counts.get(op_name, 0) + 1
        
        if self.error_counts[op_name] >= self.error_threshold:
            logger.error(
                f"Operation {op_name} has failed {self.error_counts[op_name]} times. "
                f"Disabling MPS acceleration for this operation."
            )
            self.disabled_operations.add(op_name)
    
    def is_disabled(self, op_name: str) -> bool:
        """Check if an operation should skip MPS."""
        return op_name in self.disabled_operations
    
    def reset_operation(self, op_name: str):
        """Re-enable an operation."""
        self.disabled_operations.discard(op_name)
        self.error_counts.pop(op_name, None)


# Global instances
resource_guard = ResourceGuard()
error_handler = GlobalErrorHandler()


def make_safe(func: Callable, 
              name: Optional[str] = None,
              fallback: Optional[Callable] = None) -> Callable:
    """
    Make any function safe with automatic fallback and resource guards.
    
    Example:
        safe_matmul = make_safe(torch.matmul, fallback=cpu_matmul)
    """
    op_name = name or func.__name__
    
    # Check if operation is disabled
    if error_handler.is_disabled(op_name):
        logger.info(f"{op_name} is disabled due to errors, using fallback")
        return fallback or func
    
    # Apply safety wrapper
    safe_func = SafeOperation(op_name, fallback=fallback)(func)
    
    # Apply resource guards
    safe_func = resource_guard.guard(safe_func)
    
    return safe_func


def production_config():
    """Apply production-ready configuration to OmniGPU."""
    
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Suppress PyTorch warnings in production
    if os.environ.get('OMNIGPU_QUIET', '0') == '1':
        warnings.filterwarnings('ignore', category=UserWarning, module='torch')
    
    # Set memory limits
    resource_guard.max_memory_percent = float(
        os.environ.get('OMNIGPU_MAX_MEMORY_PERCENT', '90')
    )
    
    logger.info("OmniGPU production hardening enabled")


# Auto-apply production config if env var is set
if os.environ.get('OMNIGPU_PRODUCTION', '0') == '1':
    production_config()