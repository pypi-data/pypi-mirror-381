"""Enhanced CUDA compatibility layer for OmniGPU."""

import torch
import sys
from unittest.mock import MagicMock

def patch_cuda_detection():
    """Patch CUDA availability checks to work with OmniGPU."""
    
    # 1. Make torch think CUDA is available
    original_is_available = torch.cuda.is_available
    def omnigpu_is_available():
        # Return True if MPS is available
        if hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
            return True
        return original_is_available()
    
    torch.cuda.is_available = omnigpu_is_available
    
    # 2. Fix "Torch not compiled with CUDA enabled" errors
    if not hasattr(torch._C, '_cuda_isDriverSufficient'):
        torch._C._cuda_isDriverSufficient = lambda: True
    
    # 3. Mock CUDA module attributes
    cuda_attrs = {
        'is_available': omnigpu_is_available,
        'device_count': lambda: 1 if torch.backends.mps.is_available() else 0,
        'current_device': lambda: 0,
        'get_device_name': lambda idx=0: "Apple Silicon GPU (OmniGPU)",
        'get_device_capability': lambda idx=0: (8, 0),  # Fake compute capability
        'get_arch_list': lambda: ['sm_80'],
        'is_bf16_supported': lambda: True,
        '_is_compiled': lambda: True,
        '_lazy_init': lambda: None,  # Prevent libcudart errors
        '_initialized': True,
    }
    
    for attr, value in cuda_attrs.items():
        if not hasattr(torch.cuda, attr):
            setattr(torch.cuda, attr, value)
    
    # 4. Fix torch._C CUDA attributes
    if not hasattr(torch._C, '_cuda_getDeviceCount'):
        torch._C._cuda_getDeviceCount = lambda: 1 if torch.backends.mps.is_available() else 0
    
    # 5. Add CUDA runtime version info
    if not hasattr(torch.version, 'cuda'):
        torch.version.cuda = "11.8"  # Fake CUDA version
    
    print("✅ Enhanced CUDA compatibility patching complete")