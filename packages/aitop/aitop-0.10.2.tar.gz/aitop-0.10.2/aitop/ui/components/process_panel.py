#!/usr/bin/env python3
"""Process information panel component."""

import curses
from typing import List, Dict, Any, Optional, Tuple

from ...core.gpu.base import GPUInfo
from ..display import Display


class ProcessPanel:
    """Renders AI process information panel."""
    
    def __init__(self, display: Display):
        """Initialize the process panel.
        
        Args:
            display: Display instance
        """
        self.display = display
        self.headers = {
            'PID': 7,
            'CPU%': 7,
            'MEM%': 7,
            'GPU%': 7,
            'VRAM%': 7,
            'STATUS': 8,
            'Process': 30
        }
    
    def _calculate_gpu_metrics(self, process: Dict[str, Any], 
                             gpus: List[GPUInfo]) -> Tuple[float, float]:
        """Calculate GPU utilization and VRAM usage for a process.
        
        Args:
            process: Process information dictionary
            gpus: List of GPUInfo objects
            
        Returns:
            Tuple of (GPU utilization percentage, VRAM usage percentage)
            
        Note:
            - For processes running on multiple GPUs, returns the highest 
              utilization and VRAM percentage across all GPUs.
            - GPU utilization is estimated based on process memory usage relative 
              to total GPU memory. For more accurate GPU utilization, vendor-specific 
              metrics would be needed.
        """
        gpu_util = 0.0
        vram_percent = 0.0
        
        if not gpus:
            return gpu_util, vram_percent
            
        # Check all available GPUs
        for gpu in gpus:
            for gpu_proc in gpu.processes:
                if gpu_proc['pid'] == process['pid']:
                    # Calculate GPU utilization
                    current_util = 0.0
                    
                    # If available, use cu_occupancy (AMD specific)
                    if 'cu_occupancy' in gpu_proc and gpu_proc['cu_occupancy'] is not None:
                        try:
                            current_util = float(gpu_proc['cu_occupancy'].rstrip('%'))
                        except (ValueError, AttributeError):
                            # Fallback: estimate based on memory usage
                            total_proc_memory = sum(p['memory'] for p in gpu.processes)
                            if total_proc_memory > 0:
                                memory_ratio = gpu_proc['memory'] / total_proc_memory
                                current_util = gpu.utilization * memory_ratio
                    else:
                        # Fallback: estimate based on memory usage
                        total_proc_memory = sum(p['memory'] for p in gpu.processes)
                        if total_proc_memory > 0:
                            memory_ratio = gpu_proc['memory'] / total_proc_memory
                            current_util = gpu.utilization * memory_ratio
                    
                    # Get VRAM usage
                    proc_memory = gpu_proc['memory']
                    
                    # Handle AMD case where memory might be in bytes instead of MB
                    if proc_memory > gpu.memory_total * 2:  # Heuristic to detect bytes
                        proc_memory = proc_memory / (1024 * 1024)  # Convert bytes to MB
                        
                    current_vram = (proc_memory / gpu.memory_total * 100) if gpu.memory_total > 0 else 0.0
                    
                    # Take the highest values across all GPUs
                    gpu_util = max(gpu_util, current_util)
                    vram_percent = max(vram_percent, current_vram)
                    
        return gpu_util, vram_percent
    
    def _render_header(self, y: int, indent: int = 2) -> int:
        """Render the process list header."""
        header = ""
        for col, width in self.headers.items():
            header += f"{col:>{width if col != 'Process' else ''}} "
            
        self.display.safe_addstr(y, indent, header,
                               curses.color_pair(1) | curses.A_BOLD)
        return y + 1
    
    def _render_process_line(self, process: Dict[str, Any],
                           gpu_util: float, vram_percent: float,
                           y: int, indent: int = 2, selected: bool = False) -> int:
        """Render a single process line.

        Args:
            process: Process information
            gpu_util: GPU utilization percentage
            vram_percent: VRAM usage percentage
            y: Y coordinate
            indent: Indentation level
            selected: Whether this process is selected

        Returns:
            Next Y coordinate
        """
        name_width = self.headers['Process']
        name_display = process['name']
        if len(name_display) > name_width:
            name_display = name_display[:name_width-3] + "..."

        line = (
            f"{process['pid']:7d} "
            f"{process['cpu_percent']:7.1f} "
            f"{process['memory_percent']:7.1f} "
            f"{gpu_util:7.1f} "
            f"{vram_percent:7.1f} "
            f"{process['status']:>8} "
            f"{name_display:<{name_width}}"
        )

        # Apply selection highlighting
        attr = curses.A_REVERSE if selected else curses.color_pair(6)
        self.display.safe_addstr(y, indent, line, attr)
        
        # Render summarized command line if available
        if y + 1 < self.display.height - 1:
            if 'cmdline_summary' in process:
                # Use the summarized version
                cmdline = f"  └─ {process['cmdline_summary']}"
                self.display.safe_addstr(y + 1, indent, cmdline, 
                                       curses.color_pair(5))
                return y + 2
            elif 'cmdline' in process:
                # Fallback to original cmdline
                cmdline = f"  └─ {process['cmdline']}"
                self.display.safe_addstr(y + 1, indent, cmdline, 
                                       curses.color_pair(5))
                return y + 2
            
        return y + 1
    
    def render(self, processes: List[Dict[str, Any]], gpus: List[GPUInfo],
               start_y: int = 3, indent: int = 2,
               sort_by: str = 'cpu_percent',
               sort_reverse: bool = True,
               scroll_position: int = 0,
               selected_index: int = 0) -> int:
        """Render the complete process panel.

        Args:
            processes: List of process information dictionaries
            gpus: List of GPUInfo objects
            start_y: Starting Y coordinate
            indent: Indentation level
            sort_by: Key to sort processes by
            sort_reverse: Sort in reverse order
            scroll_position: Current scroll position
            selected_index: Index of selected process

        Returns:
            Final Y coordinate after rendering
        """
        # Sort processes
        processes.sort(
            key=lambda x: x.get(sort_by, 0),
            reverse=sort_reverse
        )

        # Render header
        y = self._render_header(start_y, indent)

        # Calculate visible area
        max_processes = self.display.height - y - 1
        start_idx = min(scroll_position, len(processes) - max_processes)
        if start_idx < 0:
            start_idx = 0

        visible_processes = processes[start_idx:start_idx + max_processes]

        # Render processes
        for idx, process in enumerate(visible_processes):
            if y >= self.display.height - 1:
                break

            gpu_util, vram_percent = self._calculate_gpu_metrics(process, gpus)
            is_selected = (start_idx + idx) == selected_index
            y = self._render_process_line(process, gpu_util, vram_percent, y, indent, is_selected)

        return y
    
    def get_max_scroll_position(self, processes: List[Dict[str, Any]], 
                              start_y: int = 3) -> int:
        """Calculate maximum scroll position."""
        visible_height = self.display.height - start_y - 2
        return max(0, len(processes) - visible_height)
    
    def handle_scroll(self, key: int, current_scroll: int,
                     processes: List[Dict[str, Any]]) -> int:
        """Handle scroll input."""
        max_scroll = self.get_max_scroll_position(processes)

        if key == curses.KEY_UP:
            return max(0, current_scroll - 1)
        elif key == curses.KEY_DOWN:
            return min(max_scroll, current_scroll + 1)

        return current_scroll

    def get_selected_process(self, processes: List[Dict[str, Any]],
                           selected_index: int,
                           sort_by: str = 'cpu_percent',
                           sort_reverse: bool = True) -> Optional[Dict[str, Any]]:
        """Get the currently selected process.

        Args:
            processes: List of process information dictionaries
            selected_index: Index of selected process
            sort_by: Key to sort processes by
            sort_reverse: Sort in reverse order

        Returns:
            Selected process dict or None if invalid index
        """
        if not processes:
            return None

        # Sort processes same way as render()
        sorted_processes = sorted(
            processes,
            key=lambda x: x.get(sort_by, 0),
            reverse=sort_reverse
        )

        if 0 <= selected_index < len(sorted_processes):
            return sorted_processes[selected_index]

        return None
