"""UI component modules."""

from .cpu_panel import CPUPanel
from .footer import FooterComponent
from .gpu_panel import GPUPanel
from .header import HeaderComponent
from .memory_panel import MemoryPanel
from .modal import ModalDialog
from .overview import OverviewPanel
from .process_panel import ProcessPanel
from .tabs import TabsComponent

__all__ = [
    "HeaderComponent",
    "FooterComponent",
    "TabsComponent",
    "OverviewPanel",
    "GPUPanel",
    "ProcessPanel",
    "MemoryPanel",
    "CPUPanel",
    "ModalDialog",
]
