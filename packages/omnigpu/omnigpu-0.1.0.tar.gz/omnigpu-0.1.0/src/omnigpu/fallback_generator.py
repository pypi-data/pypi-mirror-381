"""
Smart Fallback Generation for OmniGPU
Automatically generates CPU fallback wrappers for any PyTorch operation.
"""

import inspect
import torch
import torch.nn
import torch.nn.functional as F
from typing import Dict, List, Set, Callable, Any, Optional
import ast
import textwrap
import logging

logger = logging.getLogger(__name__)


class FallbackGenerator:
    """Automatically generates CPU fallback wrappers for PyTorch operations."""
    
    def __init__(self):
        self.generated_fallbacks = {}
        self.failed_ops = set()
        
    def generate_fallback(self, op_name: str, op_func: Callable, module_name: str = "torch") -> str:
        """
        Generate a CPU fallback wrapper for any PyTorch operation.
        
        Args:
            op_name: Name of the operation (e.g., 'sparse_coo_tensor')
            op_func: The actual function object
            module_name: Module name (torch, torch.nn.functional, etc.)
            
        Returns:
            Generated Python code for the fallback function
        """
        # Get function signature
        try:
            sig = inspect.signature(op_func)
        except:
            # If we can't inspect, create a generic wrapper
            return self._generate_generic_fallback(op_name, module_name)
        
        # Generate parameter list
        params = []
        param_names = []
        has_device_param = False
        
        for param_name, param in sig.parameters.items():
            if param_name == 'device':
                has_device_param = True
            
            if param.default == inspect.Parameter.empty:
                params.append(param_name)
            else:
                # Handle various default types
                default_str = self._format_default(param.default)
                params.append(f"{param_name}={default_str}")
            
            param_names.append(param_name)
        
        params_str = ", ".join(params)
        
        # Generate the fallback function
        code = f"""
def omnigpu_{op_name}_fallback({params_str}):
    '''CPU fallback for {module_name}.{op_name}'''
    import torch
    import logging
    
    logger = logging.getLogger('omnigpu.fallback')
    
    # Track device for return
    target_device = None
    
    # Check if any input tensors are on MPS/CUDA
    args_to_check = [{', '.join(f"'{p}': {p}" for p in param_names if p not in ['dtype', 'device', 'layout', 'requires_grad', 'pin_memory'])}]
    
    for arg_name, arg in args_to_check.items():
        if hasattr(arg, 'device'):
            if str(arg.device).startswith(('mps', 'cuda')):
                target_device = arg.device
                break
    
    # Convert tensors to CPU
    cpu_args = {{}}
    for arg_name, arg in args_to_check.items():
        if hasattr(arg, 'cpu'):
            cpu_args[arg_name] = arg.cpu()
        else:
            cpu_args[arg_name] = arg
    
    # Handle device parameter
    original_device = {f"locals().get('device', None)" if has_device_param else "None"}
    if 'device' in locals() and str(device).startswith(('mps', 'cuda')):
        cpu_args['device'] = 'cpu'
    
    try:
        # Call original operation on CPU
        result = {module_name}.{op_name}(**cpu_args)
        
        # Move result back to original device if needed
        if target_device is not None and hasattr(result, 'to'):
            result = result.to(target_device)
        elif original_device and str(original_device).startswith(('mps', 'cuda')) and hasattr(result, 'to'):
            result = result.to('mps' if torch.backends.mps.is_available() else 'cpu')
        
        logger.debug(f"Successfully executed {{op_name}} via CPU fallback")
        return result
        
    except Exception as e:
        logger.error(f"CPU fallback failed for {{op_name}}: {{e}}")
        raise
"""
        
        return textwrap.dedent(code).strip()
    
    def _generate_generic_fallback(self, op_name: str, module_name: str) -> str:
        """Generate a generic *args, **kwargs fallback for operations we can't inspect."""
        code = f"""
def omnigpu_{op_name}_fallback(*args, **kwargs):
    '''Generic CPU fallback for {module_name}.{op_name}'''
    import torch
    import logging
    
    logger = logging.getLogger('omnigpu.fallback')
    
    # Track device
    target_device = None
    
    # Check args for device
    cpu_args = []
    for arg in args:
        if hasattr(arg, 'device') and str(arg.device).startswith(('mps', 'cuda')):
            target_device = arg.device
            cpu_args.append(arg.cpu())
        elif hasattr(arg, 'cpu'):
            cpu_args.append(arg.cpu())
        else:
            cpu_args.append(arg)
    
    # Check kwargs for device
    cpu_kwargs = {{}}
    for k, v in kwargs.items():
        if k == 'device' and str(v).startswith(('mps', 'cuda')):
            cpu_kwargs[k] = 'cpu'
        elif hasattr(v, 'device') and str(v.device).startswith(('mps', 'cuda')):
            if target_device is None:
                target_device = v.device
            cpu_kwargs[k] = v.cpu()
        elif hasattr(v, 'cpu'):
            cpu_kwargs[k] = v.cpu()
        else:
            cpu_kwargs[k] = v
    
    try:
        # Call original operation
        result = {module_name}.{op_name}(*cpu_args, **cpu_kwargs)
        
        # Move result back if needed
        if target_device is not None and hasattr(result, 'to'):
            result = result.to(target_device)
        
        logger.debug(f"Successfully executed {op_name} via generic CPU fallback")
        return result
        
    except Exception as e:
        logger.error(f"Generic CPU fallback failed for {op_name}: {{e}}")
        raise
"""
        return textwrap.dedent(code).strip()
    
    def _format_default(self, default_value: Any) -> str:
        """Format default parameter values for code generation."""
        if default_value is None:
            return "None"
        elif isinstance(default_value, bool):
            return str(default_value)
        elif isinstance(default_value, (int, float)):
            return str(default_value)
        elif isinstance(default_value, str):
            return f"'{default_value}'"
        elif default_value == inspect.Parameter.empty:
            return "None"
        else:
            # For complex defaults, use None and handle in function
            return "None"
    
    def scan_module(self, module, module_name: str) -> Dict[str, str]:
        """
        Scan a PyTorch module and generate fallbacks for all operations.
        
        Args:
            module: The module to scan (e.g., torch, torch.nn.functional)
            module_name: String name of the module
            
        Returns:
            Dictionary mapping operation names to generated code
        """
        fallbacks = {}
        
        for name in dir(module):
            if name.startswith('_'):
                continue
                
            try:
                obj = getattr(module, name)
                
                # Check if it's a callable function
                if callable(obj) and not isinstance(obj, type):
                    code = self.generate_fallback(name, obj, module_name)
                    fallbacks[name] = code
                    logger.info(f"Generated fallback for {module_name}.{name}")
                    
            except Exception as e:
                logger.warning(f"Failed to generate fallback for {module_name}.{name}: {e}")
                self.failed_ops.add(f"{module_name}.{name}")
        
        return fallbacks
    
    def generate_all_fallbacks(self) -> Dict[str, Dict[str, str]]:
        """
        Generate fallbacks for all PyTorch operations.
        
        Returns:
            Nested dictionary: module_name -> {op_name -> code}
        """
        all_fallbacks = {}
        
        # Scan main PyTorch modules
        modules_to_scan = [
            (torch, 'torch'),
            (torch.nn.functional, 'torch.nn.functional'),
            (torch.sparse, 'torch.sparse'),
            (torch.linalg, 'torch.linalg'),
            (torch.fft, 'torch.fft'),
            (torch.special, 'torch.special'),
        ]
        
        for module, module_name in modules_to_scan:
            try:
                logger.info(f"Scanning {module_name}...")
                fallbacks = self.scan_module(module, module_name)
                all_fallbacks[module_name] = fallbacks
                logger.info(f"Generated {len(fallbacks)} fallbacks for {module_name}")
            except Exception as e:
                logger.error(f"Failed to scan {module_name}: {e}")
        
        self.generated_fallbacks = all_fallbacks
        return all_fallbacks
    
    def write_fallbacks_module(self, output_path: str = "auto_generated_fallbacks.py"):
        """Write all generated fallbacks to a Python module."""
        
        if not self.generated_fallbacks:
            self.generate_all_fallbacks()
        
        code_lines = [
            '"""',
            'Auto-generated CPU fallbacks for PyTorch operations.',
            'Generated by OmniGPU FallbackGenerator.',
            '"""',
            '',
            'import torch',
            'import torch.nn.functional as F',
            'import logging',
            '',
            'logger = logging.getLogger(__name__)',
            '',
            '# Generated fallback functions',
            ''
        ]
        
        # Count total operations
        total_ops = sum(len(ops) for ops in self.generated_fallbacks.values())
        code_lines.append(f"# Total operations with fallbacks: {total_ops}")
        code_lines.append("")
        
        # Add all fallback functions
        for module_name, operations in self.generated_fallbacks.items():
            code_lines.append(f"\n# {module_name} operations ({len(operations)} total)")
            code_lines.append("-" * 50)
            
            for op_name, code in operations.items():
                code_lines.append("")
                code_lines.append(code)
                code_lines.append("")
        
        # Add registry
        code_lines.extend([
            "",
            "# Fallback registry",
            "FALLBACK_REGISTRY = {",
        ])
        
        for module_name, operations in self.generated_fallbacks.items():
            for op_name in operations:
                code_lines.append(f"    '{module_name}.{op_name}': omnigpu_{op_name}_fallback,")
        
        code_lines.extend([
            "}",
            "",
            f"# Total fallbacks generated: {total_ops}",
            f"# Failed operations: {len(self.failed_ops)}",
        ])
        
        if self.failed_ops:
            code_lines.append("# Failed ops: " + ", ".join(sorted(self.failed_ops)))
        
        # Write to file
        with open(output_path, 'w') as f:
            f.write('\n'.join(code_lines))
        
        logger.info(f"Wrote {total_ops} fallbacks to {output_path}")
        return output_path


def main():
    """Generate all fallbacks when run as script."""
    import sys
    
    logging.basicConfig(level=logging.INFO)
    
    generator = FallbackGenerator()
    output_path = sys.argv[1] if len(sys.argv) > 1 else "auto_generated_fallbacks.py"
    
    logger.info("Starting fallback generation...")
    generator.generate_all_fallbacks()
    generator.write_fallbacks_module(output_path)
    
    print(f"\nGeneration complete!")
    print(f"Total operations with fallbacks: {sum(len(ops) for ops in generator.generated_fallbacks.values())}")
    print(f"Failed operations: {len(generator.failed_ops)}")
    print(f"Output written to: {output_path}")


if __name__ == "__main__":
    main()