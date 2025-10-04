#!/usr/bin/env python3
"""Modal dialog system for confirmations and user input."""

import curses
from typing import Optional, List, Tuple, Dict, Any


class ModalDialog:
    """Reusable modal dialog system for AITop."""

    def __init__(self, display):
        """Initialize modal dialog.

        Args:
            display: Display instance for rendering
        """
        self.display = display
        self.last_signal_index = 0  # Remember last signal choice

    def render_signal_menu(self, signals: List[Dict[str, Any]],
                          process_info: Dict[str, Any]) -> Optional[int]:
        """Render signal selection menu.

        Args:
            signals: List of signal dicts with 'num', 'name', 'desc'
            process_info: Dict with 'pid', 'name', 'username'

        Returns:
            Selected signal number or None if cancelled
        """
        height = min(len(signals) + 8, self.display.height - 4)
        width = 60
        max_y, max_x = self.display.height, self.display.width

        # Calculate center position
        top_y = max((max_y - height) // 2, 1)
        left_x = max((max_x - width) // 2, 1)

        # Create dialog window
        dialog = None
        try:
            dialog = curses.newwin(height, width, top_y, left_x)
            dialog.keypad(True)
        except curses.error:
            return None  # Terminal too small

        current_pos = self.last_signal_index

        while True:
            try:
                dialog.clear()
                dialog.box()

                # Title
                title = " Send Signal "
                dialog.addstr(0, (width - len(title)) // 2, title, curses.A_BOLD)

                # Process info
                pid = process_info.get('pid', '?')
                name = process_info.get('name', 'unknown')
                proc_line = f"PID: {pid}  Name: {name}"
                if len(proc_line) > width - 4:
                    proc_line = proc_line[:width-7] + "..."
                dialog.addstr(2, 2, proc_line)

                # Signal list header
                dialog.addstr(4, 2, "Select signal:", curses.A_BOLD)

                # Render signals
                visible_start = max(0, current_pos - (height - 10))
                visible_end = min(len(signals), visible_start + (height - 8))

                for i in range(visible_start, visible_end):
                    sig = signals[i]
                    y = 6 + (i - visible_start)
                    sig_num = sig['num']
                    sig_name = sig['name']
                    sig_desc = sig['desc']

                    text = f"{sig_num:2d} {sig_name:10s} - {sig_desc}"
                    if len(text) > width - 6:
                        text = text[:width-9] + "..."

                    attr = curses.A_REVERSE if i == current_pos else curses.A_NORMAL

                    # Highlight dangerous signals in red
                    if sig.get('dangerous') and i != current_pos:
                        color = self.display.color_manager.get_color_pair('RED', '-1')
                        attr |= color

                    dialog.addstr(y, 4, text[:width-6], attr)

                # Function bar
                func_y = height - 2
                dialog.addstr(func_y, 2, "Enter", curses.A_BOLD)
                dialog.addstr(func_y, 8, ":Send  ")
                dialog.addstr(func_y, 15, "Esc", curses.A_BOLD)
                dialog.addstr(func_y, 19, ":Cancel")

                dialog.refresh()

                # Handle input
                key = dialog.getch()

                if key == curses.KEY_UP:
                    current_pos = max(0, current_pos - 1)
                elif key == curses.KEY_DOWN:
                    current_pos = min(len(signals) - 1, current_pos + 1)
                elif key in [10, 13]:  # Enter
                    self.last_signal_index = current_pos
                    selected_signal = signals[current_pos]

                    # Extra confirmation for dangerous signals
                    if selected_signal.get('dangerous'):
                        if not self.render_confirmation(
                            "SIGKILL cannot be caught.\nThis may cause data loss.\n\nContinue?",
                            "Warning"
                        ):
                            continue  # User cancelled, stay in menu

                    # Cleanup before return
                    dialog.clear()
                    dialog.refresh()
                    del dialog
                    return selected_signal['num']

                elif key == 27:  # ESC
                    # Cleanup before return
                    dialog.clear()
                    dialog.refresh()
                    del dialog
                    return None

            except curses.error:
                # Cleanup on error
                if dialog:
                    try:
                        dialog.clear()
                        dialog.refresh()
                        del dialog
                    except:
                        pass
                return None

    def render_confirmation(self, message: str, title: str = "Confirm") -> bool:
        """Render yes/no confirmation dialog.

        Args:
            message: Message to display
            title: Dialog title

        Returns:
            True if yes, False if no/cancelled
        """
        # Split message into lines
        lines = message.split('\n')
        height = len(lines) + 6
        width = max(len(line) for line in lines) + 8
        width = min(width, self.display.width - 4)
        width = max(width, 30)

        max_y, max_x = self.display.height, self.display.width
        top_y = max((max_y - height) // 2, 1)
        left_x = max((max_x - width) // 2, 1)

        try:
            dialog = curses.newwin(height, width, top_y, left_x)
            dialog.keypad(True)
            dialog.box()

            # Title
            dialog.addstr(0, (width - len(title) - 2) // 2, f" {title} ", curses.A_BOLD)

            # Message lines
            for i, line in enumerate(lines):
                if len(line) > width - 4:
                    line = line[:width-7] + "..."
                dialog.addstr(2 + i, 2, line)

            # Options
            options_y = height - 2
            yes_text = "[Y]es"
            no_text = "[N]o"
            total_width = len(yes_text) + len(no_text) + 10
            start_x = (width - total_width) // 2

            dialog.addstr(options_y, start_x, yes_text, curses.A_BOLD)
            dialog.addstr(options_y, start_x + len(yes_text) + 10, no_text, curses.A_BOLD)

            dialog.refresh()

            # Handle input
            while True:
                key = dialog.getch()
                if key in [ord('y'), ord('Y')]:
                    return True
                elif key in [ord('n'), ord('N'), 27]:  # 27 = ESC
                    return False

        except curses.error:
            return False

    def render_status(self, message: str, success: bool = True, duration_ms: int = 500) -> None:
        """Show temporary status message.

        Args:
            message: Status message to display
            success: True for normal, False for error (with beep)
            duration_ms: How long to display message
        """
        max_y, max_x = self.display.height, self.display.width
        width = min(len(message) + 6, max_x - 4)
        height = 3

        top_y = max((max_y - height) // 2, 1)
        left_x = max((max_x - width) // 2, 1)

        try:
            status_win = curses.newwin(height, width, top_y, left_x)
            status_win.box()

            # Determine color/style
            if success:
                attr = curses.A_BOLD
            else:
                attr = curses.A_BOLD
                color = self.display.color_manager.get_color_pair('RED', '-1')
                attr |= color
                curses.beep()  # Audio feedback for errors

            # Center message
            msg_x = (width - len(message)) // 2
            if len(message) > width - 4:
                message = message[:width-7] + "..."

            status_win.addstr(1, max(msg_x, 2), message, attr)
            status_win.refresh()

            # Wait
            curses.napms(duration_ms)

            # Clear
            status_win.clear()
            status_win.refresh()

        except curses.error:
            pass

    def render_error(self, message: str, duration_ms: int = 2000) -> None:
        """Show error message.

        Args:
            message: Error message
            duration_ms: How long to display (default 2 seconds)
        """
        self.render_status(message, success=False, duration_ms=duration_ms)

    def render_warning_list(self, warnings: List[str], title: str = "Warnings") -> bool:
        """Render list of warnings with continue/cancel option.

        Args:
            warnings: List of warning messages
            title: Dialog title

        Returns:
            True to continue, False to cancel
        """
        height = min(len(warnings) + 7, self.display.height - 4)
        width = 70
        max_y, max_x = self.display.height, self.display.width

        top_y = max((max_y - height) // 2, 1)
        left_x = max((max_x - width) // 2, 1)

        try:
            dialog = curses.newwin(height, width, top_y, left_x)
            dialog.keypad(True)
            dialog.box()

            # Title with warning color
            warn_color = self.display.color_manager.get_color_pair('YELLOW', '-1')
            dialog.addstr(0, (width - len(title) - 2) // 2, f" {title} ",
                         curses.A_BOLD | warn_color)

            # Warnings
            for i, warning in enumerate(warnings[:height-5]):
                y = 2 + i
                text = f"• {warning}"
                if len(text) > width - 4:
                    text = text[:width-7] + "..."
                dialog.addstr(y, 2, text)

            # Continue/Cancel
            options_y = height - 2
            dialog.addstr(options_y, 10, "Continue? ", curses.A_BOLD)
            dialog.addstr(options_y, 20, "[Y]es")
            dialog.addstr(options_y, 30, "[N]o")

            dialog.refresh()

            # Handle input
            while True:
                key = dialog.getch()
                if key in [ord('y'), ord('Y')]:
                    return True
                elif key in [ord('n'), ord('N'), 27]:
                    return False

        except curses.error:
            return False
