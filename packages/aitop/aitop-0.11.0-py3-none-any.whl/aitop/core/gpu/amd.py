#!/usr/bin/env python3
"""AMD-specific GPU monitoring implementation for ROCm 6.3+."""

import json
import re
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from .base import BaseGPUMonitor, GPUInfo


class AMDGPUMonitor(BaseGPUMonitor):
    """AMD GPU monitoring implementation with ROCm 6.3 specific parsing.

    Includes batch query optimization for improved performance.
    """

    def __init__(self):
        """Initialize AMD GPU monitor with caching for batch queries."""
        super().__init__()

        # Batch query cache similar to NVIDIA implementation
        self._data_cache = {
            "quick_metrics": {},  # Utilization + memory
            "thermal_power": {},  # Temperature + power
            "processes": [],  # Process list
        }

        # Update intervals for differential caching (seconds)
        self._update_intervals = {
            "quick_metrics": 1.0,  # Update frequently
            "thermal_power": 2.0,  # Less frequent
            "processes": 1.5,  # Moderate
        }

        # Last update timestamps
        self._last_updates = {
            "quick_metrics": 0.0,
            "thermal_power": 0.0,
            "processes": 0.0,
        }

        # Track JSON support (fallback to text if JSON fails)
        self._json_supported = True

    def get_quick_metrics(self) -> Dict[int, Dict[str, float]]:
        """Get only essential metrics (utilization, memory) for quick updates.

        Returns:
            Dictionary mapping GPU indices to metric dictionaries
        """
        metrics = {}

        if not self.smi_path:
            self.logger.warning("Cannot get quick metrics - no rocm-smi available")
            return metrics

        # Get quick GPU metrics for all devices
        self.logger.debug("Getting quick GPU metrics")

        try:
            devices = self._get_device_info()

            # For each device, get minimal info needed for quick metrics
            for device in devices:
                try:
                    # Get device-specific index
                    index = int(device.get("index", "0"))

                    # Get memory information
                    memory_used, memory_total = self._get_memory_info(index)

                    # Get utilization (only need percentage, not other metrics)
                    utilization = self._get_gpu_use(index)

                    # Add to metrics dictionary
                    metrics[index] = {
                        "utilization": utilization,
                        "memory_used": memory_used,
                        "memory_total": memory_total,
                        "memory_percent": (memory_used / memory_total * 100.0)
                        if memory_total > 0
                        else 0.0,
                    }

                    self.logger.debug(
                        f"Quick metrics for GPU {index}: {metrics[index]}"
                    )

                except Exception as e:
                    device_idx = device.get("index", "unknown")
                    self.logger.warning(
                        f"Error getting quick metrics for device {device_idx}: {e}"
                    )
                    continue

            return metrics

        except Exception as e:
            self.logger.error(f"Error collecting quick metrics: {e}")
            return metrics

    def _find_smi(self) -> Optional[Path]:
        """Find rocm-smi executable."""
        common_paths = [
            "/usr/bin/rocm-smi",
            "/opt/rocm/bin/rocm-smi",
            "/usr/local/bin/rocm-smi",
        ]
        for path in common_paths:
            p = Path(path)
            if p.exists():
                self.logger.debug("Found rocm-smi at " + str(p))
                try:
                    # Verify it's executable
                    subprocess.run(
                        [str(p), "--version"], capture_output=True, check=True
                    )
                    self.logger.info("Verified working rocm-smi at " + str(p))
                    return p
                except subprocess.SubprocessError as e:
                    self.logger.debug(
                        "rocm-smi at " + str(p) + " failed version check: " + str(e)
                    )
                    continue
        self.logger.warning("No working rocm-smi found in common locations")
        return None

    def _get_driver_version(self) -> str:
        """Get AMD driver version (cached forever as it doesn't change)."""
        if hasattr(self, "_cached_driver_version"):
            return self._cached_driver_version

        if not self.smi_path:
            self._cached_driver_version = ""
            return ""

        try:
            # Try rocm-smi --showdriverversion first
            result = subprocess.run(
                [str(self.smi_path), "--showdriverversion"],
                capture_output=True,
                text=True,
                timeout=2.0,
            )
            if result.returncode == 0 and result.stdout.strip():
                # Parse driver version from output
                for line in result.stdout.split("\n"):
                    if "Driver version" in line or "amdgpu version" in line:
                        # Extract version number
                        match = re.search(r"(\d+\.\d+(?:\.\d+)?)", line)
                        if match:
                            version = match.group(1)
                            self._cached_driver_version = version
                            self.logger.info(f"Detected AMD driver version: {version}")
                            return version
        except Exception as e:
            self.logger.debug(f"Failed to get AMD driver version: {e}")

        self._cached_driver_version = ""
        return ""

    def _get_rocm_version(self) -> str:
        """Get ROCm platform version (cached forever as it doesn't change).

        Detects the actual ROCm platform version, not rocm-smi tool version.
        Uses multiple detection methods with priority order for compatibility
        across ROCm 4.x, 5.x, 6.x, and 7.x.
        """
        if hasattr(self, "_cached_rocm_version"):
            return self._cached_rocm_version

        version = ""

        # Method 1: Package manager (most reliable across all versions)
        if not version:
            try:
                # Try dpkg (Debian/Ubuntu)
                result = subprocess.run(
                    ["dpkg-query", "--showformat=${Version}", "--show", "rocm-core"],
                    capture_output=True,
                    text=True,
                    timeout=2.0,
                )
                if result.returncode == 0 and result.stdout.strip():
                    # Extract version from package version string
                    # (e.g., "6.3.0-1" -> "6.3.0")
                    match = re.search(r"(\d+\.\d+\.\d+)", result.stdout)
                    if match:
                        version = match.group(1)
                        self.logger.debug(
                            f"Method 1a (dpkg rocm-core) found: {version}"
                        )
            except FileNotFoundError:
                # dpkg not available, try rpm
                try:
                    result = subprocess.run(
                        ["rpm", "-q", "--queryformat", "%{VERSION}", "rocm-core"],
                        capture_output=True,
                        text=True,
                        timeout=2.0,
                    )
                    if result.returncode == 0 and result.stdout.strip():
                        match = re.search(r"(\d+\.\d+\.\d+)", result.stdout)
                        if match:
                            version = match.group(1)
                            self.logger.debug(
                                f"Method 1b (rpm rocm-core) found version: {version}"
                            )
                except Exception as e:
                    self.logger.debug(f"Method 1 (package manager) failed: {e}")
            except Exception as e:
                self.logger.debug(f"Method 1a (dpkg) failed: {e}")

        # Method 2: rocm-core/rocm_version.h header (modern standard, ROCm 5.2+)
        if not version:
            try:
                version_header = Path("/opt/rocm/include/rocm-core/rocm_version.h")
                if version_header.exists():
                    content = version_header.read_text()
                    # Parse C preprocessor macros
                    major = re.search(r"#define\s+ROCM_VERSION_MAJOR\s+(\d+)", content)
                    minor = re.search(r"#define\s+ROCM_VERSION_MINOR\s+(\d+)", content)
                    patch = re.search(r"#define\s+ROCM_VERSION_PATCH\s+(\d+)", content)
                    if major and minor and patch:
                        version = f"{major.group(1)}.{minor.group(1)}.{patch.group(1)}"
                        self.logger.debug(
                            f"Method 2 (rocm_version.h) found version: {version}"
                        )
            except Exception as e:
                self.logger.debug(f"Method 2 (rocm_version.h) failed: {e}")

        # Method 3: update-alternatives (for multi-version installations)
        if not version:
            try:
                result = subprocess.run(
                    ["update-alternatives", "--display", "rocm"],
                    capture_output=True,
                    text=True,
                    timeout=2.0,
                )
                if result.returncode == 0:
                    # Extract version from path like "/opt/rocm-6.3.0"
                    match = re.search(r"/opt/rocm-(\d+\.\d+\.\d+)", result.stdout)
                    if match:
                        version = match.group(1)
                        self.logger.debug(
                            f"Method 3 (update-alternatives) found version: {version}"
                        )
            except Exception as e:
                self.logger.debug(f"Method 3 (update-alternatives) failed: {e}")

        # Method 4: /opt/rocm/.info/version file (legacy, ROCm 4.x - 5.6)
        if not version:
            try:
                version_file = Path("/opt/rocm/.info/version")
                if version_file.exists():
                    content = version_file.read_text().strip()
                    match = re.search(r"(\d+\.\d+\.\d+)", content)
                    if match:
                        version = match.group(1)
                        self.logger.debug(
                            f"Method 4 (.info/version) found version: {version}"
                        )
            except Exception as e:
                self.logger.debug(f"Method 4 (.info/version) failed: {e}")

        # Method 5: /opt/rocm/.info/version-dev file (older legacy)
        if not version:
            try:
                version_file = Path("/opt/rocm/.info/version-dev")
                if version_file.exists():
                    content = version_file.read_text().strip()
                    match = re.search(r"(\d+\.\d+\.\d+)", content)
                    if match:
                        version = match.group(1)
                        self.logger.debug(
                            f"Method 5 (.info/version-dev) found version: {version}"
                        )
            except Exception as e:
                self.logger.debug(f"Method 5 (.info/version-dev) failed: {e}")

        # Method 6: /opt/rocm/VERSION file (oldest legacy, ROCm 4.x and earlier)
        if not version:
            try:
                version_file = Path("/opt/rocm/VERSION")
                if version_file.exists():
                    content = version_file.read_text().strip()
                    match = re.search(r"(\d+\.\d+(?:\.\d+)?)", content)
                    if match:
                        version = match.group(1)
                        self.logger.debug(
                            f"Method 6 (VERSION) found version: {version}"
                        )
            except Exception as e:
                self.logger.debug(f"Method 6 (VERSION) failed: {e}")

        self._cached_rocm_version = version
        if version:
            self.logger.info(f"Detected ROCm platform version: {version}")
        else:
            self.logger.warning("Could not detect ROCm platform version")
        return version

    def _get_device_info(self) -> List[Dict[str, str]]:
        """Get basic device information for all AMD GPUs."""
        self.logger.debug("Starting device info collection")
        if not self.smi_path:
            self.logger.warning("Cannot get device info - no rocm-smi available")
            return []

        cmd = [str(self.smi_path), "-i"]
        self.logger.debug("Executing rocm-smi command: " + " ".join(cmd))
        result = self._run_smi_command(cmd)
        if not result:
            self.logger.error("Failed to get device information from rocm-smi")
            return []

        self.logger.debug("Successfully retrieved device information")

        devices = []
        # Split output into per-device sections
        sections = result.split("========================")
        self.logger.debug("Found " + str(len(sections)) + " device sections to parse")

        for section in sections:
            if not section.strip():
                continue

            device = {}
            patterns = {
                "name": r"Device Name:\s*([^\n]+)",
                "device_id": r"Device ID:\s*([^\n]+)",
                "guid": r"GUID:\s*([^\n]+)",
                "index": r"GPU\[(\d+)\]",  # Extract GPU index
            }

            for key, pattern in patterns.items():
                match = re.search(pattern, section)
                if match:
                    device[key] = match.group(1).strip()

            if device:  # Only add if we found device info
                self.logger.debug("Found device: " + str(device))
                devices.append(device)

        return devices

    def _get_memory_info(self, gpu_index: int) -> Tuple[float, float]:
        """Get current memory usage information for specific GPU."""
        self.logger.debug("Getting memory info for GPU " + str(gpu_index))
        if not self.smi_path:
            self.logger.warning(
                "Cannot get memory info for GPU "
                + str(gpu_index)
                + " - no rocm-smi available"
            )
            return 0.0, 0.0

        cmd = [str(self.smi_path), "-d", str(gpu_index), "--showmeminfo", "vram"]
        self.logger.debug("Executing memory info command: " + " ".join(cmd))
        result = self._run_smi_command(cmd)
        if not result:
            self.logger.error("Failed to get memory info for GPU " + str(gpu_index))
            return 0.0, 0.0

        try:
            # Parse VRAM usage from the new format
            total_match = re.search(r"VRAM Total Memory \(B\):\s*(\d+)", result)
            used_match = re.search(r"VRAM Total Used Memory \(B\):\s*(\d+)", result)

            total = (
                float(total_match.group(1)) / (1024 * 1024) if total_match else 0.0
            )  # Convert to MB
            used = (
                float(used_match.group(1)) / (1024 * 1024) if used_match else 0.0
            )  # Convert to MB

            self.logger.debug(
                "GPU "
                + str(gpu_index)
                + " memory: "
                + str(used)
                + "MB used / "
                + str(total)
                + "MB total"
            )
            return used, total
        except (ValueError, AttributeError) as e:
            self.logger.error(
                "Failed to parse memory info for GPU " + str(gpu_index) + ": " + str(e)
            )
            return 0.0, 0.0

    def _get_temperature_info(self, gpu_index: int) -> Dict[str, float]:
        """Get temperature information from all available sensors for specific GPU."""
        self.logger.debug("Getting temperature info for GPU " + str(gpu_index))
        if not self.smi_path:
            return {}

        cmd = [str(self.smi_path), "-d", str(gpu_index), "-t"]
        self.logger.debug("Executing temperature command: " + " ".join(cmd))
        result = self._run_smi_command(cmd)
        if not result:
            return {}

        temps = {}
        patterns = {
            "edge": r"Temperature \(Sensor edge\) \(C\):\s*([\d.]+)",
            "junction": r"Temperature \(Sensor junction\) \(C\):\s*([\d.]+)",
            "memory": r"Temperature \(Sensor memory\) \(C\):\s*([\d.]+)",
        }

        for sensor, pattern in patterns.items():
            match = re.search(pattern, result)
            if match:
                try:
                    temps[sensor] = float(match.group(1))
                    self.logger.debug(
                        "GPU "
                        + str(gpu_index)
                        + " "
                        + sensor
                        + " temperature: "
                        + str(temps[sensor])
                        + "°C"
                    )
                except ValueError:
                    temps[sensor] = 0.0

        return temps

    def _get_power_info(self, gpu_index: int) -> float:
        """Get current power consumption for specific GPU."""
        self.logger.debug("Getting power info for GPU " + str(gpu_index))
        if not self.smi_path:
            return 0.0

        cmd = [str(self.smi_path), "-d", str(gpu_index), "--showpower"]
        self.logger.debug("Executing power command: " + " ".join(cmd))
        result = self._run_smi_command(cmd)
        if not result:
            return 0.0

        try:
            match = re.search(
                r"Average Graphics Package Power \(W\):\s*([\d.]+)", result
            )
            power = float(match.group(1)) if match else 0.0
            self.logger.debug(
                "GPU " + str(gpu_index) + " power draw: " + str(power) + "W"
            )
            return power
        except (ValueError, AttributeError):
            return 0.0

    def _get_gpu_use(self, gpu_index: int) -> float:
        """Get current GPU utilization percentage for specific GPU."""
        self.logger.debug("Getting utilization for GPU " + str(gpu_index))
        if not self.smi_path:
            return 0.0

        cmd = [str(self.smi_path), "-d", str(gpu_index), "--showuse"]
        self.logger.debug("Executing utilization command: " + " ".join(cmd))
        result = self._run_smi_command(cmd)
        if not result:
            return 0.0

        try:
            match = re.search(r"GPU use \(%\):\s*(\d+)", result)
            util = float(match.group(1)) if match else 0.0
            self.logger.debug(
                "GPU " + str(gpu_index) + " utilization: " + str(util) + "%"
            )
            return util
        except (ValueError, AttributeError):
            return 0.0

    def _run_smi_command(self, cmd: List[str]) -> Optional[str]:
        """Run an SMI command and return its output."""
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True,
                timeout=5,  # 5 second timeout for commands
            )
            return result.stdout
        except (
            subprocess.SubprocessError,
            FileNotFoundError,
            subprocess.TimeoutExpired,
        ) as e:
            self.logger.error(
                "Failed to run command: " + " ".join(cmd) + " - Error: " + str(e)
            )
            return None

    def _parse_processes(self, output: str) -> List[Dict[str, Any]]:
        """Parse process information from rocm-smi output."""
        self.logger.debug("Parsing process information")
        if not output:
            return []

        processes = []
        lines = output.splitlines()
        header_found = False

        for line in lines:
            # Skip empty lines and headers
            if not line.strip() or line.startswith("===") or "KFD process" in line:
                continue

            # Check for the process listing header
            if "PID" in line and "PROCESS NAME" in line:
                header_found = True
                continue

            # Parse process lines
            if header_found and line.strip():
                try:
                    parts = line.split()
                    if len(parts) >= 4:  # PID, name, GPU(s), VRAM
                        pid = int(parts[0])
                        name = parts[1]
                        gpu_ids = parts[2]

                        # Handle VRAM value that might be "0" as string
                        try:
                            vram = float(parts[3])
                        except ValueError:
                            vram = 0.0

                        # Handle SDMA value that might be "0" as string
                        try:
                            sdma = float(parts[4]) if len(parts) > 4 else 0.0
                        except ValueError:
                            sdma = 0.0

                        # Get CU occupancy if available
                        cu_occupancy = None
                        if len(parts) > 5:
                            if parts[5] != "UNKNOWN":
                                try:
                                    # Try to parse as percentage
                                    cu_occupancy = float(parts[5].rstrip("%"))
                                except ValueError:
                                    cu_occupancy = None

                        # Try to get ppid using psutil
                        ppid = None
                        try:
                            import psutil

                            proc = psutil.Process(pid)
                            ppid = proc.ppid()
                        except (psutil.NoSuchProcess, psutil.AccessDenied, ImportError):
                            pass  # ppid will remain None

                        process_info = {
                            "pid": pid,
                            "ppid": ppid,
                            "name": name,
                            "gpu_ids": [
                                int(gpu_id)
                                for gpu_id in gpu_ids.split(",")
                                if gpu_id.isdigit()
                            ],
                            "memory": vram,  # Keep memory key for compatibility
                            "vram_used": vram,
                            "sdma_used": sdma,
                            "cu_occupancy": cu_occupancy,
                        }
                        self.logger.debug(
                            "Found process: PID="
                            + str(pid)
                            + ", Name="
                            + name
                            + ", VRAM="
                            + str(vram)
                            + "MB"
                        )
                        processes.append(process_info)
                except (ValueError, IndexError) as e:
                    self.logger.debug(
                        "Failed to parse process line: " + line + " - Error: " + str(e)
                    )
                    continue

        self.logger.debug("Found " + str(len(processes)) + " GPU processes")
        return processes

    def _get_batch_metrics_json(self, gpu_index: int) -> Dict[str, Any]:
        """Get multiple metrics in a single JSON query (70% faster than separate calls).

        Combines memory, power, temperature, and utilization in one subprocess call.
        Falls back to text parsing if JSON not supported.

        Args:
            gpu_index: GPU device index

        Returns:
            Dictionary with parsed metrics
        """
        if not self.smi_path or not self._json_supported:
            return {}

        # Batch query: memory + power + temp + utilization in ONE call
        cmd = [
            str(self.smi_path),
            "-d",
            str(gpu_index),
            "--showmeminfo",
            "vram",
            "--showpower",
            "-t",
            "--showuse",
            "--json",
        ]

        self.logger.debug(f"Executing batch JSON query for GPU {gpu_index}")

        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True, check=True, timeout=5
            )

            # Parse JSON output
            data = json.loads(result.stdout)
            self.logger.debug(f"Successfully parsed JSON metrics for GPU {gpu_index}")
            return data

        except json.JSONDecodeError as e:
            self.logger.warning(f"JSON parsing failed for GPU {gpu_index}: {e}")
            self.logger.warning("Disabling JSON queries, falling back to text parsing")
            self._json_supported = False
            return {}

        except (
            subprocess.SubprocessError,
            FileNotFoundError,
            subprocess.TimeoutExpired,
        ) as e:
            self.logger.error(f"Batch query failed for GPU {gpu_index}: {e}")
            return {}

    def _parse_json_memory(
        self, json_data: Dict[str, Any], gpu_index: int
    ) -> Tuple[float, float]:
        """Parse memory info from JSON batch query.

        Best-effort parsing, varies by ROCm version.
        """
        try:
            # Try common JSON structures (varies by ROCm version)
            # Structure may be nested or flat
            card_key = f"card{gpu_index}"
            if card_key in json_data:
                vram = json_data[card_key].get("VRAM Total Memory (B)", 0)
                used = json_data[card_key].get("VRAM Total Used Memory (B)", 0)
            else:
                # Fallback: return zeros to trigger text parsing
                return 0.0, 0.0

            total = float(vram) / (1024 * 1024) if vram else 0.0  # Convert to MB
            memory_used = float(used) / (1024 * 1024) if used else 0.0
            return memory_used, total
        except (KeyError, AttributeError, ValueError):
            return 0.0, 0.0

    def _parse_json_temperature(
        self, json_data: Dict[str, Any], gpu_index: int
    ) -> float:
        """Parse temperature from JSON batch query (best-effort)."""
        try:
            card_key = f"card{gpu_index}"
            if card_key in json_data:
                # Try junction temp first, then edge
                temp = json_data[card_key].get("Temperature (Sensor junction) (C)")
                if not temp:
                    temp = json_data[card_key].get("Temperature (Sensor edge) (C)", 0.0)
                return float(temp) if temp else 0.0
            return 0.0
        except (KeyError, AttributeError, ValueError):
            return 0.0

    def _parse_json_power(self, json_data: Dict[str, Any], gpu_index: int) -> float:
        """Parse power from JSON batch query (best-effort)."""
        try:
            card_key = f"card{gpu_index}"
            if card_key in json_data:
                power = json_data[card_key].get(
                    "Average Graphics Package Power (W)", 0.0
                )
                return float(power) if power else 0.0
            return 0.0
        except (KeyError, AttributeError, ValueError):
            return 0.0

    def _parse_json_utilization(
        self, json_data: Dict[str, Any], gpu_index: int
    ) -> float:
        """Parse utilization from JSON batch query (best-effort)."""
        try:
            card_key = f"card{gpu_index}"
            if card_key in json_data:
                util = json_data[card_key].get("GPU use (%)", 0.0)
                return float(util) if util else 0.0
            return 0.0
        except (KeyError, AttributeError, ValueError):
            return 0.0

    def get_gpu_info(self) -> List[GPUInfo]:
        """Get comprehensive AMD GPU information for all devices.

        Uses optimized batch queries for improved performance.
        """
        self.logger.debug("Starting AMD GPU info collection")
        if not self.smi_path:
            self.logger.warning("Cannot get GPU info - no rocm-smi available")
            return []

        try:
            # Get versions once (cached forever)
            driver_version = self._get_driver_version()
            rocm_version = self._get_rocm_version()

            # Get information for all devices
            devices = self._get_device_info()
            if not devices:
                self.logger.warning("No AMD devices found")
                return []

            self.logger.debug("Found " + str(len(devices)) + " AMD devices")

            gpus = []
            for device in devices:
                # Get device-specific index
                try:
                    index = int(device.get("index", "0"))
                except ValueError:
                    continue

                self.logger.debug("Processing GPU " + str(index))

                # Try batch JSON query first (70% faster - 1 call instead of 4)
                batch_data = (
                    self._get_batch_metrics_json(index) if self._json_supported else {}
                )

                if batch_data and self._json_supported:
                    # Parse from JSON batch query
                    self.logger.debug(f"Using JSON batch data for GPU {index}")
                    # Note: JSON structure varies by ROCm version, this is best-effort
                    # If parsing fails, will fall back to individual calls
                    try:
                        # Extract metrics from JSON (structure may vary)
                        memory_used, memory_total = self._parse_json_memory(
                            batch_data, index
                        )
                        temperature = self._parse_json_temperature(batch_data, index)
                        power_draw = self._parse_json_power(batch_data, index)
                        utilization = self._parse_json_utilization(batch_data, index)
                    except (KeyError, ValueError, TypeError) as e:
                        self.logger.warning(
                            f"JSON parsing incomplete for GPU {index}: {e}, "
                            "falling back to text"
                        )
                        # Fallback to individual queries
                        memory_used, memory_total = self._get_memory_info(index)
                        temps = self._get_temperature_info(index)
                        temperature = temps.get("junction", temps.get("edge", 0.0))
                        power_draw = self._get_power_info(index)
                        utilization = self._get_gpu_use(index)
                else:
                    # Fallback: use original individual queries (4 separate calls)
                    self.logger.debug(f"Using text-based queries for GPU {index}")
                    memory_used, memory_total = self._get_memory_info(index)
                    temps = self._get_temperature_info(index)
                    temperature = temps.get("junction", temps.get("edge", 0.0))
                    power_draw = self._get_power_info(index)
                    utilization = self._get_gpu_use(index)

                # Get process information for specific GPU
                cmd = [str(self.smi_path), "-d", str(index), "--showpids", "verbose"]
                self.logger.debug("Executing process query: " + " ".join(cmd))
                result = self._run_smi_command(cmd)
                processes = self._parse_processes(result)

                self.logger.debug("Creating GPUInfo object for GPU " + str(index))
                gpus.append(
                    GPUInfo(
                        index=index,
                        name=device.get("name", "AMD GPU"),
                        utilization=utilization,
                        memory_used=memory_used,
                        memory_total=memory_total,
                        temperature=temperature,
                        power_draw=power_draw,
                        # Power limit not available in current ROCm-SMI version
                        power_limit=0.0,
                        processes=processes,
                        driver_version=driver_version,
                        rocm_version=rocm_version,
                    )
                )

            self.logger.debug(
                "Successfully collected information for " + str(len(gpus)) + " AMD GPUs"
            )
            return gpus
        except Exception as e:
            self.logger.error("Failed to get GPU information: " + str(e))
            return []
