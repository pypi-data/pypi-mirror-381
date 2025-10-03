"""Graph-level optimization for OmniGPU.

This module implements computation graph analysis and optimization,
including operation fusion, memory optimization, and device-specific rewrites.
"""
import torch
import torch.nn as nn
from typing import Dict, List, Tuple, Optional, Any, Union
from dataclasses import dataclass
import logging
from collections import defaultdict
import torch.fx as fx
from torch.fx.passes.shape_prop import ShapeProp
from .fusion_kernels import (
    FusedConvBNReLU, FusedLinearActivation, OptimizedMultiHeadAttention,
    optimize_sequential_block, apply_device_optimizations,
    create_fused_conv_bn_relu
)

logger = logging.getLogger(__name__)


@dataclass
class OptimizationStats:
    """Statistics about graph optimizations performed."""
    original_ops: int
    optimized_ops: int
    fusions_applied: int
    memory_saved_bytes: int
    estimated_speedup: float
    failure_reason: Optional[str] = None
    details: Optional[Dict[str, Any]] = None


class PatternMatcher:
    """Identifies optimization patterns in computation graphs."""
    
    def __init__(self):
        self.patterns = {
            'conv_bn_relu': self._match_conv_bn_relu,
            'linear_activation': self._match_linear_activation,
            'attention_pattern': self._match_attention_pattern,
            'matmul_chain': self._match_matmul_chain,
        }
    
    def find_patterns(self, graph: fx.Graph) -> Dict[str, List[fx.Node]]:
        """Find all optimization patterns in the graph."""
        matches = defaultdict(list)
        
        for pattern_name, matcher in self.patterns.items():
            nodes = list(graph.nodes)
            for i, node in enumerate(nodes):
                if match := matcher(node, nodes[i:]):
                    matches[pattern_name].append(match)
        
        return dict(matches)
    
    def _match_conv_bn_relu(self, node: fx.Node, remaining: List[fx.Node]) -> Optional[List[fx.Node]]:
        """Match Conv2d -> BatchNorm2d -> ReLU pattern."""
        if len(remaining) < 3:
            return None
            
        conv_node = remaining[0]
        if not (conv_node.op == 'call_module' and 
                isinstance(conv_node.target, str) and 
                'conv' in conv_node.target.lower()):
            return None
        
        # Check if next node is BatchNorm
        bn_node = None
        relu_node = None
        
        for next_node in remaining[1:3]:
            if (next_node.op == 'call_module' and 
                'bn' in str(next_node.target).lower() and
                conv_node in next_node.args):
                bn_node = next_node
                
                # Look for ReLU after BatchNorm
                for final_node in remaining[2:4]:
                    if (final_node.op == 'call_function' and
                        final_node.target in [torch.relu, torch.nn.functional.relu] and
                        bn_node in final_node.args):
                        relu_node = final_node
                        break
                break
        
        if bn_node and relu_node:
            return [conv_node, bn_node, relu_node]
        return None
    
    def _match_linear_activation(self, node: fx.Node, remaining: List[fx.Node]) -> Optional[List[fx.Node]]:
        """Match Linear -> Activation patterns."""
        if len(remaining) < 2:
            return None
            
        linear_node = remaining[0]
        if not (linear_node.op == 'call_module' and
                isinstance(linear_node.target, str) and
                'linear' in linear_node.target.lower()):
            return None
        
        # Check next node for activation
        for next_node in remaining[1:3]:
            if (next_node.op in ['call_function', 'call_module'] and
                linear_node in next_node.args):
                # Check if it's an activation
                if next_node.op == 'call_function':
                    if next_node.target in [torch.relu, torch.gelu, torch.sigmoid, 
                                           torch.tanh, torch.nn.functional.relu,
                                           torch.nn.functional.gelu]:
                        return [linear_node, next_node]
        
        return None
    
    def _match_attention_pattern(self, node: fx.Node, remaining: List[fx.Node]) -> Optional[List[fx.Node]]:
        """Match multi-head attention patterns that can be optimized."""
        # Simplified - would need more complex matching for real attention
        if (node.op == 'call_module' and 
            'attention' in str(node.target).lower()):
            return [node]
        return None
    
    def _match_matmul_chain(self, node: fx.Node, remaining: List[fx.Node]) -> Optional[List[fx.Node]]:
        """Match chains of matrix multiplications."""
        if not (node.op == 'call_function' and node.target == torch.matmul):
            return None
        
        chain = [node]
        current = node
        
        # Follow the chain
        for next_node in remaining[1:]:
            if (next_node.op == 'call_function' and 
                next_node.target == torch.matmul and
                current in next_node.args):
                chain.append(next_node)
                current = next_node
            else:
                break
        
        return chain if len(chain) > 1 else None


class GraphRewriter:
    """Rewrites computation graphs for optimization."""
    
    def __init__(self, device_type: str):
        self.device_type = device_type
        self.stats = OptimizationStats(0, 0, 0, 0, 1.0)
    
    def rewrite_graph(
        self,
        model: nn.Module,
        graph: fx.Graph,
        patterns: Dict[str, List[Any]],
        *,
        example_inputs: Tuple[Any, ...] = (),
        example_kwargs: Optional[Dict[str, Any]] = None,
    ) -> fx.Graph:
        """Apply optimizing rewrites to the graph."""
        self.stats = OptimizationStats(
            original_ops=len(list(graph.nodes)),
            optimized_ops=len(list(graph.nodes)),
            fusions_applied=0,
            memory_saved_bytes=0,
            estimated_speedup=1.0,
            failure_reason=None,
            details={'example_kwargs': bool(example_kwargs)} if example_kwargs else None,
        )

        # Apply different optimizations
        if 'conv_bn_relu' in patterns:
            self._fuse_conv_bn_relu(model, graph, patterns['conv_bn_relu'])
        
        if 'linear_activation' in patterns:
            self._fuse_linear_activation(model, graph, patterns['linear_activation'])
            
        if 'matmul_chain' in patterns:
            self._optimize_matmul_chain(model, graph, patterns['matmul_chain'])
        
        self.stats.optimized_ops = len(list(graph.nodes))
        return graph
    
    def _fuse_conv_bn_relu(self, model: nn.Module, graph: fx.Graph, matches: List[List[fx.Node]]):
        """Fuse Conv-BN-ReLU into a single operation."""
        for conv_node, bn_node, relu_node in matches:
            # Get the actual modules
            conv_module = dict(model.named_modules())[conv_node.target]
            bn_module = dict(model.named_modules())[bn_node.target]
            
            # Create fused module
            fused = create_fused_conv_bn_relu(conv_module, bn_module)
            
            # Replace in model
            parent_name = '.'.join(conv_node.target.split('.')[:-1]) if '.' in conv_node.target else ''
            child_name = conv_node.target.split('.')[-1]
            
            if parent_name:
                parent = dict(model.named_modules())[parent_name]
                setattr(parent, child_name, fused)
            else:
                setattr(model, child_name, fused)
            
            # Update graph to skip BN and ReLU
            conv_node.meta['fused_with'] = ['bn', 'relu']
            self.stats.fusions_applied += 1
            self.stats.estimated_speedup *= 1.15  # 15% speedup estimate
    
    def _fuse_linear_activation(self, model: nn.Module, graph: fx.Graph, matches: List[List[fx.Node]]):
        """Fuse Linear with activation functions."""
        for linear_node, act_node in matches:
            if linear_node.op == 'call_module' and act_node.op == 'call_function':
                # Get linear module
                linear_module = dict(model.named_modules())[linear_node.target]
                
                # Determine activation type
                act_name = act_node.target.__name__ if hasattr(act_node.target, '__name__') else 'relu'
                
                # Create fused module
                fused = FusedLinearActivation(linear_module, act_name)
                
                # Replace in model
                parent_name = '.'.join(linear_node.target.split('.')[:-1]) if '.' in linear_node.target else ''
                child_name = linear_node.target.split('.')[-1]
                
                if parent_name:
                    parent = dict(model.named_modules())[parent_name]
                    setattr(parent, child_name, fused)
                else:
                    setattr(model, child_name, fused)
                
                linear_node.meta['fused_activation'] = act_name
                self.stats.fusions_applied += 1
                self.stats.estimated_speedup *= 1.05  # 5% speedup estimate
    
    def _optimize_matmul_chain(self, model: nn.Module, graph: fx.Graph, matches: List[List[fx.Node]]):
        """Optimize chains of matrix multiplications."""
        for chain in matches:
            if len(chain) > 2:
                # Mark for optimization
                chain[0].meta['matmul_chain_length'] = len(chain)
                self.stats.fusions_applied += 1
                self.stats.estimated_speedup *= (1.0 + 0.2 * (len(chain) - 1))


class MemoryOptimizer:
    """Optimizes memory usage in computation graphs."""
    
    def __init__(self):
        self.reuse_map = {}
    
    def optimize_memory(self, graph: fx.Graph) -> fx.Graph:
        """Apply memory optimizations to the graph."""
        # Analyze tensor lifetimes
        tensor_lifetimes = self._analyze_lifetimes(graph)
        
        # Find reuse opportunities
        self._find_reuse_opportunities(tensor_lifetimes)
        
        # Apply in-place operations where possible
        self._apply_inplace_ops(graph)
        
        return graph
    
    def _analyze_lifetimes(self, graph: fx.Graph) -> Dict[fx.Node, Tuple[int, int]]:
        """Analyze when tensors are created and last used."""
        lifetimes = {}
        node_positions = {node: i for i, node in enumerate(graph.nodes)}
        
        for i, node in enumerate(graph.nodes):
            # First occurrence is creation
            if node not in lifetimes:
                lifetimes[node] = [i, i]
            
            # Update last use for all arguments
            for arg in node.args:
                if isinstance(arg, fx.Node) and arg in lifetimes:
                    lifetimes[arg][1] = i
        
        return lifetimes
    
    def _find_reuse_opportunities(self, lifetimes: Dict[fx.Node, Tuple[int, int]]):
        """Find tensors that can reuse memory."""
        # Sort by end time
        sorted_tensors = sorted(lifetimes.items(), key=lambda x: x[1][1])
        
        for i, (tensor1, (start1, end1)) in enumerate(sorted_tensors):
            for tensor2, (start2, end2) in sorted_tensors[i+1:]:
                # If tensor2 starts after tensor1 ends, can reuse
                if start2 > end1:
                    self.reuse_map[tensor2] = tensor1
                    break
    
    def _apply_inplace_ops(self, graph: fx.Graph):
        """Convert operations to in-place where possible."""
        inplace_map = {
            torch.relu: torch.relu_,
            torch.nn.functional.relu: torch.nn.functional.relu_,
        }
        
        for node in graph.nodes:
            if node.op == 'call_function' and node.target in inplace_map:
                # Check if safe to do in-place
                if self._is_safe_inplace(node):
                    node.target = inplace_map[node.target]
                    node.meta['inplace'] = True
    
    def _is_safe_inplace(self, node: fx.Node) -> bool:
        """Check if in-place operation is safe."""
        # Simplified check - in reality would need more analysis
        return len(node.users) == 1


class GraphOptimizer:
    """Main graph optimization interface."""
    
    def __init__(self, device_type: str = 'auto', optimization_level: str = 'auto'):
        self.device_type = device_type
        self.default_optimization_level = optimization_level
        self.pattern_matcher = PatternMatcher()
        self.graph_rewriter = GraphRewriter(device_type)
        self.memory_optimizer = MemoryOptimizer()
    
    def optimize(
        self,
        model: nn.Module,
        optimization_level: Optional[str] = None,
        sample_input: Optional[Any] = None,
    ) -> Tuple[nn.Module, OptimizationStats]:
        """Optimize a model's computation graph.
        
        Args:
            model: PyTorch model to optimize
            optimization_level: 'conservative', 'auto', 'aggressive'
            sample_input: Sample input for tracing (if needed)
            
        Returns:
            Tuple of (optimized_model, optimization_stats)
        """
        level = optimization_level or self.default_optimization_level

        if not isinstance(model, nn.Module):
            raise TypeError("Expected torch.nn.Module for model optimization")

        graph: Optional[fx.Graph] = None

        try:
            # Determine example inputs for tracing metadata
            if sample_input is None:
                sample_input = self._create_sample_input(model)

            example_args, example_kwargs = self._normalize_example_inputs(sample_input)

            # Trace the model to get computation graph
            traced = fx.symbolic_trace(model)
            graph = traced.graph

            if example_args or example_kwargs:
                # Propagate shapes & devices for downstream passes
                self._propagate_example_metadata(traced, example_args, example_kwargs)

            # Find optimization patterns
            patterns = self.pattern_matcher.find_patterns(graph)
            logger.info(f"Found optimization patterns: {list(patterns.keys())}")

            # Apply rewrites based on optimization level
            if level in ['auto', 'aggressive']:
                graph = self.graph_rewriter.rewrite_graph(
                    model,
                    graph,
                    patterns,
                    example_inputs=example_args,
                    example_kwargs=example_kwargs,
                )

            # Memory optimizations
            if level == 'aggressive':
                graph = self.memory_optimizer.optimize_memory(graph)
            
            # Recompile the graph
            traced.recompile()
            
            # Apply device-specific optimizations
            optimized_model = self._apply_device_optimizations(traced, level)

            return optimized_model, self.graph_rewriter.stats
            
        except Exception as e:
            logger.warning(f"Graph optimization failed: {e}. Returning original model.")
            partial_stats = OptimizationStats(
                original_ops=len(list(graph.nodes)) if graph is not None else 0,
                optimized_ops=len(list(graph.nodes)) if graph is not None else 0,
                fusions_applied=getattr(self.graph_rewriter.stats, 'fusions_applied', 0),
                memory_saved_bytes=getattr(self.graph_rewriter.stats, 'memory_saved_bytes', 0),
                estimated_speedup=getattr(self.graph_rewriter.stats, 'estimated_speedup', 1.0),
                failure_reason=str(e),
                details={'phase': 'graph_optimization'},
            )
            return model, partial_stats
    
    def _create_sample_input(self, model: nn.Module) -> torch.Tensor:
        """Try to create a sample input for the model."""
        first_leaf = self._find_first_leaf_module(model)

        if isinstance(first_leaf, nn.Conv2d):
            spatial = first_leaf.kernel_size
            if isinstance(spatial, tuple):
                spatial = max(spatial)
            spatial = max(int(spatial) * 16, 32)
            return torch.randn(1, first_leaf.in_channels, spatial, spatial)

        if isinstance(first_leaf, nn.Conv1d):
            kernel = first_leaf.kernel_size
            if isinstance(kernel, tuple):
                kernel = kernel[0]
            length = max(int(kernel) * 16, 32)
            return torch.randn(1, first_leaf.in_channels, length)

        if isinstance(first_leaf, nn.Linear):
            return torch.randn(1, first_leaf.in_features)

        if isinstance(first_leaf, nn.Embedding):
            return torch.randint(0, first_leaf.num_embeddings, (1, 16))

        # Default vision-style shape
        return torch.randn(1, 3, 224, 224)

    def _find_first_leaf_module(self, module: nn.Module) -> nn.Module:
        for child in module.children():
            leaf = self._find_first_leaf_module(child)
            if leaf is not None:
                return leaf
        return module

    def _normalize_example_inputs(self, sample_input: Optional[Any]) -> Tuple[Tuple[Any, ...], Dict[str, Any]]:
        if sample_input is None:
            return (), {}
        if isinstance(sample_input, dict):
            return (), dict(sample_input)
        if isinstance(sample_input, (list, tuple)):
            return tuple(sample_input), {}
        return (sample_input,), {}

    def _propagate_example_metadata(
        self,
        traced_module: fx.GraphModule,
        example_args: Tuple[Any, ...],
        example_kwargs: Dict[str, Any],
    ) -> None:
        try:
            ShapeProp(traced_module).propagate(*example_args, **example_kwargs)
        except Exception as meta_err:
            logger.debug("Shape propagation failed during optimization: %s", meta_err)
    
    def _apply_device_optimizations(self, model: nn.Module, level: str) -> nn.Module:
        """Apply device-specific optimizations."""
        if self.device_type == 'mps' and level in ['auto', 'aggressive']:
            # MPS-specific optimizations
            model = self._optimize_for_mps(model)
        elif self.device_type == 'cuda' and level in ['auto', 'aggressive']:
            # CUDA-specific optimizations
            model = self._optimize_for_cuda(model)
        
        return model
    
    def _optimize_for_mps(self, model: nn.Module) -> nn.Module:
        """Apply MPS-specific optimizations."""
        return apply_device_optimizations(model, 'mps')
    
    def _optimize_for_cuda(self, model: nn.Module) -> nn.Module:
        """Apply CUDA-specific optimizations."""
        return apply_device_optimizations(model, 'cuda')


# Convenience function
def optimize_graph(model: nn.Module, 
                  device_type: str = 'auto',
                  optimization_level: str = 'auto',
                  sample_input: Optional[Any] = None) -> Tuple[nn.Module, OptimizationStats]:
    """Optimize a model's computation graph.
    
    Args:
        model: Model to optimize
        device_type: Target device type ('cuda', 'mps', 'cpu', 'auto')
        optimization_level: 'conservative', 'auto', 'aggressive'
        sample_input: Sample input for tracing
        
    Returns:
        Tuple of (optimized_model, stats)
    """
    optimizer = GraphOptimizer(device_type)
    return optimizer.optimize(model, optimization_level, sample_input)
