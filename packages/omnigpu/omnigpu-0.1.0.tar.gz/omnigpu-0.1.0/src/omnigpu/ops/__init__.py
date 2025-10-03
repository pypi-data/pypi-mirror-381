"""OmniGPU operation patches module."""

from .missing_ops import patch_missing_operations
from .extended_ops import patch_all_failed_operations

__all__ = ['patch_missing_operations', 'patch_all_failed_operations']