"""Optimization modules for OmniGPU."""
from .graph_optimizer import (
    GraphOptimizer,
    optimize_graph,
    OptimizationStats,
    PatternMatcher,
    GraphRewriter,
    MemoryOptimizer
)

from .fusion_kernels import (
    FusedConvBNReLU,
    FusedLinearActivation,
    OptimizedMultiHeadAttention,
    optimize_sequential_block,
    apply_device_optimizations
)

__all__ = [
    # Graph optimization
    'GraphOptimizer',
    'optimize_graph', 
    'OptimizationStats',
    'PatternMatcher',
    'GraphRewriter',
    'MemoryOptimizer',
    
    # Fused kernels
    'FusedConvBNReLU',
    'FusedLinearActivation',
    'OptimizedMultiHeadAttention',
    'optimize_sequential_block',
    'apply_device_optimizations'
]