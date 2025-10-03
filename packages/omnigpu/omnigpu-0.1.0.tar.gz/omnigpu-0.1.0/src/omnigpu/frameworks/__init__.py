"""Framework-specific patches for OmniGPU."""

from typing import List, Optional

# Only list frameworks we actually support
SUPPORTED_FRAMEWORKS = ['pytorch', 'jax']

def detect_available_frameworks() -> List[str]:
    """Detect which ML frameworks are installed."""
    available = []
    
    try:
        import torch
        available.append('pytorch')
    except ImportError:
        pass
    
    try:
        import jax
        available.append('jax')
    except ImportError:
        pass
        
    # Note: TensorFlow and CuPy support planned for future releases
    
    return available


def patch_framework(framework: str) -> bool:
    """Patch a specific framework for OmniGPU compatibility."""
    if framework == 'pytorch':
        from ..auto_patch import patch
        patch()
        return True
    
    elif framework == 'jax':
        from .jax_patch import patch as patch_jax
        patch_jax()
        return True
        
    # TensorFlow and CuPy support coming in future releases
    elif framework in ['tensorflow', 'cupy']:
        print(f"Warning: {framework} support is not yet implemented")
        return False
    
    return False


def patch_all_available():
    """Patch all available frameworks."""
    frameworks = detect_available_frameworks()
    patched = []
    
    for framework in frameworks:
        if patch_framework(framework):
            patched.append(framework)
    
    return patched