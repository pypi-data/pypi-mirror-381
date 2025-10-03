"""Device detection and management for OmniGPU."""
import torch
import warnings
from typing import List, Dict, Any, Optional, Set, Union
from dataclasses import dataclass
from enum import Enum
import logging

logger = logging.getLogger("omnigpu.device_manager")


class DeviceType(Enum):
    """Enumeration of supported device types.
    
    Attributes:
        CUDA: NVIDIA CUDA-enabled GPUs
        MPS: Apple Metal Performance Shaders
        CPU: CPU fallback device
    """
    CUDA = "cuda"
    MPS = "mps"
    CPU = "cpu"


@dataclass
class Device:
    """Container for device information.
    
    Attributes:
        type: Device type (cuda, mps, or cpu)
        index: Device index (0 for primary device)
        name: Human-readable device name
        memory: Total device memory in bytes (None for CPU)
        compute_capability: CUDA compute capability (None for non-CUDA)
    """
    type: str
    index: int
    name: str
    memory: Optional[int]  # in bytes
    compute_capability: Optional[float]
    
    @property
    def device_string(self) -> str:
        """Get PyTorch-compatible device string.
        
        Returns:
            String representation suitable for torch.device()
            e.g., 'cuda', 'cuda:1', 'mps', 'cpu'
        """
        if self.type == DeviceType.CPU.value:
            return self.type
        if self.index == 0:
            return self.type
        return f"{self.type}:{self.index}"
    
    def to_torch_device(self) -> torch.device:
        """Convert to PyTorch device object.
        
        Returns:
            torch.device: PyTorch device object for this device
        """
        if self.type in (DeviceType.CUDA.value, DeviceType.MPS.value):
            return torch.device(f"{self.type}:{self.index}")
        return torch.device(self.type)


@dataclass
class MemoryInfo:
    """Container for device memory information.
    
    Attributes:
        total: Total device memory in bytes
        allocated: Currently allocated memory in bytes
        reserved: Reserved memory in bytes
        available: Available memory in bytes
    """
    total: int
    allocated: int
    reserved: int
    available: int
    
    @property
    def utilization(self) -> float:
        """Calculate memory utilization percentage.
        
        Returns:
            float: Memory utilization as percentage (0-100)
        """
        if self.total == 0:
            return 0.0
        return (self.allocated / self.total) * 100


@dataclass
class DeviceInfo:
    """Comprehensive device information container.
    
    Attributes:
        device: Basic device information
        memory_info: Memory usage statistics
        features: Dictionary of supported features
        compute_capability: String representation of compute capability
    """
    device: Device
    memory_info: MemoryInfo
    features: Dict[str, bool]
    compute_capability: Optional[str]


class DeviceManager:
    """Central hub for device detection and management.
    
    Handles automatic device detection, preference-based selection,
    and memory management across different GPU backends.
    
    Attributes:
        _available_devices: Cached list of detected devices
        _device_capabilities: Detailed capabilities per device
        _current_device: Currently selected device
        _device_preferences: Ordered list of preferred device types
        _cache_enabled: Whether to cache device detection results
    """
    
    def __init__(self):
        """Initialize DeviceManager with default preferences."""
        self._available_devices: Optional[List[Device]] = None
        self._device_capabilities: Dict[str, DeviceInfo] = {}
        self._current_device: Optional[torch.device] = None
        self._device_preferences = [DeviceType.CUDA.value, DeviceType.MPS.value, DeviceType.CPU.value]
        self._cache_enabled = True
        
    def detect_devices(self) -> List[Device]:
        """Detect all available GPU devices.
        
        Returns:
            List of available devices
        """
        if self._available_devices is not None and self._cache_enabled:
            return self._available_devices
            
        devices = []
        
        # CUDA detection
        try:
            if torch.cuda.is_available():
                for i in range(torch.cuda.device_count()):
                    props = torch.cuda.get_device_properties(i)
                    devices.append(Device(
                        type=DeviceType.CUDA.value,
                        index=i,
                        name=props.name,
                        memory=props.total_memory,
                        compute_capability=float(f"{props.major}.{props.minor}")
                    ))
                    logger.info(f"Detected CUDA device {i}: {props.name}")
        except Exception as e:
            logger.warning(f"CUDA detection failed: {e}")
            
        # MPS detection
        try:
            if hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
                # MPS doesn't expose multiple devices, treat as single device
                devices.append(Device(
                    type=DeviceType.MPS.value,
                    index=0,
                    name='Apple GPU',
                    memory=self._get_mps_memory(),
                    compute_capability=None
                ))
                logger.info("Detected MPS (Apple Metal) device")
        except Exception as e:
            logger.warning(f"MPS detection failed: {e}")
            
        # CPU always available
        devices.append(Device(
            type=DeviceType.CPU.value,
            index=0,
            name='CPU',
            memory=self._get_system_memory(),
            compute_capability=None
        ))
        
        self._available_devices = devices
        return devices
        
    def get_device_info(self, device: Optional[Union[str, torch.device]] = None) -> DeviceInfo:
        """Get detailed device information.
        
        Args:
            device: Device string or torch.device, or None for current device
            
        Returns:
            DeviceInfo object with complete device details
        """
        if device is None:
            device = str(self.get_current_device())
        elif isinstance(device, torch.device):
            device = str(device)
            
        # Return cached info if available
        if device in self._device_capabilities:
            return self._device_capabilities[device]
            
        # Find the device
        device_obj = None
        
        # Normalize device string (e.g., "mps:0" -> "mps" for index 0)
        normalized_device = device
        if ":" in device:
            dev_type, dev_idx = device.split(":", 1)
            if dev_idx == "0":
                normalized_device = dev_type
        
        for d in self.detect_devices():
            if d.device_string == device or d.device_string == normalized_device or d.type == normalized_device:
                device_obj = d
                break
                
        if device_obj is None:
            raise ValueError(f"Device {device} not found")
            
        # Get memory info
        memory_info = self.get_memory_info(device)
        
        # Get device features
        features = self._detect_device_features(device_obj)
        
        # Create DeviceInfo
        info = DeviceInfo(
            device=device_obj,
            memory_info=memory_info,
            features=features,
            compute_capability=str(device_obj.compute_capability) if device_obj.compute_capability else None
        )
        
        # Cache the info
        self._device_capabilities[device] = info
        
        return info
        
    def select_best_device(self) -> torch.device:
        """Auto-select optimal device based on availability and preferences.
        
        Returns:
            torch.device: The selected device
        """
        available_devices = self.detect_devices()
        
        # Check preferences in order
        for preferred_type in self._device_preferences:
            for device in available_devices:
                if device.type == preferred_type:
                    selected = device.to_torch_device()
                    logger.info(f"Selected device: {selected}")
                    return selected
                    
        # Fallback to CPU (should always be available)
        return torch.device('cpu')
        
    def get_memory_info(self, device: str) -> MemoryInfo:
        """Get memory information for device.
        
        Args:
            device: Device string
            
        Returns:
            MemoryInfo object
        """
        if device.startswith('cuda'):
            device_idx = 0 if ':' not in device else int(device.split(':')[1])
            torch_device = torch.device(f'cuda:{device_idx}')
            
            # Ensure we're getting info for the right device
            with torch.cuda.device(torch_device):
                return MemoryInfo(
                    total=torch.cuda.get_device_properties(device_idx).total_memory,
                    allocated=torch.cuda.memory_allocated(device_idx),
                    reserved=torch.cuda.memory_reserved(device_idx),
                    available=torch.cuda.get_device_properties(device_idx).total_memory - 
                             torch.cuda.memory_allocated(device_idx)
                )
        elif device.startswith('mps'):
            # MPS memory tracking
            if hasattr(torch.mps, 'driver_allocated_memory'):
                total = self._get_mps_memory()
                allocated = torch.mps.current_allocated_memory() if hasattr(torch.mps, 'current_allocated_memory') else 0
                return MemoryInfo(
                    total=total,
                    allocated=allocated,
                    reserved=torch.mps.driver_allocated_memory() if hasattr(torch.mps, 'driver_allocated_memory') else allocated,
                    available=total - allocated
                )
            else:
                # Fallback for older PyTorch versions
                total = self._get_mps_memory()
                return MemoryInfo(
                    total=total,
                    allocated=0,
                    reserved=0,
                    available=total
                )
        else:  # CPU
            import psutil
            memory = psutil.virtual_memory()
            return MemoryInfo(
                total=memory.total,
                allocated=memory.used,
                reserved=memory.total,
                available=memory.available
            )
            
    def available_devices(self) -> List[str]:
        """Get list of available device strings.
        
        Returns:
            List of device strings like ['cuda:0', 'cuda:1', 'mps:0', 'cpu:0']
        """
        devices = self.detect_devices()
        return [d.device_string for d in devices]
        
    def gpu_available(self) -> bool:
        """Check if any GPU is available.
        
        Returns:
            True if CUDA or MPS available, False otherwise
        """
        devices = self.detect_devices()
        return any(d.type in [DeviceType.CUDA.value, DeviceType.MPS.value] for d in devices)
        
    def set_device_preference(self, devices: List[str]) -> None:
        """Set device preference order.
        
        Args:
            devices: List of device preferences in order
        """
        # Validate device types
        valid_types = {t.value for t in DeviceType}
        for device in devices:
            if device not in valid_types:
                raise ValueError(f"Invalid device type: {device}. Must be one of {valid_types}")
                
        self._device_preferences = devices
        logger.info(f"Device preferences set to: {devices}")
        
    def get_current_device(self) -> torch.device:
        """Get current active device.
        
        Returns:
            Current torch.device
        """
        if self._current_device is None:
            self._current_device = self.select_best_device()
        return self._current_device
        
    def set_current_device(self, device: torch.device) -> None:
        """Set current active device.
        
        Args:
            device: torch.device to set as current
        """
        self._current_device = device
        
    def empty_cache(self, device: Optional[str] = None) -> None:
        """Clear memory cache on device.
        
        Args:
            device: Device to clear cache on, or None for current device
        """
        if device is None:
            device = str(self.get_current_device())
            
        if device.startswith('cuda'):
            torch.cuda.empty_cache()
            logger.info(f"Cleared CUDA cache on {device}")
        elif device.startswith('mps'):
            if hasattr(torch.mps, 'empty_cache'):
                torch.mps.empty_cache()
                logger.info("Cleared MPS cache")
            else:
                logger.warning("MPS cache clearing not available in this PyTorch version")
        # CPU doesn't need cache clearing
        
    def refresh_devices(self) -> None:
        """Force re-detection of devices."""
        self._available_devices = None
        self._device_capabilities.clear()
        logger.info("Device cache cleared, will re-detect on next access")
        
    def _get_mps_memory(self) -> int:
        """Get total MPS memory (estimated)."""
        # MPS doesn't expose total memory directly, estimate based on system
        import platform
        import subprocess
        
        try:
            if platform.system() == 'Darwin':
                # Try to get GPU memory from system_profiler
                result = subprocess.run(
                    ['system_profiler', 'SPDisplaysDataType'],
                    capture_output=True,
                    text=True
                )
                output = result.stdout
                
                # Parse output for VRAM info
                for line in output.split('\n'):
                    if 'VRAM' in line or 'Chipset Model' in line:
                        # Extract memory size
                        if 'GB' in line:
                            # Extract number before GB
                            import re
                            match = re.search(r'(\d+)\s*GB', line)
                            if match:
                                return int(match.group(1)) * 1024 * 1024 * 1024
                                
            # Default estimate for Apple Silicon
            return 8 * 1024 * 1024 * 1024  # 8GB default
        except:
            return 8 * 1024 * 1024 * 1024  # 8GB default
            
    def _get_system_memory(self) -> int:
        """Get total system memory."""
        try:
            import psutil
            return psutil.virtual_memory().total
        except:
            return 8 * 1024 * 1024 * 1024  # 8GB default
            
    def _detect_device_features(self, device: Device) -> Dict[str, bool]:
        """Detect supported features for a device."""
        features = {}
        
        if device.type == DeviceType.CUDA.value:
            features['tensor_cores'] = device.compute_capability >= 7.0 if device.compute_capability else False
            features['mixed_precision'] = True
            features['distributed'] = True
            features['cuda_graphs'] = device.compute_capability >= 7.0 if device.compute_capability else False
            
        elif device.type == DeviceType.MPS.value:
            features['tensor_cores'] = False
            features['mixed_precision'] = True
            features['distributed'] = False
            features['metal_performance_shaders'] = True
            
        else:  # CPU
            features['tensor_cores'] = False
            features['mixed_precision'] = True
            features['distributed'] = True
            features['vectorization'] = True
            
        return features


# Global device manager instance
_global_device_manager = None


def get_device_manager() -> DeviceManager:
    """Get global device manager instance."""
    global _global_device_manager
    if _global_device_manager is None:
        _global_device_manager = DeviceManager()
    return _global_device_manager
