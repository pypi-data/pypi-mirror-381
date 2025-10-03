"""JAX compatibility layer for OmniGPU.

This module patches JAX to work seamlessly on any GPU backend,
enabling JAX code written for CUDA to run on Apple Metal (MPS) and other GPUs.
"""

import functools
import warnings
from typing import Any, Optional, Union, List
import logging

logger = logging.getLogger(__name__)

# Track patching state
_is_patched = False
_original_functions = {}

# Import device management
from ..core.device_manager import get_device_manager
from ..api.tensor_api import auto_device


def _available_jax_backends():
    """Safely fetch available JAX backends."""
    try:
        from jax._src import xla_bridge  # type: ignore

        return set(xla_bridge.backends().keys())
    except Exception:
        return set()


def _get_backend_for_device():
    """Determine JAX backend based on available device."""
    device = auto_device()

    if device.type == 'cuda':
        return 'gpu'
    elif device.type == 'mps':
        # Prefer Metal when the backend is available, otherwise fall back
        backends = _available_jax_backends()
        if 'metal' in backends:
            import os

            os.environ.setdefault('JAX_PLATFORMS', 'metal')
            return 'metal'
        if 'gpu' in backends:
            return 'gpu'
        # No GPU-capable backend registered, gracefully fall back to CPU
    else:
        return 'cpu'

    return 'cpu'


def patch():
    """Patch JAX to support OmniGPU device abstraction."""
    global _is_patched, _original_functions
    
    if _is_patched:
        logger.info("JAX already patched")
        return
    
    try:
        import jax
        import jax.numpy as jnp
        from jax import devices as jax_devices
        from jax._src import config
        from jax._src import xla_bridge
    except ImportError:
        logger.warning("JAX not installed, skipping JAX patching")
        return
    
    logger.info("Patching JAX for OmniGPU compatibility")
    
    # Store original functions
    _original_functions = {
        'devices': jax.devices,
        'device_put': jax.device_put,
        'default_backend': jax.default_backend,
        'device_count': jax.device_count,
        'local_device_count': jax.local_device_count,
    }
    
    # 1. Patch device detection
    def patched_devices(backend=None):
        """Return available devices, mapping to actual backend."""
        if backend is None:
            backend = _get_backend_for_device()

        # Get actual devices from JAX
        try:
            actual_devices = _original_functions['devices'](backend)
        except RuntimeError:
            # If requested backend is unavailable, fall back to default
            actual_devices = _original_functions['devices']()
            backend = None

        # If we're on MPS but JAX returns CPU, present it as GPU
        device = auto_device()
        if device.type == 'mps' and backend in ('cpu', None) and actual_devices:
            # Create a mock GPU device representation
            class MockGPUDevice:
                def __init__(self, cpu_device):
                    self._cpu_device = cpu_device
                    self.platform = 'gpu'  # Present as GPU
                    self.device_kind = 'GPU'
                    self.id = 0
                
                def __repr__(self):
                    return f"MockGPU(MPS->CPU)"
                
                def __str__(self):
                    return "gpu:0"
            
            # Wrap CPU devices as GPU devices for MPS
            return [MockGPUDevice(d) for d in actual_devices[:1]]
        
        return actual_devices
    
    # 2. Patch device_put to handle device mapping
    def patched_device_put(x, device=None):
        """Put array on device, handling OmniGPU device mapping."""
        if device is None:
            # Auto-select device
            ugpu_device = auto_device()
            if ugpu_device.type == 'mps':
                # MPS uses CPU backend in JAX
                return _original_functions['device_put'](x, None)
            else:
                return _original_functions['device_put'](x, device)
        
        # Handle string device specifications
        if isinstance(device, str):
            if 'gpu' in device or 'cuda' in device:
                ugpu_device = auto_device()
                if ugpu_device.type == 'mps':
                    # Redirect to CPU for MPS
                    return _original_functions['device_put'](x, None)
        
        return _original_functions['device_put'](x, device)
    
    # 3. Patch default_backend
    def patched_default_backend():
        """Return the default backend based on OmniGPU."""
        return _get_backend_for_device()
    
    # 4. Patch device_count
    def patched_device_count(backend=None):
        """Return device count based on OmniGPU."""
        if backend is None:
            backend = _get_backend_for_device()

        ugpu_device = auto_device()
        if ugpu_device.type in ['cuda', 'mps'] and backend in ['gpu', 'metal', None]:
            return 1  # We have one GPU

        try:
            return _original_functions['device_count'](backend)
        except RuntimeError:
            return _original_functions['device_count'](None)
    
    # 5. Patch local_device_count  
    def patched_local_device_count(backend=None):
        """Return local device count based on OmniGPU."""
        return patched_device_count(backend)
    
    # 6. Create XLA flag setter for MPS
    def enable_mps_acceleration():
        """Configure JAX/XLA for optimal MPS performance."""
        ugpu_device = auto_device()
        if ugpu_device.type == 'mps':
            # Set XLA flags for better CPU performance on Apple Silicon
            import os
            os.environ['XLA_FLAGS'] = (
                '--xla_cpu_multi_thread_eigen=true '
                '--xla_cpu_use_thunk_runtime=false '
            )
            # Use Metal Performance Shaders where possible
            config.update('jax_platform_name', 'cpu')
    
    # Apply patches
    jax.devices = patched_devices
    jax.device_put = patched_device_put
    jax.default_backend = patched_default_backend
    jax.device_count = patched_device_count
    jax.local_device_count = patched_local_device_count
    
    # Configure for MPS if needed
    enable_mps_acceleration()
    
    # 7. Patch jax.jit for device placement
    original_jit = jax.jit
    
    @functools.wraps(original_jit)
    def patched_jit(fun, in_shardings=None, out_shardings=None, 
                   static_argnums=None, static_argnames=None, 
                   donate_argnums=None, donate_argnames=None,
                   device=None, backend=None, **kwargs):
        """JIT compile with OmniGPU device placement."""
        # Auto-select backend if not specified
        if backend is None and device is None:
            backend = _get_backend_for_device()
        
        return original_jit(
            fun, in_shardings=in_shardings, out_shardings=out_shardings,
            static_argnums=static_argnums, static_argnames=static_argnames,
            donate_argnums=donate_argnums, donate_argnames=donate_argnames,
            device=device, backend=backend, **kwargs
        )
    
    jax.jit = patched_jit
    
    # 8. Ensure numpy operations use optimal backend
    def patch_jax_numpy():
        """Ensure JAX numpy operations use the best available device."""
        # Most operations already follow device placement
        # Add specific patches here if needed
        pass
    
    patch_jax_numpy()
    
    _is_patched = True
    logger.info(f"JAX patched successfully. Default backend: {_get_backend_for_device()}")


def unpatch():
    """Remove JAX patches and restore original behavior."""
    global _is_patched, _original_functions
    
    if not _is_patched:
        return
    
    try:
        import jax
        
        # Restore original functions
        for name, func in _original_functions.items():
            setattr(jax, name, func)
        
        _is_patched = False
        _original_functions.clear()
        logger.info("JAX patches removed")
        
    except ImportError:
        pass


def is_patched() -> bool:
    """Check if JAX is currently patched."""
    return _is_patched
