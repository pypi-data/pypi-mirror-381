"""Memory management across different devices."""
import torch
from typing import Dict, Optional, Tuple, List, Any
from dataclasses import dataclass
import warnings
import logging
from contextlib import contextmanager
import gc

from .device_manager import get_device_manager, DeviceType

logger = logging.getLogger(__name__)


@dataclass
class MemoryStats:
    """Memory statistics for a device."""
    device: str
    allocated: int
    reserved: int
    free: int
    total: int
    peak_allocated: int
    num_allocs: int
    num_frees: int
    
    @property
    def utilization(self) -> float:
        """Memory utilization percentage."""
        if self.total == 0:
            return 0.0
        return (self.allocated / self.total) * 100
        
    @property
    def fragmentation(self) -> float:
        """Memory fragmentation percentage."""
        if self.reserved == 0:
            return 0.0
        return ((self.reserved - self.allocated) / self.reserved) * 100


class MemoryManager:
    """Manages memory across different devices."""
    
    def __init__(self):
        self.device_manager = get_device_manager()
        self.memory_limits: Dict[str, int] = {}
        self.allocation_history: List[Dict[str, Any]] = []
        self.enable_profiling = False
        self._peak_memory: Dict[str, int] = {}
        
    def get_memory_stats(self, device: Optional[str] = None) -> MemoryStats:
        """Get memory statistics for a device.
        
        Args:
            device: Device string, or None for current device
            
        Returns:
            MemoryStats object
        """
        if device is None:
            device = str(self.device_manager.get_current_device())
            
        device_type = device.split(':')[0]
        
        if device_type == 'cuda':
            device_idx = 0 if ':' not in device else int(device.split(':')[1])
            
            # Get CUDA memory stats
            props = torch.cuda.get_device_properties(device_idx)
            allocated = torch.cuda.memory_allocated(device_idx)
            reserved = torch.cuda.memory_reserved(device_idx)
            
            # Track peak memory
            peak = torch.cuda.max_memory_allocated(device_idx)
            if device not in self._peak_memory:
                self._peak_memory[device] = peak
            else:
                self._peak_memory[device] = max(self._peak_memory[device], peak)
                
            stats = torch.cuda.memory_stats(device_idx) if hasattr(torch.cuda, 'memory_stats') else {}
            
            return MemoryStats(
                device=device,
                allocated=allocated,
                reserved=reserved,
                free=props.total_memory - allocated,
                total=props.total_memory,
                peak_allocated=self._peak_memory[device],
                num_allocs=stats.get('allocation.all.allocated', 0),
                num_frees=stats.get('allocation.all.freed', 0)
            )
            
        elif device_type == 'mps':
            # Get MPS memory stats
            total = self.device_manager.get_memory_info(device).total
            
            if hasattr(torch.mps, 'current_allocated_memory'):
                allocated = torch.mps.current_allocated_memory()
            else:
                allocated = 0
                
            if hasattr(torch.mps, 'driver_allocated_memory'):
                reserved = torch.mps.driver_allocated_memory()
            else:
                reserved = allocated
                
            # Track peak memory
            if device not in self._peak_memory:
                self._peak_memory[device] = allocated
            else:
                self._peak_memory[device] = max(self._peak_memory[device], allocated)
                
            return MemoryStats(
                device=device,
                allocated=allocated,
                reserved=reserved,
                free=total - allocated,
                total=total,
                peak_allocated=self._peak_memory[device],
                num_allocs=0,  # MPS doesn't provide this
                num_frees=0
            )
            
        else:  # CPU
            import psutil
            memory = psutil.virtual_memory()
            
            # Track peak memory (approximate)
            if device not in self._peak_memory:
                self._peak_memory[device] = memory.used
            else:
                self._peak_memory[device] = max(self._peak_memory[device], memory.used)
                
            return MemoryStats(
                device=device,
                allocated=memory.used,
                reserved=memory.total,
                free=memory.available,
                total=memory.total,
                peak_allocated=self._peak_memory[device],
                num_allocs=0,  # CPU doesn't track this
                num_frees=0
            )
            
    def empty_cache(self, device: Optional[str] = None) -> None:
        """Clear memory cache on device.
        
        Args:
            device: Device to clear cache on, or None for all devices
        """
        if device is None:
            # Clear cache on all available devices
            for device_str in self.device_manager.available_devices():
                self.empty_cache(device_str)
            return
            
        device_type = device.split(':')[0]
        
        if device_type == 'cuda':
            torch.cuda.empty_cache()
            logger.info(f"Cleared CUDA cache on {device}")
            
        elif device_type == 'mps':
            if hasattr(torch.mps, 'empty_cache'):
                torch.mps.empty_cache()
                logger.info(f"Cleared MPS cache on {device}")
            else:
                logger.warning("MPS cache clearing not available in this PyTorch version")
                
        else:  # CPU
            # Force garbage collection for CPU memory
            gc.collect()
            logger.info("Forced garbage collection for CPU memory")
            
    def set_memory_limit(self, device: str, limit_bytes: int) -> None:
        """Set memory limit for a device.
        
        Args:
            device: Device to set limit for
            limit_bytes: Memory limit in bytes
        """
        self.memory_limits[device] = limit_bytes
        logger.info(f"Set memory limit for {device} to {limit_bytes / (1024**3):.2f} GB")
        
        # Apply limit if possible
        device_type = device.split(':')[0]
        if device_type == 'cuda':
            device_idx = 0 if ':' not in device else int(device.split(':')[1])
            if hasattr(torch.cuda, 'set_per_process_memory_fraction'):
                total_memory = torch.cuda.get_device_properties(device_idx).total_memory
                fraction = limit_bytes / total_memory
                torch.cuda.set_per_process_memory_fraction(fraction, device_idx)
                
    def check_memory_available(self, size_bytes: int, device: str) -> bool:
        """Check if enough memory is available for allocation.
        
        Args:
            size_bytes: Size of allocation in bytes
            device: Target device
            
        Returns:
            True if enough memory is available
        """
        stats = self.get_memory_stats(device)
        
        # Check against limit if set
        if device in self.memory_limits:
            available = self.memory_limits[device] - stats.allocated
        else:
            available = stats.free
            
        return available >= size_bytes
        
    def optimize_memory_layout(self, tensors: List[torch.Tensor]) -> List[torch.Tensor]:
        """Optimize memory layout of tensors for better performance.
        
        Args:
            tensors: List of tensors to optimize
            
        Returns:
            List of optimized tensors
        """
        optimized = []
        
        for tensor in tensors:
            # Ensure tensor is contiguous
            if not tensor.is_contiguous():
                tensor = tensor.contiguous()
                logger.debug(f"Made tensor contiguous: shape={tensor.shape}")
                
            # Consider memory format based on tensor dimensions
            if len(tensor.shape) == 4:  # Likely a conv tensor
                # Use channels_last format for better performance
                if tensor.device.type in ['cuda', 'mps']:
                    tensor = tensor.to(memory_format=torch.channels_last)
                    logger.debug(f"Converted to channels_last format: shape={tensor.shape}")
                    
            optimized.append(tensor)
            
        return optimized
        
    @contextmanager
    def memory_efficient_mode(self, device: Optional[str] = None):
        """Context manager for memory-efficient computation.
        
        Args:
            device: Device to optimize for, or None for current device
        """
        if device is None:
            device = str(self.device_manager.get_current_device())
            
        # Store original settings
        original_empty_cache_threshold = getattr(self, '_empty_cache_threshold', None)
        
        # Enable memory-efficient settings
        self._empty_cache_threshold = 0.8  # Empty cache when 80% full
        
        # Clear cache before starting
        self.empty_cache(device)
        
        try:
            yield
        finally:
            # Restore original settings
            if original_empty_cache_threshold is not None:
                self._empty_cache_threshold = original_empty_cache_threshold
            else:
                delattr(self, '_empty_cache_threshold')
                
            # Final cache clear
            self.empty_cache(device)
            
    def get_optimal_batch_size(self, model: torch.nn.Module, input_shape: Tuple[int, ...], 
                             device: str, target_utilization: float = 0.8) -> int:
        """Estimate optimal batch size for model and device.
        
        Args:
            model: PyTorch model
            input_shape: Shape of single input (without batch dimension)
            device: Target device
            target_utilization: Target memory utilization (0-1)
            
        Returns:
            Estimated optimal batch size
        """
        # Move model to device
        model = model.to(device)
        model.eval()
        
        # Get current memory usage
        self.empty_cache(device)
        stats_before = self.get_memory_stats(device)
        
        # Try forward pass with batch size 1
        batch_size = 1
        test_input = torch.randn(batch_size, *input_shape, device=device)
        
        try:
            with torch.no_grad():
                _ = model(test_input)
                
            # Get memory usage after forward pass
            stats_after = self.get_memory_stats(device)
            memory_per_sample = stats_after.allocated - stats_before.allocated
            
            # Calculate available memory
            if device in self.memory_limits:
                available_memory = self.memory_limits[device] * target_utilization
            else:
                available_memory = stats_before.total * target_utilization
                
            # Estimate optimal batch size
            optimal_batch_size = int((available_memory - stats_before.allocated) / memory_per_sample)
            
            # Ensure at least batch size 1
            optimal_batch_size = max(1, optimal_batch_size)
            
            logger.info(f"Estimated optimal batch size: {optimal_batch_size} for {device}")
            return optimal_batch_size
            
        except RuntimeError as e:
            if 'out of memory' in str(e):
                logger.warning(f"OOM with batch size 1, model may be too large for {device}")
                return 0
            raise
            
        finally:
            self.empty_cache(device)
            
    def profile_memory_usage(self, func: callable, *args, device: str = None, **kwargs) -> Tuple[Any, MemoryStats]:
        """Profile memory usage of a function.
        
        Args:
            func: Function to profile
            *args: Function arguments
            device: Device to profile on
            **kwargs: Function keyword arguments
            
        Returns:
            Tuple of (function result, memory stats)
        """
        if device is None:
            device = str(self.device_manager.get_current_device())
            
        # Clear cache and get baseline
        self.empty_cache(device)
        stats_before = self.get_memory_stats(device)
        
        # Run function
        result = func(*args, **kwargs)
        
        # Get memory usage after
        stats_after = self.get_memory_stats(device)
        
        # Calculate memory used
        memory_used = MemoryStats(
            device=device,
            allocated=stats_after.allocated - stats_before.allocated,
            reserved=stats_after.reserved - stats_before.reserved,
            free=stats_after.free,
            total=stats_after.total,
            peak_allocated=stats_after.peak_allocated,
            num_allocs=stats_after.num_allocs - stats_before.num_allocs,
            num_frees=stats_after.num_frees - stats_before.num_frees
        )
        
        if self.enable_profiling:
            self.allocation_history.append({
                'function': func.__name__,
                'device': device,
                'memory_allocated': memory_used.allocated,
                'memory_reserved': memory_used.reserved
            })
            
        return result, memory_used
        
    def get_memory_summary(self) -> Dict[str, Dict[str, Any]]:
        """Get memory summary for all devices.
        
        Returns:
            Dict mapping device to memory information
        """
        summary = {}
        
        for device in self.device_manager.available_devices():
            try:
                stats = self.get_memory_stats(device)
                summary[device] = {
                    'allocated_gb': stats.allocated / (1024**3),
                    'reserved_gb': stats.reserved / (1024**3),
                    'free_gb': stats.free / (1024**3),
                    'total_gb': stats.total / (1024**3),
                    'utilization_pct': stats.utilization,
                    'fragmentation_pct': stats.fragmentation
                }
                
                if device in self.memory_limits:
                    summary[device]['limit_gb'] = self.memory_limits[device] / (1024**3)
                    
            except Exception as e:
                logger.warning(f"Failed to get memory stats for {device}: {e}")
                summary[device] = {'error': str(e)}
                
        return summary


# Global memory manager instance
_global_memory_manager = None


def get_memory_manager() -> MemoryManager:
    """Get global memory manager instance."""
    global _global_memory_manager
    if _global_memory_manager is None:
        _global_memory_manager = MemoryManager()
    return _global_memory_manager