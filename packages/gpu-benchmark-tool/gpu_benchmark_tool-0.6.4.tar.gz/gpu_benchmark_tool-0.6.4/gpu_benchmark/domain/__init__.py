"""Domain layer for GPU Benchmark Tool.

This package contains the core business logic, domain models, and business rules.
It's independent of external concerns like databases, APIs, or user interfaces.
"""

from .models import (
    GPUDevice,
    BenchmarkResult,
    HealthScore,
    StressTestResult,
    AIWorkloadResult,
    BenchmarkConfig,
    SystemContext
)

from .services import (
    HealthScoringService
)

from .repositories import (
    GPURepository,
    BenchmarkRepository,
    ConfigurationRepository
)

__all__ = [
    # Models
    "GPUDevice",
    "BenchmarkResult", 
    "HealthScore",
    "StressTestResult",
    "AIWorkloadResult",
    "BenchmarkConfig",
    "SystemContext",
    
    # Services
    "HealthScoringService",
    
    # Repositories
    "GPURepository",
    "BenchmarkRepository",
    "ConfigurationRepository"
]
