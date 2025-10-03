"""GPU Repository interface.

This module defines the contract for GPU device data access operations.
"""

from abc import ABC, abstractmethod
from typing import List, Optional

from ..models.gpu_device import GPUDevice


class GPURepository(ABC):
    """Abstract repository for GPU device operations.
    
    This interface defines the contract for accessing GPU device information
    and managing GPU device data. Implementations should handle the specific
    details of GPU detection, monitoring, and data persistence.
    """
    
    @abstractmethod
    def get_available_devices(self) -> List[GPUDevice]:
        """Get all available GPU devices.
        
        Returns:
            List[GPUDevice]: List of available GPU devices.
            
        Raises:
            GPUDetectionError: If GPU detection fails.
        """
        pass
    
    @abstractmethod
    def get_device_by_id(self, device_id: int) -> Optional[GPUDevice]:
        """Get a specific GPU device by ID.
        
        Args:
            device_id: The GPU device ID.
            
        Returns:
            Optional[GPUDevice]: The GPU device if found, None otherwise.
            
        Raises:
            GPUAccessError: If device access fails.
        """
        pass
    
    @abstractmethod
    def get_device_count(self) -> int:
        """Get the number of available GPU devices.
        
        Returns:
            int: Number of available GPU devices.
        """
        pass
    
    @abstractmethod
    def update_device_metrics(self, device_id: int, metrics) -> None:
        """Update metrics for a specific GPU device.
        
        Args:
            device_id: The GPU device ID.
            metrics: The new metrics to update.
            
        Raises:
            GPUAccessError: If device access fails.
            InvalidMetricsError: If metrics are invalid.
        """
        pass
    
    @abstractmethod
    def is_device_available(self, device_id: int) -> bool:
        """Check if a GPU device is available.
        
        Args:
            device_id: The GPU device ID.
            
        Returns:
            bool: True if device is available, False otherwise.
        """
        pass
    
    @abstractmethod
    def get_device_capabilities(self, device_id: int) -> dict:
        """Get capabilities of a specific GPU device.
        
        Args:
            device_id: The GPU device ID.
            
        Returns:
            dict: Device capabilities information.
            
        Raises:
            GPUAccessError: If device access fails.
        """
        pass
    
    @abstractmethod
    def save_device_profile(self, device: GPUDevice) -> None:
        """Save device profile for future reference.
        
        Args:
            device: The GPU device to save.
            
        Raises:
            PersistenceError: If saving fails.
        """
        pass
    
    @abstractmethod
    def load_device_profile(self, device_id: int) -> Optional[GPUDevice]:
        """Load previously saved device profile.
        
        Args:
            device_id: The GPU device ID.
            
        Returns:
            Optional[GPUDevice]: The saved device profile if found, None otherwise.
            
        Raises:
            PersistenceError: If loading fails.
        """
        pass
