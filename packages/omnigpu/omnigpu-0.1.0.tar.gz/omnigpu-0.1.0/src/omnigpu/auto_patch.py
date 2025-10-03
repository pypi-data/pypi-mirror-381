"""OmniGPU Auto-Patching for PyTorch CUDA Compatibility.

This module provides seamless CUDA-to-MPS translation for existing PyTorch code.
Import this module and call patch() to enable CUDA compatibility on any device.
"""

import logging
import os
import sys
import warnings
from typing import List, Optional, Callable, Any
import functools

# Try to import torch - might not be available
try:
    import torch
    TORCH_AVAILABLE = True
except ImportError:
    torch = None
    TORCH_AVAILABLE = False

# Import required components
from .core.device_manager import get_device_manager
from .ops.missing_ops import patch_missing_operations
from .ops.extended_ops import patch_all_failed_operations  
from .ops.advanced_indexing import patch_advanced_indexing_operations
from .cuda_compat import patch_cuda_detection

logger = logging.getLogger("omnigpu.auto_patch")

# Global state tracking
_is_patched = False
_original_functions = {}
_patch_history = []


def is_patched() -> bool:
    """Check if OmniGPU patches are currently applied."""
    return _is_patched


def get_patch_info() -> dict:
    """Get information about current patch state."""
    return {
        'is_patched': _is_patched,
        'patch_count': len(_patch_history),
        'original_functions_stored': len(_original_functions),
        'device_manager_active': get_device_manager() is not None
    }


def patch_pytorch_core():
    """Apply core PyTorch CUDA-to-MPS patches."""
    global _is_patched, _original_functions
    
    if not TORCH_AVAILABLE:
        logger.warning("PyTorch not available, skipping patches")
        return
        
    if _is_patched:
        logger.debug("PyTorch already patched for OmniGPU")
        return
    
    logger.info("Applying core PyTorch CUDA-to-MPS patches...")
    
    # Store original functions for potential restoration
    _original_functions.update({
        'torch.cuda.is_available': torch.cuda.is_available,
        'torch.cuda.device_count': torch.cuda.device_count,
        'torch.cuda.current_device': torch.cuda.current_device,
        'torch.Tensor.cuda': torch.Tensor.cuda,
        'torch.Tensor.is_cuda': torch.Tensor.is_cuda,
    })
    
    device_manager = get_device_manager()
    
    # 1. Patch CUDA availability detection
    def omnigpu_is_available():
        """Return True if any GPU (CUDA or MPS) is available."""
        return device_manager.gpu_available()
    
    def omnigpu_device_count():
        """Return number of available GPU devices."""
        devices = device_manager.available_devices()
        # Count non-CPU devices
        gpu_count = sum(1 for d in devices if d != 'cpu')
        return max(1, gpu_count)  # Always return at least 1 if GPU available
    
    def omnigpu_current_device():
        """Return current device index."""
        current = device_manager.get_current_device()
        return 0 if current.type != 'cpu' else -1
    
    def omnigpu_get_device_name(device=None):
        """Return device name."""
        if device_manager.get_current_device().type == 'mps':
            return "Apple Silicon GPU (via OmniGPU)"
        elif device_manager.get_current_device().type == 'cuda':
            return _original_functions.get('torch.cuda.get_device_name', lambda d: "CUDA GPU")(device)
        return "CPU"
    
    # 2. Patch tensor.cuda() method
    original_cuda_method = torch.Tensor.cuda
    
    def omnigpu_tensor_cuda(self, device=None, non_blocking=False, memory_format=torch.preserve_format):
        """Enhanced .cuda() method that works on any device."""
        target_device = device_manager.select_best_device()
        
        if target_device.type == 'cuda':
            # Use original CUDA method if available
            return original_cuda_method(self, device, non_blocking, memory_format)
        elif target_device.type == 'mps':
            # Redirect to MPS
            return self.to('mps', non_blocking=non_blocking)
        else:
            # Fallback to CPU with warning
            if not getattr(omnigpu_tensor_cuda, '_cpu_warning_shown', False):
                logger.warning("No GPU available, keeping tensor on CPU")
                omnigpu_tensor_cuda._cpu_warning_shown = True
            return self.to('cpu')
    
    # 3. Patch tensor.is_cuda property
    def omnigpu_is_cuda_getter(self):
        """Enhanced .is_cuda property that includes MPS."""
        if hasattr(self, 'device'):
            device_str = str(self.device)
            # Consider MPS as CUDA for compatibility
            return 'cuda' in device_str or 'mps' in device_str
        return False
    
    # 4. Patch nn.Module.cuda() method
    original_module_cuda = torch.nn.Module.cuda
    
    def omnigpu_module_cuda(self, device=None):
        """Enhanced module.cuda() that works on any device."""
        target_device = device_manager.select_best_device()
        
        if target_device.type == 'cuda':
            return original_module_cuda(self, device)
        elif target_device.type == 'mps':
            return self.to('mps')
        else:
            if not getattr(omnigpu_module_cuda, '_cpu_warning_shown', False):
                logger.warning("No GPU available, keeping module on CPU")
                omnigpu_module_cuda._cpu_warning_shown = True
            return self.to('cpu')
    
    # Apply all patches
    torch.cuda.is_available = omnigpu_is_available
    torch.cuda.device_count = omnigpu_device_count  
    torch.cuda.current_device = omnigpu_current_device
    torch.cuda.get_device_name = omnigpu_get_device_name
    torch.Tensor.cuda = omnigpu_tensor_cuda
    torch.nn.Module.cuda = omnigpu_module_cuda
    
    # Use property for is_cuda
    if hasattr(torch.Tensor, 'is_cuda'):
        # Store original property
        _original_functions['torch.Tensor.is_cuda_prop'] = torch.Tensor.is_cuda
        # Create new property
        torch.Tensor.is_cuda = property(omnigpu_is_cuda_getter)
    
    # Additional CUDA namespace patches
    if hasattr(torch.cuda, 'synchronize'):
        original_sync = torch.cuda.synchronize
        def omnigpu_synchronize(device=None):
            if device_manager.get_current_device().type == 'mps':
                torch.mps.synchronize()
            elif device_manager.get_current_device().type == 'cuda':
                original_sync(device)
        torch.cuda.synchronize = omnigpu_synchronize
    
    # Patch memory management functions
    if hasattr(torch.cuda, 'empty_cache'):
        original_empty_cache = torch.cuda.empty_cache
        def omnigpu_empty_cache():
            if device_manager.get_current_device().type == 'mps':
                torch.mps.empty_cache()
            elif device_manager.get_current_device().type == 'cuda':
                original_empty_cache()
        torch.cuda.empty_cache = omnigpu_empty_cache
    
    _is_patched = True
    _patch_history.append('core')
    logger.info("✅ Core PyTorch CUDA-to-MPS patches applied")


def patch_models():
    """Apply patches to common model patterns."""
    global _patch_history
    
    logger.debug("Patching common model patterns...")
    
    # Patch DataParallel to work with single GPU
    if hasattr(torch.nn, 'DataParallel'):
        original_dp = torch.nn.DataParallel
        
        class OmniGPUDataParallel(original_dp):
            def __init__(self, module, device_ids=None, output_device=None, dim=0):
                # On MPS, always use single device
                if get_device_manager().get_current_device().type == 'mps':
                    device_ids = None
                    output_device = None
                super().__init__(module, device_ids, output_device, dim)
        
        torch.nn.DataParallel = OmniGPUDataParallel
        _original_functions['torch.nn.DataParallel'] = original_dp
    
    _patch_history.append('models')


def patch(silent: bool = False, comprehensive: bool = True):
    """
    Apply all OmniGPU patches to enable CUDA code on any device.
    
    Args:
        silent: If True, suppress informational messages
        comprehensive: If True, apply all available patches including experimental ones
    """
    global _is_patched
    
    if not TORCH_AVAILABLE:
        if not silent:
            logger.warning("PyTorch not installed. Install with: pip install torch")
        return
        
    if _is_patched:
        if not silent:
            logger.info("OmniGPU patches already applied")
        return
    
    try:
        # Configure logging
        if silent:
            logger.setLevel(logging.WARNING)
        else:
            logger.setLevel(logging.INFO)
        
        # Apply core patches
        patch_pytorch_core()
        
        # Apply model patches
        patch_models()
        
        # Apply operation patches
        if comprehensive:
            try:
                patch_missing_operations()
                _patch_history.append('missing_ops')
                logger.debug("Applied missing operations patches")
            except Exception as e:
                logger.warning(f"Failed to apply missing operations patches: {e}")
            
            try:
                patch_all_failed_operations()
                _patch_history.append('failed_ops')
                logger.debug("Applied failed operations patches")
            except Exception as e:
                logger.warning(f"Failed to apply failed operations patches: {e}")
            
            try:
                patch_advanced_indexing_operations()
                _patch_history.append('advanced_indexing')
                logger.debug("Applied advanced indexing patches")
            except Exception as e:
                logger.warning(f"Failed to apply advanced indexing patches: {e}")
            
            try:
                patch_cuda_detection()
                _patch_history.append('cuda_detection')
                logger.debug("Applied CUDA detection patches")
            except Exception as e:
                logger.warning(f"Failed to apply CUDA detection patches: {e}")
        
        if not silent:
            device = get_device_manager().get_current_device()
            logger.info(f"✅ OmniGPU enabled! CUDA calls will use: {device.type.upper()}")
            
    except Exception as e:
        logger.error(f"Failed to apply OmniGPU patches: {e}")
        raise


def unpatch():
    """Remove all OmniGPU patches and restore original PyTorch behavior."""
    global _is_patched, _original_functions, _patch_history
    
    if not TORCH_AVAILABLE:
        logger.debug("PyTorch not available, nothing to unpatch")
        return
        
    if not _is_patched:
        logger.info("OmniGPU patches not applied, nothing to remove")
        return
    
    logger.info("Removing OmniGPU patches...")
    
    # Restore original functions
    for name, original_func in _original_functions.items():
        try:
            parts = name.split('.')
            if len(parts) == 3 and parts[1] == 'cuda':
                # torch.cuda.function
                setattr(torch.cuda, parts[2], original_func)
            elif len(parts) == 3 and parts[1] == 'Tensor':
                # torch.Tensor.method
                if name.endswith('_prop'):
                    # Special handling for properties
                    setattr(torch.Tensor, parts[2].replace('_prop', ''), original_func)
                else:
                    setattr(torch.Tensor, parts[2], original_func)
            elif len(parts) == 3 and parts[1] == 'nn':
                # torch.nn.Class
                setattr(torch.nn, parts[2], original_func)
            elif len(parts) == 4 and parts[1] == 'nn' and parts[2] == 'Module':
                # torch.nn.Module.method
                setattr(torch.nn.Module, parts[3], original_func)
        except Exception as e:
            logger.warning(f"Failed to restore {name}: {e}")
    
    _is_patched = False
    _original_functions.clear()
    _patch_history.clear()
    logger.info("✅ OmniGPU patches removed, PyTorch restored to original behavior")


def patch_on_import():
    """
    Automatically patch when omnigpu is imported.
    This is called from __init__.py based on configuration.
    """
    # Check if auto-patching is enabled
    auto_patch = os.environ.get('OMNIGPU_AUTO_PATCH', 'true').lower() in ('true', '1', 'yes')
    
    if not auto_patch:
        logger.debug("Auto-patching disabled by environment variable")
        return
        
    if not TORCH_AVAILABLE:
        logger.debug("PyTorch not available, skipping auto-patch")
        return
    
    # Check if torch is already imported
    torch_already_imported = 'torch' in sys.modules
    
    try:
        # Apply patches silently unless there's an issue
        patch(silent=True, comprehensive=True)
        
        # Warn if torch was imported first
        if torch_already_imported:
            warnings.warn(
                "PyTorch was imported before OmniGPU. For best results, import in this order:\n"
                "    import omnigpu\n"
                "    import torch\n"
                "This ensures all patches are applied correctly.",
                ImportWarning,
                stacklevel=3
            )
            
    except Exception as e:
        # If auto-patching fails, warn but don't crash
        warnings.warn(
            f"OmniGPU auto-patching failed: {e}\n"
            f"You can manually enable with: omnigpu.enable()",
            RuntimeWarning,
            stacklevel=2
        )


# Convenience aliases
enable = patch
disable = unpatch
patch_all = lambda: patch(silent=False, comprehensive=True)


__all__ = [
    'patch', 'unpatch', 'is_patched', 'enable', 'disable', 
    'get_patch_info', 'patch_on_import', 'patch_all'
]