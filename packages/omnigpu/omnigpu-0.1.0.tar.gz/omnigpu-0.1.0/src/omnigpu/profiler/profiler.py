"""Performance profiler for OmniGPU operations."""

import time
import functools
import threading
from typing import Dict, List, Optional, Any, Callable
from dataclasses import dataclass, field
from collections import defaultdict
import json

@dataclass
class ProfileEvent:
    """Single profiling event."""
    name: str
    start_time: float
    end_time: float
    duration: float
    device: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    @property
    def duration_ms(self) -> float:
        """Duration in milliseconds."""
        return self.duration * 1000


@dataclass 
class ProfileData:
    """Collection of profile events."""
    events: List[ProfileEvent] = field(default_factory=list)
    device_info: Dict[str, Any] = field(default_factory=dict)
    start_time: float = 0
    end_time: float = 0
    
    def add_event(self, event: ProfileEvent):
        """Add a profiling event."""
        self.events.append(event)
        
    def get_summary(self) -> Dict[str, Any]:
        """Get profiling summary statistics."""
        if not self.events:
            return {}
            
        total_time = sum(e.duration for e in self.events)
        
        # Group by operation name
        op_times = defaultdict(list)
        for event in self.events:
            op_times[event.name].append(event.duration)
        
        op_stats = {}
        for op, times in op_times.items():
            op_stats[op] = {
                'count': len(times),
                'total_ms': sum(times) * 1000,
                'avg_ms': (sum(times) / len(times)) * 1000,
                'min_ms': min(times) * 1000,
                'max_ms': max(times) * 1000
            }
        
        return {
            'total_time_ms': total_time * 1000,
            'num_operations': len(self.events),
            'operation_stats': op_stats,
            'device': self.device_info
        }
    
    def to_json(self) -> str:
        """Convert to JSON format."""
        data = {
            'events': [
                {
                    'name': e.name,
                    'start': e.start_time - self.start_time,
                    'duration': e.duration,
                    'device': str(e.device) if hasattr(e.device, '__str__') else e.device,
                    'metadata': e.metadata
                }
                for e in self.events
            ],
            'device_info': self.device_info,
            'total_duration': self.end_time - self.start_time
        }
        return json.dumps(data, indent=2, default=str)


class Profiler:
    """Performance profiler for OmniGPU operations."""
    
    def __init__(self, name: Optional[str] = None):
        self._active = False
        self._profile_data = ProfileData()
        self._start_stack = []
        self._lock = threading.Lock()
        self._device_info = None  # Lazy initialization
        self.name = name or "ugpu-profiler"
        
    def _get_device_info(self):
        """Get device info lazily."""
        if self._device_info is None:
            try:
                from ..api.tensor_api import auto_device, get_device_info
                device = auto_device()
                self._device_info = get_device_info(device)
            except Exception:
                # Fallback if device detection fails
                self._device_info = {'type': 'unknown', 'name': 'unknown'}
        return self._device_info
        
    def start(self):
        """Start profiling."""
        with self._lock:
            self._active = True
            self._profile_data = ProfileData()
            self._profile_data.start_time = time.time()
            self._profile_data.device_info = self._get_device_info()
            
    def stop(self) -> ProfileData:
        """Stop profiling and return data."""
        with self._lock:
            self._active = False
            self._profile_data.end_time = time.time()
            return self._profile_data
            
    def record_event(self, name: str, duration: float, device: str = "unknown", 
                    metadata: Optional[Dict[str, Any]] = None):
        """Record a profiling event."""
        if not self._active:
            return
            
        with self._lock:
            event = ProfileEvent(
                name=name,
                start_time=time.time() - duration,
                end_time=time.time(),
                duration=duration,
                device=device,
                metadata=metadata or {}
            )
            self._profile_data.add_event(event)
            
    def begin_range(self, name: str):
        """Begin a timing range."""
        if not self._active:
            return
            
        with self._lock:
            self._start_stack.append((name, time.time()))
            
    def end_range(self, metadata: Optional[Dict[str, Any]] = None):
        """End the current timing range."""
        if not self._active:
            return
            
        with self._lock:
            if not self._start_stack:
                return
                
            name, start_time = self._start_stack.pop()
            end_time = time.time()
            
            from ..api.tensor_api import auto_device
            device = str(auto_device())
            
            event = ProfileEvent(
                name=name,
                start_time=start_time,
                end_time=end_time,
                duration=end_time - start_time,
                device=device,
                metadata=metadata or {}
            )
            self._profile_data.add_event(event)
            
    @property
    def is_active(self) -> bool:
        """Check if profiler is active."""
        return self._active
        
    def get_data(self) -> ProfileData:
        """Get current profile data."""
        with self._lock:
            return self._profile_data


# Global profiler instance
_global_profiler = Profiler()


def profile(name: Optional[str] = None):
    """Decorator to profile a function.
    
    Args:
        name: Optional name for the profiled operation.
              If not provided, uses function name.
    
    Example:
        @profile()
        def my_operation(x):
            return x @ x.T
    """
    def decorator(func: Callable) -> Callable:
        op_name = name or func.__name__
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if _global_profiler.is_active:
                _global_profiler.begin_range(op_name)
                try:
                    result = func(*args, **kwargs)
                    
                    # Try to get shape information
                    metadata = {}
                    if hasattr(result, 'shape'):
                        metadata['output_shape'] = str(result.shape)
                    
                    _global_profiler.end_range(metadata)
                    return result
                except Exception as e:
                    _global_profiler.end_range({'error': str(e)})
                    raise
            else:
                return func(*args, **kwargs)
                
        return wrapper
    return decorator


# Context manager interface
class profile_range:
    """Context manager for profiling a code block.
    
    Example:
        with profile_range("data_loading"):
            data = load_data()
    """
    
    def __init__(self, name: str):
        self.name = name
        
    def __enter__(self):
        _global_profiler.begin_range(self.name)
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        metadata = {}
        if exc_type is not None:
            metadata['error'] = str(exc_val)
        _global_profiler.end_range(metadata)


# Public API
def start_profiling():
    """Start the global profiler."""
    _global_profiler.start()
    
def _profile_events_to_dict(data: ProfileData) -> Dict[str, Any]:
    """Serialize ProfileData into public dict format."""
    operations = [
        {
            'name': event.name,
            'duration_ms': event.duration_ms,
            'device': event.device,
            'metadata': event.metadata,
            'start_ms': (event.start_time - data.start_time) * 1000,
            'end_ms': (event.end_time - data.start_time) * 1000,
        }
        for event in data.events
    ]

    if not operations:
        total_ms = max((data.end_time - data.start_time) * 1000, 0.0)
        operations.append({
            'name': 'total_run',
            'duration_ms': total_ms,
            'device': data.device_info.get('type', 'unknown') if isinstance(data.device_info, dict) else 'unknown',
            'metadata': {'auto_generated': True},
            'start_ms': 0.0,
            'end_ms': total_ms,
        })

    return {
        'operations': operations,
        'total_time_ms': (data.end_time - data.start_time) * 1000,
        'device': data.device_info,
        'summary': data.get_summary(),
    }


class ProfileSummary(dict):
    """Dictionary-like container that also exposes ProfileData attributes."""

    def __init__(self, profile_data: ProfileData):
        payload = _profile_events_to_dict(profile_data)
        super().__init__(payload)
        self._profile_data = profile_data

    def __getattr__(self, item: str):
        if hasattr(self._profile_data, item):
            return getattr(self._profile_data, item)
        raise AttributeError(item)

    @property
    def events(self):
        return self._profile_data.events

    @property
    def start_time(self):
        return self._profile_data.start_time

    @property
    def end_time(self):
        return self._profile_data.end_time

    def to_profile_data(self) -> ProfileData:
        """Access the underlying ProfileData instance."""
        return self._profile_data


def stop_profiling() -> Dict[str, Any]:
    """Stop the global profiler and return public summary data."""
    data = _global_profiler.stop()
    return ProfileSummary(data)
    
def get_profiler() -> Profiler:
    """Get the global profiler instance."""
    return _global_profiler


class MemoryProfiler:
    """Memory profiling utility."""
    
    def __init__(self):
        self.memory_stats = []
        self.start_memory = None
        self._session_active = False
        self._session_events = []
        self._session_peak_gb = 0.0
        self._session_start_gb = 0.0

    def _capture_memory(self):
        """Capture current allocated/reserved memory in GB."""
        import torch

        if torch.cuda.is_available():
            torch.cuda.synchronize()
            allocated = torch.cuda.memory_allocated() / 1e9
            reserved = torch.cuda.memory_reserved() / 1e9
            peak = torch.cuda.max_memory_allocated() / 1e9
        elif hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
            allocated = 0.0
            reserved = 0.0
            peak = 0.0
            if hasattr(torch.mps, 'synchronize'):
                torch.mps.synchronize()
            if hasattr(torch.mps, 'current_allocated_memory'):
                allocated = torch.mps.current_allocated_memory() / 1e9
                peak = max(peak, allocated)
            if hasattr(torch.mps, 'driver_allocated_memory'):
                reserved = torch.mps.driver_allocated_memory() / 1e9
                peak = max(peak, reserved)
            if reserved == 0.0:
                reserved = allocated
        else:
            allocated = reserved = peak = 0.0

        return allocated, reserved, peak

    def __call__(self, func=None):
        """Decorator for memory profiling."""
        if func is None:
            return self
            
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            import torch
            
            start_alloc, start_reserved, start_peak = self._capture_memory()
            
            # Run function
            result = func(*args, **kwargs)
            
            end_alloc, end_reserved, end_peak = self._capture_memory()
            
            # Record stats
            self.memory_stats.append({
                'function': func.__name__,
                'allocated_before': start_alloc,
                'allocated_after': end_alloc,
                'allocated_delta': end_alloc - start_alloc,
                'reserved_before': start_reserved,
                'reserved_after': end_reserved,
                'reserved_delta': end_reserved - start_reserved,
                'timestamp': time.time()
            })
            if self._session_active:
                self._session_events.append(self.memory_stats[-1])
                self._session_peak_gb = max(
                    self._session_peak_gb,
                    start_peak,
                    end_peak,
                    end_alloc
                )
            
            return result
        return wrapper

    def start(self):
        """Begin a memory profiling session."""
        self._session_active = True
        self._session_events = []
        start_alloc, _, peak = self._capture_memory()
        self._session_start_gb = start_alloc
        self._session_peak_gb = max(peak, start_alloc)

    def stop(self):
        """Finish the active memory profiling session."""
        if not self._session_active:
            return {
                'peak_memory_mb': 0.0,
                'total_allocations': 0,
                'allocations': []
            }

        end_alloc, _, end_peak = self._capture_memory()
        self._session_peak_gb = max(self._session_peak_gb, end_alloc, end_peak)
        self._session_active = False

        summary = {
            'peak_memory_mb': self._session_peak_gb * 1000,
            'total_allocations': len(self._session_events),
            'allocations': list(self._session_events),
            'start_memory_mb': self._session_start_gb * 1000,
            'end_memory_mb': end_alloc * 1000,
        }

        self._session_events = []
        return summary

    def get_stats(self):
        """Get memory statistics."""
        if not self.memory_stats:
            return {'peak_memory_mb': 0, 'total_allocations': 0}
        
        peak_alloc = max(s['allocated_after'] for s in self.memory_stats)
        return {
            'peak_memory_mb': peak_alloc * 1000,  # Convert GB to MB
            'total_allocations': len(self.memory_stats),
            'stats': self.memory_stats
        }
    
    def show_timeline(self):
        """Show memory timeline (placeholder for notebook)."""
        stats = self.get_stats()
        print(f"Peak memory: {stats['peak_memory_mb']:.1f} MB")
        print(f"Total allocations: {stats['total_allocations']}")
        for stat in self.memory_stats:
            print(f"  {stat['function']}: {stat['allocated_delta']*1000:+.1f} MB")


# Create global instance
memory_profile = MemoryProfiler()
