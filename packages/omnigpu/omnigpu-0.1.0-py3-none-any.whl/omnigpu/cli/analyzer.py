"""Compatibility analyzer for OmniGPU.

Analyzes Python code to determine GPU compatibility and suggests fixes.
"""

import ast
import os
import sys
from typing import Dict, List, Set, Tuple, Optional
from dataclasses import dataclass, field
from pathlib import Path
import json

@dataclass
class CompatibilityIssue:
    """Represents a compatibility issue found in code."""
    file: str
    line: int
    column: int
    issue_type: str
    description: str
    suggestion: str
    severity: str  # 'error', 'warning', 'info'
    code_snippet: Optional[str] = None

@dataclass
class AnalysisResult:
    """Results of compatibility analysis."""
    total_files: int = 0
    compatible_files: int = 0
    issues: List[CompatibilityIssue] = field(default_factory=list)
    cuda_calls: Dict[str, int] = field(default_factory=dict)
    frameworks_detected: Set[str] = field(default_factory=set)
    estimated_compatibility: float = 0.0
    
    def add_issue(self, issue: CompatibilityIssue):
        """Add a compatibility issue."""
        self.issues.append(issue)
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization."""
        return {
            'total_files': self.total_files,
            'compatible_files': self.compatible_files,
            'issues': [
                {
                    'file': i.file,
                    'line': i.line,
                    'column': i.column,
                    'type': i.issue_type,
                    'description': i.description,
                    'suggestion': i.suggestion,
                    'severity': i.severity,
                    'code_snippet': i.code_snippet
                } for i in self.issues
            ],
            'cuda_calls': self.cuda_calls,
            'frameworks_detected': list(self.frameworks_detected),
            'estimated_compatibility': self.estimated_compatibility
        }


class CUDACallVisitor(ast.NodeVisitor):
    """AST visitor to find CUDA-specific calls."""
    
    def __init__(self, filename: str, result: AnalysisResult):
        self.filename = filename
        self.result = result
        self.current_line = 0
        
        # Patterns to detect
        self.cuda_patterns = {
            'cuda': 'Direct .cuda() call',
            'to': 'tensor.to("cuda") call',
            'torch.cuda': 'torch.cuda namespace',
            'device': 'torch.device("cuda")',
            'is_available': 'cuda.is_available()',
            'cupy': 'CuPy library usage',
            'numba.cuda': 'Numba CUDA kernels'
        }
        
        # Compatible patterns (already work with OmniGPU)
        self.compatible_patterns = {
            'omnigpu',
            'ugpu',
            'auto_device',
            'to_device'
        }
    
    def visit_Call(self, node: ast.Call):
        """Visit function calls."""
        self.current_line = node.lineno
        
        # Check for .cuda() calls
        if isinstance(node.func, ast.Attribute):
            if node.func.attr == 'cuda':
                self._add_cuda_call('cuda', node)
            elif node.func.attr == 'to':
                # Check if it's .to('cuda') or .to(device='cuda')
                for arg in node.args:
                    if isinstance(arg, ast.Str) and 'cuda' in arg.s:
                        self._add_cuda_call('to', node)
                for keyword in node.keywords:
                    if keyword.arg == 'device' and isinstance(keyword.value, ast.Str):
                        if 'cuda' in keyword.value.s:
                            self._add_cuda_call('to', node)
        
        # Check for torch.cuda calls
        if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Attribute):
            if (hasattr(node.func.value, 'id') and node.func.value.id == 'torch' and 
                node.func.value.attr == 'cuda'):
                self._add_cuda_call('torch.cuda', node)
        
        self.generic_visit(node)
    
    def visit_Attribute(self, node: ast.Attribute):
        """Visit attribute access."""
        self.current_line = node.lineno
        
        # Check for torch.cuda namespace
        if isinstance(node.value, ast.Name) and node.value.id == 'torch' and node.attr == 'cuda':
            self._add_cuda_call('torch.cuda', node)
        
        self.generic_visit(node)
    
    def visit_Import(self, node: ast.Import):
        """Visit import statements."""
        for alias in node.names:
            if 'torch' in alias.name:
                self.result.frameworks_detected.add('pytorch')
            elif 'tensorflow' in alias.name or 'tf' == alias.name:
                self.result.frameworks_detected.add('tensorflow')
            elif 'jax' in alias.name:
                self.result.frameworks_detected.add('jax')
            elif 'cupy' in alias.name:
                self.result.frameworks_detected.add('cupy')
                self._add_issue(
                    node.lineno, node.col_offset,
                    'framework', 'CuPy detected',
                    'CuPy may require additional OmniGPU support',
                    'warning'
                )
        
        self.generic_visit(node)
    
    def visit_ImportFrom(self, node: ast.ImportFrom):
        """Visit from imports."""
        if node.module:
            if 'torch' in node.module:
                self.result.frameworks_detected.add('pytorch')
            elif 'tensorflow' in node.module:
                self.result.frameworks_detected.add('tensorflow')
            elif 'jax' in node.module:
                self.result.frameworks_detected.add('jax')
            elif 'numba' in node.module and any('cuda' in n.name for n in node.names):
                self._add_issue(
                    node.lineno, node.col_offset,
                    'cuda_kernel', 'Numba CUDA kernel detected',
                    'Custom CUDA kernels require manual porting',
                    'error'
                )
        
        self.generic_visit(node)
    
    def _add_cuda_call(self, call_type: str, node: ast.AST):
        """Record a CUDA call."""
        key = f"{call_type}:{self.filename}:{node.lineno}"
        self.result.cuda_calls[call_type] = self.result.cuda_calls.get(call_type, 0) + 1
        
        if call_type == 'cuda':
            self._add_issue(
                node.lineno, node.col_offset,
                'cuda_call', 'Direct .cuda() call detected',
                'Will be automatically handled by OmniGPU auto_patch',
                'info'
            )
        elif call_type == 'to':
            self._add_issue(
                node.lineno, node.col_offset,
                'cuda_to', '.to("cuda") call detected',
                'Will be automatically handled by OmniGPU auto_patch',
                'info'
            )
    
    def _add_issue(self, line: int, col: int, issue_type: str, 
                   description: str, suggestion: str, severity: str):
        """Add a compatibility issue."""
        issue = CompatibilityIssue(
            file=self.filename,
            line=line,
            column=col,
            issue_type=issue_type,
            description=description,
            suggestion=suggestion,
            severity=severity
        )
        self.result.add_issue(issue)


class CompatibilityAnalyzer:
    """Analyzes code compatibility with OmniGPU."""
    
    def __init__(self):
        self.result = AnalysisResult()
    
    def analyze_file(self, filepath: Path) -> None:
        """Analyze a single Python file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            tree = ast.parse(content, filename=str(filepath))
            visitor = CUDACallVisitor(str(filepath), self.result)
            visitor.visit(tree)
            
            self.result.total_files += 1
            
            # Check if file uses OmniGPU
            if 'omnigpu' in content or 'ugpu' in content:
                self.result.compatible_files += 1
            
        except SyntaxError as e:
            self.result.add_issue(CompatibilityIssue(
                file=str(filepath),
                line=e.lineno or 0,
                column=e.offset or 0,
                issue_type='syntax_error',
                description=f'Python syntax error: {e.msg}',
                suggestion='Fix syntax errors before analysis',
                severity='error'
            ))
        except Exception as e:
            self.result.add_issue(CompatibilityIssue(
                file=str(filepath),
                line=0,
                column=0,
                issue_type='analysis_error',
                description=f'Error analyzing file: {str(e)}',
                suggestion='Check file permissions and encoding',
                severity='error'
            ))
    
    def analyze_directory(self, directory: Path, recursive: bool = True) -> None:
        """Analyze all Python files in a directory."""
        pattern = '**/*.py' if recursive else '*.py'
        
        for filepath in directory.glob(pattern):
            if filepath.is_file() and not filepath.name.startswith('.'):
                # Skip virtual environments and common non-source directories
                parts = filepath.parts
                skip_dirs = {'venv', 'env', '.env', 'node_modules', '__pycache__', 
                           '.git', '.tox', 'build', 'dist', '.eggs'}
                
                if not any(part in skip_dirs for part in parts):
                    self.analyze_file(filepath)
    
    def calculate_compatibility(self) -> None:
        """Calculate overall compatibility score."""
        if self.result.total_files == 0:
            self.result.estimated_compatibility = 0.0
            return
        
        # Base score from file compatibility
        base_score = (self.result.compatible_files / self.result.total_files) * 100
        
        # Penalty for issues
        error_count = sum(1 for i in self.result.issues if i.severity == 'error')
        warning_count = sum(1 for i in self.result.issues if i.severity == 'warning')
        
        penalty = (error_count * 5 + warning_count * 2)
        
        # Bonus for using compatible frameworks
        framework_bonus = len(self.result.frameworks_detected & {'pytorch', 'jax'}) * 5
        
        # Calculate final score
        score = max(0, min(100, base_score - penalty + framework_bonus))
        
        # Adjust based on CUDA call density
        total_cuda_calls = sum(self.result.cuda_calls.values())
        if total_cuda_calls > 0:
            # Most CUDA calls are automatically handled
            auto_handled = self.result.cuda_calls.get('cuda', 0) + self.result.cuda_calls.get('to', 0)
            handled_ratio = auto_handled / total_cuda_calls
            score = score * 0.5 + (score * handled_ratio * 0.5)
        
        self.result.estimated_compatibility = round(score, 1)
    
    def generate_report(self) -> str:
        """Generate a human-readable report."""
        self.calculate_compatibility()
        
        report = []
        report.append("═" * 60)
        report.append("OmniGPU Compatibility Analysis Report")
        report.append("═" * 60)
        report.append("")
        
        # Summary
        report.append("📊 Summary")
        report.append(f"   Files analyzed: {self.result.total_files}")
        report.append(f"   Compatible files: {self.result.compatible_files}")
        report.append(f"   Compatibility score: {self.result.estimated_compatibility}%")
        report.append("")
        
        # Frameworks detected
        if self.result.frameworks_detected:
            report.append("🔧 Frameworks Detected")
            for fw in sorted(self.result.frameworks_detected):
                status = "✅" if fw in {'pytorch', 'jax'} else "⚠️"
                report.append(f"   {status} {fw}")
            report.append("")
        
        # CUDA usage statistics
        if self.result.cuda_calls:
            report.append("🎮 CUDA Usage Statistics")
            for call_type, count in sorted(self.result.cuda_calls.items()):
                report.append(f"   {call_type}: {count} occurrences")
            report.append("")
        
        # Issues by severity
        errors = [i for i in self.result.issues if i.severity == 'error']
        warnings = [i for i in self.result.issues if i.severity == 'warning']
        info = [i for i in self.result.issues if i.severity == 'info']
        
        if errors:
            report.append(f"❌ Errors ({len(errors)})")
            for issue in errors[:5]:  # Show first 5
                report.append(f"   {issue.file}:{issue.line} - {issue.description}")
                report.append(f"      💡 {issue.suggestion}")
            if len(errors) > 5:
                report.append(f"   ... and {len(errors) - 5} more")
            report.append("")
        
        if warnings:
            report.append(f"⚠️  Warnings ({len(warnings)})")
            for issue in warnings[:5]:
                report.append(f"   {issue.file}:{issue.line} - {issue.description}")
            if len(warnings) > 5:
                report.append(f"   ... and {len(warnings) - 5} more")
            report.append("")
        
        # Recommendations
        report.append("💡 Recommendations")
        if self.result.estimated_compatibility >= 90:
            report.append("   ✅ Your code is highly compatible with OmniGPU!")
            report.append("   Add these lines to enable OmniGPU:")
            report.append("      import omnigpu")
            report.append("      omnigpu.enable_cuda_compatibility()")
        elif self.result.estimated_compatibility >= 70:
            report.append("   ⚠️  Your code is mostly compatible with OmniGPU")
            report.append("   Some manual changes may be needed for:")
            for issue in errors[:3]:
                report.append(f"      - {issue.description}")
        else:
            report.append("   ❌ Significant changes needed for OmniGPU compatibility")
            report.append("   Main issues:")
            for issue in errors[:3]:
                report.append(f"      - {issue.description}")
        
        report.append("")
        report.append("═" * 60)
        
        return "\n".join(report)


def main():
    """CLI entry point for the analyzer."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Analyze code compatibility with OmniGPU',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  ugpu analyze myproject/              # Analyze a directory
  ugpu analyze script.py               # Analyze a single file
  ugpu analyze . --output report.json  # Save detailed JSON report
        """
    )
    
    parser.add_argument('path', help='File or directory to analyze')
    parser.add_argument('--no-recursive', action='store_true', 
                       help='Don\'t analyze subdirectories')
    parser.add_argument('--output', '-o', help='Save detailed results to JSON file')
    parser.add_argument('--quiet', '-q', action='store_true',
                       help='Only show compatibility score')
    
    args = parser.parse_args()
    
    # Create analyzer
    analyzer = CompatibilityAnalyzer()
    path = Path(args.path)
    
    # Analyze
    if path.is_file():
        analyzer.analyze_file(path)
    elif path.is_dir():
        analyzer.analyze_directory(path, recursive=not args.no_recursive)
    else:
        print(f"Error: {path} not found")
        sys.exit(1)
    
    # Output results
    if args.quiet:
        analyzer.calculate_compatibility()
        print(f"{analyzer.result.estimated_compatibility}%")
    else:
        print(analyzer.generate_report())
    
    # Save JSON if requested
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(analyzer.result.to_dict(), f, indent=2)
        print(f"\n📄 Detailed results saved to {args.output}")
    
    # Exit code based on compatibility
    sys.exit(0 if analyzer.result.estimated_compatibility >= 70 else 1)


if __name__ == '__main__':
    main()