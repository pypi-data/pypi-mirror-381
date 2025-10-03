#!/usr/bin/env python3
"""Command-line interface for OmniGPU benchmarks."""
import argparse
import sys
import os
import json
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import omnigpu as ugpu
from omnigpu.utils.benchmarks import (
    run_standard_benchmarks, 
    save_benchmark_results,
    compare_with_baseline,
    benchmark_operation,
    benchmark_model
)


def print_summary(results):
    """Print a summary of benchmark results."""
    print("\n" + "=" * 60)
    print("BENCHMARK SUMMARY")
    print("=" * 60)
    
    # Device information
    print("\nDevices tested:")
    for device in results['metadata']['devices']:
        info = ugpu.get_device_info(device)
        print(f"  - {device}: {info['name']}")
        if 'memory_total_gb' in info:
            print(f"    Memory: {info['memory_total_gb']:.1f} GB")
    
    # Results summary
    print("\nBenchmark Results:")
    for bench_name, bench_data in results['benchmarks'].items():
        print(f"\n{bench_name}:")
        if 'fastest_device' in bench_data:
            print(f"  Fastest device: {bench_data['fastest_device']}")
            if 'speedup_ratios' in bench_data:
                for device, ratio in sorted(bench_data['speedup_ratios'].items(), 
                                          key=lambda x: -x[1]):
                    print(f"  - {device}: {ratio:.2f}x")


def run_quick_benchmark(args):
    """Run a quick benchmark."""
    print("Running quick benchmark...")
    
    devices = args.devices.split(',') if args.devices else None
    
    # Quick matrix multiplication test
    def matmul_test(a, b):
        return torch.matmul(a, b)
    
    import torch
    a = torch.randn(512, 512)
    b = torch.randn(512, 512)
    
    result = benchmark_operation(
        matmul_test, a, b,
        devices=devices,
        iterations=50,
        warmup=10,
        operation_name="matmul_512x512"
    )
    
    print(result)
    
    if args.output:
        results = {
            'metadata': {
                'timestamp': datetime.now().isoformat(),
                'mode': 'quick'
            },
            'benchmarks': {
                'matmul_512x512': {
                    'fastest_device': result.fastest_device,
                    'speedup_ratios': result.speedup_ratios
                }
            }
        }
        save_benchmark_results(results, args.output)


def run_full_benchmark(args):
    """Run full benchmark suite."""
    print("Running full benchmark suite...")
    
    devices = args.devices.split(',') if args.devices else None
    
    results = run_standard_benchmarks(devices)
    
    print_summary(results)
    
    if args.output:
        save_benchmark_results(results, args.output)
    
    if args.compare:
        print("\nComparing with baseline...")
        comparison = compare_with_baseline(results, args.compare)
        
        print("\nComparison Results:")
        if comparison['improved']:
            print("Improved:")
            for item in comparison['improved']:
                print(f"  - {item['benchmark']}: +{item['improvement']}")
        
        if comparison['regressed']:
            print("Regressed:")
            for item in comparison['regressed']:
                print(f"  - {item['benchmark']}: -{item['regression']}")
        
        if comparison['unchanged']:
            print(f"Unchanged: {len(comparison['unchanged'])} benchmarks")


def run_custom_benchmark(args):
    """Run custom benchmark from file."""
    print(f"Running custom benchmark from {args.custom}...")
    
    # Load and execute custom benchmark file
    import importlib.util
    spec = importlib.util.spec_from_file_location("custom_benchmark", args.custom)
    custom_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(custom_module)
    
    if hasattr(custom_module, 'run_benchmark'):
        results = custom_module.run_benchmark()
        
        if args.output:
            save_benchmark_results(results, args.output)
    else:
        print("Error: Custom benchmark file must define 'run_benchmark()' function")
        sys.exit(1)


def main():
    """Main entry point for benchmark CLI."""
    parser = argparse.ArgumentParser(
        description='OmniGPU Benchmark Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run quick benchmark on all devices
  ugpu-benchmark --quick
  
  # Run full benchmark suite and save results
  ugpu-benchmark --full --output results.json
  
  # Benchmark specific devices
  ugpu-benchmark --devices cuda:0,mps:0 --full
  
  # Compare with baseline
  ugpu-benchmark --full --compare baseline.json
  
  # Run custom benchmark
  ugpu-benchmark --custom my_benchmark.py
        """
    )
    
    # Benchmark modes
    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument('--quick', action='store_true',
                           help='Run quick benchmark (single operation)')
    mode_group.add_argument('--full', action='store_true',
                           help='Run full benchmark suite')
    mode_group.add_argument('--custom', type=str,
                           help='Run custom benchmark from file')
    
    # Options
    parser.add_argument('--devices', type=str,
                       help='Comma-separated list of devices to benchmark')
    parser.add_argument('--output', '-o', type=str,
                       help='Save results to JSON file')
    parser.add_argument('--compare', '-c', type=str,
                       help='Compare with baseline JSON file')
    parser.add_argument('--iterations', '-i', type=int, default=100,
                       help='Number of iterations per benchmark (default: 100)')
    parser.add_argument('--list-devices', action='store_true',
                       help='List available devices and exit')
    
    args = parser.parse_args()
    
    # List devices if requested
    if args.list_devices:
        print("Available devices:")
        for device in ugpu.available_devices():
            info = ugpu.get_device_info(device)
            print(f"  - {device}: {info['name']}")
        sys.exit(0)
    
    # Run appropriate benchmark
    try:
        if args.quick:
            run_quick_benchmark(args)
        elif args.full:
            run_full_benchmark(args)
        elif args.custom:
            run_custom_benchmark(args)
    except KeyboardInterrupt:
        print("\nBenchmark interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\nError during benchmark: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()