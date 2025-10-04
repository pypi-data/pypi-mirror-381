#!/usr/bin/env python3
"""System memory monitoring functionality."""

from dataclasses import dataclass
from typing import Dict, Any
import psutil


@dataclass
class MemoryStats:
    """Container for memory statistics."""
    total: float  # Total physical memory in bytes
    used: float   # Used memory in bytes
    free: float   # Free memory in bytes
    percent: float  # Memory usage percentage
    swap_total: float  # Total swap memory in bytes
    swap_used: float   # Used swap memory in bytes
    swap_free: float   # Free swap memory in bytes
    swap_percent: float  # Swap usage percentage


class SystemMemoryMonitor:
    """Monitors system memory usage."""
    
    @staticmethod
    def get_memory_stats() -> MemoryStats:
        """Get current memory statistics with error handling."""
        try:
            vm = psutil.virtual_memory()
            swap = psutil.swap_memory()

            return MemoryStats(
                total=vm.total,
                used=vm.used,
                free=vm.free,
                percent=vm.percent,
                swap_total=swap.total,
                swap_used=swap.used,
                swap_free=swap.free,
                swap_percent=swap.percent
            )
        except Exception as e:
            # Return safe defaults if memory monitoring fails
            import logging
            logging.error(f"Failed to get memory stats: {e}")
            return MemoryStats(
                total=0, used=0, free=0, percent=0.0,
                swap_total=0, swap_used=0, swap_free=0, swap_percent=0.0
            )
    
    @staticmethod
    def get_memory_by_type() -> Dict[str, float]:
        """Get memory usage broken down by type (in bytes)."""
        vm = psutil.virtual_memory()
        return {
            'available': vm.available,
            'buffers': getattr(vm, 'buffers', 0),
            'cached': getattr(vm, 'cached', 0),
            'shared': getattr(vm, 'shared', 0),
            'slab': getattr(vm, 'slab', 0)
        }
    
    @staticmethod
    def bytes_to_gb(bytes_value: float) -> float:
        """Convert bytes to gigabytes."""
        return bytes_value / (1024 ** 3)
    
    def get_formatted_stats(self) -> Dict[str, Any]:
        """Get memory statistics formatted in GB with percentages."""
        stats = self.get_memory_stats()
        memory_types = self.get_memory_by_type()
        
        return {
            'ram': {
                'total_gb': self.bytes_to_gb(stats.total),
                'used_gb': self.bytes_to_gb(stats.used),
                'free_gb': self.bytes_to_gb(stats.free),
                'percent': stats.percent,
                'details': {
                    name: self.bytes_to_gb(value)
                    for name, value in memory_types.items()
                }
            },
            'swap': {
                'total_gb': self.bytes_to_gb(stats.swap_total),
                'used_gb': self.bytes_to_gb(stats.swap_used),
                'free_gb': self.bytes_to_gb(stats.swap_free),
                'percent': stats.swap_percent
            }
        }