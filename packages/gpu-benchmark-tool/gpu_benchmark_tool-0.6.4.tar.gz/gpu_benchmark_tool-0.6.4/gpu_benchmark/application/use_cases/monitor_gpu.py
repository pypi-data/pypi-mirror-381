"""Monitor GPU Use Case.

This use case handles real-time GPU monitoring operations.
"""

import logging
import time
from typing import Dict, Any, Optional
from datetime import datetime

from ...domain.repositories.gpu_repository import GPURepository
from ...domain.models.gpu_device import GPUMetrics


class MonitorGPUUseCase:
    """Use case for real-time GPU monitoring.

    This use case provides methods for monitoring GPU metrics in real-time,
    collecting telemetry data, and tracking GPU performance over time.
    """

    def __init__(self,
                 gpu_repository: GPURepository,
                 logger: Optional[logging.Logger] = None):
        """Initialize the monitor use case.

        Args:
            gpu_repository: Repository for GPU device operations.
            logger: Logger for operations.
        """
        self._gpu_repository = gpu_repository
        self._logger = logger or logging.getLogger(__name__)

    def get_current_metrics(self, device_id: int) -> Dict[str, Any]:
        """Get current GPU metrics.

        Args:
            device_id: GPU device ID to monitor.

        Returns:
            Dict containing current GPU metrics.
        """
        try:
            # Get device
            device = self._gpu_repository.get_device_by_id(device_id)
            if not device:
                raise MonitorError(f"Device {device_id} not found")

            # Refresh metrics from hardware
            if hasattr(self._gpu_repository, 'refresh_device_metrics'):
                metrics = self._gpu_repository.refresh_device_metrics(device_id)
            else:
                metrics = device.current_metrics

            if not metrics:
                return {
                    "device_id": device_id,
                    "device_name": device.info.name,
                    "error": "No metrics available"
                }

            return {
                "device_id": device_id,
                "device_name": device.info.name,
                "gpu_type": device.info.gpu_type.value,
                "timestamp": metrics.timestamp.isoformat(),
                "temperature_celsius": metrics.temperature_celsius,
                "power_usage_watts": metrics.power_usage_watts,
                "utilization_percent": metrics.utilization_percent,
                "fan_speed_percent": metrics.fan_speed_percent,
                "clock_speed_mhz": metrics.clock_speed_mhz,
                "memory_clock_mhz": metrics.memory_clock_mhz,
                "memory_used_mb": device.info.memory_used_mb,
                "memory_total_mb": device.info.memory_total_mb,
                "memory_usage_percent": device.info.memory_usage_percent,
                "status": device.status.value,
                "thermal_throttling_risk": device.get_thermal_throttling_risk(),
                "power_efficiency_score": device.get_power_efficiency_score()
            }

        except Exception as e:
            self._logger.error(f"Failed to get current metrics: {e}", exc_info=True)
            raise MonitorError(f"Failed to get current metrics: {e}") from e

    def monitor_continuous(self,
                          device_id: int,
                          duration_seconds: int = 60,
                          sample_interval: float = 1.0) -> Dict[str, Any]:
        """Monitor GPU continuously for a period of time.

        Args:
            device_id: GPU device ID to monitor.
            duration_seconds: How long to monitor (seconds).
            sample_interval: Time between samples (seconds).

        Returns:
            Dict containing monitoring results with telemetry history.
        """
        try:
            device = self._gpu_repository.get_device_by_id(device_id)
            if not device:
                raise MonitorError(f"Device {device_id} not found")

            self._logger.info(f"Starting continuous monitoring of device {device_id} for {duration_seconds}s")

            telemetry = []
            start_time = time.time()
            end_time = start_time + duration_seconds

            while time.time() < end_time:
                try:
                    # Get current metrics
                    metrics_dict = self.get_current_metrics(device_id)

                    # Store telemetry sample
                    telemetry.append({
                        "timestamp": datetime.utcnow().isoformat(),
                        "elapsed_seconds": time.time() - start_time,
                        **metrics_dict
                    })

                    # Wait for next sample
                    time.sleep(sample_interval)

                except Exception as e:
                    self._logger.warning(f"Failed to collect sample: {e}")
                    continue

            # Calculate statistics
            stats = self._calculate_monitoring_statistics(telemetry)

            return {
                "device_id": device_id,
                "device_name": device.info.name,
                "duration_seconds": duration_seconds,
                "sample_count": len(telemetry),
                "sample_interval": sample_interval,
                "telemetry": telemetry,
                "statistics": stats
            }

        except Exception as e:
            self._logger.error(f"Continuous monitoring failed: {e}", exc_info=True)
            raise MonitorError(f"Continuous monitoring failed: {e}") from e

    def _calculate_monitoring_statistics(self, telemetry: list) -> Dict[str, Any]:
        """Calculate statistics from telemetry data.

        Args:
            telemetry: List of telemetry samples.

        Returns:
            Dict containing statistics.
        """
        if not telemetry:
            return {}

        temps = [s.get("temperature_celsius", 0) for s in telemetry if s.get("temperature_celsius")]
        powers = [s.get("power_usage_watts", 0) for s in telemetry if s.get("power_usage_watts")]
        utils = [s.get("utilization_percent", 0) for s in telemetry if s.get("utilization_percent")]

        stats = {
            "temperature": {
                "min": min(temps) if temps else 0,
                "max": max(temps) if temps else 0,
                "avg": sum(temps) / len(temps) if temps else 0
            },
            "power": {
                "min": min(powers) if powers else 0,
                "max": max(powers) if powers else 0,
                "avg": sum(powers) / len(powers) if powers else 0
            },
            "utilization": {
                "min": min(utils) if utils else 0,
                "max": max(utils) if utils else 0,
                "avg": sum(utils) / len(utils) if utils else 0
            }
        }

        return stats


class MonitorError(Exception):
    """Exception raised when monitoring operations fail."""
    pass