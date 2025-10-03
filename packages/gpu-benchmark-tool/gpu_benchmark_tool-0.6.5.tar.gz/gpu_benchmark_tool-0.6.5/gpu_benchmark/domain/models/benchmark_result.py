"""Benchmark Result domain model.

This module defines the benchmark result entity and related value objects.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional, Any
from enum import Enum

from .gpu_device import GPUDevice
from .health_score import HealthScore


class BenchmarkStatus(Enum):
    """Benchmark execution status."""
    SUCCESS = "success"
    PARTIAL_SUCCESS = "partial_success"
    FAILED = "failed"
    CANCELLED = "cancelled"


@dataclass(frozen=True)
class BenchmarkMetadata:
    """Immutable benchmark metadata value object."""
    benchmark_id: str
    version: str = "1.0.0"
    timestamp: datetime = field(default_factory=datetime.utcnow)
    duration_seconds: float = 0.0
    gpu_device_id: int = 0
    benchmark_type: str = "standard"
    configuration: Optional[Dict[str, Any]] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "benchmark_id": self.benchmark_id,
            "version": self.version,
            "timestamp": self.timestamp.isoformat(),
            "duration_seconds": self.duration_seconds,
            "gpu_device_id": self.gpu_device_id,
            "benchmark_type": self.benchmark_type,
            "configuration": self.configuration or {}
        }


@dataclass
class BenchmarkResult:
    """Benchmark Result domain entity.
    
    This entity represents the complete result of a benchmark execution,
    including all metrics, health assessment, and metadata.
    """
    metadata: BenchmarkMetadata
    gpu_device: GPUDevice
    health_score: HealthScore
    stress_test_results: Optional[Dict[str, Any]] = None
    performance_metrics: Optional[Dict[str, Any]] = None
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    status: BenchmarkStatus = BenchmarkStatus.SUCCESS
    
    def __post_init__(self):
        """Validate result after initialization."""
        if self.status == BenchmarkStatus.FAILED and not self.errors:
            raise ValueError("Failed benchmark must have error messages")
    
    def add_warning(self, warning: str) -> None:
        """Add a warning message."""
        if warning not in self.warnings:
            self.warnings.append(warning)
    
    def add_error(self, error: str) -> None:
        """Add an error message."""
        if error not in self.errors:
            self.errors.append(error)
    
    def is_successful(self) -> bool:
        """Check if benchmark was successful."""
        return self.status in [BenchmarkStatus.SUCCESS, BenchmarkStatus.PARTIAL_SUCCESS]
    
    def has_warnings(self) -> bool:
        """Check if benchmark has warnings."""
        return len(self.warnings) > 0
    
    def has_errors(self) -> bool:
        """Check if benchmark has errors."""
        return len(self.errors) > 0
    
    def get_summary(self) -> Dict[str, Any]:
        """Get a summary of the benchmark result."""
        return {
            "status": self.status.value,
            "health_score": self.health_score.score,
            "health_status": self.health_score.status.value,
            "gpu_name": self.gpu_device.info.name,
            "gpu_type": self.gpu_device.info.gpu_type.value,
            "duration_seconds": self.metadata.duration_seconds,
            "has_warnings": self.has_warnings(),
            "has_errors": self.has_errors(),
            "warning_count": len(self.warnings),
            "error_count": len(self.errors)
        }
    
    def get_recommendations(self) -> List[str]:
        """Get all recommendations from health score and warnings."""
        recommendations = [self.health_score.recommendation]
        recommendations.extend(self.health_score.specific_recommendations)
        
        # Add recommendations based on warnings
        for warning in self.warnings:
            if "temperature" in warning.lower():
                recommendations.append("Monitor GPU temperature during workloads")
            elif "power" in warning.lower():
                recommendations.append("Check power supply and GPU power settings")
            elif "memory" in warning.lower():
                recommendations.append("Monitor GPU memory usage")
        
        return list(set(recommendations))  # Remove duplicates
    
    def is_suitable_for_workload(self, workload_type: str) -> bool:
        """Check if GPU is suitable for specific workload type."""
        if not self.is_successful():
            return False
        
        return self.health_score.is_suitable_for_workload(workload_type)
    
    def get_performance_summary(self) -> Dict[str, Any]:
        """Get performance metrics summary."""
        if not self.performance_metrics:
            return {}
        
        summary = {}
        
        # Extract key performance metrics
        if "matrix_multiply" in self.performance_metrics:
            mm_data = self.performance_metrics["matrix_multiply"]
            summary["compute_tflops"] = mm_data.get("tflops", 0)
        
        if "memory_bandwidth" in self.performance_metrics:
            mb_data = self.performance_metrics["memory_bandwidth"]
            summary["memory_bandwidth_gbps"] = mb_data.get("bandwidth_gbps", 0)
        
        if "mixed_precision" in self.performance_metrics:
            mp_data = self.performance_metrics["mixed_precision"]
            summary["mixed_precision_supported"] = mp_data.get("supported", False)
        
        return summary
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "metadata": self.metadata.to_dict(),
            "gpu_device": self.gpu_device.to_dict(),
            "health_score": self.health_score.to_dict(),
            "stress_test_results": self.stress_test_results or {},
            "performance_metrics": self.performance_metrics or {},
            "warnings": self.warnings,
            "errors": self.errors,
            "status": self.status.value,
            "summary": self.get_summary(),
            "recommendations": self.get_recommendations(),
            "performance_summary": self.get_performance_summary()
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'BenchmarkResult':
        """Create BenchmarkResult from dictionary."""
        metadata_data = data["metadata"]
        metadata = BenchmarkMetadata(
            benchmark_id=metadata_data["benchmark_id"],
            version=metadata_data.get("version", "1.0.0"),
            timestamp=datetime.fromisoformat(metadata_data["timestamp"]),
            duration_seconds=metadata_data.get("duration_seconds", 0.0),
            gpu_device_id=metadata_data.get("gpu_device_id", 0),
            benchmark_type=metadata_data.get("benchmark_type", "standard"),
            configuration=metadata_data.get("configuration")
        )
        
        gpu_device = GPUDevice.from_dict(data["gpu_device"])
        health_score = HealthScore.from_dict(data["health_score"])
        
        return cls(
            metadata=metadata,
            gpu_device=gpu_device,
            health_score=health_score,
            stress_test_results=data.get("stress_test_results"),
            performance_metrics=data.get("performance_metrics"),
            warnings=data.get("warnings", []),
            errors=data.get("errors", []),
            status=BenchmarkStatus(data.get("status", "success"))
        )
