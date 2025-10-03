"""
Memory stress tests for OmniGPU on M4 hardware.
Tests memory limits, garbage collection, and OOM handling.
"""

import torch
import gc
import psutil
import os
import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple
import traceback


class MemoryStressTest:
    def __init__(self, max_memory_gb: float = 32):
        self.max_memory_gb = max_memory_gb
        self.device = 'mps' if torch.backends.mps.is_available() else 'cpu'
        self.results = {
            'timestamp': datetime.now().isoformat(),
            'device': self.device,
            'system_memory_gb': psutil.virtual_memory().total / (1024**3),
            'tests': []
        }
        
    def get_memory_usage(self) -> Dict[str, float]:
        """Get current memory usage."""
        vm = psutil.virtual_memory()
        
        memory_info = {
            'system_used_gb': vm.used / (1024**3),
            'system_available_gb': vm.available / (1024**3),
            'system_percent': vm.percent
        }
        
        if self.device == 'mps':
            # Try to get MPS memory usage
            try:
                memory_info['mps_allocated_mb'] = torch.mps.driver_allocated_memory() / (1024**2)
            except:
                memory_info['mps_allocated_mb'] = -1
        
        return memory_info
    
    def test_large_tensor_allocation(self) -> Dict:
        """Test allocation of increasingly large tensors."""
        print("\n1. Testing large tensor allocation...")
        test_result = {
            'test_name': 'large_tensor_allocation',
            'status': 'started',
            'max_size_gb': 0,
            'allocations': []
        }
        
        try:
            # Start with 1GB and double each time
            size_gb = 0.5
            while size_gb <= self.max_memory_gb:
                elements = int(size_gb * 1024**3 / 4)  # float32 = 4 bytes
                
                try:
                    # Clear previous allocations
                    if self.device == 'mps':
                        torch.mps.empty_cache()
                    gc.collect()
                    
                    mem_before = self.get_memory_usage()
                    tensor = torch.randn(elements, device=self.device)
                    mem_after = self.get_memory_usage()
                    
                    allocation_info = {
                        'size_gb': size_gb,
                        'shape': list(tensor.shape),
                        'memory_delta_gb': mem_after['system_used_gb'] - mem_before['system_used_gb'],
                        'success': True
                    }
                    
                    test_result['allocations'].append(allocation_info)
                    test_result['max_size_gb'] = size_gb
                    print(f"  ✅ Allocated {size_gb:.1f}GB tensor")
                    
                    del tensor
                    
                except Exception as e:
                    allocation_info = {
                        'size_gb': size_gb,
                        'success': False,
                        'error': str(e)
                    }
                    test_result['allocations'].append(allocation_info)
                    print(f"  ❌ Failed at {size_gb:.1f}GB: {e}")
                    break
                
                size_gb *= 2
            
            test_result['status'] = 'completed'
            
        except Exception as e:
            test_result['status'] = 'failed'
            test_result['error'] = str(e)
        
        return test_result
    
    def test_many_small_tensors(self) -> Dict:
        """Test allocation of many small tensors."""
        print("\n2. Testing many small tensor allocations...")
        test_result = {
            'test_name': 'many_small_tensors',
            'status': 'started',
            'num_tensors': 0,
            'tensor_size_mb': 10
        }
        
        try:
            tensors = []
            tensor_size = 10 * 1024 * 1024 // 4  # 10MB tensors
            
            mem_start = self.get_memory_usage()
            
            while True:
                try:
                    tensor = torch.randn(tensor_size, device=self.device)
                    tensors.append(tensor)
                    
                    if len(tensors) % 100 == 0:
                        mem_current = self.get_memory_usage()
                        print(f"  Allocated {len(tensors)} tensors, "
                              f"memory used: {mem_current['system_percent']:.1f}%")
                        
                        if mem_current['system_percent'] > 90:
                            print("  ⚠️  Approaching memory limit")
                            break
                    
                except Exception as e:
                    print(f"  Stopped at {len(tensors)} tensors: {e}")
                    break
            
            mem_end = self.get_memory_usage()
            
            test_result['num_tensors'] = len(tensors)
            test_result['total_allocated_gb'] = len(tensors) * 10 / 1024
            test_result['memory_increase_gb'] = mem_end['system_used_gb'] - mem_start['system_used_gb']
            test_result['status'] = 'completed'
            
            # Cleanup
            tensors.clear()
            
        except Exception as e:
            test_result['status'] = 'failed'
            test_result['error'] = str(e)
        
        return test_result
    
    def test_memory_fragmentation(self) -> Dict:
        """Test memory fragmentation by allocating and deallocating randomly."""
        print("\n3. Testing memory fragmentation...")
        test_result = {
            'test_name': 'memory_fragmentation',
            'status': 'started',
            'iterations': 0
        }
        
        try:
            import random
            tensors = {}
            
            for i in range(1000):
                if random.random() < 0.7 and len(tensors) < 100:
                    # Allocate
                    size = random.randint(1, 100) * 1024 * 1024 // 4  # 1-100MB
                    key = f"tensor_{i}"
                    tensors[key] = torch.randn(size, device=self.device)
                elif tensors:
                    # Deallocate
                    key = random.choice(list(tensors.keys()))
                    del tensors[key]
                
                if i % 100 == 0:
                    if self.device == 'mps':
                        torch.mps.empty_cache()
                    gc.collect()
                    
                    mem = self.get_memory_usage()
                    print(f"  Iteration {i}: {len(tensors)} tensors, "
                          f"memory: {mem['system_percent']:.1f}%")
            
            test_result['iterations'] = 1000
            test_result['status'] = 'completed'
            test_result['final_tensor_count'] = len(tensors)
            
        except Exception as e:
            test_result['status'] = 'failed'
            test_result['error'] = str(e)
            test_result['traceback'] = traceback.format_exc()
        
        return test_result
    
    def test_operation_memory_usage(self) -> Dict:
        """Test memory usage of various operations."""
        print("\n4. Testing operation memory usage...")
        test_result = {
            'test_name': 'operation_memory_usage',
            'status': 'started',
            'operations': []
        }
        
        operations = [
            ('matmul', lambda x: torch.matmul(x, x.T)),
            ('conv2d', lambda x: torch.nn.functional.conv2d(
                x.view(1, 1, int(x.shape[0]**0.5), int(x.shape[0]**0.5)),
                torch.randn(1, 1, 3, 3, device=self.device))),
            ('fft', lambda x: torch.fft.fft(x)),
            ('sort', lambda x: torch.sort(x)),
            ('svd', lambda x: torch.svd(x.view(1000, -1)[:, :1000])),
        ]
        
        try:
            base_tensor = torch.randn(1000000, device=self.device)  # 4MB tensor
            
            for op_name, op_func in operations:
                try:
                    gc.collect()
                    if self.device == 'mps':
                        torch.mps.empty_cache()
                    
                    mem_before = self.get_memory_usage()
                    result = op_func(base_tensor)
                    mem_peak = self.get_memory_usage()
                    del result
                    gc.collect()
                    mem_after = self.get_memory_usage()
                    
                    op_info = {
                        'operation': op_name,
                        'peak_increase_mb': (mem_peak['system_used_gb'] - mem_before['system_used_gb']) * 1024,
                        'permanent_increase_mb': (mem_after['system_used_gb'] - mem_before['system_used_gb']) * 1024,
                        'success': True
                    }
                    test_result['operations'].append(op_info)
                    print(f"  {op_name}: peak +{op_info['peak_increase_mb']:.1f}MB")
                    
                except Exception as e:
                    op_info = {
                        'operation': op_name,
                        'success': False,
                        'error': str(e)
                    }
                    test_result['operations'].append(op_info)
                    print(f"  {op_name}: failed - {e}")
            
            test_result['status'] = 'completed'
            
        except Exception as e:
            test_result['status'] = 'failed'
            test_result['error'] = str(e)
        
        return test_result
    
    def test_gradient_accumulation(self) -> Dict:
        """Test memory usage during gradient accumulation."""
        print("\n5. Testing gradient accumulation memory...")
        test_result = {
            'test_name': 'gradient_accumulation',
            'status': 'started'
        }
        
        try:
            # Simple model
            model = torch.nn.Sequential(
                torch.nn.Linear(1000, 1000),
                torch.nn.ReLU(),
                torch.nn.Linear(1000, 1000)
            ).to(self.device)
            
            optimizer = torch.optim.Adam(model.parameters())
            
            mem_start = self.get_memory_usage()
            memory_measurements = []
            
            # Accumulate gradients
            for step in range(100):
                x = torch.randn(32, 1000, device=self.device)
                y = model(x)
                loss = y.mean()
                loss.backward()
                
                if step % 10 == 0:
                    mem = self.get_memory_usage()
                    memory_measurements.append({
                        'step': step,
                        'memory_used_gb': mem['system_used_gb']
                    })
                
                if step % 20 == 0:
                    optimizer.step()
                    optimizer.zero_grad()
            
            mem_end = self.get_memory_usage()
            
            test_result['memory_measurements'] = memory_measurements
            test_result['memory_increase_gb'] = mem_end['system_used_gb'] - mem_start['system_used_gb']
            test_result['status'] = 'completed'
            
        except Exception as e:
            test_result['status'] = 'failed'
            test_result['error'] = str(e)
        
        return test_result
    
    def run_all_tests(self) -> Dict:
        """Run all memory stress tests."""
        print(f"Starting memory stress tests on {self.device}")
        print(f"System memory: {self.results['system_memory_gb']:.1f}GB")
        print("=" * 50)
        
        tests = [
            self.test_large_tensor_allocation,
            self.test_many_small_tensors,
            self.test_memory_fragmentation,
            self.test_operation_memory_usage,
            self.test_gradient_accumulation
        ]
        
        for test_func in tests:
            result = test_func()
            self.results['tests'].append(result)
            
            # Force cleanup between tests
            if self.device == 'mps':
                torch.mps.empty_cache()
            gc.collect()
        
        return self.results
    
    def save_results(self, output_dir: str):
        """Save test results."""
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        # Save JSON results
        results_file = output_path / f"memory_stress_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(results_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print(f"\nResults saved to: {results_file}")
        
        # Generate summary
        self.print_summary()
    
    def print_summary(self):
        """Print test summary."""
        print("\n" + "=" * 50)
        print("Memory Stress Test Summary")
        print("=" * 50)
        
        for test in self.results['tests']:
            status_icon = "✅" if test['status'] == 'completed' else "❌"
            print(f"\n{status_icon} {test['test_name']}:")
            
            if test['test_name'] == 'large_tensor_allocation':
                print(f"  Maximum tensor size: {test.get('max_size_gb', 0):.1f}GB")
            elif test['test_name'] == 'many_small_tensors':
                print(f"  Allocated {test.get('num_tensors', 0)} tensors")
                print(f"  Total size: {test.get('total_allocated_gb', 0):.1f}GB")
            elif test['test_name'] == 'memory_fragmentation':
                print(f"  Completed {test.get('iterations', 0)} iterations")
            
            if test['status'] == 'failed':
                print(f"  Error: {test.get('error', 'Unknown')}")


def main():
    parser = argparse.ArgumentParser(description="Run OmniGPU memory stress tests")
    parser.add_argument('--max-memory-gb', type=float, default=32, 
                        help='Maximum memory to test (GB)')
    parser.add_argument('--output', default='memory-results',
                        help='Output directory for results')
    
    args = parser.parse_args()
    
    # Run tests
    tester = MemoryStressTest(max_memory_gb=args.max_memory_gb)
    tester.run_all_tests()
    tester.save_results(args.output)


if __name__ == '__main__':
    main()