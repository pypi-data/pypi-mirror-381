#!/usr/bin/env python3
"""Overview panel component combining GPU, process, and memory information."""

import curses
import os
from typing import List, Dict, Any, Optional, Tuple

from ...core.gpu.base import GPUInfo
from ...core.system.memory import MemoryStats
from ...core.system.cpu import CPUStats
from ..display import Display


class OverviewPanel:
    """Renders system overview combining all information."""
    
    def __init__(self, display: Display):
        """Initialize the overview panel.
        
        Args:
            display: Display instance
        """
        self.display = display
        # Base header widths for fixed columns
        self.base_headers = {
            'PID': 7,
            'CPU%': 7,
            'MEM%': 7,
            'GPU%': 7,
            'VRAM%': 7,
            'Status': 8
        }
        self.min_name_width = 20  # Minimum width for process name
    
    def _render_gpu_overview(self, gpu: GPUInfo, vendor: str,
                           y: int, x: int, width: int) -> int:
        """Render GPU overview section.
        
        Args:
            gpu: GPU information
            vendor: GPU vendor string
            y: Starting Y coordinate
            x: Starting X coordinate
            width: Available width
            
        Returns:
            Next Y coordinate
        """
        # Title
        self.display.safe_addstr(y, x, "GPU Status",
                               curses.color_pair(1) | curses.A_BOLD)
        y += 1
        
        # GPU model with index
        vendor_prefix = ""
        if all(v.upper() not in gpu.name.upper()
               for v in ["NVIDIA", "AMD", "INTEL"]):
            vendor_prefix = f"{vendor.upper()} "
        self.display.safe_addstr(y, x, f"GPU {gpu.index}: {vendor_prefix}{gpu.name}",
                               curses.color_pair(5))
        y += 1

        # Framework versions (if available)
        version_parts = []
        if gpu.cuda_version:
            version_parts.append(f"CUDA: {gpu.cuda_version}")
        if gpu.rocm_version:
            version_parts.append(f"ROCm: {gpu.rocm_version}")
        if gpu.driver_version:
            version_parts.append(f"Driver: {gpu.driver_version}")

        if version_parts:
            version_line = "       " + "  ".join(version_parts)
            self.display.safe_addstr(y, x, version_line, curses.color_pair(6))
            y += 1

        y += 1
        
        # GPU metrics - calculate bar widths based on actual line format
        # GPU line format: "GPU    [bar] 100.0%" = 7 + 2 + bar + 1 + 6 = 16 + bar
        gpu_bar_width = max(0, min(30, width - 16))

        # Utilization
        bar, color = self.display.create_bar(gpu.utilization, gpu_bar_width)
        line = f"GPU    [{bar}] {gpu.utilization:5.1f}%"
        self.display.safe_addstr(y, x, line, color)
        y += 1

        # Memory
        mem_percent = (gpu.memory_used / gpu.memory_total * 100
                      if gpu.memory_total else 0)
        # VRAM line format: "VRAM   [bar]  12.5/ 24.0GB ( 52.1%)" = 7 + 2 + bar + 2 + 24 = 35 + bar
        vram_bar_width = max(0, min(30, width - 35))
        bar, color = self.display.create_bar(mem_percent, vram_bar_width)

        # Convert memory values from MB to GB for display
        mem_used_gb = gpu.memory_used / 1024
        mem_total_gb = gpu.memory_total / 1024
        line = f"VRAM   [{bar}] {mem_used_gb:5.1f}/{mem_total_gb:5.1f}GB ({mem_percent:5.1f}%)"
        self.display.safe_addstr(y, x, line, color)
        y += 1
        
        # Temperature
        if gpu.temperature > 0:
            line = f"Temp   {gpu.temperature:5.1f}°C"
            self.display.safe_addstr(y, x, line,
                                   self.display.get_color(gpu.temperature))
            y += 1
        
        return y + 1
    
    def _render_memory_overview(self, memory_stats: MemoryStats,
                              y: int, x: int, width: int) -> int:
        """Render memory overview section.
        
        Args:
            memory_stats: Memory statistics
            y: Starting Y coordinate
            x: Starting X coordinate
            width: Available width
            
        Returns:
            Next Y coordinate
        """
        # Title
        self.display.safe_addstr(y, x, "System Memory",
                               curses.color_pair(1) | curses.A_BOLD)
        y += 1
        
        # RAM usage
        # RAM line format: "RAM    [bar]  18.5/ 62.7GB ( 29.5%)" = 7 + 2 + bar + 2 + 24 = 35 + bar
        mem_bar_width = max(0, min(30, width - 35))
        bar, color = self.display.create_bar(memory_stats.percent, mem_bar_width)

        ram_used_gb = memory_stats.used / (1024 ** 3)
        ram_total_gb = memory_stats.total / (1024 ** 3)
        line = f"RAM    [{bar}] {ram_used_gb:5.1f}/{ram_total_gb:5.1f}GB ({memory_stats.percent:5.1f}%)"
        self.display.safe_addstr(y, x, line, color)
        y += 1

        # Swap usage if available
        if memory_stats.swap_total > 0:
            swap_used_gb = memory_stats.swap_used / (1024 ** 3)
            swap_total_gb = memory_stats.swap_total / (1024 ** 3)
            # Swap line format same as RAM: 35 + bar
            swap_bar_width = max(0, min(30, width - 35))
            bar, color = self.display.create_bar(memory_stats.swap_percent, swap_bar_width)
            line = f"Swap   [{bar}] {swap_used_gb:5.1f}/{swap_total_gb:5.1f}GB ({memory_stats.swap_percent:5.1f}%)"
            self.display.safe_addstr(y, x, line, color)
            y += 1
        
        return y
    
    def _render_process_overview(self, processes: List[Dict[str, Any]],
                               gpus: List[GPUInfo], y: int, x: int,
                               width: int, max_processes: int = 5) -> int:
        """Render process overview section.
        
        Args:
            processes: List of process information
            gpus: List of GPU information
            y: Starting Y coordinate
            x: Starting X coordinate
            width: Available width
            max_processes: Maximum number of processes to show
            
        Returns:
            Next Y coordinate
        """
        # Title
        self.display.safe_addstr(y, x, "Top Processes",
                               curses.color_pair(1) | curses.A_BOLD)
        y += 2
        
        # Calculate dynamic widths based on available space
        total_fixed_width = sum(self.base_headers.values()) + len(self.base_headers)  # Add 1 for each separator
        name_width = max(self.min_name_width, width - total_fixed_width - 2)  # -2 for margins
        
        # Create headers dict with dynamic name width
        headers = self.base_headers.copy()
        headers['Name'] = name_width
        
        # Header
        header = ""
        for col, col_width in headers.items():
            # Right-align all columns except Name which is left-aligned
            if col == 'Name':
                header += f"{col:<{col_width}}"
            else:
                header += f"{col:>{col_width}} "
        self.display.safe_addstr(y, x, header, curses.color_pair(5))
        y += 1
        
        # Sort processes by CPU usage
        processes.sort(key=lambda p: p['cpu_percent'], reverse=True)
        
        # Show top processes
        for proc in processes[:max_processes]:
            # Get GPU metrics across all GPUs
            gpu_util = 0.0
            vram_percent = 0.0
            if gpus:
                for gpu in gpus:
                    for gpu_proc in gpu.processes:
                        if gpu_proc['pid'] == proc['pid']:
                            # Calculate GPU utilization
                            current_util = 0.0
                            if 'cu_occupancy' in gpu_proc and gpu_proc['cu_occupancy'] is not None:
                                try:
                                    current_util = float(gpu_proc['cu_occupancy'].rstrip('%'))
                                except (ValueError, AttributeError):
                                    current_util = gpu.utilization
                            else:
                                current_util = gpu.utilization
                            
                            # Use highest utilization across GPUs
                            gpu_util = max(gpu_util, current_util)
                            
                            # Calculate VRAM percentage
                            proc_memory = gpu_proc['memory']
                            
                            # All memory values in GPUInfo should be in MB already, but some GPU backends
                            # might provide process memory in different units
                            # AMD case: Memory might be in bytes
                            if proc_memory > gpu.memory_total * 2:  # Heuristic to detect bytes
                                proc_memory = proc_memory / (1024 * 1024)  # Convert bytes to MB
                                
                            # Calculate percentage based on MB values
                            current_vram = (proc_memory / gpu.memory_total * 100) if gpu.memory_total > 0 else 0.0
                            
                            # Use highest VRAM percentage across GPUs
                            vram_percent = max(vram_percent, current_vram)
            
            # Format process line using dynamic width
            name_width = headers['Name']  # Use dynamic width from headers
            # Use the summarized command line if available, otherwise use process name
            if 'cmdline_summary' in proc:
                name_display = proc['cmdline_summary']
            elif 'cmdline' in proc:
                name_display = proc['cmdline']
            else:
                name_display = proc['name']
            if len(name_display) > name_width:
                name_display = name_display[:name_width-3] + "..."
            
            # Determine process status
            status = "running" if proc['cpu_percent'] > 0.1 else "sleeping"
            status_color = curses.color_pair(2) if status == "running" else curses.color_pair(6)
            
            # Format base metrics
            base_metrics = (
                f"{proc['pid']:7d} "
                f"{proc['cpu_percent']:7.1f} "
                f"{proc['memory_percent']:7.1f} "
                f"{gpu_util:7.1f} "
                f"{vram_percent:7.1f} "
            )
            
            # Format status and name
            status_field = f"{status:8} "  # Added space after status
            name_field = f"{name_display:<{name_width}}"
            
            # Combine all parts
            line = base_metrics + status_field + name_field
            
            # Write with different colors for status
            self.display.safe_addstr(y, x, base_metrics, curses.color_pair(6))
            self.display.safe_addstr(y, x + len(base_metrics), status_field, status_color)
            self.display.safe_addstr(y, x + len(base_metrics) + len(status_field), name_field, curses.color_pair(6))
            
            y += 1
        
        return y
    
    def _render_cpu_overview(self, cpu_stats: CPUStats,
                           y: int, x: int, width: int) -> int:
        """Render CPU overview section.
        
        Args:
            cpu_stats: CPU statistics
            y: Starting Y coordinate
            x: Starting X coordinate
            width: Available width
            
        Returns:
            Next Y coordinate
        """
        # Title
        self.display.safe_addstr(y, x, "CPU Status",
                               curses.color_pair(1) | curses.A_BOLD)
        y += 1
        
        # CPU model
        self.display.safe_addstr(y, x, f"Model: {cpu_stats.model}",
                               curses.color_pair(5))
        y += 2
        
        # CPU utilization
        # CPU line format: "CPU    [bar]  28.0%" = 7 + 2 + bar + 2 + 5 = 16 + bar
        cpu_bar_width = max(0, min(30, width - 16))
        bar, color = self.display.create_bar(cpu_stats.total_percent, cpu_bar_width)
        line = f"CPU    [{bar}] {cpu_stats.total_percent:5.1f}%"
        self.display.safe_addstr(y, x, line, color)
        y += 1
        
        # CPU temperature if available
        if cpu_stats.temperature > 0:
            line = f"Temp   {cpu_stats.temperature:5.1f}°C"
            self.display.safe_addstr(y, x, line,
                                   self.display.get_color(cpu_stats.temperature))
            y += 1
        
        # Load averages
        line = f"Load   {cpu_stats.load_1min:5.2f} {cpu_stats.load_5min:5.2f} {cpu_stats.load_15min:5.2f}"
        self.display.safe_addstr(y, x, line, curses.color_pair(6))
        y += 1
        
        return y + 1

    def render(self, gpu_info: List[tuple[GPUInfo, str]], processes: List[Dict[str, Any]],
               memory_stats: MemoryStats, cpu_stats: CPUStats, primary_vendor: str,
               start_y: int = 3) -> None:
        """Render the complete overview panel.

        Args:
            gpu_info: List of tuples containing (GPU information, vendor string)
            processes: List of process information
            memory_stats: Memory statistics
            primary_vendor: Primary GPU vendor string
            start_y: Starting Y coordinate (ignored, uses layout system)
        """
        # Get layout from centralized layout calculator
        layout = self.display.layout.calculate()
        left_rect = layout['overview_left']
        right_rect = layout['overview_right']
        separator_x = layout['overview_separator_x']

        # Check if we're using split layout (separator_x >= 0)
        if separator_x >= 0:
            # Draw vertical separator from content start to footer
            content_rect = layout['content']
            for row in range(content_rect.y, content_rect.bottom):
                self.display.safe_addstr(row, separator_x, "│", curses.color_pair(1))

            # Left panel (System Information)
            # Apply left margin to content
            left_inner = left_rect.inner(left=self.display.layout.CONTENT_MARGIN_LEFT)
            y = left_inner.y
            y = self._render_cpu_overview(cpu_stats, y, left_inner.x, left_inner.width)
            y += 1

            # Render all detected GPUs
            for gpu, vendor in gpu_info:
                y = self._render_gpu_overview(gpu, vendor, y, left_inner.x, left_inner.width)
                y += 1

            y = self._render_memory_overview(memory_stats, y, left_inner.x, left_inner.width)

            # Right panel (Process Information)
            # Right panel already includes proper spacing from separator
            self._render_process_overview(processes, [gpu for gpu, _ in gpu_info],
                                       right_rect.y, right_rect.x, right_rect.width)
            return

        # Stacked layout for narrow windows (use full content width)
        content = self.display.layout.get_content_area()
        y = content.y

        # Render system information
        y = self._render_cpu_overview(cpu_stats, y, content.x, content.width)
        y += 1

        # Render all detected GPUs
        for gpu, vendor in gpu_info:
            y = self._render_gpu_overview(gpu, vendor, y, content.x, content.width)
            y += 1

        y = self._render_memory_overview(memory_stats, y, content.x, content.width)
        y += 1

        # Render process information
        self._render_process_overview(processes, [gpu for gpu, _ in gpu_info],
                                    y, content.x, content.width)
