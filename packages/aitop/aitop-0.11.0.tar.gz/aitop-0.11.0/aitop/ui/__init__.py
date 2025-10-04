"""User interface components."""

from .components import (
    FooterComponent,
    GPUPanel,
    HeaderComponent,
    MemoryPanel,
    OverviewPanel,
    ProcessPanel,
    TabsComponent,
)
from .display import Display

__all__ = [
    "Display",
    "HeaderComponent",
    "FooterComponent",
    "TabsComponent",
    "OverviewPanel",
    "GPUPanel",
    "ProcessPanel",
    "MemoryPanel",
]
