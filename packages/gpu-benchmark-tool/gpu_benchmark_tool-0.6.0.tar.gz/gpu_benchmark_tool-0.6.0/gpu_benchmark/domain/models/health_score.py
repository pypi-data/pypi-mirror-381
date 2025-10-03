"""Health Score domain model.

This module defines the health scoring system and related value objects.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional
from enum import Enum


class HealthStatus(Enum):
    """Health status levels."""
    HEALTHY = "healthy"      # 85-100 points
    GOOD = "good"           # 70-84 points  
    DEGRADED = "degraded"   # 55-69 points
    WARNING = "warning"     # 40-54 points
    CRITICAL = "critical"   # 0-39 points


@dataclass(frozen=True)
class HealthScoreBreakdown:
    """Immutable breakdown of health score components."""
    temperature: float = 0.0
    baseline_temperature: float = 0.0
    power_efficiency: float = 0.0
    utilization: float = 0.0
    throttling: float = 0.0
    errors: float = 0.0
    temperature_stability: float = 0.0
    
    @property
    def total_score(self) -> float:
        """Calculate total score from components."""
        return (
            self.temperature +
            self.baseline_temperature +
            self.power_efficiency +
            self.utilization +
            self.throttling +
            self.errors +
            self.temperature_stability
        )
    
    def to_dict(self) -> Dict[str, float]:
        """Convert to dictionary."""
        return {
            "temperature": self.temperature,
            "baseline_temperature": self.baseline_temperature,
            "power_efficiency": self.power_efficiency,
            "utilization": self.utilization,
            "throttling": self.throttling,
            "errors": self.errors,
            "temperature_stability": self.temperature_stability
        }


@dataclass(frozen=True)
class HealthScore:
    """Immutable health score value object."""
    score: float
    status: HealthStatus
    breakdown: HealthScoreBreakdown
    recommendation: str
    specific_recommendations: List[str] = field(default_factory=list)
    timestamp: datetime = field(default_factory=datetime.utcnow)
    
    def __post_init__(self):
        """Validate score after initialization."""
        if not 0 <= self.score <= 100:
            raise ValueError(f"Health score must be between 0 and 100, got {self.score}")
    
    @classmethod
    def create(
        cls,
        breakdown: HealthScoreBreakdown,
        recommendation: str,
        specific_recommendations: Optional[List[str]] = None
    ) -> 'HealthScore':
        """Create health score from breakdown."""
        score = breakdown.total_score
        status = cls._determine_status(score)
        
        return cls(
            score=score,
            status=status,
            breakdown=breakdown,
            recommendation=recommendation,
            specific_recommendations=specific_recommendations or []
        )
    
    @staticmethod
    def _determine_status(score: float) -> HealthStatus:
        """Determine health status from score."""
        if score >= 85:
            return HealthStatus.HEALTHY
        elif score >= 70:
            return HealthStatus.GOOD
        elif score >= 55:
            return HealthStatus.DEGRADED
        elif score >= 40:
            return HealthStatus.WARNING
        else:
            return HealthStatus.CRITICAL
    
    def get_status_emoji(self) -> str:
        """Get emoji representation of status."""
        emoji_map = {
            HealthStatus.HEALTHY: "🟢",
            HealthStatus.GOOD: "🟢", 
            HealthStatus.DEGRADED: "🟡",
            HealthStatus.WARNING: "🟡",
            HealthStatus.CRITICAL: "🔴"
        }
        return emoji_map.get(self.status, "⚪")
    
    def get_status_description(self) -> str:
        """Get human-readable status description."""
        descriptions = {
            HealthStatus.HEALTHY: "Safe for all workloads including AI training",
            HealthStatus.GOOD: "Suitable for most workloads",
            HealthStatus.DEGRADED: "Limit to inference or light compute",
            HealthStatus.WARNING: "Monitor closely, avoid heavy workloads",
            HealthStatus.CRITICAL: "Do not use for production"
        }
        return descriptions.get(self.status, "Unknown status")
    
    def is_suitable_for_workload(self, workload_type: str) -> bool:
        """Check if GPU is suitable for specific workload type."""
        if self.status in [HealthStatus.HEALTHY, HealthStatus.GOOD]:
            return True
        elif self.status == HealthStatus.DEGRADED:
            return workload_type in ["inference", "light_compute", "gaming"]
        elif self.status == HealthStatus.WARNING:
            return workload_type in ["inference", "light_compute"]
        else:  # CRITICAL
            return False
    
    def get_improvement_suggestions(self) -> List[str]:
        """Get suggestions for improving health score."""
        suggestions = []
        
        if self.breakdown.temperature < 15:
            suggestions.append("Improve cooling system - temperature is high")
        
        if self.breakdown.power_efficiency < 5:
            suggestions.append("Check power settings and GPU utilization")
        
        if self.breakdown.throttling < 15:
            suggestions.append("Address thermal or power throttling issues")
        
        if self.breakdown.errors < 15:
            suggestions.append("Investigate GPU errors and stability issues")
        
        if self.breakdown.temperature_stability < 7:
            suggestions.append("Improve temperature stability during workloads")
        
        return suggestions
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization."""
        return {
            "score": self.score,
            "status": self.status.value,
            "breakdown": self.breakdown.to_dict(),
            "recommendation": self.recommendation,
            "specific_recommendations": self.specific_recommendations,
            "timestamp": self.timestamp.isoformat(),
            "status_emoji": self.get_status_emoji(),
            "status_description": self.get_status_description()
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'HealthScore':
        """Create HealthScore from dictionary."""
        breakdown_data = data["breakdown"]
        breakdown = HealthScoreBreakdown(
            temperature=breakdown_data["temperature"],
            baseline_temperature=breakdown_data["baseline_temperature"],
            power_efficiency=breakdown_data["power_efficiency"],
            utilization=breakdown_data["utilization"],
            throttling=breakdown_data["throttling"],
            errors=breakdown_data["errors"],
            temperature_stability=breakdown_data["temperature_stability"]
        )
        
        return cls(
            score=data["score"],
            status=HealthStatus(data["status"]),
            breakdown=breakdown,
            recommendation=data["recommendation"],
            specific_recommendations=data.get("specific_recommendations", []),
            timestamp=datetime.fromisoformat(data["timestamp"])
        )
