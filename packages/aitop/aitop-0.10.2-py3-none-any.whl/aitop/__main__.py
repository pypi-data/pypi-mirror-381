#!/usr/bin/env python3
"""AITop - A high performance AI/ML workload monitoring system."""

import curses
import sys
import os
import time
import logging
import argparse
import threading
from typing import Optional

from aitop.core.gpu.factory import GPUMonitorFactory
from aitop.ui.display import Display
from aitop.ui.components.header import HeaderComponent
from aitop.ui.components.footer import FooterComponent
from aitop.ui.components.tabs import TabsComponent
from aitop.ui.components.overview import OverviewPanel
from aitop.ui.components.gpu_panel import GPUPanel
from aitop.ui.components.process_panel import ProcessPanel
from aitop.ui.components.memory_panel import MemoryPanel
from aitop.ui.components.cpu_panel import CPUPanel
from aitop.ui.components.modal import ModalDialog
from aitop.core.system.memory import SystemMemoryMonitor
from aitop.core.system.cpu import CPUStats
from aitop.core.process.killer import ProcessTerminator
from aitop.version import __version__

# Import optimized data collector (from earlier artifact)
from aitop.data_collector import DataCollector, SystemData


def setup_logging(debug_mode: bool = False, log_file: str = 'aitop.log') -> None:
    """Configure logging with performance optimizations.
    
    Args:
        debug_mode: If True, enable debug logging to file
        log_file: Path to log file for debug mode
    """
    # Set up root logger
    root_logger = logging.getLogger()
    
    # Always log warnings and above to console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_formatter = logging.Formatter('%(levelname)s: %(message)s')
    console_handler.setFormatter(console_formatter)
    root_logger.addHandler(console_handler)
    
    if debug_mode:
        # Optimize file logging for performance
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        
        # More efficient formatter
        file_formatter = logging.Formatter(
            '%(asctime)s.%(msecs)03d [%(threadName)s] %(name)s:%(lineno)d - %(levelname)s - %(message)s',
            datefmt='%H:%M:%S'  # Use shorter timestamp for better performance
        )
        file_handler.setFormatter(file_formatter)
        root_logger.addHandler(file_handler)
        root_logger.setLevel(logging.DEBUG)
        
        # Log basic system information
        import platform
        logging.debug("=== AITop v%s ===", __version__)
        logging.debug("Platform: %s, Python: %s", platform.platform(), sys.version.split()[0])
    else:
        root_logger.setLevel(logging.WARNING)


class AITop:
    """Main application class with performance optimizations."""

    def __init__(self, stdscr):
        """Initialize the application.
        
        Args:
            stdscr: curses screen object
        """
        self.stdscr = stdscr
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.debug("Initializing AITop application")

        # Application state with thread safety
        self.running = True
        self.selected_tab = 0
        self.sort_by = 'cpu_percent'
        self.sort_reverse = True
        self.scroll_position = 0
        self.selected_process_index = 0  # For process selection and killing (AI Processes tab)
        self.selected_gpu_process_index = 0  # For GPU tab process selection
        self.needs_redraw = True
        self.render_lock = threading.RLock()
        
        # Performance settings
        self.input_poll_interval = 0.05      # 50ms input polling (20Hz)
        self.render_interval = 0.2           # 200ms render interval (5 FPS)
        self.last_input_poll = 0
        self.last_render = 0
        self.last_resize_check = 0
        self.resize_check_interval = 0.5     # Check for resize every 500ms
        
        # Initialize display with better performance
        self.display = Display(stdscr)
        self.last_size = self.display.get_dimensions()
        
        # Initialize UI components
        self.header = HeaderComponent(self.display)
        self.footer = FooterComponent(self.display)
        self.tabs = TabsComponent(self.display)
        self.overview = OverviewPanel(self.display)
        self.gpu_panel = GPUPanel(self.display)
        self.process_panel = ProcessPanel(self.display)
        self.memory_panel = MemoryPanel(self.display)
        self.cpu_panel = CPUPanel(self.display)
        self.modal = ModalDialog(self.display)

        # Process termination system
        self.terminator = ProcessTerminator(ai_process_monitor=None)  # Will be set later if AI monitor available
        
        # Performance metrics for UI
        self.perf_metrics = {
            'render_time': 0.0,
            'collection_time': 0.0,
            'frames_per_second': 0.0,
            'last_fps_calc': time.time(),
            'frame_count': 0
        }

        # Data collector will be initialized and started in _main() with CLI args
        # This prevents double initialization and resource leaks
        self.collector = None
        self.system_data = None

    def handle_input(self) -> None:
        """Handle user input efficiently."""
        try:
            # Only poll for input at specified interval
            current_time = time.time()
            if current_time - self.last_input_poll < self.input_poll_interval:
                return
                
            self.last_input_poll = current_time
            key = self.display.stdscr.getch()

            if key == curses.ERR:  # No input available
                return

            self.needs_redraw = True  # Input requires redraw

            if key == ord('q'):
                self.running = False
                self.logger.debug("User requested exit")
            elif key == ord('c'):
                self.sort_by = 'cpu_percent'
                self.sort_reverse = True
            elif key == ord('m'):
                self.sort_by = 'memory_percent'
                self.sort_reverse = True
            elif key == ord('h'):
                self.sort_reverse = not self.sort_reverse
            elif key == ord('r'):  # Add refresh key
                self.display.force_redraw()
                self.logger.debug("Manual refresh requested")
            elif key == curses.KEY_RESIZE:  # Handle terminal resize
                self.display.handle_resize()
                self.needs_redraw = True
                self.last_size = self.display.get_dimensions()
                self.logger.debug("Terminal resize event handled")
            elif key == ord('k'):  # Kill process
                if self.selected_tab == 1 and self.system_data:  # AI Processes tab
                    self.handle_kill_request()
                elif self.selected_tab == 2 and self.system_data:  # GPU tab
                    self.handle_gpu_kill_request()
            elif key in [curses.KEY_LEFT, curses.KEY_RIGHT]:
                self.selected_tab = self.tabs.handle_tab_input(key, self.selected_tab)
                self.scroll_position = 0
                self.selected_process_index = 0  # Reset selection when changing tabs
                self.selected_gpu_process_index = 0
            elif key in [curses.KEY_UP, curses.KEY_DOWN] and self.system_data:
                if self.selected_tab == 1:  # AI Processes tab
                    # Update both scroll position and selection index together
                    old_pos = self.selected_process_index
                    if key == curses.KEY_UP:
                        self.selected_process_index = max(0, self.selected_process_index - 1)
                    elif key == curses.KEY_DOWN:
                        self.selected_process_index = min(
                            len(self.system_data.processes) - 1,
                            self.selected_process_index + 1
                        )
                    # Scroll position follows selection
                    if self.selected_process_index != old_pos:
                        self.scroll_position = self.process_panel.handle_scroll(
                            key, self.scroll_position, self.system_data.processes
                        )
                elif self.selected_tab == 2:  # GPU tab
                    # Navigate GPU processes
                    gpu_processes = self.gpu_panel.get_all_gpu_processes(self.system_data.gpu_info)
                    if gpu_processes:
                        if key == curses.KEY_UP:
                            self.selected_gpu_process_index = max(0, self.selected_gpu_process_index - 1)
                        elif key == curses.KEY_DOWN:
                            self.selected_gpu_process_index = min(
                                len(gpu_processes) - 1,
                                self.selected_gpu_process_index + 1
                            )
        except Exception as e:
            self.logger.error(f"Input handling error: {e}", exc_info=True)

    def handle_kill_request(self) -> None:
        """Handle user request to kill a process from AI Processes tab."""
        if not self.system_data or not self.system_data.processes:
            return

        try:
            # Get the selected process
            selected_process = self.process_panel.get_selected_process(
                self.system_data.processes,
                self.selected_process_index,
                self.sort_by,
                self.sort_reverse
            )

            if not selected_process:
                self.modal.render_error("No process selected")
                return

            # Build process info for modal
            process_info = {
                'pid': selected_process['pid'],
                'name': selected_process['name'],
                'username': selected_process.get('username', 'unknown')
            }

            # Show signal selection menu
            signals = ProcessTerminator.get_available_signals()
            selected_signal = self.modal.render_signal_menu(signals, process_info)

            if selected_signal is None:
                # User cancelled
                return

            # Attempt to terminate the process
            result = self.terminator.terminate_process(
                pid=selected_process['pid'],
                signal_num=selected_signal,
                force=False
            )

            # Show warnings if any (before attempting kill)
            if result['warnings']:
                if not self.modal.render_warning_list(result['warnings'], "AI Process Warning"):
                    # User chose not to continue
                    return

            # Show result
            if result['success']:
                self.modal.render_status(result['message'], success=True)
                self.logger.info(f"Process kill: {result['message']}")
            else:
                error_msg = result['message']
                if result['errors']:
                    error_msg = result['errors'][0]
                self.modal.render_error(error_msg)
                self.logger.warning(f"Process kill failed: {error_msg}")

        except Exception as e:
            self.logger.error(f"Kill request error: {e}", exc_info=True)
            self.modal.render_error(f"Error: {str(e)}")

    def handle_gpu_kill_request(self) -> None:
        """Handle user request to kill a process from GPU tab."""
        if not self.system_data or not self.system_data.gpu_info:
            return

        try:
            # Get the selected GPU process
            selected_process = self.gpu_panel.get_selected_process_by_index(
                self.system_data.gpu_info,
                self.selected_gpu_process_index
            )

            if not selected_process:
                self.modal.render_error("No GPU process selected")
                return

            # Build process info for modal (GPU processes have limited info)
            process_info = {
                'pid': selected_process['pid'],
                'name': selected_process['name'],
                'username': 'unknown'  # GPU info doesn't include username
            }

            # Show signal selection menu
            signals = ProcessTerminator.get_available_signals()
            selected_signal = self.modal.render_signal_menu(signals, process_info)

            if selected_signal is None:
                # User cancelled
                return

            # Attempt to terminate the process
            result = self.terminator.terminate_process(
                pid=selected_process['pid'],
                signal_num=selected_signal,
                force=False
            )

            # Show warnings if any
            if result['warnings']:
                if not self.modal.render_warning_list(result['warnings'], "GPU Process Warning"):
                    # User chose not to continue
                    return

            # Show result
            if result['success']:
                self.modal.render_status(result['message'], success=True)
                self.logger.info(f"GPU process kill: {result['message']}")
            else:
                error_msg = result['message']
                if result['errors']:
                    error_msg = result['errors'][0]
                self.modal.render_error(error_msg)
                self.logger.warning(f"GPU process kill failed: {error_msg}")

        except Exception as e:
            self.logger.error(f"GPU kill request error: {e}", exc_info=True)
            self.modal.render_error(f"Error: {str(e)}")

    def check_resize(self) -> bool:
        """Check if terminal has been resized.

        Returns:
            bool: True if resized, False otherwise
        """
        current_time = time.time()
        if current_time - self.last_resize_check < self.resize_check_interval:
            return False

        self.last_resize_check = current_time
        current_size = self.display.get_dimensions()

        if current_size != self.last_size:
            self.display.handle_resize()
            self.needs_redraw = True
            self.last_size = current_size
            self.logger.debug(f"Terminal resized to {current_size[1]}x{current_size[0]}")
            return True

        return False

    def update_data(self) -> bool:
        """Update system data from collector.

        Returns:
            bool: True if data was updated, False otherwise
        """
        # Check if collector is initialized
        if not self.collector:
            return False

        # Get latest data if available
        new_data = self.collector.get_data(timeout=0.01)
        if new_data:
            self.system_data = new_data
            self.needs_redraw = True
            return True
        return False

    def _get_footer_controls(self) -> list:
        """Get footer controls based on current tab.

        Returns:
            List of (key, action) tuples for footer
        """
        base_controls = [
            ('q', 'quit'),
            ('c', 'sort CPU'),
            ('m', 'sort MEM'),
            ('h', 'toggle sort'),
            ('arrows', 'navigate')
        ]

        # Add kill control for AI Processes and GPU tabs
        if self.selected_tab == 1:  # AI Processes tab
            base_controls.insert(1, ('k', 'kill'))
        elif self.selected_tab == 2:  # GPU tab
            base_controls.insert(1, ('k', 'kill'))

        return base_controls

    def update_performance_metrics(self, render_time: float) -> None:
        """Update performance tracking metrics."""
        self.perf_metrics['render_time'] = render_time

        # Update FPS calculation
        current_time = time.time()
        self.perf_metrics['frame_count'] += 1

        # Calculate FPS every second
        elapsed = current_time - self.perf_metrics['last_fps_calc']
        if elapsed >= 1.0:
            self.perf_metrics['frames_per_second'] = self.perf_metrics['frame_count'] / elapsed
            self.perf_metrics['frame_count'] = 0
            self.perf_metrics['last_fps_calc'] = current_time

    def render(self) -> None:
        """Render the complete interface with optimizations."""
        # Skip rendering if not needed or not time yet
        current_time = time.time()
        if not self.needs_redraw and current_time - self.last_render < self.render_interval:
            return
            
        # Check for data to render
        if not self.system_data:
            return
            
        render_start = time.time()
        with self.render_lock:  # Thread safety for rendering
            try:
                self.display.clear()

                # Render common elements
                self.header.render(self.system_data.primary_vendor)
                self.tabs.render(self.selected_tab, 1)

                # Render tab-specific content
                if self.selected_tab == 0:  # Overview
                    self.overview.render(
                        self.system_data.gpu_info,
                        self.system_data.processes,
                        self.system_data.memory_stats,
                        self.system_data.cpu_stats,
                        self.system_data.primary_vendor
                    )
                elif self.selected_tab == 1:  # AI Processes
                    self.process_panel.render(
                        self.system_data.processes,
                        [gpu for gpu, _ in self.system_data.gpu_info],
                        3, 2,
                        self.sort_by,
                        self.sort_reverse,
                        self.scroll_position,
                        self.selected_process_index
                    )
                elif self.selected_tab == 2:  # GPU
                    # Get selected process PID for highlighting
                    selected_process = self.gpu_panel.get_selected_process_by_index(
                        self.system_data.gpu_info,
                        self.selected_gpu_process_index
                    )
                    selected_pid = selected_process['pid'] if selected_process else None
                    self.gpu_panel.render(self.system_data.gpu_info, 3, 2, selected_pid)
                elif self.selected_tab == 3:  # Memory
                    self.memory_panel.render(
                        self.system_data.memory_stats,
                        self.system_data.memory_types
                    )
                elif self.selected_tab == 4:  # CPU
                    self.cpu_panel.render(self.system_data.cpu_stats)

                # Render footer with tab-specific controls
                footer_controls = self._get_footer_controls()
                self.footer.render(custom_controls=footer_controls)
                self.display.refresh()
                
                # Update metrics and flags
                render_time = time.time() - render_start
                self.update_performance_metrics(render_time)
                self.needs_redraw = False
                self.last_render = time.time()
                
                self.logger.debug(f"UI rendered in {render_time:.3f}s")
            except Exception as e:
                self.logger.error(f"Render error: {e}", exc_info=True)

    def cleanup(self) -> None:
        """Clean up resources."""
        self.logger.debug("Cleaning up application")
        if self.collector:
            self.collector.stop()
            
        if self.display:
            self.display.cleanup()

    def run(self) -> None:
        """Main application loop with performance optimizations."""
        self.logger.debug("Application run loop started")
        try:
            # Use adaptive timing logic
            while self.running:
                # Check for terminal resize (less frequent)
                self.check_resize()
                
                # Handle input (moderate frequency)
                self.handle_input()
                
                # Update data (when available)
                self.update_data()
                
                # Render UI (controlled by render_interval)
                self.render()
                
                # Sleep to reduce CPU usage - adaptive sleep
                if self.needs_redraw:
                    # Shorter sleep when UI needs updating
                    time.sleep(0.01)
                else:
                    # Longer sleep when idle
                    time.sleep(0.05)
                    
        except KeyboardInterrupt:
            self.logger.debug("Application interrupted by user")
        except Exception as e:
            self.logger.error(f"Run loop error: {e}", exc_info=True)
        finally:
            self.cleanup()
            self.logger.debug("Application terminated")


def _main(stdscr, args) -> int:
    """Initialize and run the application with custom parameters.
    
    Args:
        stdscr: Curses screen object
        args: Command line arguments
        
    Returns:
        int: Exit code (0 for success, non-zero for error)
    """
    try:
        # Update AITop initialization with command line parameters
        app = AITop(stdscr)
        
        # Apply custom intervals from command line
        app.render_interval = args.render_interval
        
        # Configure data collector with command line arguments
        app.collector = DataCollector(
            update_interval=args.update_interval,
            process_interval=args.process_interval,
            gpu_info_interval=args.gpu_interval,
            max_workers=args.workers
        )
        
        # Configure adaptive timing if specified
        if args.no_adaptive_timing and hasattr(app.collector, '_adaptive_timing'):
            app.collector._adaptive_timing = False
            
        # Start collector
        app.collector.start()
        app.logger.debug("DataCollector thread started with custom parameters")
        
        # Run the application
        app.run()
        return 0
    except Exception as e:
        logging.error(f"Main error: {e}", exc_info=True)
        return 1


def main():
    """Entry point for the application with enhanced error handling."""
    parser = argparse.ArgumentParser(
        description='AITop - A high performance system monitor for AI/ML workloads'
    )
    # Basic options
    parser.add_argument('--debug', action='store_true', 
                      help='Enable debug logging to aitop.log')
    parser.add_argument('--log-file', default='aitop.log',
                      help='Path to log file for debug mode')
    
    # Performance tuning options
    parser.add_argument('--update-interval', type=float, default=0.5,
                      help='Base data update interval in seconds (default: 0.5)')
    parser.add_argument('--process-interval', type=float, default=2.0,
                      help='Process data collection interval in seconds (default: 2.0)')
    parser.add_argument('--gpu-interval', type=float, default=1.0,
                      help='Full GPU info update interval in seconds (default: 1.0)')
    parser.add_argument('--render-interval', type=float, default=0.2,
                      help='UI render interval in seconds (default: 0.2)')
    parser.add_argument('--workers', type=int, default=3,
                      help='Number of worker threads for data collection (default: 3)')
    
    # Display options
    parser.add_argument('--theme', type=str,
                      help='Override theme selection (e.g., monokai_pro, nord)')
    parser.add_argument('--no-adaptive-timing', action='store_true',
                      help='Disable adaptive timing based on system load')
    
    args = parser.parse_args()
    
    # Configure logging based on debug flag
    setup_logging(args.debug, args.log_file)
    
    # Set theme environment variable if specified
    if args.theme:
        os.environ['AITOP_THEME'] = args.theme
        logging.debug(f"Setting theme from command line: {args.theme}")
    
    try:
        # Pass args to curses wrapper
        return curses.wrapper(lambda stdscr: _main(stdscr, args))
    except KeyboardInterrupt:
        logging.debug("Application interrupted by user")
        return 0
    except curses.error as e:
        logging.error(f"Curses error: {e}", exc_info=True)
        print(f"Terminal error: {e}")
        print("Please make sure your terminal supports at least 80x24 characters.")
        return 1
    except Exception as e:
        logging.error(f"Unhandled exception: {e}", exc_info=True)
        print(f"Fatal error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
