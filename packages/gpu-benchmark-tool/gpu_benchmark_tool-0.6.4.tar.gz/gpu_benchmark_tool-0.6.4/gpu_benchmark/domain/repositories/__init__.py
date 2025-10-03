"""Repository interfaces for GPU Benchmark Tool.

These interfaces define the contracts for data access operations.
They are implemented in the infrastructure layer.
"""

from .gpu_repository import GPURepository
from .benchmark_repository import BenchmarkRepository
from .configuration_repository import ConfigurationRepository

__all__ = [
    "GPURepository",
    "BenchmarkRepository", 
    "ConfigurationRepository"
]
