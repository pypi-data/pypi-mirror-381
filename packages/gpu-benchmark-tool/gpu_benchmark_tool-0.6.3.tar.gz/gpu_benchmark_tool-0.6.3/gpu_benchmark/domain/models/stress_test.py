"""Stress Test domain model.

This module defines stress test results and related value objects.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional, Any
from enum import Enum


class StressTestType(Enum):
    """Types of stress tests."""
    COMPUTE = "compute"
    MEMORY = "memory"
    MIXED_PRECISION = "mixed_precision"
    THERMAL = "thermal"
    POWER = "power"


class StressTestStatus(Enum):
    """Stress test execution status."""
    SUCCESS = "success"
    FAILED = "failed"
    PARTIAL = "partial"
    SKIPPED = "skipped"


@dataclass(frozen=True)
class StressTestMetrics:
    """Immutable stress test metrics value object."""
    test_type: StressTestType
    duration_seconds: float
    iterations_completed: int
    target_iterations: int
    success_rate: float
    average_temperature: float
    peak_temperature: float
    average_power_watts: float
    peak_power_watts: float
    average_utilization: float
    errors_count: int
    throttling_events: int
    timestamp: datetime = field(default_factory=datetime.utcnow)
    
    @property
    def completion_rate(self) -> float:
        """Calculate completion rate as percentage."""
        if self.target_iterations == 0:
            return 0.0
        return (self.iterations_completed / self.target_iterations) * 100.0
    
    @property
    def temperature_delta(self) -> float:
        """Calculate temperature increase during test."""
        return self.peak_temperature - self.average_temperature
    
    def is_successful(self) -> bool:
        """Check if test was successful."""
        return (
            self.success_rate >= 95.0 and
            self.completion_rate >= 90.0 and
            self.errors_count == 0
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "test_type": self.test_type.value,
            "duration_seconds": self.duration_seconds,
            "iterations_completed": self.iterations_completed,
            "target_iterations": self.target_iterations,
            "success_rate": self.success_rate,
            "completion_rate": self.completion_rate,
            "average_temperature": self.average_temperature,
            "peak_temperature": self.peak_temperature,
            "temperature_delta": self.temperature_delta,
            "average_power_watts": self.average_power_watts,
            "peak_power_watts": self.peak_power_watts,
            "average_utilization": self.average_utilization,
            "errors_count": self.errors_count,
            "throttling_events": self.throttling_events,
            "timestamp": self.timestamp.isoformat()
        }


@dataclass
class StressTestResult:
    """Stress Test Result domain entity.
    
    This entity represents the result of a stress test execution,
    including metrics, status, and any issues encountered.
    """
    test_type: StressTestType
    status: StressTestStatus
    metrics: Optional[StressTestMetrics] = None
    error_message: Optional[str] = None
    warnings: List[str] = field(default_factory=list)
    additional_data: Dict[str, Any] = field(default_factory=dict)
    
    def add_warning(self, warning: str) -> None:
        """Add a warning message."""
        if warning not in self.warnings:
            self.warnings.append(warning)
    
    def is_successful(self) -> bool:
        """Check if stress test was successful."""
        if self.status != StressTestStatus.SUCCESS:
            return False
        
        if self.metrics:
            return self.metrics.is_successful()
        
        return True
    
    def get_performance_score(self) -> float:
        """Calculate performance score (0.0 to 1.0)."""
        if not self.metrics:
            return 0.0
        
        # Base score from success rate
        score = self.metrics.success_rate / 100.0
        
        # Penalize for errors
        if self.metrics.errors_count > 0:
            score *= 0.5
        
        # Penalize for throttling
        if self.metrics.throttling_events > 0:
            score *= 0.8
        
        # Bonus for high utilization
        if self.metrics.average_utilization > 95:
            score *= 1.1
        
        return min(1.0, score)
    
    def get_thermal_score(self) -> float:
        """Calculate thermal performance score (0.0 to 1.0)."""
        if not self.metrics:
            return 0.0
        
        temp = self.metrics.peak_temperature
        
        # Score decreases as temperature increases
        if temp <= 70:
            return 1.0
        elif temp <= 80:
            return 0.9
        elif temp <= 85:
            return 0.7
        elif temp <= 90:
            return 0.5
        else:
            return 0.2
    
    def get_stability_score(self) -> float:
        """Calculate stability score (0.0 to 1.0)."""
        if not self.metrics:
            return 0.0
        
        # Base score from completion rate
        score = self.metrics.completion_rate / 100.0
        
        # Penalize for errors
        error_penalty = min(0.5, self.metrics.errors_count * 0.1)
        score -= error_penalty
        
        # Penalize for throttling
        throttle_penalty = min(0.3, self.metrics.throttling_events * 0.05)
        score -= throttle_penalty
        
        return max(0.0, score)
    
    def get_summary(self) -> Dict[str, Any]:
        """Get summary of stress test result."""
        summary = {
            "test_type": self.test_type.value,
            "status": self.status.value,
            "successful": self.is_successful(),
            "performance_score": self.get_performance_score(),
            "thermal_score": self.get_thermal_score(),
            "stability_score": self.get_stability_score()
        }
        
        if self.metrics:
            summary.update({
                "duration_seconds": self.metrics.duration_seconds,
                "completion_rate": self.metrics.completion_rate,
                "success_rate": self.metrics.success_rate,
                "peak_temperature": self.metrics.peak_temperature,
                "peak_power_watts": self.metrics.peak_power_watts,
                "errors_count": self.metrics.errors_count,
                "throttling_events": self.metrics.throttling_events
            })
        
        if self.error_message:
            summary["error_message"] = self.error_message
        
        if self.warnings:
            summary["warnings"] = self.warnings
        
        return summary
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "test_type": self.test_type.value,
            "status": self.status.value,
            "metrics": self.metrics.to_dict() if self.metrics else None,
            "error_message": self.error_message,
            "warnings": self.warnings,
            "additional_data": self.additional_data,
            "summary": self.get_summary()
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'StressTestResult':
        """Create StressTestResult from dictionary."""
        metrics = None
        if data.get("metrics"):
            metrics_data = data["metrics"]
            metrics = StressTestMetrics(
                test_type=StressTestType(metrics_data["test_type"]),
                duration_seconds=metrics_data["duration_seconds"],
                iterations_completed=metrics_data["iterations_completed"],
                target_iterations=metrics_data["target_iterations"],
                success_rate=metrics_data["success_rate"],
                average_temperature=metrics_data["average_temperature"],
                peak_temperature=metrics_data["peak_temperature"],
                average_power_watts=metrics_data["average_power_watts"],
                peak_power_watts=metrics_data["peak_power_watts"],
                average_utilization=metrics_data["average_utilization"],
                errors_count=metrics_data["errors_count"],
                throttling_events=metrics_data["throttling_events"],
                timestamp=datetime.fromisoformat(metrics_data["timestamp"])
            )
        
        return cls(
            test_type=StressTestType(data["test_type"]),
            status=StressTestStatus(data["status"]),
            metrics=metrics,
            error_message=data.get("error_message"),
            warnings=data.get("warnings", []),
            additional_data=data.get("additional_data", {})
        )
