#!/usr/bin/env python3
"""Process termination with safety checks and AI-specific warnings."""

import os
import signal
import logging
import getpass
from typing import Dict, Any, Optional, Tuple
import psutil


class ProcessTerminator:
    """Handles safe process termination with comprehensive error handling and safety checks."""

    # Supported signals with descriptions
    SIGNALS = [
        {'num': signal.SIGTERM, 'name': 'SIGTERM', 'desc': 'Terminate (graceful shutdown)', 'default': True},
        {'num': signal.SIGKILL, 'name': 'SIGKILL', 'desc': 'Kill (immediate, cannot be caught)', 'dangerous': True},
        {'num': signal.SIGHUP, 'name': 'SIGHUP', 'desc': 'Hangup (reload config)'},
        {'num': signal.SIGINT, 'name': 'SIGINT', 'desc': 'Interrupt (like Ctrl+C)'},
        {'num': signal.SIGQUIT, 'name': 'SIGQUIT', 'desc': 'Quit with core dump'},
        {'num': signal.SIGSTOP, 'name': 'SIGSTOP', 'desc': 'Stop (pause process)'},
        {'num': signal.SIGCONT, 'name': 'SIGCONT', 'desc': 'Continue (resume process)'},
    ]

    def __init__(self, ai_process_monitor=None):
        """Initialize the process terminator.

        Args:
            ai_process_monitor: Optional AIProcessMonitor for AI-specific warnings
        """
        self.logger = logging.getLogger(self.__class__.__name__)
        self.ai_monitor = ai_process_monitor

    def terminate_process(self, pid: int, signal_num: int = signal.SIGTERM,
                         force: bool = False) -> Dict[str, Any]:
        """Terminate a process with comprehensive safety checks.

        Args:
            pid: Process ID to terminate
            signal_num: Signal number to send (default: SIGTERM)
            force: Skip safety checks if True

        Returns:
            dict: {
                'success': bool,
                'pid': int,
                'signal_sent': str or None,
                'warnings': list of str,
                'errors': list of str,
                'message': str
            }
        """
        result = {
            'success': False,
            'pid': pid,
            'signal_sent': None,
            'warnings': [],
            'errors': [],
            'message': ''
        }

        # Step 1: Verify process exists
        verify = self._verify_process_exists(pid)
        if not verify['exists']:
            result['errors'].append(verify['message'])
            result['message'] = verify['message']
            return result

        if verify['is_zombie']:
            result['errors'].append('Cannot send signal to zombie process')
            result['message'] = 'Process is a zombie (already terminated)'
            return result

        if not verify['accessible'] and not force:
            result['errors'].append(verify['message'])
            result['message'] = verify['message']
            return result

        try:
            proc = psutil.Process(pid)

            # Step 2: Check permissions (unless forcing)
            if not force:
                perm_check = self._check_permissions(proc)
                if not perm_check['can_terminate']:
                    result['errors'].append(perm_check['reason'])
                    result['message'] = perm_check['reason']
                    if perm_check['requires_root']:
                        result['message'] = 'Root/administrator privileges required'
                    return result

            # Step 3: Check if system critical (unless forcing)
            if not force:
                critical_check = self._is_system_critical(proc)
                if not critical_check['safe_to_kill']:
                    result['errors'].append(critical_check['reason'])
                    result['message'] = f"Cannot kill: {critical_check['reason']}"
                    return result

            # Step 4: Get AI process warnings (always inform user)
            if self.ai_monitor:
                ai_warnings = self._get_ai_warnings(proc)
                if ai_warnings['has_warnings']:
                    result['warnings'].extend(ai_warnings['warnings'])
                    result['warnings'].append(
                        f"Data loss risk: {ai_warnings['data_loss_risk'].upper()}"
                    )

            # Step 5: Send signal
            signal_name = self._get_signal_name(signal_num)
            proc.send_signal(signal_num)
            result['signal_sent'] = signal_name
            result['success'] = True
            result['message'] = f'Signal {signal_name} sent to PID {pid}'

            # Wait briefly to check if it terminated
            try:
                exit_code = proc.wait(timeout=0.5)
                result['message'] += f' (process terminated with exit code {exit_code})'
            except psutil.TimeoutExpired:
                result['message'] += ' (signal sent, process still running)'

            self.logger.info(result['message'])
            return result

        except psutil.NoSuchProcess:
            result['success'] = True  # Already gone is success
            result['message'] = 'Process already terminated'
            return result
        except psutil.AccessDenied as e:
            result['errors'].append(f'Permission denied: {e}')
            result['message'] = 'Permission denied'
            return result
        except Exception as e:
            result['errors'].append(f'Unexpected error: {e}')
            result['message'] = f'Error: {e}'
            self.logger.error(f'Failed to terminate PID {pid}: {e}', exc_info=True)
            return result

    def _verify_process_exists(self, pid: int) -> Dict[str, Any]:
        """Verify that a process exists and is accessible.

        Returns:
            dict: {'exists': bool, 'accessible': bool, 'is_zombie': bool, 'message': str}
        """
        info = {
            'exists': False,
            'accessible': False,
            'is_zombie': False,
            'message': ''
        }

        # Check if PID exists
        if not psutil.pid_exists(pid):
            info['message'] = f'PID {pid} does not exist'
            return info

        info['exists'] = True

        try:
            proc = psutil.Process(pid)

            # Check if zombie
            if proc.status() == psutil.STATUS_ZOMBIE:
                info['is_zombie'] = True
                info['message'] = 'Process is a zombie (terminated but not reaped)'
                return info

            # Try to access basic info
            proc.name()
            info['accessible'] = True
            info['message'] = 'Process exists and is accessible'

        except psutil.NoSuchProcess:
            info['message'] = 'Process terminated during check'
        except psutil.AccessDenied:
            info['accessible'] = False
            info['message'] = 'Process exists but access denied'
        except psutil.ZombieProcess:
            info['is_zombie'] = True
            info['message'] = 'Process is a zombie'

        return info

    def _check_permissions(self, proc: psutil.Process) -> Dict[str, Any]:
        """Check if we have permission to terminate a process.

        Returns:
            dict: {
                'can_terminate': bool,
                'requires_root': bool,
                'reason': str,
                'process_owner': str
            }
        """
        info = {
            'can_terminate': False,
            'requires_root': False,
            'reason': '',
            'process_owner': ''
        }

        try:
            # Get process owner
            proc_owner = proc.username()
            info['process_owner'] = proc_owner

            # Get current user
            current_user = getpass.getuser()

            # Check if we're root
            is_root = os.geteuid() == 0 if hasattr(os, 'geteuid') else False

            # Check if we own the process
            owns_process = proc_owner == current_user

            if is_root:
                info['can_terminate'] = True
                info['reason'] = 'Running as root/administrator'
            elif owns_process:
                info['can_terminate'] = True
                info['reason'] = f'Process owned by current user ({current_user})'
            else:
                info['can_terminate'] = False
                info['requires_root'] = True
                info['reason'] = (
                    f'Process owned by {proc_owner}, current user is {current_user}. '
                    'Root/administrator privileges required (try sudo).'
                )

        except psutil.AccessDenied:
            info['can_terminate'] = False
            info['requires_root'] = True
            info['reason'] = 'Cannot access process information (likely requires elevated privileges)'

        return info

    def _is_system_critical(self, proc: psutil.Process) -> Dict[str, Any]:
        """Check if a process is system-critical and shouldn't be killed.

        Returns:
            dict: {'is_critical': bool, 'reason': str, 'safe_to_kill': bool}
        """
        info = {
            'is_critical': False,
            'reason': '',
            'safe_to_kill': True
        }

        try:
            pid = proc.pid
            name = proc.name().lower()

            # System PIDs (0, 1, etc.)
            if pid <= 1:
                info['is_critical'] = True
                info['safe_to_kill'] = False
                info['reason'] = f'System process (PID {pid})'
                return info

            # Critical system processes (Linux)
            critical_names = {
                'systemd', 'init', 'kernel', 'kthreadd',
                'sshd', 'dbus', 'udev', 'networkmanager',
                'gdm', 'lightdm', 'sddm',  # Display managers
                'xorg', 'x', 'wayland',  # Display servers
            }

            if name in critical_names:
                info['is_critical'] = True
                info['safe_to_kill'] = False
                info['reason'] = f'Critical system service: {name}'
                return info

            # Check if parent is init/systemd (likely a service)
            try:
                parent = proc.parent()
                if parent and parent.pid == 1:
                    # Check if it's a known safe service or user process
                    safe_user_processes = {'python', 'python3', 'node', 'java', 'ruby'}
                    base_name = name.split('-')[0]  # Handle names like 'python3-'

                    if base_name not in safe_user_processes:
                        info['is_critical'] = True
                        info['safe_to_kill'] = False
                        info['reason'] = f'System service (parent is init/systemd)'
                        return info
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

        except Exception as e:
            info['reason'] = f'Error checking process: {e}'

        return info

    def _get_ai_warnings(self, proc: psutil.Process) -> Dict[str, Any]:
        """Generate warnings specific to AI/ML processes.

        Returns:
            dict: {
                'has_warnings': bool,
                'warnings': list of str,
                'data_loss_risk': str,  # 'high', 'medium', 'low'
            }
        """
        info = {
            'has_warnings': False,
            'warnings': [],
            'data_loss_risk': 'low'
        }

        try:
            name = proc.name().lower()
            cmdline = ' '.join(proc.cmdline()).lower()

            # Check if it's an AI process
            if not self.ai_monitor.is_ai_process(name, cmdline):
                return info

            # Check for training processes
            training_indicators = [
                'train', 'training', 'fit', 'learn',
                'torch.distributed', 'horovod', 'deepspeed',
                'wandb', 'mlflow', 'tensorboard'
            ]

            is_training = any(indicator in cmdline for indicator in training_indicators)

            if is_training:
                info['has_warnings'] = True
                info['data_loss_risk'] = 'high'
                info['warnings'].append(
                    'Training process - may lose unsaved model checkpoints'
                )

            # Check for distributed training
            distributed_indicators = [
                'distributed', 'ddp', 'horovod', 'mpi',
                'nccl', 'gloo', 'allreduce', 'world_size'
            ]

            is_distributed = any(indicator in cmdline for indicator in distributed_indicators)

            if is_distributed:
                info['has_warnings'] = True
                info['warnings'].append(
                    'Part of distributed job - other processes may hang'
                )
                if info['data_loss_risk'] == 'low':
                    info['data_loss_risk'] = 'medium'

            # Check for Jupyter notebooks
            if 'jupyter' in name or 'ipython' in name:
                info['has_warnings'] = True
                info['warnings'].append(
                    'Jupyter kernel - will disconnect notebook and lose unsaved work'
                )
                if info['data_loss_risk'] == 'low':
                    info['data_loss_risk'] = 'medium'

            # Check for inference servers
            server_indicators = [
                'serve', 'server', 'api', 'flask', 'fastapi',
                'torchserve', 'triton', 'seldon', 'uvicorn'
            ]

            is_server = any(indicator in cmdline for indicator in server_indicators)

            if is_server:
                info['has_warnings'] = True
                info['warnings'].append(
                    'Inference server - will disrupt active predictions/requests'
                )

        except Exception as e:
            self.logger.debug(f'Error checking AI warnings: {e}')

        return info

    def _get_signal_name(self, signal_num: int) -> str:
        """Get signal name from signal number."""
        for sig in self.SIGNALS:
            if sig['num'] == signal_num:
                return sig['name']
        return f'Signal {signal_num}'

    @classmethod
    def get_available_signals(cls) -> list:
        """Get list of available signals for the current platform.

        Returns:
            list of dict with signal information
        """
        return cls.SIGNALS.copy()
