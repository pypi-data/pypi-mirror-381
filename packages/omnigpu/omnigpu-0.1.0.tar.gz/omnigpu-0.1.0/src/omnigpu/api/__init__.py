"""OmniGPU API module."""
from .tensor_api import *
from .model_api import *

__all__ = [
    # From tensor_api
    'auto_device', 'zeros', 'ones', 'randn', 'tensor',
    'to_device', 'get_tensor_device', 'is_gpu_tensor',
    'empty_cache', 'get_device_info', 'available_devices',
    'gpu_available', 'set_device_preference',
    
    # From model_api
    'load_model', 'save_model', 'optimize_model',
    'wrap_model', 'distribute_model', 'get_model_info'
]