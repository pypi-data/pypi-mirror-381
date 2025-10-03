"""GPU Device domain model.

This module defines the core GPU device entity and related value objects.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional, Any
from enum import Enum


class GPUType(Enum):
    """GPU vendor types."""
    NVIDIA = "nvidia"
    AMD = "amd"
    INTEL = "intel"
    MOCK = "mock"
    UNKNOWN = "unknown"


class GPUStatus(Enum):
    """GPU operational status."""
    HEALTHY = "healthy"
    WARNING = "warning"
    CRITICAL = "critical"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class GPUInfo:
    """Immutable GPU information value object."""
    name: str
    device_id: int
    gpu_type: GPUType
    memory_total_mb: int
    memory_used_mb: int
    driver_version: Optional[str] = None
    cuda_version: Optional[str] = None
    is_mock: bool = False
    
    @property
    def memory_available_mb(self) -> int:
        """Calculate available memory in MB."""
        return max(0, self.memory_total_mb - self.memory_used_mb)
    
    @property
    def memory_usage_percent(self) -> float:
        """Calculate memory usage percentage."""
        if self.memory_total_mb == 0:
            return 0.0
        return (self.memory_used_mb / self.memory_total_mb) * 100.0


@dataclass(frozen=True)
class GPUMetrics:
    """Immutable GPU metrics value object."""
    temperature_celsius: float
    power_usage_watts: float
    utilization_percent: float
    fan_speed_percent: Optional[float] = None
    clock_speed_mhz: Optional[float] = None
    memory_clock_mhz: Optional[float] = None
    timestamp: datetime = field(default_factory=datetime.utcnow)
    
    def is_valid(self) -> bool:
        """Check if metrics are within reasonable ranges."""
        return (
            0 <= self.temperature_celsius <= 150 and
            0 <= self.power_usage_watts <= 1000 and
            0 <= self.utilization_percent <= 100 and
            (self.fan_speed_percent is None or 0 <= self.fan_speed_percent <= 100)
        )


@dataclass
class GPUDevice:
    """GPU Device domain entity.
    
    This is the main entity representing a GPU device with its current state
    and capabilities. It encapsulates business logic related to GPU operations.
    """
    info: GPUInfo
    current_metrics: Optional[GPUMetrics] = None
    status: GPUStatus = GPUStatus.UNKNOWN
    last_updated: datetime = field(default_factory=datetime.utcnow)
    
    def update_metrics(self, metrics: GPUMetrics) -> None:
        """Update GPU metrics and status."""
        if not metrics.is_valid():
            raise ValueError("Invalid GPU metrics provided")
        
        self.current_metrics = metrics
        self.last_updated = datetime.utcnow()
        self._update_status()
    
    def _update_status(self) -> None:
        """Update GPU status based on current metrics."""
        if not self.current_metrics:
            self.status = GPUStatus.UNKNOWN
            return
        
        metrics = self.current_metrics
        
        # Determine status based on temperature and other factors
        if metrics.temperature_celsius > 90:
            self.status = GPUStatus.CRITICAL
        elif metrics.temperature_celsius > 80:
            self.status = GPUStatus.WARNING
        else:
            self.status = GPUStatus.HEALTHY
    
    def is_available(self) -> bool:
        """Check if GPU is available for benchmarking."""
        return (
            self.status != GPUStatus.CRITICAL and
            self.current_metrics is not None and
            self.current_metrics.is_valid()
        )
    
    def get_thermal_throttling_risk(self) -> float:
        """Calculate thermal throttling risk (0.0 to 1.0)."""
        if not self.current_metrics:
            return 0.0
        
        temp = self.current_metrics.temperature_celsius
        
        # Risk increases exponentially above 80°C
        if temp <= 80:
            return 0.0
        elif temp <= 90:
            return (temp - 80) / 10.0
        else:
            return 1.0
    
    def get_power_efficiency_score(self) -> float:
        """Calculate power efficiency score (0.0 to 1.0)."""
        if not self.current_metrics:
            return 0.0
        
        metrics = self.current_metrics
        
        # Simple efficiency calculation based on utilization vs power
        if metrics.power_usage_watts == 0:
            return 0.0
        
        efficiency = metrics.utilization_percent / metrics.power_usage_watts
        return min(1.0, efficiency / 2.0)  # Normalize to 0-1 range
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "info": {
                "name": self.info.name,
                "device_id": self.info.device_id,
                "gpu_type": self.info.gpu_type.value,
                "memory_total_mb": self.info.memory_total_mb,
                "memory_used_mb": self.info.memory_used_mb,
                "driver_version": self.info.driver_version,
                "cuda_version": self.info.cuda_version,
                "is_mock": self.info.is_mock
            },
            "current_metrics": {
                "temperature_celsius": self.current_metrics.temperature_celsius,
                "power_usage_watts": self.current_metrics.power_usage_watts,
                "utilization_percent": self.current_metrics.utilization_percent,
                "fan_speed_percent": self.current_metrics.fan_speed_percent,
                "clock_speed_mhz": self.current_metrics.clock_speed_mhz,
                "memory_clock_mhz": self.current_metrics.memory_clock_mhz,
                "timestamp": self.current_metrics.timestamp.isoformat()
            } if self.current_metrics else None,
            "status": self.status.value,
            "last_updated": self.last_updated.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'GPUDevice':
        """Create GPUDevice from dictionary."""
        info_data = data["info"]
        info = GPUInfo(
            name=info_data["name"],
            device_id=info_data["device_id"],
            gpu_type=GPUType(info_data["gpu_type"]),
            memory_total_mb=info_data["memory_total_mb"],
            memory_used_mb=info_data["memory_used_mb"],
            driver_version=info_data.get("driver_version"),
            cuda_version=info_data.get("cuda_version"),
            is_mock=info_data.get("is_mock", False)
        )
        
        gpu = cls(
            info=info,
            status=GPUStatus(data["status"]),
            last_updated=datetime.fromisoformat(data["last_updated"])
        )
        
        if data.get("current_metrics"):
            metrics_data = data["current_metrics"]
            metrics = GPUMetrics(
                temperature_celsius=metrics_data["temperature_celsius"],
                power_usage_watts=metrics_data["power_usage_watts"],
                utilization_percent=metrics_data["utilization_percent"],
                fan_speed_percent=metrics_data.get("fan_speed_percent"),
                clock_speed_mhz=metrics_data.get("clock_speed_mhz"),
                memory_clock_mhz=metrics_data.get("memory_clock_mhz"),
                timestamp=datetime.fromisoformat(metrics_data["timestamp"])
            )
            gpu.current_metrics = metrics
        
        return gpu
