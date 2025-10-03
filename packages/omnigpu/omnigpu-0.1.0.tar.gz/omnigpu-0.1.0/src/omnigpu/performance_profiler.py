"""
Performance Profiler for OmniGPU
Tracks and analyzes performance characteristics of operations.
"""

import torch
import time
import psutil
import os
import json
from typing import Dict, List, Optional, Callable, Any, Tuple
from collections import defaultdict, deque
from datetime import datetime
import threading
import functools
import numpy as np
import logging

logger = logging.getLogger(__name__)


class PerformanceMetrics:
    """Container for performance metrics of an operation."""
    
    def __init__(self, op_name: str):
        self.op_name = op_name
        self.execution_times = deque(maxlen=1000)  # Keep last 1000 measurements
        self.memory_usage = deque(maxlen=1000)
        self.tensor_sizes = deque(maxlen=1000)
        self.device_types = defaultdict(int)
        self.success_count = 0
        self.failure_count = 0
        self.fallback_count = 0
        self.last_updated = datetime.now()
    
    def add_measurement(self, 
                       execution_time: float,
                       memory_delta: float = 0,
                       tensor_size: Optional[int] = None,
                       device: Optional[str] = None,
                       used_fallback: bool = False):
        """Add a new measurement."""
        self.execution_times.append(execution_time)
        self.memory_usage.append(memory_delta)
        if tensor_size:
            self.tensor_sizes.append(tensor_size)
        if device:
            self.device_types[device] += 1
        if used_fallback:
            self.fallback_count += 1
        else:
            self.success_count += 1
        self.last_updated = datetime.now()
    
    def get_stats(self) -> Dict[str, Any]:
        """Calculate statistics from measurements."""
        if not self.execution_times:
            return {
                'op_name': self.op_name,
                'measurements': 0,
                'status': 'no_data'
            }
        
        exec_times = list(self.execution_times)
        
        stats = {
            'op_name': self.op_name,
            'measurements': len(exec_times),
            'success_rate': self.success_count / (self.success_count + self.failure_count) if (self.success_count + self.failure_count) > 0 else 0,
            'fallback_rate': self.fallback_count / self.success_count if self.success_count > 0 else 0,
            'execution_time': {
                'mean': np.mean(exec_times),
                'median': np.median(exec_times),
                'std': np.std(exec_times),
                'min': np.min(exec_times),
                'max': np.max(exec_times),
                'p95': np.percentile(exec_times, 95),
                'p99': np.percentile(exec_times, 99)
            },
            'device_distribution': dict(self.device_types),
            'last_updated': self.last_updated.isoformat()
        }
        
        if self.memory_usage:
            mem_usage = list(self.memory_usage)
            stats['memory'] = {
                'mean_delta_mb': np.mean(mem_usage),
                'max_delta_mb': np.max(mem_usage)
            }
        
        if self.tensor_sizes:
            sizes = list(self.tensor_sizes)
            stats['tensor_sizes'] = {
                'mean_elements': np.mean(sizes),
                'max_elements': np.max(sizes)
            }
        
        return stats


class PerformanceProfiler:
    """Main performance profiling system for OmniGPU."""
    
    def __init__(self, 
                 profile_memory: bool = True,
                 profile_cuda: bool = False,
                 auto_export_interval: Optional[int] = 300):
        self.profile_memory = profile_memory
        self.profile_cuda = profile_cuda and torch.cuda.is_available()
        self.metrics = defaultdict(lambda: PerformanceMetrics("unknown"))
        self.global_stats = {
            'total_operations': 0,
            'total_time': 0,
            'start_time': datetime.now()
        }
        
        # Auto-export thread
        self.auto_export_interval = auto_export_interval
        self._export_thread = None
        if auto_export_interval:
            self._start_auto_export()
    
    def profile(self, op_name: Optional[str] = None) -> Callable:
        """
        Decorator to profile a function.
        
        Example:
            @profiler.profile("my_operation")
            def my_function(x):
                return x * 2
        """
        def decorator(func: Callable) -> Callable:
            nonlocal op_name
            if op_name is None:
                op_name = func.__name__
            
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return self._profile_execution(func, op_name, args, kwargs)
            
            # Store reference to metrics
            wrapper._omnigpu_metrics = self.metrics[op_name]
            return wrapper
        
        return decorator
    
    def _profile_execution(self, func: Callable, op_name: str, args: tuple, kwargs: dict) -> Any:
        """Profile a single function execution."""
        # Prepare measurement
        start_time = time.perf_counter()
        start_memory = self._get_memory_usage() if self.profile_memory else 0
        
        # Detect device
        device = self._detect_device(args, kwargs)
        tensor_size = self._estimate_tensor_size(args, kwargs)
        
        # CUDA events for precise GPU timing
        cuda_start = cuda_end = None
        if self.profile_cuda and device == 'cuda':
            cuda_start = torch.cuda.Event(enable_timing=True)
            cuda_end = torch.cuda.Event(enable_timing=True)
            cuda_start.record()
        
        try:
            # Execute function
            result = func(*args, **kwargs)
            
            # End timing
            if cuda_start:
                cuda_end.record()
                torch.cuda.synchronize()
                execution_time = cuda_start.elapsed_time(cuda_end) / 1000  # Convert to seconds
            else:
                execution_time = time.perf_counter() - start_time
            
            # Memory measurement
            end_memory = self._get_memory_usage() if self.profile_memory else 0
            memory_delta = end_memory - start_memory
            
            # Check if fallback was used
            used_fallback = self._detect_fallback(result, device)
            
            # Record metrics
            self.metrics[op_name].add_measurement(
                execution_time=execution_time,
                memory_delta=memory_delta,
                tensor_size=tensor_size,
                device=device,
                used_fallback=used_fallback
            )
            
            # Update global stats
            self.global_stats['total_operations'] += 1
            self.global_stats['total_time'] += execution_time
            
            return result
            
        except Exception as e:
            self.metrics[op_name].failure_count += 1
            raise
    
    def _detect_device(self, args: tuple, kwargs: dict) -> str:
        """Detect device from function arguments."""
        # Check kwargs first
        if 'device' in kwargs:
            return str(kwargs['device'])
        
        # Check tensor arguments
        for arg in args:
            if hasattr(arg, 'device'):
                return str(arg.device).split(':')[0]
        
        # Check MPS availability
        if hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
            return 'mps'
        
        return 'cpu'
    
    def _estimate_tensor_size(self, args: tuple, kwargs: dict) -> Optional[int]:
        """Estimate total tensor size in elements."""
        total_size = 0
        
        for arg in args:
            if isinstance(arg, torch.Tensor):
                total_size += arg.numel()
        
        for value in kwargs.values():
            if isinstance(value, torch.Tensor):
                total_size += value.numel()
        
        return total_size if total_size > 0 else None
    
    def _detect_fallback(self, result: Any, expected_device: str) -> bool:
        """Detect if operation used fallback."""
        if hasattr(result, 'device'):
            actual_device = str(result.device).split(':')[0]
            # If expected MPS but got CPU, likely a fallback
            if expected_device in ['mps', 'cuda'] and actual_device == 'cpu':
                return True
        return False
    
    def _get_memory_usage(self) -> float:
        """Get current memory usage in MB."""
        process = psutil.Process(os.getpid())
        return process.memory_info().rss / 1024 / 1024
    
    def get_operation_stats(self, op_name: str) -> Dict[str, Any]:
        """Get statistics for a specific operation."""
        if op_name in self.metrics:
            return self.metrics[op_name].get_stats()
        return {'op_name': op_name, 'status': 'not_profiled'}
    
    def get_summary(self) -> Dict[str, Any]:
        """Get overall profiling summary."""
        all_stats = []
        for op_name, metrics in self.metrics.items():
            stats = metrics.get_stats()
            if stats['measurements'] > 0:
                all_stats.append(stats)
        
        # Sort by total time
        all_stats.sort(
            key=lambda x: x['execution_time']['mean'] * x['measurements'],
            reverse=True
        )
        
        # Calculate global statistics
        total_measurements = sum(s['measurements'] for s in all_stats)
        
        summary = {
            'profiling_duration_seconds': (datetime.now() - self.global_stats['start_time']).total_seconds(),
            'total_operations_profiled': len(all_stats),
            'total_measurements': total_measurements,
            'total_execution_time': self.global_stats['total_time'],
            'top_time_consuming': all_stats[:10],  # Top 10 by total time
            'highest_latency': sorted(all_stats, key=lambda x: x['execution_time']['max'], reverse=True)[:10],
            'most_failures': sorted(
                [s for s in all_stats if s.get('fallback_rate', 0) > 0],
                key=lambda x: x['fallback_rate'],
                reverse=True
            )[:10]
        }
        
        # Device distribution
        device_counts = defaultdict(int)
        for stats in all_stats:
            for device, count in stats.get('device_distribution', {}).items():
                device_counts[device] += count
        summary['device_distribution'] = dict(device_counts)
        
        return summary
    
    def compare_operations(self, op1: str, op2: str) -> Dict[str, Any]:
        """Compare performance of two operations."""
        stats1 = self.get_operation_stats(op1)
        stats2 = self.get_operation_stats(op2)
        
        if stats1['status'] == 'no_data' or stats2['status'] == 'no_data':
            return {
                'status': 'insufficient_data',
                'message': 'One or both operations have no profiling data'
            }
        
        comparison = {
            'operations': [op1, op2],
            'execution_time_ratio': stats1['execution_time']['mean'] / stats2['execution_time']['mean'],
            'op1_stats': stats1,
            'op2_stats': stats2,
            'faster_operation': op1 if stats1['execution_time']['mean'] < stats2['execution_time']['mean'] else op2,
            'speedup': abs(stats1['execution_time']['mean'] - stats2['execution_time']['mean']) / max(stats1['execution_time']['mean'], stats2['execution_time']['mean'])
        }
        
        return comparison
    
    def export_profile(self, output_path: str = "omnigpu_profile.json") -> str:
        """Export profiling data to JSON file."""
        export_data = {
            'metadata': {
                'export_time': datetime.now().isoformat(),
                'profiling_start': self.global_stats['start_time'].isoformat(),
                'omnigpu_version': '0.1.0'  # Would get from package
            },
            'summary': self.get_summary(),
            'operations': {}
        }
        
        # Add detailed stats for each operation
        for op_name, metrics in self.metrics.items():
            export_data['operations'][op_name] = metrics.get_stats()
        
        with open(output_path, 'w') as f:
            json.dump(export_data, f, indent=2)
        
        logger.info(f"Exported profile data to {output_path}")
        return output_path
    
    def _start_auto_export(self):
        """Start automatic export thread."""
        def export_periodically():
            while self.auto_export_interval:
                time.sleep(self.auto_export_interval)
                try:
                    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                    self.export_profile(f"omnigpu_profile_{timestamp}.json")
                except Exception as e:
                    logger.error(f"Auto-export failed: {e}")
        
        self._export_thread = threading.Thread(target=export_periodically, daemon=True)
        self._export_thread.start()
    
    def get_recommendations(self) -> List[Dict[str, Any]]:
        """Generate performance recommendations based on profiling data."""
        recommendations = []
        
        summary = self.get_summary()
        
        # Check for high-latency operations
        for op_stats in summary.get('highest_latency', [])[:5]:
            if op_stats['execution_time']['max'] > 0.1:  # 100ms
                recommendations.append({
                    'type': 'high_latency',
                    'operation': op_stats['op_name'],
                    'message': f"{op_stats['op_name']} has high latency (max: {op_stats['execution_time']['max']*1000:.1f}ms)",
                    'suggestion': 'Consider optimizing this operation or using smaller batch sizes'
                })
        
        # Check for high fallback rates
        for op_stats in summary.get('most_failures', []):
            if op_stats['fallback_rate'] > 0.5:  # >50% fallback
                recommendations.append({
                    'type': 'high_fallback_rate',
                    'operation': op_stats['op_name'],
                    'message': f"{op_stats['op_name']} falls back to CPU {op_stats['fallback_rate']*100:.1f}% of the time",
                    'suggestion': 'This operation needs MPS optimization'
                })
        
        # Memory usage patterns
        memory_intensive_ops = []
        for op_name, metrics in self.metrics.items():
            stats = metrics.get_stats()
            if 'memory' in stats and stats['memory']['max_delta_mb'] > 100:
                memory_intensive_ops.append((op_name, stats['memory']['max_delta_mb']))
        
        if memory_intensive_ops:
            memory_intensive_ops.sort(key=lambda x: x[1], reverse=True)
            for op_name, memory_mb in memory_intensive_ops[:3]:
                recommendations.append({
                    'type': 'high_memory_usage',
                    'operation': op_name,
                    'message': f"{op_name} uses up to {memory_mb:.1f}MB of memory",
                    'suggestion': 'Monitor memory usage and consider gradient checkpointing if needed'
                })
        
        return recommendations


# Global profiler instance
_global_profiler = None


def get_profiler() -> PerformanceProfiler:
    """Get or create global profiler instance."""
    global _global_profiler
    if _global_profiler is None:
        _global_profiler = PerformanceProfiler()
    return _global_profiler


def profile(op_name: Optional[str] = None) -> Callable:
    """
    Convenience decorator using global profiler.
    
    Example:
        @profile("matmul")
        def my_matmul(a, b):
            return torch.matmul(a, b)
    """
    return get_profiler().profile(op_name)


def export_profile(output_path: str = "omnigpu_profile.json") -> str:
    """Export global profiler data."""
    return get_profiler().export_profile(output_path)


def get_recommendations() -> List[Dict[str, Any]]:
    """Get performance recommendations from global profiler."""
    return get_profiler().get_recommendations()


def main():
    """Demo of performance profiler."""
    import torch.nn.functional as F
    
    # Create profiler
    profiler = PerformanceProfiler()
    
    # Example profiled operations
    @profiler.profile("test_matmul")
    def test_matmul(a, b):
        return torch.matmul(a, b)
    
    @profiler.profile("test_conv2d")
    def test_conv2d(x, weight):
        return F.conv2d(x, weight)
    
    print("Running performance profiling demo...")
    
    # Run some operations
    device = 'mps' if torch.backends.mps.is_available() else 'cpu'
    
    # Test matmul with different sizes
    for size in [100, 500, 1000]:
        a = torch.randn(size, size, device=device)
        b = torch.randn(size, size, device=device)
        test_matmul(a, b)
    
    # Test conv2d
    x = torch.randn(1, 3, 224, 224, device=device)
    weight = torch.randn(64, 3, 7, 7, device=device)
    test_conv2d(x, weight)
    
    # Get results
    print("\nProfiler Summary:")
    summary = profiler.get_summary()
    print(f"Total operations profiled: {summary['total_operations_profiled']}")
    print(f"Total measurements: {summary['total_measurements']}")
    print(f"Total execution time: {summary['total_execution_time']:.3f}s")
    
    print("\nTop operations by time:")
    for op in summary['top_time_consuming'][:3]:
        print(f"  {op['op_name']}: {op['execution_time']['mean']*1000:.2f}ms average")
    
    # Get recommendations
    print("\nRecommendations:")
    for rec in profiler.get_recommendations():
        print(f"  [{rec['type']}] {rec['message']}")
        print(f"    Suggestion: {rec['suggestion']}")
    
    # Export profile
    output_file = profiler.export_profile()
    print(f"\nProfile exported to: {output_file}")


if __name__ == "__main__":
    main()