"""
Systematic API Scanner for OmniGPU
Discovers all PyTorch operations by systematically scanning the API.
"""

import torch
import torch.nn
import torch.nn.functional as F
import inspect
from typing import Dict, List, Set, Tuple, Optional, Callable, Any
import logging
from collections import defaultdict
import json
import re

logger = logging.getLogger(__name__)


class PyTorchAPIScanner:
    """Systematically scans PyTorch modules to discover all operations."""
    
    def __init__(self):
        self.discovered_ops = defaultdict(list)
        self.operation_signatures = {}
        self.operation_metadata = {}
        self.categories = defaultdict(set)
        
    def scan_module(self, module, module_name: str, max_depth: int = 3) -> Dict[str, List[str]]:
        """
        Recursively scan a module for operations.
        
        Args:
            module: The module to scan
            module_name: Name of the module (e.g., 'torch')
            max_depth: Maximum recursion depth
        """
        logger.info(f"Scanning module: {module_name}")
        
        def _scan_recursive(obj, path: str, depth: int = 0):
            if depth > max_depth:
                return
            
            # Skip private attributes and special cases
            if any(skip in path for skip in ['_', '__', 'test', 'Test']):
                return
            
            try:
                for attr_name in dir(obj):
                    # Skip private and special attributes
                    if attr_name.startswith('_'):
                        continue
                    
                    try:
                        attr = getattr(obj, attr_name)
                        full_path = f"{path}.{attr_name}" if path else attr_name
                        
                        # Check if it's a callable operation
                        if callable(attr) and not isinstance(attr, type):
                            # Get operation info
                            op_info = self._analyze_operation(attr, full_path, module_name)
                            if op_info:
                                self.discovered_ops[module_name].append(op_info)
                                self.operation_metadata[full_path] = op_info
                        
                        # Recurse into submodules
                        elif inspect.ismodule(attr) and depth < max_depth:
                            _scan_recursive(attr, full_path, depth + 1)
                        
                    except Exception as e:
                        logger.debug(f"Error accessing {path}.{attr_name}: {e}")
                        
            except Exception as e:
                logger.debug(f"Error scanning {path}: {e}")
        
        _scan_recursive(module, module_name)
        
        logger.info(f"Found {len(self.discovered_ops[module_name])} operations in {module_name}")
        return self.discovered_ops[module_name]
    
    def _analyze_operation(self, op: Callable, path: str, module: str) -> Optional[Dict]:
        """Analyze a single operation to extract metadata."""
        try:
            # Get signature
            try:
                sig = inspect.signature(op)
                params = []
                for param_name, param in sig.parameters.items():
                    param_info = {
                        'name': param_name,
                        'default': param.default if param.default != inspect.Parameter.empty else None,
                        'annotation': str(param.annotation) if param.annotation != inspect.Parameter.empty else None
                    }
                    params.append(param_info)
            except:
                sig = None
                params = []
            
            # Get docstring
            doc = inspect.getdoc(op) or ""
            
            # Categorize operation
            category = self._categorize_operation(path, doc)
            
            # Check if it's tensor operation
            is_tensor_op = self._is_tensor_operation(op, doc, params)
            
            # Extract shape requirements
            shape_info = self._extract_shape_requirements(doc)
            
            op_info = {
                'name': path.split('.')[-1],
                'full_path': path,
                'module': module,
                'category': category,
                'is_tensor_op': is_tensor_op,
                'parameters': params,
                'docstring': doc[:200] + '...' if len(doc) > 200 else doc,
                'shape_requirements': shape_info,
                'has_cuda_kernel': self._likely_has_cuda_kernel(path, doc),
                'signature': str(sig) if sig else 'unknown'
            }
            
            # Add to category
            self.categories[category].add(path)
            
            return op_info
            
        except Exception as e:
            logger.debug(f"Error analyzing {path}: {e}")
            return None
    
    def _categorize_operation(self, path: str, doc: str) -> str:
        """Categorize operation based on name and documentation."""
        path_lower = path.lower()
        doc_lower = doc.lower()
        
        # Check common categories
        categories = {
            'math': ['add', 'sub', 'mul', 'div', 'matmul', 'dot', 'mm', 'bmm', 'pow', 'sqrt', 'exp', 'log'],
            'reduction': ['sum', 'mean', 'max', 'min', 'argmax', 'argmin', 'prod', 'std', 'var'],
            'activation': ['relu', 'sigmoid', 'tanh', 'gelu', 'softmax', 'logsoftmax', 'elu', 'selu'],
            'normalization': ['batch_norm', 'layer_norm', 'group_norm', 'instance_norm', 'normalize'],
            'convolution': ['conv', 'conv1d', 'conv2d', 'conv3d', 'conv_transpose'],
            'pooling': ['pool', 'max_pool', 'avg_pool', 'adaptive_pool'],
            'indexing': ['index', 'gather', 'scatter', 'select', 'take', 'put', 'narrow'],
            'shape': ['reshape', 'view', 'flatten', 'squeeze', 'unsqueeze', 'permute', 'transpose'],
            'creation': ['zeros', 'ones', 'empty', 'full', 'arange', 'linspace', 'eye', 'rand'],
            'comparison': ['eq', 'ne', 'lt', 'gt', 'le', 'ge', 'equal', 'allclose'],
            'sparse': ['sparse', 'coo', 'csr', 'csc'],
            'fft': ['fft', 'ifft', 'rfft', 'irfft'],
            'linalg': ['svd', 'eig', 'qr', 'cholesky', 'inv', 'solve', 'det', 'norm'],
            'special': ['gamma', 'digamma', 'erf', 'erfc', 'bessel'],
            'random': ['rand', 'randn', 'randint', 'multinomial', 'normal', 'uniform'],
            'nn': ['linear', 'dropout', 'embedding', 'lstm', 'gru', 'rnn', 'attention']
        }
        
        for category, keywords in categories.items():
            if any(kw in path_lower or kw in doc_lower for kw in keywords):
                return category
        
        return 'other'
    
    def _is_tensor_operation(self, op: Callable, doc: str, params: List[Dict]) -> bool:
        """Check if operation works with tensors."""
        tensor_indicators = [
            'tensor', 'Tensor',
            any(p['name'] in ['input', 'x', 'tensor', 'mat', 'vec'] for p in params),
            any('Tensor' in str(p.get('annotation', '')) for p in params),
            'tensor' in doc.lower()
        ]
        return any(tensor_indicators)
    
    def _extract_shape_requirements(self, doc: str) -> Dict[str, any]:
        """Extract shape requirements from documentation."""
        shape_info = {
            'dims': None,
            'broadcasting': False,
            'constraints': []
        }
        
        # Look for dimension requirements
        dim_patterns = [
            r'(\d+)[dD][-\s]?[tT]ensor',
            r'(\d+)[-\s]?dimensional',
            r'shape:?\s*\(([^)]+)\)'
        ]
        
        for pattern in dim_patterns:
            match = re.search(pattern, doc)
            if match:
                try:
                    shape_info['dims'] = int(match.group(1))
                except:
                    shape_info['constraints'].append(match.group(0))
        
        # Check for broadcasting
        if 'broadcast' in doc.lower():
            shape_info['broadcasting'] = True
        
        return shape_info
    
    def _likely_has_cuda_kernel(self, path: str, doc: str) -> bool:
        """Estimate if operation likely has CUDA kernel."""
        # Operations that typically have CUDA kernels
        cuda_likely = [
            'conv', 'matmul', 'bmm', 'addmm', 'linear',
            'batch_norm', 'layer_norm', 'softmax',
            'relu', 'gelu', 'pool',
            'embedding', 'lstm', 'gru'
        ]
        
        return any(op in path.lower() for op in cuda_likely)
    
    def scan_all_pytorch(self) -> Dict[str, List[Dict]]:
        """Scan all major PyTorch modules."""
        modules_to_scan = [
            (torch, 'torch'),
            (torch.nn.functional, 'torch.nn.functional'),
            (torch.nn, 'torch.nn'),
            (torch.Tensor, 'torch.Tensor'),
            (torch.sparse, 'torch.sparse'),
            (torch.linalg, 'torch.linalg'),
            (torch.fft, 'torch.fft'),
            (torch.special, 'torch.special'),
            (torch.cuda, 'torch.cuda'),
        ]
        
        all_ops = {}
        
        for module, name in modules_to_scan:
            try:
                ops = self.scan_module(module, name)
                all_ops[name] = ops
            except Exception as e:
                logger.error(f"Failed to scan {name}: {e}")
        
        return all_ops
    
    def find_unsupported_operations(self, supported_ops: Set[str]) -> List[Dict]:
        """Find operations that are not in the supported set."""
        unsupported = []
        
        for module, ops in self.discovered_ops.items():
            for op in ops:
                op_name = op['name']
                full_path = op['full_path']
                
                # Check various naming conventions
                is_supported = any([
                    op_name in supported_ops,
                    full_path in supported_ops,
                    f"torch.{op_name}" in supported_ops,
                    f"F.{op_name}" in supported_ops,
                ])
                
                if not is_supported and op['is_tensor_op']:
                    unsupported.append(op)
        
        return unsupported
    
    def generate_coverage_report(self, supported_ops: Set[str]) -> Dict[str, any]:
        """Generate detailed coverage report."""
        total_ops = sum(len(ops) for ops in self.discovered_ops.values())
        tensor_ops = sum(
            1 for ops in self.discovered_ops.values()
            for op in ops if op['is_tensor_op']
        )
        
        supported_count = 0
        supported_by_category = defaultdict(int)
        total_by_category = defaultdict(int)
        
        for module, ops in self.discovered_ops.items():
            for op in ops:
                if not op['is_tensor_op']:
                    continue
                    
                total_by_category[op['category']] += 1
                
                # Check if supported
                if any([
                    op['name'] in supported_ops,
                    op['full_path'] in supported_ops,
                    f"torch.{op['name']}" in supported_ops
                ]):
                    supported_count += 1
                    supported_by_category[op['category']] += 1
        
        # Calculate coverage by category
        category_coverage = {}
        for category in total_by_category:
            if total_by_category[category] > 0:
                coverage = supported_by_category[category] / total_by_category[category] * 100
                category_coverage[category] = {
                    'supported': supported_by_category[category],
                    'total': total_by_category[category],
                    'coverage': coverage
                }
        
        report = {
            'total_operations_found': total_ops,
            'tensor_operations': tensor_ops,
            'supported_operations': supported_count,
            'overall_coverage': (supported_count / tensor_ops * 100) if tensor_ops > 0 else 0,
            'coverage_by_category': category_coverage,
            'modules_scanned': list(self.discovered_ops.keys())
        }
        
        return report
    
    def export_operation_list(self, output_path: str = "pytorch_operations.json"):
        """Export discovered operations to JSON file."""
        export_data = {
            'metadata': {
                'total_operations': sum(len(ops) for ops in self.discovered_ops.values()),
                'modules': list(self.discovered_ops.keys()),
                'categories': {k: list(v) for k, v in self.categories.items()}
            },
            'operations': self.operation_metadata
        }
        
        with open(output_path, 'w') as f:
            json.dump(export_data, f, indent=2, default=str)
        
        logger.info(f"Exported {len(self.operation_metadata)} operations to {output_path}")
        return output_path
    
    def find_implementation_gaps(self) -> List[Tuple[str, List[str]]]:
        """Identify common operation patterns that might need implementation."""
        gaps = []
        
        # Group operations by prefix/suffix patterns
        patterns = defaultdict(list)
        
        for ops in self.discovered_ops.values():
            for op in ops:
                name = op['name']
                
                # Common patterns
                if name.endswith('_'):  # In-place operations
                    patterns['inplace'].append(name)
                elif name.endswith('_backward'):  # Backward passes
                    patterns['backward'].append(name)
                elif name.startswith('_'):  # Internal operations
                    patterns['internal'].append(name)
                elif 'sparse' in name:  # Sparse operations
                    patterns['sparse'].append(name)
                elif op['has_cuda_kernel']:  # Likely performance critical
                    patterns['performance_critical'].append(name)
        
        # Report significant patterns
        for pattern, ops in patterns.items():
            if len(ops) > 5:  # Only report patterns with multiple operations
                gaps.append((pattern, ops[:10]))  # Show first 10 examples
        
        return gaps


def main():
    """Run the API scanner."""
    import sys
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    scanner = PyTorchAPIScanner()
    
    logger.info("Starting PyTorch API scan...")
    all_ops = scanner.scan_all_pytorch()
    
    # Generate summary
    total = sum(len(ops) for ops in all_ops.values())
    print(f"\nDiscovered {total} total operations across PyTorch")
    
    # Show breakdown by module
    print("\nOperations by module:")
    for module, ops in sorted(all_ops.items(), key=lambda x: len(x[1]), reverse=True):
        print(f"  {module}: {len(ops)} operations")
    
    # Show category breakdown
    print("\nOperations by category:")
    for category, op_set in sorted(scanner.categories.items(), key=lambda x: len(x[1]), reverse=True):
        print(f"  {category}: {len(op_set)} operations")
    
    # Export results
    output_file = scanner.export_operation_list()
    print(f"\nDetailed results exported to: {output_file}")
    
    # Find implementation gaps
    gaps = scanner.find_implementation_gaps()
    if gaps:
        print("\nImplementation patterns to consider:")
        for pattern, examples in gaps:
            print(f"  {pattern}: {len(examples)} operations")
            print(f"    Examples: {', '.join(examples[:5])}")
    
    # Generate coverage report (using mock supported ops for demo)
    from omnigpu.ops import PATCH_REGISTRY
    supported = set(PATCH_REGISTRY.keys())
    
    coverage_report = scanner.generate_coverage_report(supported)
    print(f"\nCoverage Analysis:")
    print(f"  Total tensor operations: {coverage_report['tensor_operations']}")
    print(f"  Supported operations: {coverage_report['supported_operations']}")
    print(f"  Overall coverage: {coverage_report['overall_coverage']:.1f}%")
    
    print("\nCoverage by category:")
    for category, stats in sorted(
        coverage_report['coverage_by_category'].items(),
        key=lambda x: x[1]['coverage'],
        reverse=True
    ):
        print(f"  {category}: {stats['coverage']:.1f}% ({stats['supported']}/{stats['total']})")


if __name__ == "__main__":
    main()