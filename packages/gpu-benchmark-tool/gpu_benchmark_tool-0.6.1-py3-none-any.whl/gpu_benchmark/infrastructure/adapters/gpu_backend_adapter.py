"""GPU Backend Adapter.

This adapter bridges the existing GPU backends with the new domain architecture.
"""

import logging
from typing import List, Optional, Dict, Any
from datetime import datetime

from ...domain.repositories.gpu_repository import GPURepository
from ...domain.models.gpu_device import GPUDevice, GPUInfo, GPUMetrics, GPUType, GPUStatus
from ...domain.error_handling.error_boundary import GPUErrorBoundary
from ...domain.error_handling.error_types import GPUAccessError, ErrorType


class GPUBackendAdapter(GPURepository):
    """Adapter that wraps existing GPU backends with the new domain interface.
    
    This adapter provides a clean interface to the existing GPU backend system
    while maintaining compatibility with the new domain-driven architecture.
    """
    
    def __init__(self, 
                 backend_factory,
                 logger: Optional[logging.Logger] = None,
                 error_boundary: Optional[GPUErrorBoundary] = None):
        """Initialize the GPU backend adapter.
        
        Args:
            backend_factory: Factory for creating GPU backends.
            logger: Logger for operations.
            error_boundary: Error boundary for graceful error handling.
        """
        self._backend_factory = backend_factory
        self._logger = logger or logging.getLogger(__name__)
        self._error_boundary = error_boundary or GPUErrorBoundary(self._logger)
        self._backends: Dict[str, Any] = {}
        self._devices: Dict[int, GPUDevice] = {}
        self._initialized = False
    
    def _ensure_initialized(self) -> None:
        """Ensure the adapter is initialized with available backends."""
        if self._initialized:
            return
        
        try:
            self._initialize_backends()
            self._initialized = True
        except Exception as e:
            self._logger.error(f"Failed to initialize GPU backends: {e}")
            raise GPUAccessError(f"GPU backend initialization failed: {e}", error_type=ErrorType.CRITICAL)
    
    def _initialize_backends(self) -> None:
        """Initialize available GPU backends."""
        self._logger.info("Initializing GPU backends...")
        
        # Get available backends from factory
        available_backends = self._backend_factory.get_available_backends()
        
        for backend_name, backend in available_backends.items():
            if backend.is_available():
                self._backends[backend_name] = backend
                self._logger.info(f"Initialized {backend_name} backend")
                
                # Discover devices for this backend
                self._discover_devices_for_backend(backend_name, backend)
            else:
                self._logger.warning(f"{backend_name} backend not available")
        
        if not self._backends:
            self._logger.warning("No GPU backends available, using mock mode")
            self._create_mock_device()
    
    def _discover_devices_for_backend(self, backend_name: str, backend) -> None:
        """Discover devices for a specific backend."""
        try:
            device_count = backend.get_device_count()
            self._logger.info(f"Found {device_count} devices in {backend_name} backend")
            
            for device_id in range(device_count):
                try:
                    device_info = backend.get_device_info(device_id)
                    gpu_device = self._create_gpu_device_from_backend_info(
                        device_info, backend_name, device_id
                    )
                    self._devices[device_id] = gpu_device
                    self._logger.debug(f"Discovered device {device_id}: {gpu_device.info.name}")
                    
                except Exception as e:
                    self._logger.warning(f"Failed to get info for device {device_id}: {e}")
                    
        except Exception as e:
            self._logger.error(f"Failed to discover devices for {backend_name}: {e}")
    
    def _create_gpu_device_from_backend_info(self, 
                                           device_info: Dict[str, Any], 
                                           backend_name: str, 
                                           device_id: int) -> GPUDevice:
        """Create a GPUDevice from backend device info."""
        # Map backend name to GPU type
        gpu_type_map = {
            "nvidia": GPUType.NVIDIA,
            "amd": GPUType.AMD,
            "intel": GPUType.INTEL,
            "mock": GPUType.MOCK
        }
        
        gpu_type = gpu_type_map.get(backend_name, GPUType.UNKNOWN)
        
        # Extract device information
        name = device_info.get("name", f"Unknown {backend_name} GPU")
        memory_total = device_info.get("memory_total_mb", 0)
        memory_used = device_info.get("memory_used_mb", 0)
        driver_version = device_info.get("driver_version")
        cuda_version = device_info.get("cuda_version")
        
        # Create GPU info
        gpu_info = GPUInfo(
            name=name,
            device_id=device_id,
            gpu_type=gpu_type,
            memory_total_mb=memory_total,
            memory_used_mb=memory_used,
            driver_version=driver_version,
            cuda_version=cuda_version,
            is_mock=(backend_name == "mock")
        )

        # Create initial metrics for the device
        # These will be updated when actual monitoring happens
        initial_metrics = GPUMetrics(
            temperature_celsius=0.0,
            power_usage_watts=0.0,
            utilization_percent=0.0,
            fan_speed_percent=0.0,
            clock_speed_mhz=0.0,
            memory_clock_mhz=0.0
        )

        # Create GPU device with initial metrics
        gpu_device = GPUDevice(
            info=gpu_info,
            current_metrics=initial_metrics,
            status=GPUStatus.UNKNOWN
        )

        return gpu_device
    
    def _create_mock_device(self) -> None:
        """Create a mock device when no real GPUs are available."""
        mock_info = GPUInfo(
            name="Mock GPU (No real GPUs detected)",
            device_id=0,
            gpu_type=GPUType.MOCK,
            memory_total_mb=8192,
            memory_used_mb=0,
            driver_version="Mock Driver",
            cuda_version="Mock CUDA",
            is_mock=True
        )
        
        mock_metrics = GPUMetrics(
            temperature_celsius=45.0,
            power_usage_watts=0.0,
            utilization_percent=0.0,
            fan_speed_percent=0.0,
            clock_speed_mhz=0.0,
            memory_clock_mhz=0.0
        )
        
        mock_device = GPUDevice(
            info=mock_info,
            current_metrics=mock_metrics,
            status=GPUStatus.HEALTHY
        )
        
        self._devices[0] = mock_device
        self._logger.info("Created mock GPU device")
    
    def get_available_devices(self) -> List[GPUDevice]:
        """Get all available GPU devices."""
        self._ensure_initialized()
        return list(self._devices.values())
    
    def get_device_by_id(self, device_id: int) -> Optional[GPUDevice]:
        """Get a specific GPU device by ID."""
        self._ensure_initialized()
        return self._devices.get(device_id)
    
    def get_device_count(self) -> int:
        """Get the number of available GPU devices."""
        self._ensure_initialized()
        return len(self._devices)
    
    def update_device_metrics(self, device_id: int, metrics: GPUMetrics) -> None:
        """Update metrics for a specific GPU device."""
        self._ensure_initialized()
        
        if device_id not in self._devices:
            raise GPUAccessError(f"Device {device_id} not found", gpu_id=device_id)
        
        if not metrics.is_valid():
            raise ValueError("Invalid GPU metrics provided")
        
        device = self._devices[device_id]
        device.update_metrics(metrics)
        
        self._logger.debug(f"Updated metrics for device {device_id}")
    
    def is_device_available(self, device_id: int) -> bool:
        """Check if a GPU device is available."""
        self._ensure_initialized()
        
        device = self._devices.get(device_id)
        return device is not None and device.is_available()
    
    def get_device_capabilities(self, device_id: int) -> Dict[str, Any]:
        """Get capabilities of a specific GPU device."""
        self._ensure_initialized()
        
        device = self._devices.get(device_id)
        if not device:
            raise GPUAccessError(f"Device {device_id} not found", gpu_id=device_id)
        
        return {
            "gpu_type": device.info.gpu_type.value,
            "memory_total_mb": device.info.memory_total_mb,
            "memory_available_mb": device.info.memory_available_mb,
            "driver_version": device.info.driver_version,
            "cuda_version": device.info.cuda_version,
            "is_mock": device.info.is_mock,
            "status": device.status.value,
            "is_available": device.is_available(),
            "thermal_throttling_risk": device.get_thermal_throttling_risk(),
            "power_efficiency_score": device.get_power_efficiency_score()
        }
    
    def save_device_profile(self, device: GPUDevice) -> None:
        """Save device profile for future reference."""
        self._logger.info(f"Saving profile for device {device.info.device_id}")
        # In a real implementation, this would persist to storage
        # For now, we'll just log the action
    
    def load_device_profile(self, device_id: int) -> Optional[GPUDevice]:
        """Load previously saved device profile."""
        self._logger.info(f"Loading profile for device {device_id}")
        # In a real implementation, this would load from storage
        # For now, return None to indicate no saved profile
        return None
    
    def refresh_device_metrics(self, device_id: int) -> Optional[GPUMetrics]:
        """Refresh metrics for a device using the backend monitor.
        
        This method provides a way to get fresh metrics from the actual GPU hardware.
        """
        self._ensure_initialized()
        
        device = self._devices.get(device_id)
        if not device:
            raise GPUAccessError(f"Device {device_id} not found", gpu_id=device_id)
        
        # Find the backend for this device
        backend_name = self._get_backend_for_device(device)
        if not backend_name or backend_name not in self._backends:
            self._logger.warning(f"No backend available for device {device_id}")
            return None
        
        backend = self._backends[backend_name]
        
        try:
            # Create monitor for the device
            monitor = backend.create_monitor(device_id)
            
            # Get fresh metrics
            temperature = monitor.get_temperature()
            power_usage = monitor.get_power_usage()
            utilization = monitor.get_utilization()
            memory_info = monitor.get_memory_info()
            
            # Create metrics object
            metrics = GPUMetrics(
                temperature_celsius=temperature if temperature >= 0 else 45.0,
                power_usage_watts=power_usage if power_usage >= 0 else 0.0,
                utilization_percent=utilization if utilization >= 0 else 0.0,
                fan_speed_percent=None,  # Not available in current backend
                clock_speed_mhz=None,    # Not available in current backend
                memory_clock_mhz=None,   # Not available in current backend
                timestamp=datetime.utcnow()
            )
            
            # Update device with fresh metrics
            device.update_metrics(metrics)
            
            self._logger.debug(f"Refreshed metrics for device {device_id}")
            return metrics
            
        except Exception as e:
            self._logger.warning(f"Failed to refresh metrics for device {device_id}: {e}")
            return None
    
    def _get_backend_for_device(self, device: GPUDevice) -> Optional[str]:
        """Get the backend name for a specific device."""
        gpu_type_to_backend = {
            GPUType.NVIDIA: "nvidia",
            GPUType.AMD: "amd", 
            GPUType.INTEL: "intel",
            GPUType.MOCK: "mock"
        }
        
        return gpu_type_to_backend.get(device.info.gpu_type)
    
    def get_backend_status(self) -> Dict[str, Any]:
        """Get status information about available backends."""
        self._ensure_initialized()
        
        status = {
            "initialized": self._initialized,
            "available_backends": list(self._backends.keys()),
            "device_count": len(self._devices),
            "devices": {}
        }
        
        for device_id, device in self._devices.items():
            status["devices"][device_id] = {
                "name": device.info.name,
                "gpu_type": device.info.gpu_type.value,
                "status": device.status.value,
                "is_available": device.is_available()
            }
        
        return status
