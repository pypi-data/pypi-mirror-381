"""Error handling framework for GPU Benchmark Tool.

This package provides a comprehensive error handling system with
graceful degradation, fallback strategies, and error boundaries.
"""

from .error_types import (
    ErrorType,
    BenchmarkError,
    GPUAccessError,
    HealthAssessmentError,
    PersistenceError,
    ConfigurationError,
    RecoverableError,
    CriticalError
)

from .error_boundary import ErrorBoundary
from .fallback_strategies import (
    FallbackStrategy,
    MockGPUFallback,
    ReducedBatchSizeFallback,
    CloudStorageFallback
)

# Error recovery module not yet implemented
# from .error_recovery import (
#     RetryableOperation,
#     CircuitBreaker,
#     HealthChecker
# )

__all__ = [
    # Error Types
    "ErrorType",
    "BenchmarkError",
    "GPUAccessError", 
    "HealthAssessmentError",
    "PersistenceError",
    "ConfigurationError",
    "RecoverableError",
    "CriticalError",
    
    # Error Boundary
    "ErrorBoundary",
    
    # Fallback Strategies
    "FallbackStrategy",
    "MockGPUFallback",
    "ReducedBatchSizeFallback", 
    "CloudStorageFallback",
    
    # Error Recovery (not yet implemented)
    # "RetryableOperation",
    # "CircuitBreaker",
    # "HealthChecker"
]
