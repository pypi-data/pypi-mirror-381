"""OmniGPU CLI tools."""

from .analyzer import main as analyze_main
from .commands import cli_main, get_device_info_impl, run_optimization_demo_impl, analyze_code_impl

# Expose programmatic interfaces
def get_device_info():
    """Get device information programmatically."""
    return get_device_info_impl()

def analyze_code(code):
    """Analyze code for CUDA compatibility programmatically."""
    return analyze_code_impl(code)

def run_optimization_demo():
    """Run optimization demo programmatically."""
    return run_optimization_demo_impl()

__all__ = ['analyze_main', 'cli_main', 'get_device_info', 'analyze_code', 'run_optimization_demo']