"""
Layout management for AITop terminal UI.

Provides centralized layout calculations following KISS principle.
All layout math is concentrated here to maintain DRY and SOLID principles.
"""

from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict, Optional, Tuple

if TYPE_CHECKING:
    from .display import Display


@dataclass(frozen=True)
class LayoutRect:
    """
    Immutable rectangle specification for UI regions.

    Attributes:
        y: Top-left Y coordinate
        x: Top-left X coordinate
        height: Height in rows
        width: Width in columns
    """

    y: int
    x: int
    height: int
    width: int

    @property
    def bottom(self) -> int:
        """Bottom edge (y + height)."""
        return self.y + self.height

    @property
    def right(self) -> int:
        """Right edge (x + width)."""
        return self.x + self.width

    def inner(
        self,
        margin: int = 0,
        left: Optional[int] = None,
        right: Optional[int] = None,
        top: Optional[int] = None,
        bottom: Optional[int] = None,
    ) -> "LayoutRect":
        """
        Return inner rectangle with margins applied.

        Args:
            margin: Uniform margin for all sides (if specific margins not provided)
            left: Left margin override
            right: Right margin override
            top: Top margin override
            bottom: Bottom margin override

        Returns:
            New LayoutRect with margins applied
        """
        left_margin = left if left is not None else margin
        right_margin = right if right is not None else margin
        top_margin = top if top is not None else margin
        bottom_margin = bottom if bottom is not None else margin

        return LayoutRect(
            y=self.y + top_margin,
            x=self.x + left_margin,
            height=max(0, self.height - top_margin - bottom_margin),
            width=max(0, self.width - left_margin - right_margin),
        )


class LayoutCalculator:
    """
    Calculates layout rectangles for all UI components.

    This class centralizes all layout calculations to maintain DRY principle.
    Layout is cached and only recalculated when terminal dimensions change.

    Responsibilities:
    - Calculate positions and sizes for all UI regions
    - Handle terminal resize by invalidating cache
    - Provide layout queries for components

    NOT responsible for:
    - Rendering (that's Display's job)
    - Component logic (that's each panel's job)
    """

    # Layout constants - centralized for easy adjustment
    HEADER_HEIGHT = 1
    TABS_HEIGHT = 1
    FOOTER_HEIGHT = 1
    CONTENT_MARGIN_LEFT = 2
    CONTENT_MARGIN_RIGHT = 2

    # Overview tab specific
    OVERVIEW_SPLIT_MIN_WIDTH = 120
    OVERVIEW_LEFT_PERCENT = 40  # Left panel takes 40% when split
    OVERVIEW_SEPARATOR_WIDTH = 2  # Space for "│" separator plus padding

    # Minimum dimensions
    MIN_TERMINAL_WIDTH = 80
    MIN_TERMINAL_HEIGHT = 24

    def __init__(self, display: "Display"):
        """
        Initialize layout calculator.

        Args:
            display: Display instance for dimension queries
        """
        self.display = display
        self._cached_layout = None
        self._cached_dimensions = None

    def calculate(self) -> Dict[str, LayoutRect]:
        """
        Calculate layout for current terminal dimensions.

        Uses caching to avoid redundant calculations. Cache is invalidated
        when terminal dimensions change.

        Returns:
            Dictionary with layout regions:
            - 'screen': Full screen rectangle
            - 'header': Header area (top)
            - 'tabs': Tab navigation area
            - 'content': Main content area (flexible)
            - 'footer': Footer area (bottom)
            - 'overview_left': Left panel for Overview tab
            - 'overview_right': Right panel for Overview tab
            - 'overview_separator_x': X coordinate for separator line
        """
        # Check cache
        current_dims = (self.display.height, self.display.width)
        if self._cached_dimensions == current_dims and self._cached_layout:
            return self._cached_layout

        # Calculate fresh layout
        layout = self._calculate_layout()

        # Update cache
        self._cached_layout = layout
        self._cached_dimensions = current_dims

        return layout

    def _calculate_layout(self) -> Dict[str, LayoutRect]:
        """
        Internal: perform actual layout calculation.

        Returns:
            Dictionary of layout regions
        """
        height = self.display.height
        width = self.display.width

        # Full screen
        screen = LayoutRect(y=0, x=0, height=height, width=width)

        # Header (top, fixed height)
        header = LayoutRect(y=0, x=0, height=self.HEADER_HEIGHT, width=width)

        # Tabs (below header, fixed height)
        tabs = LayoutRect(y=header.bottom, x=0, height=self.TABS_HEIGHT, width=width)

        # Footer (bottom, fixed height)
        footer = LayoutRect(
            y=height - self.FOOTER_HEIGHT, x=0, height=self.FOOTER_HEIGHT, width=width
        )

        # Content (fills remaining vertical space)
        content_y = tabs.bottom
        content_height = footer.y - content_y
        content = LayoutRect(
            y=content_y, x=0, height=max(0, content_height), width=width
        )

        # Overview-specific split layout calculation
        overview_left, overview_right, separator_x = self._calculate_overview_split(
            content
        )

        return {
            "screen": screen,
            "header": header,
            "tabs": tabs,
            "content": content,
            "footer": footer,
            "overview_left": overview_left,
            "overview_right": overview_right,
            "overview_separator_x": separator_x,
        }

    def _calculate_overview_split(
        self, content: LayoutRect
    ) -> Tuple[LayoutRect, LayoutRect, int]:
        """
        Calculate 2-column layout for Overview tab.

        Args:
            content: Content area rectangle

        Returns:
            Tuple of (left_rect, right_rect, separator_x)
            If terminal too narrow, returns (full_rect, empty_rect, -1)
        """
        # Use full width if too narrow for split layout
        if content.width < self.OVERVIEW_SPLIT_MIN_WIDTH:
            empty = LayoutRect(0, 0, 0, 0)
            return content, empty, -1

        # Calculate available width (account for content margins)
        available_width = (
            content.width - self.CONTENT_MARGIN_LEFT - self.CONTENT_MARGIN_RIGHT
        )

        # Calculate left panel width (percentage-based)
        left_content_width = int(available_width * self.OVERVIEW_LEFT_PERCENT / 100)

        # Left panel (includes left margin)
        left = LayoutRect(
            y=content.y,
            x=content.x,
            height=content.height,
            width=self.CONTENT_MARGIN_LEFT + left_content_width,
        )

        # Separator position (immediately after left panel)
        separator_x = left.right

        # Right panel (remaining space after separator)
        right_x = separator_x + self.OVERVIEW_SEPARATOR_WIDTH
        right_width = content.width - right_x

        right = LayoutRect(
            y=content.y, x=right_x, height=content.height, width=max(0, right_width)
        )

        return left, right, separator_x

    def invalidate_cache(self) -> None:
        """
        Force recalculation on next layout request.

        Call this when terminal is resized.
        """
        self._cached_layout = None
        self._cached_dimensions = None

    # Convenience methods for common queries

    def get_content_area(self) -> LayoutRect:
        """
        Get main content area with standard margins applied.

        Returns:
            Content rectangle with left/right margins
        """
        layout = self.calculate()
        return layout["content"].inner(
            left=self.CONTENT_MARGIN_LEFT, right=self.CONTENT_MARGIN_RIGHT
        )

    def get_bar_width(self, max_width: int = 50, label_width: int = 20) -> int:
        """
        Calculate appropriate progress bar width for current terminal size.

        Args:
            max_width: Maximum bar width
            label_width: Space reserved for labels

        Returns:
            Recommended bar width in characters
        """
        content = self.get_content_area()
        available = content.width - label_width
        return min(max_width, max(10, available))
