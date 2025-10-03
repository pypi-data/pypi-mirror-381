"""Benchmarking utilities for OmniGPU."""
import torch
import time
import statistics
from typing import Dict, List, Any, Optional, Callable, Tuple
from dataclasses import dataclass, field
import json
from datetime import datetime

from ..core.device_manager import get_device_manager
from ..core.memory_manager import get_memory_manager
from ..api.tensor_api import to_device


@dataclass
class BenchmarkResult:
    """Container for benchmark results."""
    operation: str
    device: str
    mean_time: float
    std_time: float
    min_time: float
    max_time: float
    throughput: Optional[float] = None
    memory_used: Optional[int] = None
    samples: List[float] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __str__(self):
        return (f"{self.operation} on {self.device}: "
                f"{self.mean_time*1000:.2f}±{self.std_time*1000:.2f}ms")
    
    def to_dict(self):
        """Convert to dictionary for serialization."""
        return {
            'operation': self.operation,
            'device': self.device,
            'mean_time_ms': self.mean_time * 1000,
            'std_time_ms': self.std_time * 1000,
            'min_time_ms': self.min_time * 1000,
            'max_time_ms': self.max_time * 1000,
            'throughput': self.throughput,
            'memory_used_mb': self.memory_used / (1024**2) if self.memory_used else None,
            'samples': len(self.samples),
            'metadata': self.metadata
        }


@dataclass
class ComparisonResult:
    """Container for device comparison results."""
    operation: str
    results: Dict[str, BenchmarkResult]
    fastest_device: str
    speedup_ratios: Dict[str, float]  # Relative to fastest
    
    def __str__(self):
        lines = [f"\nComparison for {self.operation}:"]
        lines.append(f"Fastest device: {self.fastest_device}")
        lines.append("\nResults by device:")
        
        for device, result in sorted(self.results.items(), 
                                   key=lambda x: x[1].mean_time):
            speedup = self.speedup_ratios.get(device, 1.0)
            lines.append(f"  {device}: {result.mean_time*1000:.2f}ms "
                        f"(speedup: {speedup:.2f}x)")
        
        return "\n".join(lines)


def benchmark_operation(operation: Callable, *args, 
                       devices: Optional[List[str]] = None,
                       iterations: int = 100,
                       warmup: int = 10,
                       operation_name: Optional[str] = None,
                       **kwargs) -> ComparisonResult:
    """Benchmark an operation across multiple devices.
    
    Args:
        operation: Function to benchmark
        *args: Arguments for the operation
        devices: List of devices to test (None for all available)
        iterations: Number of benchmark iterations
        warmup: Number of warmup iterations
        operation_name: Name for the operation (default: function name)
        **kwargs: Keyword arguments for the operation
        
    Returns:
        ComparisonResult with benchmarks for all devices
    """
    device_manager = get_device_manager()
    memory_manager = get_memory_manager()
    
    if devices is None:
        devices = device_manager.available_devices()
    
    if operation_name is None:
        operation_name = operation.__name__ if hasattr(operation, '__name__') else 'operation'
    
    results = {}
    
    for device in devices:
        try:
            print(f"Benchmarking {operation_name} on {device}...")
            
            # Move inputs to device
            device_args = []
            for arg in args:
                if isinstance(arg, torch.Tensor):
                    device_args.append(to_device(arg, device))
                elif isinstance(arg, torch.nn.Module):
                    device_args.append(to_device(arg, device))
                else:
                    device_args.append(arg)
                    
            device_kwargs = {}
            for k, v in kwargs.items():
                if isinstance(v, torch.Tensor):
                    device_kwargs[k] = to_device(v, device)
                elif isinstance(v, torch.nn.Module):
                    device_kwargs[k] = to_device(v, device)
                else:
                    device_kwargs[k] = v
            
            # Clear cache before benchmark
            memory_manager.empty_cache(device)
            
            # Warmup runs
            for _ in range(warmup):
                _ = operation(*device_args, **device_kwargs)
                
            # Synchronize before timing
            if device.startswith('cuda'):
                torch.cuda.synchronize()
            elif device.startswith('mps'):
                if hasattr(torch.mps, 'synchronize'):
                    torch.mps.synchronize()
                    
            # Get memory baseline
            mem_before = memory_manager.get_memory_stats(device).allocated
            
            # Benchmark runs
            times = []
            for _ in range(iterations):
                start_time = time.perf_counter()
                
                result = operation(*device_args, **device_kwargs)
                
                # Synchronize to ensure operation completes
                if device.startswith('cuda'):
                    torch.cuda.synchronize()
                elif device.startswith('mps'):
                    if hasattr(torch.mps, 'synchronize'):
                        torch.mps.synchronize()
                        
                end_time = time.perf_counter()
                times.append(end_time - start_time)
            
            # Get memory usage
            mem_after = memory_manager.get_memory_stats(device).allocated
            memory_used = mem_after - mem_before
            
            # Calculate statistics
            mean_time = statistics.mean(times)
            std_time = statistics.stdev(times) if len(times) > 1 else 0
            min_time = min(times)
            max_time = max(times)
            
            # Calculate throughput if result is a tensor
            throughput = None
            if isinstance(result, torch.Tensor):
                # Estimate FLOPS based on tensor size
                elements = result.numel()
                throughput = elements / mean_time  # Elements per second
            
            results[device] = BenchmarkResult(
                operation=operation_name,
                device=device,
                mean_time=mean_time,
                std_time=std_time,
                min_time=min_time,
                max_time=max_time,
                throughput=throughput,
                memory_used=memory_used,
                samples=times,
                metadata={'iterations': iterations, 'warmup': warmup}
            )
            
        except Exception as e:
            print(f"Failed to benchmark on {device}: {e}")
            
    # Find fastest device
    if results:
        fastest_device = min(results.items(), key=lambda x: x[1].mean_time)[0]
        fastest_time = results[fastest_device].mean_time
        
        # Calculate speedup ratios
        speedup_ratios = {
            device: fastest_time / result.mean_time 
            for device, result in results.items()
        }
    else:
        fastest_device = 'none'
        speedup_ratios = {}
    
    return ComparisonResult(
        operation=operation_name,
        results=results,
        fastest_device=fastest_device,
        speedup_ratios=speedup_ratios
    )


def benchmark_model(model: torch.nn.Module, 
                   input_shape: Tuple[int, ...],
                   batch_sizes: Optional[List[int]] = None,
                   devices: Optional[List[str]] = None,
                   iterations: int = 100) -> Dict[str, ComparisonResult]:
    """Benchmark model inference across devices and batch sizes.
    
    Args:
        model: PyTorch model to benchmark
        input_shape: Shape of single input (without batch)
        batch_sizes: List of batch sizes to test
        devices: List of devices to test
        iterations: Number of iterations per benchmark
        
    Returns:
        Dict mapping batch size to comparison results
    """
    if batch_sizes is None:
        batch_sizes = [1, 8, 16, 32]
    
    results = {}
    
    for batch_size in batch_sizes:
        print(f"\nBenchmarking batch size {batch_size}...")
        
        def inference_fn(model, data):
            with torch.no_grad():
                return model(data)
        
        # Create dummy input
        dummy_input = torch.randn(batch_size, *input_shape)
        
        # Benchmark across devices
        comparison = benchmark_operation(
            inference_fn,
            model,
            dummy_input,
            devices=devices,
            iterations=iterations,
            operation_name=f"{model.__class__.__name__}_batch{batch_size}"
        )
        
        results[f"batch_{batch_size}"] = comparison
    
    return results


def run_standard_benchmarks(devices: Optional[List[str]] = None) -> Dict[str, Any]:
    """Run a standard set of benchmarks.
    
    Args:
        devices: Devices to benchmark (None for all)
        
    Returns:
        Dict with all benchmark results
    """
    print("Running OmniGPU Standard Benchmarks")
    print("=" * 50)
    
    results = {
        'metadata': {
            'timestamp': datetime.now().isoformat(),
            'devices': devices or get_device_manager().available_devices(),
            'torch_version': torch.__version__
        },
        'benchmarks': {}
    }
    
    # Matrix multiplication benchmarks
    sizes = [(100, 100), (512, 512), (1024, 1024)]
    for m, n in sizes:
        print(f"\nMatrix multiplication {m}x{n}...")
        
        def matmul_op(a, b):
            return torch.matmul(a, b)
        
        a = torch.randn(m, n)
        b = torch.randn(n, m)
        
        result = benchmark_operation(
            matmul_op, a, b,
            devices=devices,
            operation_name=f"matmul_{m}x{n}"
        )
        
        results['benchmarks'][f'matmul_{m}x{n}'] = {
            'comparison': result.to_dict() if hasattr(result, 'to_dict') else str(result),
            'fastest_device': result.fastest_device,
            'speedup_ratios': result.speedup_ratios
        }
    
    # Convolution benchmarks
    print("\nConvolution operations...")
    
    def conv2d_op(x):
        conv = torch.nn.Conv2d(3, 64, 3, padding=1)
        return conv(x)
    
    conv_input = torch.randn(8, 3, 224, 224)
    conv_result = benchmark_operation(
        conv2d_op, conv_input,
        devices=devices,
        operation_name="conv2d_3x224x224"
    )
    
    results['benchmarks']['conv2d'] = {
        'comparison': str(conv_result),
        'fastest_device': conv_result.fastest_device,
        'speedup_ratios': conv_result.speedup_ratios
    }
    
    # Memory transfer benchmarks
    print("\nMemory transfer benchmarks...")
    
    def transfer_op(x, target_device):
        return to_device(x, target_device)
    
    transfer_data = torch.randn(1000, 1000)
    for device in devices or get_device_manager().available_devices():
        if device != 'cpu':
            result = benchmark_operation(
                transfer_op, transfer_data, device,
                devices=['cpu'],  # Benchmark from CPU
                operation_name=f"transfer_to_{device}",
                iterations=50
            )
            
            if 'cpu' in result.results:
                results['benchmarks'][f'transfer_to_{device}'] = {
                    'time_ms': result.results['cpu'].mean_time * 1000,
                    'throughput_gb_s': (transfer_data.nbytes / (1024**3)) / 
                                     result.results['cpu'].mean_time
                }
    
    return results


def save_benchmark_results(results: Dict[str, Any], filename: str):
    """Save benchmark results to JSON file.
    
    Args:
        results: Benchmark results dictionary
        filename: Output filename
    """
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nBenchmark results saved to {filename}")


def compare_with_baseline(current_results: Dict[str, Any], 
                         baseline_file: str) -> Dict[str, Any]:
    """Compare current results with baseline.
    
    Args:
        current_results: Current benchmark results
        baseline_file: Path to baseline results file
        
    Returns:
        Comparison summary
    """
    with open(baseline_file, 'r') as f:
        baseline = json.load(f)
    
    comparison = {
        'improved': [],
        'regressed': [],
        'unchanged': []
    }
    
    for bench_name, current in current_results.get('benchmarks', {}).items():
        if bench_name in baseline.get('benchmarks', {}):
            baseline_bench = baseline['benchmarks'][bench_name]
            
            # Compare fastest times
            if 'fastest_device' in current and 'fastest_device' in baseline_bench:
                current_device = current['fastest_device']
                baseline_device = baseline_bench['fastest_device']
                
                if current_device in current.get('speedup_ratios', {}):
                    current_ratio = current['speedup_ratios'][current_device]
                    baseline_ratio = baseline_bench.get('speedup_ratios', {}).get(baseline_device, 1.0)
                    
                    improvement = (current_ratio / baseline_ratio - 1) * 100
                    
                    if improvement > 5:
                        comparison['improved'].append({
                            'benchmark': bench_name,
                            'improvement': f"{improvement:.1f}%"
                        })
                    elif improvement < -5:
                        comparison['regressed'].append({
                            'benchmark': bench_name,
                            'regression': f"{-improvement:.1f}%"
                        })
                    else:
                        comparison['unchanged'].append(bench_name)
    
    return comparison