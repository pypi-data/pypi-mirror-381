"""Visualization tools for profiling data."""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle
import numpy as np
from typing import List, Optional, Tuple, Dict, Any
import json

from .profiler import ProfileData, ProfileEvent


def _coerce_profile_data(profile_data: Any) -> ProfileData:
    """Normalize profiling payloads into ProfileData objects."""
    if isinstance(profile_data, ProfileData):
        return profile_data

    if hasattr(profile_data, 'to_profile_data'):
        return profile_data.to_profile_data()

    if isinstance(profile_data, dict):
        data = ProfileData()
        total_ms = profile_data.get('total_time_ms', 0.0)
        data.start_time = 0.0
        data.end_time = total_ms / 1000.0

        device_info = profile_data.get('device') or {}
        if isinstance(device_info, dict):
            data.device_info = device_info

        for op in profile_data.get('operations', []):
            start_ms = op.get('start_ms', 0.0)
            duration_ms = op.get('duration_ms', op.get('end_ms', start_ms))
            if op.get('end_ms') is not None:
                duration_ms = op['end_ms'] - start_ms
            event = ProfileEvent(
                name=op.get('name', 'operation'),
                start_time=start_ms / 1000.0,
                end_time=(start_ms + duration_ms) / 1000.0,
                duration=duration_ms / 1000.0,
                device=str(op.get('device', 'unknown')),
                metadata=op.get('metadata', {}),
            )
            data.add_event(event)

        return data

    raise TypeError(f"Unsupported profile data type: {type(profile_data)}")


class ProfileVisualizer:
    """Visualizer for profiling data."""
    
    def __init__(self, profile_data: ProfileData):
        self.data = _coerce_profile_data(profile_data)
        self.colors = plt.cm.tab10(np.linspace(0, 1, 10))
        
    def timeline(self, figsize: Tuple[int, int] = (12, 6), 
                save_path: Optional[str] = None):
        """Create timeline visualization of operations.
        
        Args:
            figsize: Figure size (width, height)
            save_path: Optional path to save the figure
        """
        if not self.data.events:
            print("No events to visualize")
            return
            
        fig, ax = plt.subplots(figsize=figsize)
        
        # Sort events by start time
        events = sorted(self.data.events, key=lambda e: e.start_time)
        
        # Create operation name to color mapping
        op_names = list(set(e.name for e in events))
        op_colors = {name: self.colors[i % len(self.colors)] 
                    for i, name in enumerate(op_names)}
        
        # Find time range
        start_time = min(e.start_time for e in events)
        end_time = max(e.end_time for e in events)
        total_duration = end_time - start_time
        
        # Create timeline bars
        y_pos = 0
        y_labels = []
        
        for event in events:
            x_start = (event.start_time - start_time) / total_duration
            width = event.duration / total_duration
            
            # Create rectangle
            rect = Rectangle((x_start, y_pos), width, 0.8, 
                           facecolor=op_colors[event.name],
                           edgecolor='black', linewidth=0.5)
            ax.add_patch(rect)
            
            # Add text label if bar is wide enough
            if width > 0.05:  # Only show text for bars wider than 5%
                ax.text(x_start + width/2, y_pos + 0.4, 
                       f"{event.name}\n{event.duration_ms:.1f}ms",
                       ha='center', va='center', fontsize=8)
            
            y_labels.append(f"Op {len(y_labels)+1}")
            y_pos += 1
        
        # Configure axes
        ax.set_xlim(0, 1)
        ax.set_ylim(-0.5, len(events) - 0.5)
        ax.set_xlabel('Time (normalized)')
        ax.set_ylabel('Operations')
        ax.set_title(f'OmniGPU Operation Timeline\nTotal: {total_duration*1000:.1f}ms on {self.data.device_info.get("type", "unknown")} device')
        
        # Add legend
        legend_elements = [patches.Patch(facecolor=color, label=name)
                         for name, color in op_colors.items()]
        ax.legend(handles=legend_elements, loc='center left', 
                 bbox_to_anchor=(1, 0.5))
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
        
        plt.show()
        
    def operation_breakdown(self, figsize: Tuple[int, int] = (10, 6),
                          save_path: Optional[str] = None):
        """Create pie chart of operation time breakdown.
        
        Args:
            figsize: Figure size (width, height) 
            save_path: Optional path to save the figure
        """
        if not self.data.events:
            print("No events to visualize")
            return
            
        summary = self.data.get_summary()
        op_stats = summary['operation_stats']
        
        # Prepare data for pie chart
        labels = []
        sizes = []
        
        for op, stats in op_stats.items():
            labels.append(f"{op}\n({stats['count']} calls)")
            sizes.append(stats['total_ms'])
            
        fig, ax = plt.subplots(figsize=figsize)
        
        # Create pie chart
        wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%',
                                          startangle=90, colors=self.colors)
        
        # Enhance text
        for text in texts:
            text.set_fontsize(10)
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
            autotext.set_fontsize(9)
            
        ax.set_title(f'Operation Time Breakdown\nTotal: {summary["total_time_ms"]:.1f}ms')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
            
        plt.show()
        
    def performance_bars(self, figsize: Tuple[int, int] = (10, 6),
                        save_path: Optional[str] = None):
        """Create bar chart of operation performance.
        
        Args:
            figsize: Figure size (width, height)
            save_path: Optional path to save the figure
        """
        if not self.data.events:
            print("No events to visualize")
            return
            
        summary = self.data.get_summary()
        op_stats = summary['operation_stats']
        
        # Sort by total time
        sorted_ops = sorted(op_stats.items(), 
                          key=lambda x: x[1]['total_ms'], 
                          reverse=True)
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)
        
        # Bar chart 1: Total time per operation
        ops = [op for op, _ in sorted_ops]
        total_times = [stats['total_ms'] for _, stats in sorted_ops]
        
        y_pos = np.arange(len(ops))
        ax1.barh(y_pos, total_times, color=self.colors[0])
        ax1.set_yticks(y_pos)
        ax1.set_yticklabels(ops)
        ax1.set_xlabel('Total Time (ms)')
        ax1.set_title('Total Time per Operation Type')
        ax1.grid(axis='x', alpha=0.3)
        
        # Bar chart 2: Average time per operation
        avg_times = [stats['avg_ms'] for _, stats in sorted_ops]
        counts = [stats['count'] for _, stats in sorted_ops]
        
        ax2.barh(y_pos, avg_times, color=self.colors[1])
        ax2.set_yticks(y_pos)
        ax2.set_yticklabels([f"{op} ({counts[i]}x)" 
                            for i, op in enumerate(ops)])
        ax2.set_xlabel('Average Time (ms)')
        ax2.set_title('Average Time per Operation Call')
        ax2.grid(axis='x', alpha=0.3)
        
        plt.suptitle(f'Performance Analysis on {self.data.device_info.get("type", "unknown")} device')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
            
        plt.show()
        
    def save_html_report(self, filepath: str):
        """Save an interactive HTML report.
        
        Args:
            filepath: Path to save the HTML report
        """
        html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>OmniGPU Profile Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }}
        .header {{
            background-color: #2c3e50;
            color: white;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 20px;
        }}
        .summary {{
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }}
        .operation {{
            background-color: white;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        .metric {{
            display: inline-block;
            margin: 10px 20px 10px 0;
        }}
        .metric-value {{
            font-size: 24px;
            font-weight: bold;
            color: #3498db;
        }}
        .metric-label {{
            color: #7f8c8d;
            font-size: 14px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        th, td {{
            padding: 10px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        th {{
            background-color: #34495e;
            color: white;
        }}
        tr:hover {{
            background-color: #f5f5f5;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>OmniGPU Profile Report</h1>
        <p>Device: {device_type} | Total Duration: {total_duration:.2f}ms</p>
    </div>
    
    <div class="summary">
        <h2>Summary</h2>
        <div class="metric">
            <div class="metric-value">{num_operations}</div>
            <div class="metric-label">Total Operations</div>
        </div>
        <div class="metric">
            <div class="metric-value">{total_time:.2f}ms</div>
            <div class="metric-label">Total Time</div>
        </div>
        <div class="metric">
            <div class="metric-value">{num_unique_ops}</div>
            <div class="metric-label">Unique Operations</div>
        </div>
    </div>
    
    <div class="summary">
        <h2>Operation Statistics</h2>
        <table>
            <tr>
                <th>Operation</th>
                <th>Count</th>
                <th>Total (ms)</th>
                <th>Average (ms)</th>
                <th>Min (ms)</th>
                <th>Max (ms)</th>
            </tr>
            {operation_rows}
        </table>
    </div>
    
    <div class="summary">
        <h2>Timeline Events</h2>
        <table>
            <tr>
                <th>Time</th>
                <th>Operation</th>
                <th>Duration (ms)</th>
                <th>Device</th>
            </tr>
            {event_rows}
        </table>
    </div>
</body>
</html>
"""
        
        summary = self.data.get_summary()
        
        # Generate operation statistics rows
        operation_rows = []
        for op, stats in sorted(summary['operation_stats'].items()):
            row = f"""
            <tr>
                <td>{op}</td>
                <td>{stats['count']}</td>
                <td>{stats['total_ms']:.2f}</td>
                <td>{stats['avg_ms']:.2f}</td>
                <td>{stats['min_ms']:.2f}</td>
                <td>{stats['max_ms']:.2f}</td>
            </tr>
            """
            operation_rows.append(row)
            
        # Generate event timeline rows
        event_rows = []
        start_time = self.data.start_time if self.data.events else 0
        
        for event in sorted(self.data.events, key=lambda e: e.start_time):
            relative_time = (event.start_time - start_time) * 1000
            row = f"""
            <tr>
                <td>{relative_time:.2f}ms</td>
                <td>{event.name}</td>
                <td>{event.duration_ms:.2f}</td>
                <td>{event.device}</td>
            </tr>
            """
            event_rows.append(row)
            
        # Fill template
        html_content = html_template.format(
            device_type=self.data.device_info.get('type', 'Unknown'),
            total_duration=(self.data.end_time - self.data.start_time) * 1000,
            num_operations=len(self.data.events),
            total_time=summary.get('total_time_ms', 0),
            num_unique_ops=len(summary.get('operation_stats', {})),
            operation_rows=''.join(operation_rows),
            event_rows=''.join(event_rows[:100])  # Limit to first 100 events
        )
        
        with open(filepath, 'w') as f:
            f.write(html_content)
            
        print(f"HTML report saved to: {filepath}")


def visualize_profile(profile_data: Any, 
                     show_timeline: bool = True,
                     show_breakdown: bool = True,
                     show_bars: bool = True,
                     save_prefix: Optional[str] = None):
    """Convenience function to create all visualizations.
    
    Args:
        profile_data: Profiling data to visualize
        show_timeline: Whether to show timeline visualization
        show_breakdown: Whether to show operation breakdown
        show_bars: Whether to show performance bars
        save_prefix: Optional prefix for saving figures
    """
    visualizer = ProfileVisualizer(profile_data)
    
    if show_timeline:
        save_path = f"{save_prefix}_timeline.png" if save_prefix else None
        visualizer.timeline(save_path=save_path)
        
    if show_breakdown:
        save_path = f"{save_prefix}_breakdown.png" if save_prefix else None
        visualizer.operation_breakdown(save_path=save_path)
        
    if show_bars:
        save_path = f"{save_prefix}_bars.png" if save_prefix else None
        visualizer.performance_bars(save_path=save_path)
        
    # Always save HTML report if prefix provided
    if save_prefix:
        visualizer.save_html_report(f"{save_prefix}_report.html")
