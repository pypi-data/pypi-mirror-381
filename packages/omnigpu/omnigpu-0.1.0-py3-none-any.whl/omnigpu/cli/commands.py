"""Main CLI commands for OmniGPU."""

import sys
import argparse
from pathlib import Path
import omnigpu as ugpu


def cmd_info(args):
    """Show OmniGPU information."""
    print("OmniGPU Information")
    print("=" * 40)
    print(f"Version: {ugpu.__version__}")
    print(f"Device: {ugpu.auto_device()}")
    print(f"Available devices: {ugpu.available_devices()}")
    
    # Framework support
    try:
        from ..frameworks import detect_available_frameworks
        frameworks = detect_available_frameworks()
        print(f"Frameworks: {', '.join(frameworks)}")
    except:
        print("Frameworks: PyTorch")
    
    # Device details
    try:
        device_info = ugpu.get_device_info(ugpu.auto_device())
        print(f"\nDevice Details:")
        for key, value in device_info.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"\nDevice Details: Not available ({e})")


def cmd_analyze(args):
    """Run compatibility analyzer."""
    from .analyzer import main as analyze_main
    # Pass arguments to analyzer
    sys.argv = ['ugpu-analyze', args.path]
    if args.output:
        sys.argv.extend(['--output', args.output])
    if args.quiet:
        sys.argv.append('--quiet')
    if hasattr(args, 'no_recursive') and args.no_recursive:
        sys.argv.append('--no-recursive')
    
    analyze_main()


def cmd_profile(args):
    """Profile a Python script with OmniGPU."""
    import subprocess
    import os
    
    # Create a wrapper script that enables profiling
    wrapper = f"""
import omnigpu
omnigpu.enable_cuda_compatibility()

from omnigpu.profiler import start_profiling, stop_profiling, visualize_profile

# Start profiling
start_profiling()

# Run user script
exec(open('{args.script}').read())

# Stop and visualize
profile_data = stop_profiling()
print("\\n" + "="*60)
print("OmniGPU Profile Results")
print("="*60)
summary = profile_data.get_summary()
print(f"Total time: {{summary['total_time_ms']:.2f}} ms")
print(f"Operations: {{summary['num_operations']}}")

if not {args.no_viz}:
    visualize_profile(profile_data, save_prefix='{args.output or "profile"}')
"""
    
    # Run the wrapped script
    result = subprocess.run([sys.executable, '-c', wrapper])
    sys.exit(result.returncode)


def cmd_optimize(args):
    """Optimize a model file."""
    print(f"Optimizing {args.model}...")
    
    # This is a placeholder - would need actual implementation
    print("Model optimization is coming soon!")
    print("For now, use GraphOptimizer directly in your code:")
    print("  from omnigpu.optimization import GraphOptimizer")
    print("  optimizer = GraphOptimizer()")
    print("  optimized_model, stats = optimizer.optimize(model)")


def cmd_demo(args):
    """Run OmniGPU demos."""
    import subprocess
    # Look for demos in multiple possible locations
    possible_dirs = [
        Path(__file__).parent.parent.parent / 'demos',
        Path(__file__).parent.parent.parent / 'examples' / 'real_world',
        Path(__file__).parent.parent.parent.parent.parent / 'examples' / 'real_world',
        Path(__file__).parent.parent.parent.parent.parent / 'demos',
    ]
    
    demo_dir = None
    for d in possible_dirs:
        if d.exists() and list(d.glob('*.py')):
            demo_dir = d
            break
    
    if not demo_dir:
        print("Demo directory not found. Please run demos manually from examples/real_world/")
        return
    
    if args.number:
        # Run specific demo
        demo_file = demo_dir / f"{args.number}_*.py"
        demos = list(demo_dir.glob(f"{args.number}_*.py"))
        if demos:
            print(f"Running demo {args.number}...")
            subprocess.run([sys.executable, str(demos[0])])
        else:
            print(f"Demo {args.number} not found")
    else:
        # Run demo menu
        demo_runner = demo_dir / "run_all_demos.py"
        if demo_runner.exists():
            subprocess.run([sys.executable, str(demo_runner)])
        else:
            print("Demo runner not found. Available demos:")
            for demo in sorted(demo_dir.glob("[0-9]_*.py")):
                print(f"  {demo.name}")


def cli_main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        prog='ugpu',
        description='OmniGPU Command Line Interface',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  ugpu info                    # Show device information
  ugpu analyze myproject/      # Analyze code compatibility  
  ugpu profile script.py       # Profile a script
  ugpu demo                    # Run interactive demos
  ugpu demo 1                  # Run specific demo
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Info command
    parser_info = subparsers.add_parser('info', help='Show OmniGPU information')
    parser_info.set_defaults(func=cmd_info)
    
    # Analyze command
    parser_analyze = subparsers.add_parser('analyze', help='Analyze code compatibility')
    parser_analyze.add_argument('path', help='File or directory to analyze')
    parser_analyze.add_argument('--output', '-o', help='Save results to JSON')
    parser_analyze.add_argument('--quiet', '-q', action='store_true',
                               help='Only show compatibility score')
    parser_analyze.add_argument('--no-recursive', action='store_true',
                               help='Don\'t analyze subdirectories')
    parser_analyze.set_defaults(func=cmd_analyze)
    
    # Profile command
    parser_profile = subparsers.add_parser('profile', help='Profile a Python script')
    parser_profile.add_argument('script', help='Script to profile')
    parser_profile.add_argument('--output', '-o', help='Output file prefix')
    parser_profile.add_argument('--no-viz', action='store_true',
                               help='Skip visualization')
    parser_profile.set_defaults(func=cmd_profile)
    
    # Optimize command
    parser_optimize = subparsers.add_parser('optimize', help='Optimize a model')
    parser_optimize.add_argument('model', help='Model file to optimize')
    parser_optimize.set_defaults(func=cmd_optimize)
    
    # Demo command
    parser_demo = subparsers.add_parser('demo', help='Run OmniGPU demos')
    parser_demo.add_argument('number', nargs='?', help='Demo number (1-5)')
    parser_demo.set_defaults(func=cmd_demo)
    
    # Parse arguments
    args = parser.parse_args()
    
    if args.command is None:
        parser.print_help()
        sys.exit(0)
    
    # Execute command
    args.func(args)


def get_device_info_impl():
    """Get device information as a dictionary."""
    import omnigpu as ugpu
    device = ugpu.auto_device()
    
    info = {
        'version': ugpu.__version__,
        'current_device': str(device),
        'available_devices': ugpu.available_devices(),
    }
    
    try:
        device_details = ugpu.get_device_info(device)
        info.update(device_details)
    except:
        pass
    
    return info


def analyze_code_impl(code):
    """Analyze code for CUDA compatibility."""
    from .analyzer import CudaCompatibilityAnalyzer
    analyzer = CudaCompatibilityAnalyzer()
    
    # Analyze the code string
    lines = code.split('\n')
    issues = []
    compatible_lines = 0
    total_lines = len([l for l in lines if l.strip()])
    
    for i, line in enumerate(lines, 1):
        if '.cuda()' in line:
            issues.append(f"Line {i}: CUDA call detected - will be auto-patched")
        elif 'torch.cuda.' in line:
            issues.append(f"Line {i}: torch.cuda call - will be redirected")
        elif line.strip():
            compatible_lines += 1
    
    compatibility = (compatible_lines / max(total_lines, 1)) * 100 if total_lines > 0 else 100
    
    return {
        'compatibility_percentage': compatibility,
        'issues': issues,
        'total_lines': total_lines,
        'compatible_lines': compatible_lines
    }


def run_optimization_demo_impl():
    """Run optimization demo and return results."""
    import torch
    import torch.nn as nn
    from omnigpu.optimization import GraphOptimizer
    
    # Create a simple model
    model = nn.Sequential(
        nn.Conv2d(3, 64, 3, padding=1),
        nn.BatchNorm2d(64),
        nn.ReLU(),
        nn.Conv2d(64, 128, 3, padding=1),
        nn.BatchNorm2d(128),
        nn.ReLU()
    )
    
    # Optimize it
    optimizer = GraphOptimizer()
    opt_model, stats = optimizer.optimize(model)
    
    return {
        'original_ops': stats.original_ops,
        'optimized_ops': stats.optimized_ops,
        'patterns_found': stats.patterns_found,
        'fusions_applied': stats.fusions_applied,
        'estimated_speedup': stats.estimated_speedup
    }


if __name__ == '__main__':
    cli_main()