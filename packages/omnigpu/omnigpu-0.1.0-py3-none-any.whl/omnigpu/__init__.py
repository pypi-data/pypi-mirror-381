"""OmniGPU Library - Write once, run anywhere GPU computing.

OmniGPU provides seamless GPU computation across CUDA and Metal Performance
Shaders (MPS), with automatic device detection, memory management, and optimization.

Key Features:
    - Automatic device detection and selection
    - Transparent CUDA-to-MPS translation via auto-patching
    - Graph-level optimizations with operation fusion
    - Memory-efficient tensor operations
    - CPU fallback for maximum compatibility

Quick Start:
    >>> import omnigpu as ugpu
    >>> device = ugpu.auto_device()  # Automatically selects best GPU
    >>> tensor = ugpu.randn(100, 100)  # Creates tensor on best device
    >>> model = ugpu.to_device(model)  # Moves model to best device

For CUDA compatibility:
    >>> import omnigpu
    >>> omnigpu.enable_cuda_compatibility()
    >>> # Now all CUDA calls work on any GPU!
    >>> model.cuda()  # Works on MPS/CPU too
"""

import logging
from typing import Optional

__version__ = "0.1.0"

# Make version accessible for legacy tooling
VERSION = __version__

# Configure default logging (no output unless user opts in)
logging.getLogger("omnigpu").addHandler(logging.NullHandler())

# Import core functionality
from .core.device_manager import get_device_manager
from .core.memory_manager import get_memory_manager  
from .core.precision_manager import get_precision_manager
from .core.error_handler import get_error_handler

# Import main APIs
from .api.tensor_api import (
    auto_device,
    zeros, ones, randn, tensor,
    to_device, get_tensor_device, is_gpu_tensor,
    empty_cache, get_device_info,
    available_devices, gpu_available,
    set_device_preference
)

from .api.model_api import (
    load_model, save_model,
    optimize_model, wrap_model,
    distribute_model, get_model_info
)

# Configuration functions
def configure(device_preference=None, precision_policy=None, 
              memory_strategy=None, optimization_level=None,
              fallback_enabled=True):
    """Configure universal GPU behavior.
    
    Args:
        device_preference: List of preferred devices in order
        precision_policy: 'auto', 'highest', 'fastest', 'mixed'
        memory_strategy: 'auto', 'conservative', 'aggressive'
        optimization_level: 'off', 'basic', 'auto', 'aggressive'
        fallback_enabled: Whether to enable automatic fallbacks
    """
    if device_preference is not None:
        get_device_manager().set_device_preference(device_preference)
        
    if precision_policy is not None:
        get_precision_manager().set_precision_policy(precision_policy)
        
    if fallback_enabled is not None:
        get_error_handler().set_fallback_enabled(fallback_enabled)
        
    # Future: memory_strategy and optimization_level configuration


def get_config():
    """Get current OmniGPU configuration.
    
    Returns:
        Dict[str, Any]: Configuration dictionary containing:
            - device_preference: Ordered list of preferred device types
            - precision_policy: Current precision handling policy
            - fallback_enabled: Whether automatic fallback is enabled
            - version: Library version string
    
    Example:
        >>> config = ugpu.get_config()
        >>> print(config['device_preference'])
        ['cuda', 'mps', 'cpu']
    """
    return {
        'device_preference': get_device_manager()._device_preferences,
        'precision_policy': get_precision_manager().precision_policy,
        'fallback_enabled': get_error_handler().fallback_enabled,
        'version': __version__
    }


def reset_config():
    """Reset OmniGPU to default configuration.
    
    Resets all settings to their default values:
        - Device preference: ['cuda', 'mps', 'cpu']
        - Precision policy: 'auto'
        - Fallback enabled: True
    
    Example:
        >>> ugpu.configure(device_preference=['cpu'])
        >>> ugpu.reset_config()  # Back to defaults
    """
    get_device_manager()._device_preferences = ['cuda', 'mps', 'cpu']
    get_precision_manager().precision_policy = 'auto'
    get_error_handler().set_fallback_enabled(True)


def configure_logging(level: int = logging.INFO,
                      handler: Optional[logging.Handler] = None,
                      propagate: bool = False,
                      formatter: Optional[logging.Formatter] = None,
                      reset_handlers: bool = False) -> None:
    """Configure logging for OmniGPU.

    Args:
        level: Logging level for the root ``omnigpu`` logger.
        handler: Optional handler to attach. If omitted, uses ``StreamHandler``.
        propagate: Whether log records should propagate to ancestor loggers.
        formatter: Optional ``logging.Formatter`` applied to the handler.
        reset_handlers: Remove existing handlers before attaching the new one.
    """

    logger = logging.getLogger("omnigpu")

    if reset_handlers:
        for existing in list(logger.handlers):
            logger.removeHandler(existing)

    if handler is None:
        handler = logging.StreamHandler()

    if formatter is None:
        formatter = logging.Formatter("[%(levelname)s] %(name)s: %(message)s")

    if hasattr(handler, "setFormatter"):
        handler.setFormatter(formatter)

    if handler not in logger.handlers:
        logger.addHandler(handler)

    logger.setLevel(level)
    logger.propagate = propagate


# Import optimization functionality
try:
    from .optimization import optimize_graph, GraphOptimizer, OptimizationStats
except ImportError:
    # Optimization module not available
    optimize_graph = None
    GraphOptimizer = None
    OptimizationStats = None

# Import fusion engine
try:
    from .fusion_engine import (
        FusionEngine, enable_fusion, disable_fusion,
        optimize_model_for_fusion, fusion_scope, get_fusion_stats
    )
    from .metal_kernels import create_metal_optimized_model
except ImportError:
    FusionEngine = None
    enable_fusion = None
    disable_fusion = None
    optimize_model_for_fusion = None
    fusion_scope = None
    get_fusion_stats = None
    create_metal_optimized_model = None

# Import framework patching
try:
    from .frameworks import detect_available_frameworks, patch_framework, patch_all_available
except ImportError:
    detect_available_frameworks = None
    patch_framework = None
    patch_all_available = None

# Import auto-patching functionality
try:
    from .auto_patch import patch, patch_all, patch_on_import, unpatch, is_patched, get_patch_info
    
    def enable_cuda_compatibility(enhanced=True):
        """Enable automatic CUDA-to-MPS translation for existing PyTorch code.
        
        This makes CUDA code run seamlessly on Apple Silicon and other devices.
        
        Args:
            enhanced: Whether to apply comprehensive patches including missing operations
                     and improved CUDA compatibility. Default is True.
        
        Example:
            >>> import omnigpu as ugpu
            >>> ugpu.enable_cuda_compatibility()
            >>> # Now your CUDA code works on any device!
            >>> model.cuda()  # Works on MPS/CPU too
            >>> x = torch.randn(100, 100).cuda()  # Works on MPS!
        """
        if enhanced:
            return patch_all()
        else:
            return patch()
    
    def patch_pytorch():
        """Legacy function for backward compatibility. Use enable_cuda_compatibility() instead."""
        return enable_cuda_compatibility(enhanced=True)
    
    # Aliases for convenience
    enable = enable_cuda_compatibility
    disable = unpatch
        
except ImportError:
    enable_cuda_compatibility = None
    patch_all = None
    patch = None
    patch_pytorch = None
    patch_on_import = None
    unpatch = None
    is_patched = None
    get_patch_info = None
    enable = None
    disable = None

# Import profiler
try:
    from .profiler import (
        Profiler, profile, profile_range,
        start_profiling, stop_profiling, get_profiler,
        visualize_profile
    )
except ImportError:
    Profiler = None
    profile = None
    profile_range = None
    start_profiling = None
    stop_profiling = None
    get_profiler = None
    visualize_profile = None

# Convenience imports
from . import core
from . import api

__all__ = [
    # Version
    '__version__',
    
    # Device functions
    'auto_device',
    'available_devices', 
    'gpu_available',
    'get_device_info',
    'set_device_preference',
    
    # Tensor functions
    'zeros', 'ones', 'randn', 'tensor',
    'to_device', 'get_tensor_device', 'is_gpu_tensor',
    
    # Memory functions
    'empty_cache',
    
    # Model functions
    'load_model', 'save_model',
    'optimize_model', 'wrap_model', 
    'distribute_model', 'get_model_info',
    
    # Configuration
    'configure', 'get_config', 'reset_config',
    'configure_logging',
    
    # Core modules
    'core', 'api',
    
    # Optimization (if available)
    'optimize_graph', 'GraphOptimizer', 'OptimizationStats',
    
    # Fusion Engine (if available)
    'FusionEngine', 'enable_fusion', 'disable_fusion',
    'optimize_model_for_fusion', 'fusion_scope', 'get_fusion_stats',
    'create_metal_optimized_model',
    
    # Framework patching (if available)
    'detect_available_frameworks', 'patch_framework', 'patch_all_available',
    
    # CUDA compatibility (if available)
    'enable_cuda_compatibility', 'patch_all', 'patch', 'patch_pytorch',
    'unpatch', 'is_patched', 'get_patch_info', 'enable', 'disable',
    'patch_on_import',
    
    # Profiler (if available)
    'Profiler', 'profile', 'profile_range',
    'start_profiling', 'stop_profiling', 'get_profiler',
    'visualize_profile'
]


# Auto-enable CUDA compatibility on import
# Users can control this with OMNIGPU_AUTO_PATCH environment variable
if patch_on_import is not None:
    # The patch_on_import function handles all the logic for checking
    # environment variables and applying patches appropriately
    patch_on_import()
