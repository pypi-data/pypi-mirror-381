"""Profiling utilities for OmniGPU."""

import torch
import time
import functools
from typing import Callable, Any, Dict, Optional
from contextlib import contextmanager
import logging

logger = logging.getLogger(__name__)


@contextmanager
def profile_time(name: str = "Operation") -> None:
    """Context manager to profile execution time."""
    start_time = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start_time
        logger.info(f"{name} took {elapsed:.4f} seconds")
        print(f"⏱️  {name}: {elapsed:.4f}s")


@contextmanager  
def profile_memory(device: Optional[torch.device] = None) -> Dict[str, float]:
    """Context manager to profile memory usage."""
    if device is None:
        device = torch.cuda.current_device() if torch.cuda.is_available() else None
    
    if device is None or not torch.cuda.is_available():
        yield {"allocated": 0, "cached": 0, "reserved": 0}
        return
        
    torch.cuda.synchronize(device)
    start_allocated = torch.cuda.memory_allocated(device)
    start_reserved = torch.cuda.memory_reserved(device)
    
    memory_stats = {}
    
    try:
        yield memory_stats
    finally:
        torch.cuda.synchronize(device)
        end_allocated = torch.cuda.memory_allocated(device)
        end_reserved = torch.cuda.memory_reserved(device)
        
        memory_stats.update({
            "allocated": (end_allocated - start_allocated) / 1024**2,  # MB
            "reserved": (end_reserved - start_reserved) / 1024**2,  # MB
            "peak_allocated": torch.cuda.max_memory_allocated(device) / 1024**2,  # MB
        })
        
        logger.info(f"Memory usage - Allocated: {memory_stats['allocated']:.2f} MB, "
                   f"Reserved: {memory_stats['reserved']:.2f} MB")


def profile_function(func: Callable) -> Callable:
    """Decorator to profile function execution time and memory."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        
        # Time profiling
        start_time = time.time()
        
        # Memory profiling (if CUDA available)
        if torch.cuda.is_available():
            torch.cuda.synchronize()
            start_memory = torch.cuda.memory_allocated()
        
        result = func(*args, **kwargs)
        
        # Calculate metrics
        elapsed_time = time.time() - start_time
        
        if torch.cuda.is_available():
            torch.cuda.synchronize()
            memory_used = (torch.cuda.memory_allocated() - start_memory) / 1024**2
            print(f"📊 {func_name}: {elapsed_time:.4f}s, {memory_used:.2f} MB")
        else:
            print(f"📊 {func_name}: {elapsed_time:.4f}s")
        
        return result
    
    return wrapper


class Profiler:
    """Simple profiler for tracking multiple operations."""
    
    def __init__(self):
        self.timings = {}
        self.memory_usage = {}
        self.counts = {}
    
    @contextmanager
    def profile(self, name: str):
        """Profile a code block."""
        start_time = time.time()
        
        if torch.cuda.is_available():
            torch.cuda.synchronize()
            start_memory = torch.cuda.memory_allocated()
        else:
            start_memory = 0
        
        try:
            yield
        finally:
            elapsed = time.time() - start_time
            
            if torch.cuda.is_available():
                torch.cuda.synchronize()
                memory_used = torch.cuda.memory_allocated() - start_memory
            else:
                memory_used = 0
            
            # Update statistics
            if name not in self.timings:
                self.timings[name] = []
                self.memory_usage[name] = []
                self.counts[name] = 0
            
            self.timings[name].append(elapsed)
            self.memory_usage[name].append(memory_used)
            self.counts[name] += 1
    
    def summary(self):
        """Print profiling summary."""
        print("\n📈 Profiling Summary:")
        print("=" * 60)
        
        for name in self.timings:
            avg_time = sum(self.timings[name]) / len(self.timings[name])
            total_time = sum(self.timings[name])
            avg_memory = sum(self.memory_usage[name]) / len(self.memory_usage[name]) / 1024**2
            
            print(f"\n{name}:")
            print(f"  Calls: {self.counts[name]}")
            print(f"  Total time: {total_time:.4f}s")
            print(f"  Average time: {avg_time:.4f}s")
            if avg_memory > 0:
                print(f"  Average memory: {avg_memory:.2f} MB")