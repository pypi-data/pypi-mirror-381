"""
Compatibility Scanner for OmniGPU
Analyzes Python files to identify PyTorch operations and reports support status.
"""

import ast
import os
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional
import torch
import logging
from collections import defaultdict, Counter

logger = logging.getLogger(__name__)


class TorchOperationVisitor(ast.NodeVisitor):
    """AST visitor to find PyTorch operations in Python code."""
    
    def __init__(self):
        self.operations = []
        self.torch_modules = {
            'torch', 'F', 'nn', 'torch.nn', 'torch.nn.functional',
            'torch.sparse', 'torch.linalg', 'torch.fft', 'torch.special'
        }
        self.current_file = None
        self.current_line = None
    
    def visit_Call(self, node):
        """Find function calls that might be PyTorch operations."""
        # Get the full call chain
        call_chain = self._get_call_chain(node.func)
        
        if call_chain and any(call_chain[0].startswith(m) for m in self.torch_modules):
            operation = {
                'name': call_chain[-1],
                'full_name': '.'.join(call_chain),
                'file': self.current_file,
                'line': node.lineno,
                'context': self._get_context(node)
            }
            self.operations.append(operation)
        
        self.generic_visit(node)
    
    def visit_Attribute(self, node):
        """Find attribute access that might be tensor methods."""
        # Check for tensor method calls like x.sum(), x.mean()
        if isinstance(node.value, ast.Name):
            # Could be a tensor variable
            operation = {
                'name': node.attr,
                'full_name': f'Tensor.{node.attr}',
                'file': self.current_file,
                'line': node.lineno,
                'context': self._get_context(node),
                'is_tensor_method': True
            }
            self.operations.append(operation)
        
        self.generic_visit(node)
    
    def _get_call_chain(self, node):
        """Extract the full call chain from an AST node."""
        parts = []
        
        while node:
            if isinstance(node, ast.Name):
                parts.append(node.id)
                break
            elif isinstance(node, ast.Attribute):
                parts.append(node.attr)
                node = node.value
            else:
                break
        
        return list(reversed(parts)) if parts else None
    
    def _get_context(self, node):
        """Get surrounding context for better reporting."""
        # In real implementation, would extract actual code context
        return f"Line {node.lineno}"


class CompatibilityScanner:
    """Scans codebases to identify PyTorch usage and OmniGPU compatibility."""
    
    def __init__(self):
        self.supported_ops = self._load_supported_operations()
        self.scan_results = {}
        self.operation_counts = Counter()
        self.file_stats = defaultdict(dict)
    
    def _load_supported_operations(self) -> Set[str]:
        """Load list of operations supported by OmniGPU."""
        # In production, this would load from the actual OmniGPU registry
        supported = set()
        
        # Core operations we've implemented
        core_ops = [
            'matmul', 'bmm', 'conv1d', 'conv2d', 'conv3d',
            'linear', 'addmm', 'mm', 'mv', 'dot',
            'sum', 'mean', 'max', 'min', 'argmax', 'argmin',
            'relu', 'gelu', 'sigmoid', 'tanh', 'softmax',
            'layer_norm', 'batch_norm', 'group_norm',
            'max_pool2d', 'avg_pool2d', 'adaptive_avg_pool2d',
            'dropout', 'embedding', 'one_hot',
            'cat', 'stack', 'split', 'chunk', 'reshape', 'view',
            'transpose', 'permute', 'squeeze', 'unsqueeze',
            'gather', 'scatter', 'index_select', 'masked_select',
            'where', 'clamp', 'clip',
            # Advanced indexing operations
            'index_put', 'index_add', 'index_copy', 'index_fill',
            'take_along_dim', 'put', 'take', 'narrow', 'repeat_interleave'
        ]
        
        for op in core_ops:
            supported.add(op)
            supported.add(f'torch.{op}')
            supported.add(f'F.{op}')
            supported.add(f'Tensor.{op}')
        
        return supported
    
    def scan_file(self, file_path: str) -> Dict[str, any]:
        """Scan a single Python file for PyTorch operations."""
        logger.info(f"Scanning {file_path}")
        
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Parse AST
            tree = ast.parse(content, filename=file_path)
            
            # Find operations
            visitor = TorchOperationVisitor()
            visitor.current_file = file_path
            visitor.visit(tree)
            
            # Analyze results
            total_ops = len(visitor.operations)
            supported_ops = []
            unsupported_ops = []
            unknown_ops = []
            
            for op in visitor.operations:
                op_name = op['name']
                full_name = op['full_name']
                
                # Check support status
                if any(full_name.endswith(supported) for supported in self.supported_ops):
                    supported_ops.append(op)
                    op['status'] = 'supported'
                elif self._is_likely_unsupported(op_name):
                    unsupported_ops.append(op)
                    op['status'] = 'unsupported'
                else:
                    unknown_ops.append(op)
                    op['status'] = 'unknown'
                
                # Track counts
                self.operation_counts[op_name] += 1
            
            # Calculate compatibility score
            compatibility_score = (len(supported_ops) / total_ops * 100) if total_ops > 0 else 100
            
            result = {
                'file': file_path,
                'total_operations': total_ops,
                'supported': len(supported_ops),
                'unsupported': len(unsupported_ops),
                'unknown': len(unknown_ops),
                'compatibility_score': compatibility_score,
                'operations': visitor.operations,
                'summary': {
                    'supported_ops': [op['full_name'] for op in supported_ops],
                    'unsupported_ops': [op['full_name'] for op in unsupported_ops],
                    'unknown_ops': [op['full_name'] for op in unknown_ops]
                }
            }
            
            self.scan_results[file_path] = result
            return result
            
        except Exception as e:
            logger.error(f"Error scanning {file_path}: {e}")
            return {
                'file': file_path,
                'error': str(e),
                'total_operations': 0,
                'compatibility_score': 0
            }
    
    def _is_likely_unsupported(self, op_name: str) -> bool:
        """Check if an operation is known to be unsupported."""
        unsupported_patterns = [
            'sparse_coo', 'sparse_csr', 'sparse_csc',  # Sparse operations
            'quantize', 'dequantize', 'fake_quantize',  # Quantization
            'distributed', 'all_reduce', 'all_gather',  # Distributed ops
            'jit', 'script', 'trace',  # JIT operations
            'autograd', 'backward', 'grad'  # Some autograd internals
        ]
        
        return any(pattern in op_name.lower() for pattern in unsupported_patterns)
    
    def scan_directory(self, directory: str, exclude_patterns: List[str] = None) -> Dict[str, any]:
        """Scan all Python files in a directory."""
        directory = Path(directory)
        exclude_patterns = exclude_patterns or ['__pycache__', '.git', 'venv', 'env']
        
        python_files = []
        for file_path in directory.rglob('*.py'):
            # Skip excluded directories
            if any(pattern in str(file_path) for pattern in exclude_patterns):
                continue
            python_files.append(str(file_path))
        
        logger.info(f"Found {len(python_files)} Python files to scan")
        
        # Scan all files
        results = []
        for file_path in python_files:
            result = self.scan_file(file_path)
            results.append(result)
        
        # Aggregate results
        total_files = len(results)
        total_operations = sum(r.get('total_operations', 0) for r in results)
        total_supported = sum(r.get('supported', 0) for r in results)
        total_unsupported = sum(r.get('unsupported', 0) for r in results)
        total_unknown = sum(r.get('unknown', 0) for r in results)
        
        avg_compatibility = (
            sum(r.get('compatibility_score', 0) for r in results) / total_files
            if total_files > 0 else 0
        )
        
        # Find most common operations
        most_common_ops = self.operation_counts.most_common(20)
        
        summary = {
            'directory': str(directory),
            'total_files': total_files,
            'total_operations': total_operations,
            'supported_operations': total_supported,
            'unsupported_operations': total_unsupported,
            'unknown_operations': total_unknown,
            'average_compatibility': avg_compatibility,
            'overall_compatibility': (total_supported / total_operations * 100) if total_operations > 0 else 100,
            'most_common_operations': most_common_ops,
            'file_results': results
        }
        
        return summary
    
    def generate_report(self, scan_results: Dict[str, any], output_path: Optional[str] = None) -> str:
        """Generate a detailed compatibility report."""
        report_lines = [
            "OmniGPU Compatibility Report",
            "=" * 50,
            "",
            f"Directory: {scan_results['directory']}",
            f"Total Files Scanned: {scan_results['total_files']}",
            f"Total PyTorch Operations Found: {scan_results['total_operations']}",
            "",
            "Compatibility Summary:",
            f"  Supported Operations: {scan_results['supported_operations']} ({scan_results['supported_operations']/scan_results['total_operations']*100:.1f}%)" if scan_results['total_operations'] > 0 else "  No operations found",
            f"  Unsupported Operations: {scan_results['unsupported_operations']}",
            f"  Unknown Operations: {scan_results['unknown_operations']}",
            f"  Overall Compatibility Score: {scan_results['overall_compatibility']:.1f}%",
            "",
            "Most Common Operations:",
        ]
        
        for op, count in scan_results['most_common_operations'][:10]:
            status = "✓" if op in self.supported_ops else "✗"
            report_lines.append(f"  {status} {op}: {count} occurrences")
        
        # Files with lowest compatibility
        report_lines.extend([
            "",
            "Files Needing Attention (lowest compatibility):"
        ])
        
        files_by_score = sorted(
            scan_results['file_results'],
            key=lambda x: x.get('compatibility_score', 100)
        )
        
        for file_result in files_by_score[:10]:
            if file_result.get('compatibility_score', 100) < 100:
                report_lines.append(
                    f"  {file_result['file']}: {file_result['compatibility_score']:.1f}% compatible"
                )
                if file_result.get('unsupported_ops'):
                    report_lines.append(
                        f"    Unsupported: {', '.join(file_result['summary']['unsupported_ops'][:3])}"
                    )
        
        # Recommendations
        report_lines.extend([
            "",
            "Recommendations:",
        ])
        
        if scan_results['overall_compatibility'] < 50:
            report_lines.append("  - Critical: Low compatibility detected. Consider implementing missing operations.")
        elif scan_results['overall_compatibility'] < 80:
            report_lines.append("  - Moderate compatibility. Some operations need fallbacks.")
        else:
            report_lines.append("  - Good compatibility! Most operations are supported.")
        
        if scan_results['unsupported_operations'] > 0:
            report_lines.append(f"  - {scan_results['unsupported_operations']} operations need CPU fallbacks")
        
        report = '\n'.join(report_lines)
        
        if output_path:
            with open(output_path, 'w') as f:
                f.write(report)
            logger.info(f"Report written to {output_path}")
        
        return report
    
    def check_model(self, model_class) -> Dict[str, any]:
        """Check a specific model class for compatibility."""
        # This would analyze the model's forward pass
        # For now, return a placeholder
        return {
            'model': str(model_class),
            'status': 'analysis_pending',
            'compatibility': 'unknown'
        }


def main():
    """Example usage of the compatibility scanner."""
    import sys
    
    logging.basicConfig(level=logging.INFO)
    
    scanner = CompatibilityScanner()
    
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = "."
    
    logger.info(f"Scanning {target} for PyTorch operations...")
    
    if os.path.isfile(target):
        results = scanner.scan_file(target)
        print(f"\nFile: {target}")
        print(f"Compatibility: {results['compatibility_score']:.1f}%")
        print(f"Operations: {results['total_operations']} total")
        print(f"  Supported: {results['supported']}")
        print(f"  Unsupported: {results['unsupported']}")
    else:
        results = scanner.scan_directory(target)
        report = scanner.generate_report(results)
        print("\n" + report)
        
        # Save detailed results
        import json
        with open('compatibility_scan.json', 'w') as f:
            json.dump(results, f, indent=2, default=str)
        print("\nDetailed results saved to compatibility_scan.json")


if __name__ == "__main__":
    main()