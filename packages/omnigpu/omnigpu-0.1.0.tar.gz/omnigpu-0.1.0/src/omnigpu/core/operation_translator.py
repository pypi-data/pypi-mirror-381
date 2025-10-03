"""Operation translation between CUDA and MPS."""
import torch
from typing import Dict, Optional, Callable, Any, Tuple, List
from dataclasses import dataclass
from enum import Enum
import warnings
import logging

logger = logging.getLogger(__name__)


class FallbackStrategy(Enum):
    """Fallback strategies for unsupported operations."""
    CPU_FALLBACK = "cpu_fallback"
    RAISE_ERROR = "raise_error"
    WARN_AND_CONTINUE = "warn_and_continue"
    ALTERNATIVE_OP = "alternative_op"


@dataclass
class OperationDescriptor:
    """Description of a translated operation."""
    original_op: str
    translated_op: str
    source_device: str
    target_device: str
    requires_wrapper: bool = False
    wrapper_func: Optional[Callable] = None
    notes: Optional[str] = None


@dataclass
class Strategy:
    """Fallback strategy descriptor."""
    strategy: FallbackStrategy
    alternative_op: Optional[str] = None
    warning_message: Optional[str] = None
    wrapper_func: Optional[Callable] = None


class OperationTranslator:
    """Translates operations between CUDA and MPS."""
    
    def __init__(self):
        self.operation_map = self._build_operation_map()
        self.fallback_strategies = self._build_fallback_strategies()
        self.operation_cache = {}
        
    def _build_operation_map(self) -> Dict[str, Dict[str, str]]:
        """Build mapping of operations between devices.
        
        Returns:
            Nested dict: {source_device: {operation: translated_operation}}
        """
        # Universal operations that work on all devices
        universal_ops = [
            # Basic math operations
            'torch.add', 'torch.sub', 'torch.mul', 'torch.div',
            'torch.matmul', 'torch.mm', 'torch.bmm',
            'torch.sum', 'torch.mean', 'torch.max', 'torch.min',
            'torch.abs', 'torch.sqrt', 'torch.pow', 'torch.exp', 'torch.log',
            
            # Activation functions
            'torch.relu', 'torch.sigmoid', 'torch.tanh', 'torch.softmax',
            'torch.nn.functional.relu', 'torch.nn.functional.sigmoid',
            
            # Tensor operations
            'torch.cat', 'torch.stack', 'torch.squeeze', 'torch.unsqueeze',
            'torch.transpose', 'torch.permute', 'torch.reshape', 'torch.view',
            
            # Reduction operations
            'torch.argmax', 'torch.argmin', 'torch.topk',
            
            # Linear algebra
            'torch.linalg.norm', 'torch.linalg.inv', 'torch.linalg.det',
        ]
        
        # Build operation map
        operation_map = {
            'cuda': {},
            'mps': {},
            'cpu': {}
        }
        
        # Universal operations map to themselves
        for op in universal_ops:
            for device in ['cuda', 'mps', 'cpu']:
                operation_map[device][op] = op
                
        # CUDA-specific to MPS translations
        cuda_to_mps = {
            # Device operations
            'tensor.cuda()': 'tensor.to("mps")',
            'model.cuda()': 'model.to("mps")',
            'torch.cuda.is_available()': 'torch.backends.mps.is_available()',
            'torch.cuda.device_count()': '1',  # MPS only has one device
            'torch.cuda.get_device_name()': '"Apple GPU"',
            'torch.cuda.empty_cache()': 'torch.mps.empty_cache()',
            'torch.cuda.memory_allocated()': 'torch.mps.current_allocated_memory()',
            'torch.cuda.memory_reserved()': 'torch.mps.driver_allocated_memory()',
            
            # Stream operations
            'torch.cuda.Stream()': 'None',  # MPS doesn't have explicit streams
            'torch.cuda.current_stream()': 'None',
            'torch.cuda.synchronize()': 'torch.mps.synchronize()',
            
            # Device management
            'torch.device("cuda")': 'torch.device("mps")',
            'torch.device("cuda:0")': 'torch.device("mps:0")',
            
            # Mixed precision
            'torch.cuda.amp.autocast()': 'torch.amp.autocast("mps")',
            'torch.cuda.amp.GradScaler()': 'torch.amp.GradScaler("mps")',
        }
        
        # Add CUDA to MPS translations
        for cuda_op, mps_op in cuda_to_mps.items():
            operation_map['cuda'][cuda_op] = mps_op
            
        # MPS to CUDA translations (reverse mapping)
        for cuda_op, mps_op in cuda_to_mps.items():
            # Create reverse mapping
            mps_key = mps_op.replace('"mps"', 'mps').replace("'mps'", 'mps')
            cuda_val = cuda_op.replace('"cuda"', 'cuda').replace("'cuda'", 'cuda')
            operation_map['mps'][mps_key] = cuda_val
            
        return operation_map
        
    def _build_fallback_strategies(self) -> Dict[str, Strategy]:
        """Build fallback strategies for operations."""
        strategies = {
            # CUDA-only operations
            'torch.cuda.nccl': Strategy(
                strategy=FallbackStrategy.CPU_FALLBACK,
                warning_message="NCCL operations not supported on MPS, falling back to CPU"
            ),
            
            # Complex CUDA kernels
            'torch.nn.functional.grid_sample': Strategy(
                strategy=FallbackStrategy.ALTERNATIVE_OP,
                alternative_op='torch.nn.functional.interpolate',
                warning_message="grid_sample may have different behavior on MPS"
            ),
            
            # Distributed operations
            'torch.distributed': Strategy(
                strategy=FallbackStrategy.WARN_AND_CONTINUE,
                warning_message="Distributed operations not supported on MPS"
            ),
            
            # Custom CUDA kernels
            'custom_cuda_kernel': Strategy(
                strategy=FallbackStrategy.RAISE_ERROR,
                warning_message="Custom CUDA kernels cannot be translated automatically"
            ),
        }
        
        return strategies
        
    def translate_operation(self, operation: str, source_device: str, 
                          target_device: str) -> OperationDescriptor:
        """Translate operation from source to target device.
        
        Args:
            operation: Operation to translate
            source_device: Source device type
            target_device: Target device type
            
        Returns:
            OperationDescriptor with translation details
        """
        # Check cache first
        cache_key = (operation, source_device, target_device)
        if cache_key in self.operation_cache:
            return self.operation_cache[cache_key]
            
        # Normalize device names
        source_device = source_device.split(':')[0]  # Remove device index
        target_device = target_device.split(':')[0]
        
        # If same device, no translation needed
        if source_device == target_device:
            descriptor = OperationDescriptor(
                original_op=operation,
                translated_op=operation,
                source_device=source_device,
                target_device=target_device
            )
            self.operation_cache[cache_key] = descriptor
            return descriptor
            
        # Look up translation
        if source_device in self.operation_map:
            device_map = self.operation_map[source_device]
            if operation in device_map:
                translated_op = device_map[operation]
                
                # Handle device-specific translations
                if target_device != 'cpu':
                    translated_op = translated_op.replace(source_device, target_device)
                    
                descriptor = OperationDescriptor(
                    original_op=operation,
                    translated_op=translated_op,
                    source_device=source_device,
                    target_device=target_device
                )
                self.operation_cache[cache_key] = descriptor
                return descriptor
                
        # No direct translation found, return as-is with note
        descriptor = OperationDescriptor(
            original_op=operation,
            translated_op=operation,
            source_device=source_device,
            target_device=target_device,
            notes=f"No translation found for {operation} from {source_device} to {target_device}"
        )
        self.operation_cache[cache_key] = descriptor
        return descriptor
        
    def is_supported(self, operation: str, device: str) -> bool:
        """Check if operation is supported on device.
        
        Args:
            operation: Operation to check
            device: Target device
            
        Returns:
            True if operation is supported
        """
        device = device.split(':')[0]  # Remove device index
        
        # Check if it's a universal operation
        if operation in self.operation_map.get(device, {}):
            return True
            
        # Check specific device support
        if device == 'cuda':
            # Most operations are supported on CUDA
            return not operation.startswith('torch.mps')
        elif device == 'mps':
            # Check for known unsupported operations
            unsupported_mps = [
                'torch.cuda.nccl',
                'torch.distributed',
                'torch.cuda.nvtx',
                'torch.jit.fuser',
                'torch.sparse',  # Limited support
            ]
            return not any(operation.startswith(unsup) for unsup in unsupported_mps)
        else:  # CPU
            # CPU supports most operations but not device-specific ones
            return not (operation.startswith('torch.cuda') or operation.startswith('torch.mps'))
            
    def get_fallback_strategy(self, operation: str, device: str) -> Strategy:
        """Get fallback strategy for unsupported operations.
        
        Args:
            operation: Operation that needs fallback
            device: Device where operation is not supported
            
        Returns:
            Strategy object with fallback approach
        """
        # Check if we have a specific strategy for this operation
        for op_pattern, strategy in self.fallback_strategies.items():
            if operation.startswith(op_pattern):
                return strategy
                
        # Default strategy based on device
        if device == 'mps':
            return Strategy(
                strategy=FallbackStrategy.CPU_FALLBACK,
                warning_message=f"Operation {operation} not supported on MPS, falling back to CPU"
            )
        else:
            return Strategy(
                strategy=FallbackStrategy.WARN_AND_CONTINUE,
                warning_message=f"Operation {operation} may not be optimal on {device}"
            )
            
    def translate_device_string(self, device_string: str, target_backend: str) -> str:
        """Translate device string to target backend.
        
        Args:
            device_string: Original device string (e.g., "cuda:0")
            target_backend: Target backend ("cuda", "mps", "cpu")
            
        Returns:
            Translated device string
        """
        # Handle common patterns
        if 'cuda' in device_string:
            if target_backend == 'mps':
                # MPS only has device 0
                return 'mps:0' if ':' in device_string else 'mps'
            elif target_backend == 'cpu':
                return 'cpu'
                
        elif 'mps' in device_string:
            if target_backend == 'cuda':
                # Default to cuda:0
                return 'cuda:0' if ':' in device_string else 'cuda'
            elif target_backend == 'cpu':
                return 'cpu'
                
        return device_string
        
    def get_equivalent_operations(self, operation: str) -> Dict[str, str]:
        """Get equivalent operations across all devices.
        
        Args:
            operation: Operation to find equivalents for
            
        Returns:
            Dict mapping device to equivalent operation
        """
        equivalents = {}
        
        for device in ['cuda', 'mps', 'cpu']:
            # Try to find translation
            descriptor = self.translate_operation(operation, 'cuda', device)
            equivalents[device] = descriptor.translated_op
            
        return equivalents
        
    def clear_cache(self) -> None:
        """Clear operation translation cache."""
        self.operation_cache.clear()
        logger.info("Operation translation cache cleared")


# Global translator instance
_global_translator = None


def get_operation_translator() -> OperationTranslator:
    """Get global operation translator instance."""
    global _global_translator
    if _global_translator is None:
        _global_translator = OperationTranslator()
    return _global_translator