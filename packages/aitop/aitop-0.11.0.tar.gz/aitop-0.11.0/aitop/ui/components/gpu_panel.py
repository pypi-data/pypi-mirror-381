#!/usr/bin/env python3
"""GPU information panel component."""

import curses
from typing import Dict, List, Optional, Tuple

from ...core.gpu.base import GPUInfo
from ..display import Display


class GPUPanel:
    """Renders GPU information panel."""

    def __init__(self, display: Display):
        """Initialize the GPU panel.

        Args:
            display: Display instance
        """
        self.display = display

    def _render_gpu_header(self, gpu: GPUInfo, y: int, x: int, vendor: str) -> int:
        """Render GPU header with name and vendor.

        Args:
            gpu: GPU information
            y: Starting Y coordinate
            x: Starting X coordinate
            vendor: GPU vendor string

        Returns:
            Next Y coordinate
        """
        vendor_prefix = ""
        if all(v.upper() not in gpu.name.upper() for v in ["NVIDIA", "AMD", "INTEL"]):
            vendor_prefix = f"{vendor.upper()} "

        header = f"GPU {gpu.index}: {vendor_prefix}{gpu.name}"
        self.display.safe_addstr(y, x, header, curses.color_pair(1) | curses.A_BOLD)
        return y + 2

    def _render_utilization_bar(self, gpu: GPUInfo, y: int, x: int, width: int) -> int:
        """Render GPU utilization bar.

        Args:
            gpu: GPU information
            y: Starting Y coordinate
            x: Starting X coordinate
            width: Maximum width for the bar

        Returns:
            Next Y coordinate
        """
        bar, color = self.display.create_bar(gpu.utilization, width)
        line = f"Util  [{bar}] {gpu.utilization:5.1f}%"
        self.display.safe_addstr(y, x, line, color)
        return y + 1

    def _render_memory_bar(self, gpu: GPUInfo, y: int, x: int, width: int) -> int:
        """Render memory usage bar.

        Args:
            gpu: GPU information (with memory_used and memory_total in MB)
            y: Starting Y coordinate
            x: Starting X coordinate
            width: Maximum width for the bar

        Returns:
            Next Y coordinate

        Note:
            The GPU memory values in the GPUInfo object are in MB (megabytes).
            These values are converted to GB (gigabytes) for display.
        """
        mem_percent = (
            gpu.memory_used / gpu.memory_total * 100 if gpu.memory_total else 0
        )
        bar, color = self.display.create_bar(mem_percent, width)

        # Convert memory values from MB to GB for display
        mem_used_gb = gpu.memory_used / 1024
        mem_total_gb = gpu.memory_total / 1024
        line = f"Mem   [{bar}] {mem_used_gb:5.1f}GB / " f"{mem_total_gb:5.1f}GB"
        self.display.safe_addstr(y, x, line, color)
        return y + 1

    def _render_temperature(self, gpu: GPUInfo, y: int, x: int) -> int:
        """Render temperature information.

        Args:
            gpu: GPU information
            y: Starting Y coordinate
            x: Starting X coordinate

        Returns:
            Next Y coordinate
        """
        if gpu.temperature > 0:
            line = f"Temp  {gpu.temperature:5.1f}°C"
            self.display.safe_addstr(
                y, x, line, self.display.get_color(gpu.temperature)
            )
            return y + 1
        return y

    def _render_power(self, gpu: GPUInfo, y: int, x: int) -> int:
        """Render power usage information.

        Args:
            gpu: GPU information
            y: Starting Y coordinate
            x: Starting X coordinate

        Returns:
            Next Y coordinate
        """
        if gpu.power_draw > 0 and gpu.power_limit > 0:
            power_percent = gpu.power_draw / gpu.power_limit * 100
            line = f"Power {gpu.power_draw:5.1f}W / {gpu.power_limit:5.1f}W"
            self.display.safe_addstr(y, x, line, self.display.get_color(power_percent))
            return y + 1
        return y

    def _build_process_tree(
        self, processes: List[Dict]
    ) -> Tuple[List[Dict], Dict[int, List[Dict]]]:
        """Build process tree structure from flat process list.

        Args:
            processes: List of process dictionaries with pid and ppid

        Returns:
            Tuple of (root_processes, children_map) where:
            - root_processes: Processes with no parent in the GPU process list
            - children_map: Dict mapping parent PID to list of child processes
        """
        # Build PID to process mapping
        pid_to_proc = {proc["pid"]: proc for proc in processes}

        # Build children mapping
        children_map = {}
        root_processes = []

        for proc in processes:
            ppid = proc.get("ppid")
            if ppid and ppid in pid_to_proc:
                # Parent is in GPU process list
                if ppid not in children_map:
                    children_map[ppid] = []
                children_map[ppid].append(proc)
            else:
                # Root process (no parent in GPU list)
                root_processes.append(proc)

        return root_processes, children_map

    def _render_processes(
        self, gpu: GPUInfo, y: int, x: int, selected_pid: Optional[int] = None
    ) -> int:
        """Render GPU process information with tree hierarchy.

        Args:
            gpu: GPU information
            y: Starting Y coordinate
            x: Starting X coordinate
            selected_pid: PID of selected process for highlighting

        Returns:
            Next Y coordinate
        """
        if not gpu.processes:
            return y

        y += 1
        self.display.safe_addstr(y, x, "Running Processes:", curses.color_pair(5))
        y += 1

        # Build process tree
        root_processes, children_map = self._build_process_tree(gpu.processes)

        # Render processes with tree structure
        for i, proc in enumerate(root_processes):
            is_last_root = i == len(root_processes) - 1
            y = self._render_process_tree_node(
                proc, y, x, selected_pid, children_map, is_last_root, ""
            )

        return y + 1

    def _render_process_tree_node(
        self,
        proc: Dict,
        y: int,
        x: int,
        selected_pid: Optional[int],
        children_map: Dict[int, List[Dict]],
        is_last: bool,
        prefix: str,
    ) -> int:
        """Recursively render a process tree node and its children.

        Args:
            proc: Process dictionary
            y: Current Y coordinate
            x: Starting X coordinate
            selected_pid: PID of selected process
            children_map: Map of parent PID to children
            is_last: Whether this is the last sibling
            prefix: Current tree prefix string

        Returns:
            Next Y coordinate
        """
        # Determine tree symbols
        if prefix:
            tree_symbol = "└── " if is_last else "├── "
        else:
            tree_symbol = "├── " if not is_last else "└── "

        # Get GPU utilization if available
        gpu_util_str = ""
        if "sm_util" in proc:
            gpu_util = proc["sm_util"]
            gpu_util_str = f"GPU {gpu_util:4.1f}% | "
        elif "cu_occupancy" in proc and proc["cu_occupancy"] is not None:
            gpu_util = proc["cu_occupancy"]
            gpu_util_str = f"GPU {gpu_util:4.1f}% | "

        # Process memory might be in bytes instead of MB
        # for some GPU implementations
        memory_value = proc["memory"]

        # If value is extremely large (over 1000 GB when interpreted as MB),
        # assume it's in bytes and convert directly to GB
        if memory_value > 1000 * 1024:  # If > 1000 GB as MB
            # Convert bytes to GB
            mem_gb = memory_value / (1024 * 1024 * 1024)
        else:
            # Otherwise, assume it's in MB as documented and convert to GB
            mem_gb = memory_value / 1024

        # Format with appropriate precision based on size
        if mem_gb < 0.01:  # Very tiny values (under 10MB)
            mem_format = f"{mem_gb*1024:.1f}MB"
        elif mem_gb < 0.1:  # Small values (under 100MB)
            mem_format = f"{mem_gb:.3f}GB"
        elif mem_gb < 1:  # Medium values (under 1GB)
            mem_format = f"{mem_gb:.2f}GB"
        else:  # Large values (1GB and above)
            mem_format = f"{mem_gb:.1f}GB"

        # Build the display line with tree symbols
        line = (
            f"{prefix}{tree_symbol}PID {proc['pid']:6d} | {gpu_util_str}"
            f"{mem_format:>9s} | {proc['name']}"
        )

        # Apply selection highlighting
        is_selected = selected_pid is not None and proc["pid"] == selected_pid
        attr = curses.A_REVERSE if is_selected else curses.color_pair(6)
        self.display.safe_addstr(y, x, line, attr)
        y += 1

        # Render children recursively
        children = children_map.get(proc["pid"], [])
        for i, child in enumerate(children):
            is_last_child = i == len(children) - 1
            # Update prefix for children
            child_prefix = prefix + ("    " if is_last else "│   ")
            y = self._render_process_tree_node(
                child, y, x, selected_pid, children_map, is_last_child, child_prefix
            )

        return y

    def render(
        self,
        gpu_info: List[tuple[GPUInfo, str]],
        start_y: int = 3,
        indent: int = 2,
        selected_pid: Optional[int] = None,
    ) -> int:
        """Render the complete GPU panel.

        Args:
            gpu_info: List of tuples containing (GPU information, vendor string)
            start_y: Starting Y coordinate
            indent: Left indentation
            selected_pid: PID of selected process for highlighting

        Returns:
            Next Y coordinate
        """
        if not gpu_info:
            self.display.safe_addstr(
                start_y, indent, "No compatible GPUs detected", curses.color_pair(3)
            )
            return start_y + 1

        y = start_y
        bar_width = min(50, self.display.width - 35)

        for gpu, vendor in gpu_info:
            # Render GPU sections
            y = self._render_gpu_header(gpu, y, indent, vendor)
            y = self._render_utilization_bar(gpu, y, indent, bar_width)
            y = self._render_memory_bar(gpu, y, indent, bar_width)
            y = self._render_temperature(gpu, y, indent)
            y = self._render_power(gpu, y, indent)
            y = self._render_processes(gpu, y, indent, selected_pid)

        return y

    def get_all_gpu_processes(self, gpu_info: List[tuple[GPUInfo, str]]) -> List[dict]:
        """Get all processes across all GPUs as a flat list.

        Args:
            gpu_info: List of tuples containing (GPU information, vendor string)

        Returns:
            List of process dictionaries with PID, name, and memory
        """
        all_processes = []
        seen_pids = set()

        for gpu, _ in gpu_info:
            for proc in gpu.processes:
                pid = proc["pid"]
                # Avoid duplicates (process can be on multiple GPUs)
                if pid not in seen_pids:
                    seen_pids.add(pid)
                    all_processes.append(
                        {"pid": pid, "name": proc["name"], "memory": proc["memory"]}
                    )

        return all_processes

    def get_selected_process_by_index(
        self, gpu_info: List[tuple[GPUInfo, str]], selected_index: int
    ) -> Optional[dict]:
        """Get process by selection index.

        Args:
            gpu_info: List of tuples containing (GPU information, vendor string)
            selected_index: Index of selected process

        Returns:
            Process dict or None if invalid index
        """
        all_processes = self.get_all_gpu_processes(gpu_info)

        if 0 <= selected_index < len(all_processes):
            return all_processes[selected_index]

        return None
