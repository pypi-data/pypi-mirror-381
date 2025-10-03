"""Memory-based GPU Repository implementation.

This implementation provides in-memory storage for GPU device information.
It's useful for testing and temporary storage scenarios.
"""

from typing import List, Optional, Dict, Any
from datetime import datetime

from ...domain.repositories.gpu_repository import GPURepository
from ...domain.models.gpu_device import GPUDevice, GPUInfo, GPUMetrics, GPUType, GPUStatus


class MemoryGPURepository(GPURepository):
    """In-memory implementation of GPURepository.
    
    This implementation stores GPU device information in memory.
    It's primarily useful for testing and development scenarios.
    """
    
    def __init__(self):
        """Initialize the memory-based repository."""
        self._devices: Dict[int, GPUDevice] = {}
        self._device_profiles: Dict[int, GPUDevice] = {}
        self._next_device_id = 0
    
    def get_available_devices(self) -> List[GPUDevice]:
        """Get all available GPU devices.
        
        Returns:
            List[GPUDevice]: List of available GPU devices.
        """
        return list(self._devices.values())
    
    def get_device_by_id(self, device_id: int) -> Optional[GPUDevice]:
        """Get a specific GPU device by ID.
        
        Args:
            device_id: The GPU device ID.
            
        Returns:
            Optional[GPUDevice]: The GPU device if found, None otherwise.
        """
        return self._devices.get(device_id)
    
    def get_device_count(self) -> int:
        """Get the number of available GPU devices.
        
        Returns:
            int: Number of available GPU devices.
        """
        return len(self._devices)
    
    def update_device_metrics(self, device_id: int, metrics: GPUMetrics) -> None:
        """Update metrics for a specific GPU device.
        
        Args:
            device_id: The GPU device ID.
            metrics: The new metrics to update.
            
        Raises:
            GPUAccessError: If device access fails.
            InvalidMetricsError: If metrics are invalid.
        """
        if device_id not in self._devices:
            raise GPUAccessError(f"Device {device_id} not found")
        
        if not metrics.is_valid():
            raise InvalidMetricsError("Invalid metrics provided")
        
        device = self._devices[device_id]
        device.update_metrics(metrics)
    
    def is_device_available(self, device_id: int) -> bool:
        """Check if a GPU device is available.
        
        Args:
            device_id: The GPU device ID.
            
        Returns:
            bool: True if device is available, False otherwise.
        """
        device = self._devices.get(device_id)
        return device is not None and device.is_available()
    
    def get_device_capabilities(self, device_id: int) -> Dict[str, Any]:
        """Get capabilities of a specific GPU device.
        
        Args:
            device_id: The GPU device ID.
            
        Returns:
            Dict[str, Any]: Device capabilities information.
            
        Raises:
            GPUAccessError: If device access fails.
        """
        device = self._devices.get(device_id)
        if not device:
            raise GPUAccessError(f"Device {device_id} not found")
        
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
        """Save device profile for future reference.
        
        Args:
            device: The GPU device to save.
        """
        self._device_profiles[device.info.device_id] = device
    
    def load_device_profile(self, device_id: int) -> Optional[GPUDevice]:
        """Load previously saved device profile.
        
        Args:
            device_id: The GPU device ID.
            
        Returns:
            Optional[GPUDevice]: The saved device profile if found, None otherwise.
        """
        return self._device_profiles.get(device_id)
    
    def add_device(self, device: GPUDevice) -> int:
        """Add a new device to the repository.
        
        Args:
            device: The GPU device to add.
            
        Returns:
            int: The assigned device ID.
        """
        device_id = self._next_device_id
        self._next_device_id += 1
        
        # Create new device with assigned ID
        new_info = GPUInfo(
            name=device.info.name,
            device_id=device_id,
            gpu_type=device.info.gpu_type,
            memory_total_mb=device.info.memory_total_mb,
            memory_used_mb=device.info.memory_used_mb,
            driver_version=device.info.driver_version,
            cuda_version=device.info.cuda_version,
            is_mock=device.info.is_mock
        )
        
        new_device = GPUDevice(
            info=new_info,
            current_metrics=device.current_metrics,
            status=device.status,
            last_updated=device.last_updated
        )
        
        self._devices[device_id] = new_device
        return device_id
    
    def remove_device(self, device_id: int) -> bool:
        """Remove a device from the repository.
        
        Args:
            device_id: The GPU device ID to remove.
            
        Returns:
            bool: True if device was removed, False if not found.
        """
        if device_id in self._devices:
            del self._devices[device_id]
            return True
        return False
    
    def clear_all_devices(self) -> None:
        """Clear all devices from the repository."""
        self._devices.clear()
        self._device_profiles.clear()
        self._next_device_id = 0
    
    def create_mock_device(self, name: str = "Mock GPU", memory_mb: int = 8192) -> int:
        """Create a mock GPU device for testing.
        
        Args:
            name: Name of the mock device.
            memory_mb: Memory size in MB.
            
        Returns:
            int: The device ID of the created mock device.
        """
        device_id = self._next_device_id
        self._next_device_id += 1
        
        info = GPUInfo(
            name=name,
            device_id=device_id,
            gpu_type=GPUType.MOCK,
            memory_total_mb=memory_mb,
            memory_used_mb=0,
            driver_version="Mock Driver",
            cuda_version="Mock CUDA",
            is_mock=True
        )
        
        # Create mock metrics
        metrics = GPUMetrics(
            temperature_celsius=45.0,
            power_usage_watts=0.0,
            utilization_percent=0.0,
            fan_speed_percent=0.0,
            clock_speed_mhz=0.0,
            memory_clock_mhz=0.0
        )
        
        device = GPUDevice(
            info=info,
            current_metrics=metrics,
            status=GPUStatus.HEALTHY
        )
        
        self._devices[device_id] = device
        return device_id
    
    def create_nvidia_device(self, name: str, memory_mb: int, driver_version: str = None) -> int:
        """Create a mock NVIDIA GPU device.
        
        Args:
            name: Name of the device.
            memory_mb: Memory size in MB.
            driver_version: Driver version.
            
        Returns:
            int: The device ID of the created device.
        """
        device_id = self._next_device_id
        self._next_device_id += 1
        
        info = GPUInfo(
            name=name,
            device_id=device_id,
            gpu_type=GPUType.NVIDIA,
            memory_total_mb=memory_mb,
            memory_used_mb=0,
            driver_version=driver_version or "Unknown",
            cuda_version="12.0",
            is_mock=False
        )
        
        device = GPUDevice(
            info=info,
            status=GPUStatus.HEALTHY
        )
        
        self._devices[device_id] = device
        return device_id
    
    def get_device_statistics(self) -> Dict[str, Any]:
        """Get statistics about devices in the repository.
        
        Returns:
            Dict[str, Any]: Device statistics.
        """
        if not self._devices:
            return {
                "total_devices": 0,
                "device_types": {},
                "status_distribution": {},
                "average_memory_mb": 0
            }
        
        device_types = {}
        status_distribution = {}
        total_memory = 0
        
        for device in self._devices.values():
            # Count device types
            gpu_type = device.info.gpu_type.value
            device_types[gpu_type] = device_types.get(gpu_type, 0) + 1
            
            # Count statuses
            status = device.status.value
            status_distribution[status] = status_distribution.get(status, 0) + 1
            
            # Sum memory
            total_memory += device.info.memory_total_mb
        
        return {
            "total_devices": len(self._devices),
            "device_types": device_types,
            "status_distribution": status_distribution,
            "average_memory_mb": total_memory / len(self._devices),
            "total_memory_mb": total_memory
        }


# Custom exceptions
class GPUAccessError(Exception):
    """Raised when GPU access operations fail."""
    pass


class InvalidMetricsError(Exception):
    """Raised when invalid metrics are provided."""
    pass
