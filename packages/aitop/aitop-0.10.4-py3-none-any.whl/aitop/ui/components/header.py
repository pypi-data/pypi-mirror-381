#!/usr/bin/env python3
"""Header component for the UI."""

import curses
from datetime import datetime
from typing import Optional

from ..display import Display


class HeaderComponent:
    """Renders the application header."""

    def __init__(self, display: Display):
        """Initialize the header component.

        Args:
            display: Display instance
        """
        self.display = display

    def render(self, gpu_vendor: str, y: int = 0, attr: Optional[int] = None) -> int:
        """Render the header.

        Args:
            gpu_vendor: GPU vendor string
            y: Starting Y coordinate (ignored, uses layout system)
            attr: Custom attribute override

        Returns:
            Next Y coordinate
        """
        if attr is None:
            attr = curses.color_pair(7) | curses.A_BOLD

        # Get header layout from layout system
        layout = self.display.layout.calculate()
        header_rect = layout["header"]

        # Create the header string
        current_time = datetime.now().strftime("%H:%M:%S")
        header = f" AITop - {current_time} "

        # Draw the header border (full width)
        self.display.safe_addstr(header_rect.y, 0, "=" * header_rect.width, attr)

        # Draw the centered header text
        header_x = (header_rect.width - len(header)) // 2
        self.display.safe_addstr(header_rect.y, header_x, header, attr)

        return header_rect.bottom
