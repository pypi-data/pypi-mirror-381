"""Configuration domain model.

This module defines configuration models and system context.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional, Any
from enum import Enum


class BenchmarkType(Enum):
    """Types of benchmarks."""
    STANDARD = "standard"
    QUICK = "quick"
    COMPREHENSIVE = "comprehensive"
    AI_WORKLOAD = "ai_workload"
    CUSTOM = "custom"


class UseCase(Enum):
    """Common use cases for GPU benchmarking."""
    GAMING = "gaming"
    AI_TRAINING = "ai_training"
    AI_INFERENCE = "ai_inference"
    MINING = "mining"
    RENDERING = "rendering"
    GENERAL = "general"


@dataclass(frozen=True)
class ScoringThresholds:
    """Immutable scoring thresholds configuration."""
    healthy_min: float = 85.0
    good_min: float = 70.0
    degraded_min: float = 55.0
    warning_min: float = 40.0
    critical_min: float = 0.0
    
    # Component weights (should sum to 1.0)
    temperature_weight: float = 0.2
    baseline_temperature_weight: float = 0.1
    power_efficiency_weight: float = 0.1
    utilization_weight: float = 0.1
    throttling_weight: float = 0.2
    errors_weight: float = 0.2
    temperature_stability_weight: float = 0.1
    
    def validate(self) -> None:
        """Validate threshold configuration."""
        if not (0 <= self.healthy_min <= 100):
            raise ValueError("Healthy threshold must be between 0 and 100")
        if not (0 <= self.good_min < self.healthy_min):
            raise ValueError("Good threshold must be less than healthy threshold")
        if not (0 <= self.degraded_min < self.good_min):
            raise ValueError("Degraded threshold must be less than good threshold")
        if not (0 <= self.warning_min < self.degraded_min):
            raise ValueError("Warning threshold must be less than degraded threshold")
        if not (0 <= self.critical_min < self.warning_min):
            raise ValueError("Critical threshold must be less than warning threshold")
        
        # Validate weights sum to 1.0
        total_weight = (
            self.temperature_weight +
            self.baseline_temperature_weight +
            self.power_efficiency_weight +
            self.utilization_weight +
            self.throttling_weight +
            self.errors_weight +
            self.temperature_stability_weight
        )
        if abs(total_weight - 1.0) > 0.01:
            raise ValueError(f"Scoring weights must sum to 1.0, got {total_weight}")
    
    def to_dict(self) -> Dict[str, float]:
        """Convert to dictionary."""
        return {
            "healthy_min": self.healthy_min,
            "good_min": self.good_min,
            "degraded_min": self.degraded_min,
            "warning_min": self.warning_min,
            "critical_min": self.critical_min,
            "temperature_weight": self.temperature_weight,
            "baseline_temperature_weight": self.baseline_temperature_weight,
            "power_efficiency_weight": self.power_efficiency_weight,
            "utilization_weight": self.utilization_weight,
            "throttling_weight": self.throttling_weight,
            "errors_weight": self.errors_weight,
            "temperature_stability_weight": self.temperature_stability_weight
        }


@dataclass(frozen=True)
class StressTestConfig:
    """Immutable stress test configuration."""
    duration_seconds: int = 60
    include_compute_test: bool = True
    include_memory_test: bool = True
    include_mixed_precision_test: bool = True
    compute_test_weight: float = 0.4
    memory_test_weight: float = 0.3
    mixed_precision_test_weight: float = 0.3
    target_utilization: float = 95.0
    max_temperature: float = 90.0
    
    def validate(self) -> None:
        """Validate stress test configuration."""
        if self.duration_seconds <= 0:
            raise ValueError("Duration must be positive")
        if not (0 <= self.target_utilization <= 100):
            raise ValueError("Target utilization must be between 0 and 100")
        if not (0 <= self.max_temperature <= 150):
            raise ValueError("Max temperature must be between 0 and 150")
        
        # Validate weights sum to 1.0
        total_weight = (
            self.compute_test_weight +
            self.memory_test_weight +
            self.mixed_precision_test_weight
        )
        if abs(total_weight - 1.0) > 0.01:
            raise ValueError(f"Test weights must sum to 1.0, got {total_weight}")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "duration_seconds": self.duration_seconds,
            "include_compute_test": self.include_compute_test,
            "include_memory_test": self.include_memory_test,
            "include_mixed_precision_test": self.include_mixed_precision_test,
            "compute_test_weight": self.compute_test_weight,
            "memory_test_weight": self.memory_test_weight,
            "mixed_precision_test_weight": self.mixed_precision_test_weight,
            "target_utilization": self.target_utilization,
            "max_temperature": self.max_temperature
        }


@dataclass(frozen=True)
class BenchmarkConfig:
    """Immutable benchmark configuration."""
    benchmark_type: BenchmarkType = BenchmarkType.STANDARD
    use_case: UseCase = UseCase.GENERAL
    duration_seconds: int = 60
    gpu_device_id: int = 0
    include_ai_benchmarks: bool = False
    include_stress_tests: bool = True
    include_health_scoring: bool = True
    export_results: bool = True
    export_format: str = "json"
    export_path: Optional[str] = None
    stress_test_config: Optional[StressTestConfig] = None
    scoring_thresholds: Optional[ScoringThresholds] = None
    custom_parameters: Dict[str, Any] = field(default_factory=dict)
    
    def validate(self) -> None:
        """Validate benchmark configuration."""
        if self.duration_seconds <= 0:
            raise ValueError("Duration must be positive")
        if self.gpu_device_id < 0:
            raise ValueError("GPU device ID must be non-negative")
        if self.export_format not in ["json", "yaml", "csv"]:
            raise ValueError("Export format must be json, yaml, or csv")
        
        if self.stress_test_config:
            self.stress_test_config.validate()
        
        if self.scoring_thresholds:
            self.scoring_thresholds.validate()
    
    def get_effective_duration(self) -> int:
        """Get effective duration based on benchmark type."""
        if self.benchmark_type == BenchmarkType.QUICK:
            return min(30, self.duration_seconds)
        elif self.benchmark_type == BenchmarkType.COMPREHENSIVE:
            return max(120, self.duration_seconds)
        else:
            return self.duration_seconds
    
    def should_include_test(self, test_name: str) -> bool:
        """Check if a specific test should be included."""
        if not self.include_stress_tests:
            return False
        
        if self.benchmark_type == BenchmarkType.QUICK:
            return test_name in ["compute"]
        elif self.benchmark_type == BenchmarkType.COMPREHENSIVE:
            return True
        else:
            return True
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "benchmark_type": self.benchmark_type.value,
            "use_case": self.use_case.value,
            "duration_seconds": self.duration_seconds,
            "gpu_device_id": self.gpu_device_id,
            "include_ai_benchmarks": self.include_ai_benchmarks,
            "include_stress_tests": self.include_stress_tests,
            "include_health_scoring": self.include_health_scoring,
            "export_results": self.export_results,
            "export_format": self.export_format,
            "export_path": self.export_path,
            "stress_test_config": self.stress_test_config.to_dict() if self.stress_test_config else None,
            "scoring_thresholds": self.scoring_thresholds.to_dict() if self.scoring_thresholds else None,
            "custom_parameters": self.custom_parameters
        }


@dataclass(frozen=True)
class SystemContext:
    """Immutable system context information."""
    os_name: str
    os_version: str
    architecture: str
    python_version: str
    gpu_backend_type: str
    installation_type: str  # "nvidia", "amd", "intel", "all", "basic"
    available_memory_gb: float
    cpu_cores: int
    timestamp: datetime = field(default_factory=datetime.utcnow)
    
    def is_nvidia_installation(self) -> bool:
        """Check if this is an NVIDIA-specific installation."""
        return self.installation_type in ["nvidia", "all"]
    
    def is_amd_installation(self) -> bool:
        """Check if this is an AMD-specific installation."""
        return self.installation_type in ["amd", "all"]
    
    def is_intel_installation(self) -> bool:
        """Check if this is an Intel-specific installation."""
        return self.installation_type in ["intel", "all"]
    
    def is_multi_backend_installation(self) -> bool:
        """Check if this is a multi-backend installation."""
        return self.installation_type == "all"
    
    def get_recommended_benchmark_type(self) -> BenchmarkType:
        """Get recommended benchmark type based on system context."""
        if self.installation_type == "basic":
            return BenchmarkType.QUICK
        elif self.available_memory_gb < 8:
            return BenchmarkType.QUICK
        elif self.available_memory_gb > 32:
            return BenchmarkType.COMPREHENSIVE
        else:
            return BenchmarkType.STANDARD
    
    def get_recommended_duration(self) -> int:
        """Get recommended benchmark duration based on system context."""
        if self.installation_type == "basic":
            return 30
        elif self.available_memory_gb < 8:
            return 45
        elif self.available_memory_gb > 32:
            return 120
        else:
            return 60
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "os_name": self.os_name,
            "os_version": self.os_version,
            "architecture": self.architecture,
            "python_version": self.python_version,
            "gpu_backend_type": self.gpu_backend_type,
            "installation_type": self.installation_type,
            "available_memory_gb": self.available_memory_gb,
            "cpu_cores": self.cpu_cores,
            "timestamp": self.timestamp.isoformat()
        }
