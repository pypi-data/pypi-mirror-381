"""Run Diagnostics Use Case.

This use case handles system diagnostics and environment checks.
"""

import logging
import platform
import sys
from typing import Dict, Any, Optional

from ...domain.repositories.gpu_repository import GPURepository


class RunDiagnosticsUseCase:
    """Use case for running system diagnostics.

    This use case provides methods for checking system configuration,
    GPU availability, software requirements, and generating diagnostic reports.
    """

    def __init__(self,
                 gpu_repository: GPURepository,
                 logger: Optional[logging.Logger] = None):
        """Initialize the diagnostics use case.

        Args:
            gpu_repository: Repository for GPU device operations.
            logger: Logger for operations.
        """
        self._gpu_repository = gpu_repository
        self._logger = logger or logging.getLogger(__name__)

    def get_system_info(self) -> Dict[str, Any]:
        """Get comprehensive system information.

        Returns:
            Dict containing system information.
        """
        try:
            import psutil

            # Get CPU info
            cpu_info = {
                "physical_cores": psutil.cpu_count(logical=False),
                "logical_cores": psutil.cpu_count(logical=True),
                "cpu_freq_mhz": psutil.cpu_freq().current if psutil.cpu_freq() else 0
            }

            # Get memory info
            memory = psutil.virtual_memory()
            memory_info = {
                "total_gb": round(memory.total / (1024**3), 2),
                "available_gb": round(memory.available / (1024**3), 2),
                "used_percent": memory.percent
            }

            # Get platform info
            platform_info = {
                "system": platform.system(),
                "release": platform.release(),
                "version": platform.version(),
                "machine": platform.machine(),
                "processor": platform.processor(),
                "python_version": sys.version,
                "python_implementation": platform.python_implementation()
            }

            return {
                "platform": platform_info,
                "cpu": cpu_info,
                "memory": memory_info
            }

        except Exception as e:
            self._logger.error(f"Failed to get system info: {e}", exc_info=True)
            return {
                "error": str(e),
                "platform": {"system": platform.system()},
                "cpu": {},
                "memory": {}
            }

    def check_enhanced_monitoring_requirements(self) -> Dict[str, Any]:
        """Check if requirements for enhanced monitoring are met.

        Returns:
            Dict with requirement check results.
        """
        requirements = {
            "pytorch": {"available": False, "version": None},
            "cuda": {"available": False, "version": None},
            "pynvml": {"available": False, "version": None},
            "all_met": False
        }

        # Check PyTorch
        try:
            import torch
            requirements["pytorch"]["available"] = True
            requirements["pytorch"]["version"] = torch.__version__

            # Check CUDA
            if torch.cuda.is_available():
                requirements["cuda"]["available"] = True
                requirements["cuda"]["version"] = torch.version.cuda
        except ImportError:
            pass

        # Check pynvml
        try:
            import pynvml
            requirements["pynvml"]["available"] = True
            try:
                requirements["pynvml"]["version"] = pynvml.__version__
            except AttributeError:
                requirements["pynvml"]["version"] = "unknown"
        except ImportError:
            pass

        # Check if all requirements are met
        requirements["all_met"] = (
            requirements["pytorch"]["available"] and
            requirements["pynvml"]["available"]
        )

        return requirements

    def run_comprehensive_diagnostics(self) -> Dict[str, Any]:
        """Run comprehensive diagnostics.

        Returns:
            Dict containing all diagnostic information.
        """
        try:
            self._logger.info("Running comprehensive diagnostics...")

            # Get system info
            system_info = self.get_system_info()

            # Check enhanced monitoring requirements
            requirements = self.check_enhanced_monitoring_requirements()

            # Get GPU information
            gpu_info = self._get_gpu_diagnostics()

            # Check backend status
            backend_status = self._gpu_repository.get_backend_status() if hasattr(
                self._gpu_repository, 'get_backend_status') else {}

            return {
                "system": system_info,
                "requirements": requirements,
                "gpus": gpu_info,
                "backends": backend_status,
                "diagnostics_timestamp": self._get_timestamp()
            }

        except Exception as e:
            self._logger.error(f"Comprehensive diagnostics failed: {e}", exc_info=True)
            return {
                "error": str(e),
                "system": {},
                "requirements": {},
                "gpus": {},
                "backends": {}
            }

    def _get_gpu_diagnostics(self) -> Dict[str, Any]:
        """Get GPU diagnostic information.

        Returns:
            Dict containing GPU diagnostics.
        """
        try:
            devices = self._gpu_repository.get_available_devices()
            device_count = len(devices)

            gpu_list = []
            for device in devices:
                gpu_list.append({
                    "device_id": device.info.device_id,
                    "name": device.info.name,
                    "type": device.info.gpu_type.value,
                    "memory_total_mb": device.info.memory_total_mb,
                    "memory_used_mb": device.info.memory_used_mb,
                    "memory_available_mb": device.info.memory_available_mb,
                    "driver_version": device.info.driver_version,
                    "cuda_version": device.info.cuda_version,
                    "is_mock": device.info.is_mock,
                    "status": device.status.value,
                    "is_available": device.is_available()
                })

            return {
                "count": device_count,
                "devices": gpu_list
            }

        except Exception as e:
            self._logger.error(f"Failed to get GPU diagnostics: {e}")
            return {
                "count": 0,
                "devices": [],
                "error": str(e)
            }

    def _get_timestamp(self) -> str:
        """Get current timestamp in ISO format.

        Returns:
            ISO-formatted timestamp string.
        """
        from datetime import datetime
        return datetime.utcnow().isoformat()


class DiagnosticsError(Exception):
    """Exception raised when diagnostics operations fail."""
    pass