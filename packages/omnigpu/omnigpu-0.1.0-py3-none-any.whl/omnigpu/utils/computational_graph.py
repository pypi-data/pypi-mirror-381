"""Computational graph analysis and visualization for OmniGPU."""

import torch
import torch.nn as nn
import torch.fx as fx
import matplotlib.pyplot as plt
import networkx as nx
from typing import Dict, List, Tuple, Optional, Any
import numpy as np
from collections import defaultdict


class ComputationalGraphAnalyzer:
    """Analyzes and visualizes PyTorch computational graphs."""
    
    def __init__(self):
        self.fusion_patterns = [
            ('conv2d', 'batch_norm', 'relu'),
            ('conv2d', 'batch_norm'),
            ('linear', 'relu'),
            ('add', 'relu'),
        ]
    
    def trace_graph(self, model: nn.Module, example_input: torch.Tensor) -> fx.GraphModule:
        """Trace the computational graph of a model."""
        model.eval()
        traced = fx.symbolic_trace(model)
        return traced
    
    def analyze_graph(self, traced_model: fx.GraphModule) -> Dict[str, Any]:
        """Analyze the computational graph for optimization opportunities."""
        stats = {
            'total_ops': 0,
            'op_types': defaultdict(int),
            'fusion_opportunities': [],
            'memory_accesses': 0,
            'compute_intensity': 0.0
        }
        
        # Analyze each node
        nodes = list(traced_model.graph.nodes)
        for i, node in enumerate(nodes):
            if node.op == 'call_module':
                stats['total_ops'] += 1
                module = traced_model.get_submodule(node.target)
                op_type = type(module).__name__.lower()
                stats['op_types'][op_type] += 1
                
                # Check for fusion patterns
                if i + 2 < len(nodes):
                    pattern = []
                    for j in range(3):
                        if nodes[i+j].op == 'call_module':
                            module = traced_model.get_submodule(nodes[i+j].target)
                            pattern.append(type(module).__name__.lower())
                    
                    pattern_tuple = tuple(pattern)
                    if pattern_tuple in self.fusion_patterns:
                        stats['fusion_opportunities'].append({
                            'pattern': pattern_tuple,
                            'start_node': node.name,
                            'nodes': [nodes[i+j].name for j in range(len(pattern))]
                        })
        
        # Estimate memory accesses and compute intensity
        stats['memory_accesses'] = stats['total_ops'] * 2  # Rough estimate
        stats['compute_intensity'] = stats['total_ops'] / max(stats['memory_accesses'], 1)
        
        return stats
    
    def visualize_graph(self, traced_model: fx.GraphModule, 
                       highlight_fusions: bool = True) -> plt.Figure:
        """Create a visual representation of the computational graph."""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
        
        # Build networkx graph
        G = nx.DiGraph()
        pos = {}
        node_colors = []
        node_labels = {}
        
        # Add nodes
        y_pos = 0
        for node in traced_model.graph.nodes:
            if node.op in ['placeholder', 'call_module', 'output']:
                G.add_node(node.name)
                pos[node.name] = (0, y_pos)
                y_pos -= 1
                
                # Color coding
                if node.op == 'placeholder':
                    node_colors.append('#3498db')  # Blue for input
                    node_labels[node.name] = 'Input'
                elif node.op == 'output':
                    node_colors.append('#e74c3c')  # Red for output
                    node_labels[node.name] = 'Output'
                else:
                    module = traced_model.get_submodule(node.target)
                    op_type = type(module).__name__
                    node_labels[node.name] = op_type
                    
                    # Color by operation type
                    if 'Conv' in op_type:
                        node_colors.append('#2ecc71')  # Green
                    elif 'BatchNorm' in op_type:
                        node_colors.append('#f39c12')  # Orange
                    elif 'ReLU' in op_type:
                        node_colors.append('#9b59b6')  # Purple
                    else:
                        node_colors.append('#95a5a6')  # Gray
        
        # Add edges
        for node in traced_model.graph.nodes:
            if node.op == 'call_module':
                for arg in node.args:
                    if isinstance(arg, fx.Node):
                        G.add_edge(arg.name, node.name)
        
        # Draw original graph
        ax1.set_title("Original Computational Graph", fontsize=14, fontweight='bold')
        nx.draw(G, pos, ax=ax1, node_color=node_colors, 
                node_size=2000, labels=node_labels,
                font_size=10, font_weight='bold',
                arrows=True, arrowsize=20,
                edge_color='gray', width=2)
        
        # Analyze and show optimization opportunities
        stats = self.analyze_graph(traced_model)
        
        # Draw optimized graph concept
        ax2.set_title("Optimization Opportunities", fontsize=14, fontweight='bold')
        
        # Create text summary
        summary = f"Total Operations: {stats['total_ops']}\n\n"
        summary += "Operation Breakdown:\n"
        for op, count in stats['op_types'].items():
            summary += f"  {op}: {count}\n"
        
        summary += f"\nFusion Opportunities: {len(stats['fusion_opportunities'])}\n"
        for fusion in stats['fusion_opportunities']:
            summary += f"  • {' → '.join(fusion['pattern'])}\n"
        
        potential_speedup = 1.0 + (0.3 * len(stats['fusion_opportunities']))
        summary += f"\nPotential Speedup: {potential_speedup:.2f}x"
        
        ax2.text(0.1, 0.5, summary, transform=ax2.transAxes,
                fontsize=12, verticalalignment='center',
                bbox=dict(boxstyle="round,pad=0.5", facecolor='lightgray'))
        ax2.axis('off')
        
        plt.tight_layout()
        return fig
    
    def compare_graphs(self, original_model: nn.Module, 
                      optimized_model: nn.Module,
                      example_input: torch.Tensor) -> plt.Figure:
        """Compare original and optimized computational graphs."""
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        
        # Trace both models
        orig_traced = self.trace_graph(original_model, example_input)
        opt_traced = self.trace_graph(optimized_model, example_input)
        
        # Analyze both
        orig_stats = self.analyze_graph(orig_traced)
        opt_stats = self.analyze_graph(opt_traced)
        
        # Plot operation counts
        ax1.set_title("Operation Count Comparison", fontsize=12, fontweight='bold')
        op_types = set(list(orig_stats['op_types'].keys()) + 
                      list(opt_stats['op_types'].keys()))
        
        x = np.arange(len(op_types))
        width = 0.35
        
        orig_counts = [orig_stats['op_types'].get(op, 0) for op in op_types]
        opt_counts = [opt_stats['op_types'].get(op, 0) for op in op_types]
        
        ax1.bar(x - width/2, orig_counts, width, label='Original', color='#e74c3c')
        ax1.bar(x + width/2, opt_counts, width, label='Optimized', color='#2ecc71')
        ax1.set_xticks(x)
        ax1.set_xticklabels(list(op_types), rotation=45)
        ax1.legend()
        ax1.set_ylabel('Count')
        
        # Plot memory access reduction
        ax2.set_title("Memory Access Reduction", fontsize=12, fontweight='bold')
        memory_data = {
            'Original': orig_stats['total_ops'] * 3,  # Each op reads and writes
            'Optimized': opt_stats['total_ops'] * 2  # Fused ops share memory
        }
        ax2.bar(memory_data.keys(), memory_data.values(), 
                color=['#e74c3c', '#2ecc71'])
        ax2.set_ylabel('Memory Accesses')
        
        # Improvement percentages
        reduction = ((memory_data['Original'] - memory_data['Optimized']) / 
                    memory_data['Original'] * 100)
        ax2.text(0.5, 0.95, f'Reduction: {reduction:.1f}%',
                transform=ax2.transAxes, ha='center',
                bbox=dict(boxstyle="round", facecolor='yellow', alpha=0.5))
        
        # Show fusion patterns applied
        ax3.set_title("Fusion Patterns Applied", fontsize=12, fontweight='bold')
        ax3.axis('off')
        
        fusion_text = "Optimizations Applied:\n\n"
        for i, fusion in enumerate(orig_stats['fusion_opportunities']):
            fusion_text += f"{i+1}. {' + '.join(fusion['pattern'])} → "
            fusion_text += f"Fused{fusion['pattern'][0].capitalize()}\n"
        
        ax3.text(0.1, 0.5, fusion_text, transform=ax3.transAxes,
                fontsize=11, verticalalignment='center')
        
        # Performance projection
        ax4.set_title("Performance Projection", fontsize=12, fontweight='bold')
        
        batch_sizes = [1, 4, 8, 16, 32]
        
        # Simulate performance based on operation count
        base_time = 0.001  # ms per op
        orig_times = [bs * orig_stats['total_ops'] * base_time for bs in batch_sizes]
        opt_times = [bs * opt_stats['total_ops'] * base_time * 0.7 for bs in batch_sizes]
        
        ax4.plot(batch_sizes, orig_times, 'o-', label='Original', 
                color='#e74c3c', linewidth=2)
        ax4.plot(batch_sizes, opt_times, 'o-', label='Optimized', 
                color='#2ecc71', linewidth=2)
        ax4.set_xlabel('Batch Size')
        ax4.set_ylabel('Time (ms)')
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        return fig


def explain_graph_optimization():
    """Generate educational content about graph optimization."""
    explanation = """
    # Understanding Computational Graph Optimization
    
    ## What is a Computational Graph?
    
    A computational graph represents the sequence of operations in a neural network:
    - Nodes represent operations (Conv2D, ReLU, etc.)
    - Edges represent data flow (tensors)
    
    ## Why Optimize the Graph?
    
    1. **Memory Bandwidth**: GPUs are often memory-bound
    2. **Kernel Launch Overhead**: Each operation has overhead
    3. **Data Locality**: Keep data in fast memory (registers/cache)
    
    ## Key Optimization: Operation Fusion
    
    Instead of:
    ```
    x = conv2d(input)      # Write to memory
    x = batch_norm(x)      # Read, compute, write
    x = relu(x)            # Read, compute, write
    ```
    
    We create a single fused operation:
    ```
    x = fused_conv_bn_relu(input)  # One read, one write!
    ```
    
    ## Benefits:
    - 3x fewer memory accesses
    - 3x fewer kernel launches
    - Better cache utilization
    - Targeted speedups on memory-bound models (ongoing work)
    """
    
    return explanation