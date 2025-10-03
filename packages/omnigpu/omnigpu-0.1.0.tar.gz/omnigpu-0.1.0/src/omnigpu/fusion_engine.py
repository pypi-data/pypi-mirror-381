"""
Operation Fusion Engine for OmniGPU
Detects common operation patterns and replaces them with optimized fused kernels.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Dict, List, Tuple, Optional, Callable, Any, Set
from collections import defaultdict, deque
import logging
import inspect
from dataclasses import dataclass
import weakref

logger = logging.getLogger(__name__)


@dataclass
class FusionPattern:
    """Represents a fusible operation pattern."""
    name: str
    ops: List[str]  # Operation types to match
    conditions: Optional[Callable] = None  # Additional conditions
    fused_op: Optional[Callable] = None  # The fused implementation
    estimated_speedup: float = 1.0


class OperationNode:
    """Node in the operation graph."""
    def __init__(self, op_type: str, op_func: Callable, args: tuple, kwargs: dict):
        self.op_type = op_type
        self.op_func = op_func
        self.args = args
        self.kwargs = kwargs
        self.inputs: List['OperationNode'] = []
        self.outputs: List['OperationNode'] = []
        self.output_tensor: Optional[torch.Tensor] = None
        self.node_id = id(self)
        
    def __repr__(self):
        return f"OpNode({self.op_type}, id={self.node_id})"


class OperationGraph:
    """Tracks operations to build a computation graph."""
    def __init__(self):
        self.nodes: List[OperationNode] = []
        self.tensor_to_node: weakref.WeakKeyDictionary = weakref.WeakKeyDictionary()
        self.active = False
        
    def add_operation(self, op_type: str, op_func: Callable, args: tuple, 
                     kwargs: dict, output: torch.Tensor) -> OperationNode:
        """Add an operation to the graph."""
        node = OperationNode(op_type, op_func, args, kwargs)
        node.output_tensor = output
        
        # Link inputs
        for arg in args:
            if isinstance(arg, torch.Tensor) and arg in self.tensor_to_node:
                input_node = self.tensor_to_node[arg]
                node.inputs.append(input_node)
                input_node.outputs.append(node)
        
        # Register output
        if isinstance(output, torch.Tensor):
            self.tensor_to_node[output] = node
        
        self.nodes.append(node)
        return node
    
    def find_patterns(self, patterns: List[FusionPattern]) -> List[Tuple[FusionPattern, List[OperationNode]]]:
        """Find fusible patterns in the graph."""
        matches = []
        
        for pattern in patterns:
            # Simple linear pattern matching for now
            for i in range(len(self.nodes) - len(pattern.ops) + 1):
                candidate_nodes = self.nodes[i:i + len(pattern.ops)]
                
                # Check if operation types match
                if all(node.op_type == expected_op 
                       for node, expected_op in zip(candidate_nodes, pattern.ops)):
                    
                    # Check if nodes are connected
                    connected = True
                    for j in range(len(candidate_nodes) - 1):
                        if candidate_nodes[j+1] not in candidate_nodes[j].outputs:
                            connected = False
                            break
                    
                    if connected:
                        # Check additional conditions
                        if pattern.conditions is None or pattern.conditions(candidate_nodes):
                            matches.append((pattern, candidate_nodes))
        
        return matches


class FusionEngine:
    """Main fusion engine that optimizes operation sequences."""
    
    def __init__(self):
        self.patterns = self._initialize_patterns()
        self.graph = OperationGraph()
        self.fusion_stats = defaultdict(int)
        self.original_ops = {}
        self.enabled = True
        
    def _initialize_patterns(self) -> List[FusionPattern]:
        """Initialize known fusion patterns."""
        patterns = []
        
        # Conv2d -> BatchNorm -> ReLU fusion
        patterns.append(FusionPattern(
            name="conv_bn_relu",
            ops=["conv2d", "batch_norm", "relu"],
            fused_op=self._fused_conv_bn_relu,
            estimated_speedup=1.5,
            conditions=self._check_conv_bn_relu_conditions
        ))
        
        # Conv2d -> BatchNorm fusion
        patterns.append(FusionPattern(
            name="conv_bn",
            ops=["conv2d", "batch_norm"],
            fused_op=self._fused_conv_bn,
            estimated_speedup=1.3
        ))
        
        # Linear -> ReLU fusion
        patterns.append(FusionPattern(
            name="linear_relu",
            ops=["linear", "relu"],
            fused_op=self._fused_linear_relu,
            estimated_speedup=1.2
        ))
        
        # MatMul -> Add -> ReLU fusion (common in transformers)
        patterns.append(FusionPattern(
            name="matmul_add_relu",
            ops=["matmul", "add", "relu"],
            fused_op=self._fused_matmul_add_relu,
            estimated_speedup=1.4
        ))
        
        # LayerNorm -> Linear fusion
        patterns.append(FusionPattern(
            name="layernorm_linear",
            ops=["layer_norm", "linear"],
            fused_op=self._fused_layernorm_linear,
            estimated_speedup=1.25
        ))
        
        # Attention pattern: Q*K^T -> Softmax -> *V
        patterns.append(FusionPattern(
            name="attention",
            ops=["matmul", "softmax", "matmul"],
            fused_op=self._fused_attention,
            estimated_speedup=2.0,
            conditions=self._check_attention_pattern
        ))
        
        return patterns
    
    def _check_conv_bn_relu_conditions(self, nodes: List[OperationNode]) -> bool:
        """Check if Conv->BN->ReLU can be fused."""
        conv_node, bn_node, relu_node = nodes
        
        # Check that conv output is only used by batch norm
        if len(conv_node.outputs) != 1:
            return False
            
        # Check that batch norm output is only used by relu
        if len(bn_node.outputs) != 1:
            return False
            
        # Check dimensions match
        try:
            conv_out_channels = conv_node.kwargs.get('out_channels') or conv_node.args[1]
            bn_features = bn_node.kwargs.get('num_features') or bn_node.args[0]
            return conv_out_channels == bn_features
        except:
            return True  # Assume compatible if we can't check
    
    def _check_attention_pattern(self, nodes: List[OperationNode]) -> bool:
        """Check if this is an attention pattern."""
        # Simple check - could be more sophisticated
        matmul1, softmax, matmul2 = nodes
        
        # Softmax should be on dim=-1 for attention
        softmax_dim = softmax.kwargs.get('dim', -1)
        return softmax_dim == -1 or softmax_dim == 2
    
    def _fused_conv_bn_relu(self, x: torch.Tensor, 
                           conv_weight: torch.Tensor, conv_bias: Optional[torch.Tensor],
                           bn_weight: torch.Tensor, bn_bias: torch.Tensor,
                           bn_mean: torch.Tensor, bn_var: torch.Tensor,
                           stride=1, padding=0, dilation=1, groups=1, eps=1e-5) -> torch.Tensor:
        """Fused Conv2d -> BatchNorm -> ReLU implementation."""
        # For MPS, we'll use a sequential approach but with pre-computed BN parameters
        # In production, this would be a custom Metal kernel
        
        # Fold batch norm into conv parameters
        std = (bn_var + eps).sqrt()
        conv_weight_fused = conv_weight * (bn_weight / std).reshape(-1, 1, 1, 1)
        
        if conv_bias is not None:
            conv_bias_fused = (conv_bias - bn_mean) * bn_weight / std + bn_bias
        else:
            conv_bias_fused = (- bn_mean) * bn_weight / std + bn_bias
        
        # Single fused operation
        out = F.conv2d(x, conv_weight_fused, conv_bias_fused, 
                      stride, padding, dilation, groups)
        return F.relu(out, inplace=True)
    
    def _fused_conv_bn(self, x: torch.Tensor,
                      conv_weight: torch.Tensor, conv_bias: Optional[torch.Tensor],
                      bn_weight: torch.Tensor, bn_bias: torch.Tensor,
                      bn_mean: torch.Tensor, bn_var: torch.Tensor,
                      stride=1, padding=0, dilation=1, groups=1, eps=1e-5) -> torch.Tensor:
        """Fused Conv2d -> BatchNorm implementation."""
        # Fold batch norm into conv parameters
        std = (bn_var + eps).sqrt()
        conv_weight_fused = conv_weight * (bn_weight / std).reshape(-1, 1, 1, 1)
        
        if conv_bias is not None:
            conv_bias_fused = (conv_bias - bn_mean) * bn_weight / std + bn_bias
        else:
            conv_bias_fused = (- bn_mean) * bn_weight / std + bn_bias
        
        return F.conv2d(x, conv_weight_fused, conv_bias_fused,
                       stride, padding, dilation, groups)
    
    def _fused_linear_relu(self, x: torch.Tensor, 
                          weight: torch.Tensor, bias: Optional[torch.Tensor]) -> torch.Tensor:
        """Fused Linear -> ReLU implementation."""
        # On MPS, this could be a custom kernel
        out = F.linear(x, weight, bias)
        return F.relu(out, inplace=True)
    
    def _fused_matmul_add_relu(self, a: torch.Tensor, b: torch.Tensor, 
                               c: torch.Tensor) -> torch.Tensor:
        """Fused MatMul -> Add -> ReLU implementation."""
        # Fused operation
        out = torch.addmm(c, a, b)  # More efficient than matmul + add
        return F.relu(out, inplace=True)
    
    def _fused_layernorm_linear(self, x: torch.Tensor,
                                normalized_shape: List[int], 
                                ln_weight: torch.Tensor, ln_bias: torch.Tensor,
                                linear_weight: torch.Tensor, linear_bias: Optional[torch.Tensor],
                                eps: float = 1e-5) -> torch.Tensor:
        """Fused LayerNorm -> Linear implementation."""
        # This could be optimized further with a custom kernel
        # For now, just ensure efficient memory usage
        x_normalized = F.layer_norm(x, normalized_shape, ln_weight, ln_bias, eps)
        return F.linear(x_normalized, linear_weight, linear_bias)
    
    def _fused_attention(self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor,
                        scale: Optional[float] = None) -> torch.Tensor:
        """Fused attention implementation (simplified)."""
        # Q @ K^T
        scores = torch.matmul(q, k.transpose(-2, -1))
        
        # Scale
        if scale is None:
            scale = q.size(-1) ** -0.5
        scores = scores * scale
        
        # Softmax
        attn_weights = F.softmax(scores, dim=-1)
        
        # @ V
        return torch.matmul(attn_weights, v)
    
    def patch_operations(self):
        """Patch PyTorch operations to track graph and apply fusions."""
        # Store original operations
        self.original_ops = {
            'conv2d': F.conv2d,
            'batch_norm': F.batch_norm,
            'relu': F.relu,
            'linear': F.linear,
            'matmul': torch.matmul,
            'layer_norm': F.layer_norm,
            'softmax': F.softmax,
        }
        
        # Create wrapped versions that track operations
        def make_wrapper(op_name: str, original_op: Callable):
            def wrapped(*args, **kwargs):
                if self.enabled and self.graph.active:
                    # Execute original operation
                    output = original_op(*args, **kwargs)
                    
                    # Track in graph
                    self.graph.add_operation(op_name, original_op, args, kwargs, output)
                    
                    # Try to apply fusions
                    self._try_apply_fusions()
                    
                    return output
                else:
                    return original_op(*args, **kwargs)
            
            return wrapped
        
        # Apply patches
        F.conv2d = make_wrapper('conv2d', self.original_ops['conv2d'])
        F.batch_norm = make_wrapper('batch_norm', self.original_ops['batch_norm'])
        F.relu = make_wrapper('relu', self.original_ops['relu'])
        F.linear = make_wrapper('linear', self.original_ops['linear'])
        torch.matmul = make_wrapper('matmul', self.original_ops['matmul'])
        F.layer_norm = make_wrapper('layer_norm', self.original_ops['layer_norm'])
        F.softmax = make_wrapper('softmax', self.original_ops['softmax'])
        
        logger.info("Operation fusion patches applied")
    
    def unpatch_operations(self):
        """Restore original operations."""
        if self.original_ops:
            F.conv2d = self.original_ops['conv2d']
            F.batch_norm = self.original_ops['batch_norm']
            F.relu = self.original_ops['relu']
            F.linear = self.original_ops['linear']
            torch.matmul = self.original_ops['matmul']
            F.layer_norm = self.original_ops['layer_norm']
            F.softmax = self.original_ops['softmax']
            
            logger.info("Operation fusion patches removed")
    
    def _try_apply_fusions(self):
        """Try to apply fusion patterns to the current graph."""
        if len(self.graph.nodes) < 2:
            return
        
        matches = self.graph.find_patterns(self.patterns)
        
        for pattern, nodes in matches:
            logger.debug(f"Found fusible pattern: {pattern.name}")
            self.fusion_stats[pattern.name] += 1
            
            # In a real implementation, we would:
            # 1. Replace the nodes with a fused operation
            # 2. Update the graph
            # 3. Return the fused result
            # For now, we just track statistics
    
    def optimize_model(self, model: nn.Module) -> nn.Module:
        """Optimize a model by detecting and fusing operations."""
        # This is a simplified version that analyzes module structure
        # A full implementation would trace execution
        
        optimized_modules = []
        
        for name, module in model.named_modules():
            # Check for Conv->BN->ReLU pattern
            if isinstance(module, nn.Sequential):
                i = 0
                while i < len(module):
                    # Conv->BN->ReLU
                    if (i + 2 < len(module) and
                        isinstance(module[i], nn.Conv2d) and
                        isinstance(module[i+1], nn.BatchNorm2d) and
                        isinstance(module[i+2], nn.ReLU)):
                        
                        # Create fused module
                        fused = FusedConvBNReLU(module[i], module[i+1])
                        optimized_modules.append((name, i, fused, 3))
                        logger.info(f"Fusing Conv->BN->ReLU in {name}")
                        i += 3
                        
                    # Conv->BN
                    elif (i + 1 < len(module) and
                          isinstance(module[i], nn.Conv2d) and
                          isinstance(module[i+1], nn.BatchNorm2d)):
                        
                        fused = FusedConvBN(module[i], module[i+1])
                        optimized_modules.append((name, i, fused, 2))
                        logger.info(f"Fusing Conv->BN in {name}")
                        i += 2
                        
                    else:
                        i += 1
        
        # Apply optimizations
        for module_name, idx, fused_module, num_replace in optimized_modules:
            parent = model
            parts = module_name.split('.')
            for part in parts[:-1]:
                parent = getattr(parent, part)
            
            sequential = getattr(parent, parts[-1]) if parts else model
            # Replace modules with fused version
            new_modules = list(sequential.children())
            new_modules[idx:idx+num_replace] = [fused_module]
            setattr(parent, parts[-1] if parts else '', nn.Sequential(*new_modules))
        
        return model
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get fusion statistics."""
        return {
            'fusion_counts': dict(self.fusion_stats),
            'total_fusions': sum(self.fusion_stats.values()),
            'graph_size': len(self.graph.nodes),
            'enabled': self.enabled
        }


class FusedConvBNReLU(nn.Module):
    """Fused Conv2d->BatchNorm2d->ReLU module."""
    
    def __init__(self, conv: nn.Conv2d, bn: nn.BatchNorm2d):
        super().__init__()
        self.conv = conv
        self.bn = bn
        self._prepare_fusion()
    
    def _prepare_fusion(self):
        """Prepare fused parameters."""
        # This is called once to precompute fused parameters
        if self.training:
            # During training, we can't fully fuse
            self.fused = False
        else:
            self.fused = True
            # Compute fused parameters
            conv_weight = self.conv.weight
            conv_bias = self.conv.bias
            
            bn_mean = self.bn.running_mean
            bn_var = self.bn.running_var
            bn_weight = self.bn.weight
            bn_bias = self.bn.bias
            eps = self.bn.eps
            
            # Fold BN into Conv
            std = (bn_var + eps).sqrt()
            self.weight_fused = conv_weight * (bn_weight / std).reshape(-1, 1, 1, 1)
            
            if conv_bias is not None:
                self.bias_fused = (conv_bias - bn_mean) * bn_weight / std + bn_bias
            else:
                self.bias_fused = (-bn_mean) * bn_weight / std + bn_bias
    
    def forward(self, x):
        if self.fused and not self.training:
            # Use fused operation
            return F.relu(
                F.conv2d(x, self.weight_fused, self.bias_fused,
                        self.conv.stride, self.conv.padding,
                        self.conv.dilation, self.conv.groups),
                inplace=True
            )
        else:
            # Standard execution during training
            x = self.conv(x)
            x = self.bn(x)
            return F.relu(x, inplace=True)


class FusedConvBN(nn.Module):
    """Fused Conv2d->BatchNorm2d module."""
    
    def __init__(self, conv: nn.Conv2d, bn: nn.BatchNorm2d):
        super().__init__()
        self.conv = conv
        self.bn = bn
        self._prepare_fusion()
    
    def _prepare_fusion(self):
        """Prepare fused parameters."""
        if self.training:
            self.fused = False
        else:
            self.fused = True
            # Compute fused parameters
            conv_weight = self.conv.weight
            conv_bias = self.conv.bias
            
            bn_mean = self.bn.running_mean
            bn_var = self.bn.running_var
            bn_weight = self.bn.weight
            bn_bias = self.bn.bias
            eps = self.bn.eps
            
            # Fold BN into Conv
            std = (bn_var + eps).sqrt()
            self.weight_fused = conv_weight * (bn_weight / std).reshape(-1, 1, 1, 1)
            
            if conv_bias is not None:
                self.bias_fused = (conv_bias - bn_mean) * bn_weight / std + bn_bias
            else:
                self.bias_fused = (-bn_mean) * bn_weight / std + bn_bias
    
    def forward(self, x):
        if self.fused and not self.training:
            # Use fused operation
            return F.conv2d(x, self.weight_fused, self.bias_fused,
                           self.conv.stride, self.conv.padding,
                           self.conv.dilation, self.conv.groups)
        else:
            # Standard execution during training
            x = self.conv(x)
            return self.bn(x)


# Global fusion engine instance
_fusion_engine = None


def get_fusion_engine() -> FusionEngine:
    """Get or create the global fusion engine."""
    global _fusion_engine
    if _fusion_engine is None:
        _fusion_engine = FusionEngine()
    return _fusion_engine


def enable_fusion():
    """Enable operation fusion optimization."""
    engine = get_fusion_engine()
    engine.enabled = True
    engine.patch_operations()
    logger.info("Operation fusion enabled")


def disable_fusion():
    """Disable operation fusion optimization."""
    engine = get_fusion_engine()
    engine.enabled = False
    engine.unpatch_operations()
    logger.info("Operation fusion disabled")


def optimize_model_for_fusion(model: nn.Module) -> nn.Module:
    """Optimize a model by applying operation fusion."""
    engine = get_fusion_engine()
    return engine.optimize_model(model)


def get_fusion_stats() -> Dict[str, Any]:
    """Get statistics about operation fusions."""
    engine = get_fusion_engine()
    return engine.get_statistics()


def reset_fusion_stats():
    """Reset fusion statistics."""
    engine = get_fusion_engine()
    engine.fusion_stats.clear()
    engine.graph = OperationGraph()


# Context manager for fusion scope
class fusion_scope:
    """Context manager to enable fusion for a specific scope."""
    
    def __init__(self, enabled: bool = True):
        self.enabled = enabled
        self.prev_state = None
        
    def __enter__(self):
        engine = get_fusion_engine()
        self.prev_state = engine.enabled
        if self.enabled:
            enable_fusion()
        else:
            disable_fusion()
        engine.graph.active = True
        return engine
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        engine = get_fusion_engine()
        engine.graph.active = False
        engine.enabled = self.prev_state


def main():
    """Demo of the fusion engine."""
    import time
    
    logging.basicConfig(level=logging.INFO)
    
    print("OmniGPU Operation Fusion Engine Demo")
    print("=" * 50)
    
    # Create a model with fusible patterns
    model = nn.Sequential(
        nn.Conv2d(3, 64, 3, padding=1),
        nn.BatchNorm2d(64),
        nn.ReLU(),
        nn.Conv2d(64, 128, 3, padding=1),
        nn.BatchNorm2d(128),
        nn.ReLU(),
        nn.AdaptiveAvgPool2d(1),
        nn.Flatten(),
        nn.Linear(128, 10)
    )
    
    # Input
    x = torch.randn(1, 3, 32, 32)
    device = 'mps' if torch.backends.mps.is_available() else 'cpu'
    model = model.to(device)
    x = x.to(device)
    
    # Benchmark original
    model.eval()
    with torch.no_grad():
        # Warmup
        for _ in range(10):
            _ = model(x)
        
        # Time original
        start = time.time()
        for _ in range(100):
            _ = model(x)
        original_time = time.time() - start
    
    print(f"Original model time: {original_time:.3f}s")
    
    # Optimize model
    print("\nOptimizing model...")
    optimized_model = optimize_model_for_fusion(model)
    
    # Benchmark optimized
    with torch.no_grad():
        # Warmup
        for _ in range(10):
            _ = optimized_model(x)
        
        # Time optimized
        start = time.time()
        for _ in range(100):
            _ = optimized_model(x)
        optimized_time = time.time() - start
    
    print(f"Optimized model time: {optimized_time:.3f}s")
    print(f"Speedup: {original_time / optimized_time:.2f}x")
    
    # Test with fusion scope
    print("\nTesting fusion scope...")
    with fusion_scope():
        # Operations in this scope will be tracked for fusion
        a = torch.randn(10, 20, device=device)
        b = torch.randn(20, 30, device=device)
        c = torch.randn(10, 30, device=device)
        
        # This pattern could be fused: MatMul -> Add -> ReLU
        result = torch.matmul(a, b)
        result = result + c
        result = F.relu(result)
    
    stats = get_fusion_stats()
    print(f"\nFusion statistics: {stats}")


if __name__ == "__main__":
    main()