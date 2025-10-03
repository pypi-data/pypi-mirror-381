"""Domain models for GPU Benchmark Tool.

These models represent the core business entities and value objects.
They contain business logic and are independent of external frameworks.
"""

from .gpu_device import GPUDevice, GPUInfo, GPUMetrics
from .benchmark_result import BenchmarkResult, BenchmarkMetadata
from .health_score import HealthScore, HealthScoreBreakdown, HealthStatus
from .stress_test import StressTestResult, StressTestMetrics
from .ai_workload import AIWorkloadResult, CostMetrics, ModelConfig
from .configuration import BenchmarkConfig, SystemContext, ScoringThresholds

__all__ = [
    # GPU Models
    "GPUDevice",
    "GPUInfo", 
    "GPUMetrics",
    
    # Benchmark Models
    "BenchmarkResult",
    "BenchmarkMetadata",
    
    # Health Models
    "HealthScore",
    "HealthScoreBreakdown", 
    "HealthStatus",
    
    # Stress Test Models
    "StressTestResult",
    "StressTestMetrics",
    
    # AI Workload Models
    "AIWorkloadResult",
    "CostMetrics",
    "ModelConfig",
    
    # Configuration Models
    "BenchmarkConfig",
    "SystemContext",
    "ScoringThresholds"
]
