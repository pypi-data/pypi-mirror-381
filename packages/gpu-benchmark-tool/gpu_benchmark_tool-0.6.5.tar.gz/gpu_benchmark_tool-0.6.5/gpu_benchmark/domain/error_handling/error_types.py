"""Error type definitions for GPU Benchmark Tool.

This module defines the error hierarchy and error classification system.
"""

from enum import Enum
from typing import Optional, Dict, Any


class ErrorType(Enum):
    """Classification of error types."""
    RECOVERABLE = "recoverable"      # Can continue with fallback
    DEGRADED = "degraded"           # Can continue with limited functionality
    CRITICAL = "critical"           # Cannot continue, must fail


class BaseBenchmarkError(Exception):
    """Base exception for all benchmark-related errors."""
    
    def __init__(self, message: str, error_type: ErrorType, 
                 fallback_data: Optional[Dict[str, Any]] = None):
        """Initialize the error.
        
        Args:
            message: Error message.
            error_type: Type of error (recoverable, degraded, critical).
            fallback_data: Optional data for fallback strategies.
        """
        super().__init__(message)
        self.message = message
        self.error_type = error_type
        self.fallback_data = fallback_data or {}
    
    def is_recoverable(self) -> bool:
        """Check if error is recoverable."""
        return self.error_type == ErrorType.RECOVERABLE
    
    def is_degraded(self) -> bool:
        """Check if error allows degraded operation."""
        return self.error_type in [ErrorType.RECOVERABLE, ErrorType.DEGRADED]
    
    def is_critical(self) -> bool:
        """Check if error is critical."""
        return self.error_type == ErrorType.CRITICAL


class BenchmarkError(BaseBenchmarkError):
    """General benchmark execution error."""
    
    def __init__(self, message: str, error_type: ErrorType = ErrorType.CRITICAL,
                 fallback_data: Optional[Dict[str, Any]] = None):
        super().__init__(message, error_type, fallback_data)


class GPUAccessError(BaseBenchmarkError):
    """GPU access and communication errors."""
    
    def __init__(self, message: str, gpu_id: Optional[int] = None,
                 error_type: ErrorType = ErrorType.RECOVERABLE,
                 fallback_data: Optional[Dict[str, Any]] = None):
        if gpu_id is not None:
            fallback_data = fallback_data or {}
            fallback_data["gpu_id"] = gpu_id
            fallback_data["fallback"] = "mock_mode"
        
        super().__init__(message, error_type, fallback_data)


class HealthAssessmentError(BaseBenchmarkError):
    """Health assessment and scoring errors."""
    
    def __init__(self, message: str, error_type: ErrorType = ErrorType.DEGRADED,
                 fallback_data: Optional[Dict[str, Any]] = None):
        super().__init__(message, error_type, fallback_data)


class PersistenceError(BaseBenchmarkError):
    """Data persistence and storage errors."""
    
    def __init__(self, message: str, error_type: ErrorType = ErrorType.RECOVERABLE,
                 fallback_data: Optional[Dict[str, Any]] = None):
        super().__init__(message, error_type, fallback_data)


class ConfigurationError(BaseBenchmarkError):
    """Configuration and setup errors."""
    
    def __init__(self, message: str, error_type: ErrorType = ErrorType.CRITICAL,
                 fallback_data: Optional[Dict[str, Any]] = None):
        super().__init__(message, error_type, fallback_data)


class StressTestError(BaseBenchmarkError):
    """Stress test execution errors."""
    
    def __init__(self, message: str, test_type: Optional[str] = None,
                 error_type: ErrorType = ErrorType.DEGRADED,
                 fallback_data: Optional[Dict[str, Any]] = None):
        if test_type is not None:
            fallback_data = fallback_data or {}
            fallback_data["test_type"] = test_type
            fallback_data["fallback"] = "skip_test"
        
        super().__init__(message, error_type, fallback_data)


class AIWorkloadError(BaseBenchmarkError):
    """AI workload benchmark errors."""
    
    def __init__(self, message: str, model_name: Optional[str] = None,
                 error_type: ErrorType = ErrorType.DEGRADED,
                 fallback_data: Optional[Dict[str, Any]] = None):
        if model_name is not None:
            fallback_data = fallback_data or {}
            fallback_data["model_name"] = model_name
            fallback_data["fallback"] = "skip_model"
        
        super().__init__(message, error_type, fallback_data)


class MonitoringError(BaseBenchmarkError):
    """GPU monitoring and telemetry errors."""
    
    def __init__(self, message: str, metric_type: Optional[str] = None,
                 error_type: ErrorType = ErrorType.RECOVERABLE,
                 fallback_data: Optional[Dict[str, Any]] = None):
        if metric_type is not None:
            fallback_data = fallback_data or {}
            fallback_data["metric_type"] = metric_type
            fallback_data["fallback"] = "estimated_value"
        
        super().__init__(message, error_type, fallback_data)


# Specific error types for common scenarios
class GPUUnavailableError(GPUAccessError):
    """GPU device is unavailable."""
    
    def __init__(self, gpu_id: int):
        super().__init__(
            f"GPU {gpu_id} unavailable",
            gpu_id=gpu_id,
            error_type=ErrorType.RECOVERABLE,
            fallback_data={"gpu_id": gpu_id, "fallback": "mock_mode"}
        )


class InsufficientMemoryError(StressTestError):
    """Insufficient GPU memory for operation."""
    
    def __init__(self, required: int, available: int):
        super().__init__(
            f"Insufficient memory: {required}MB required, {available}MB available",
            error_type=ErrorType.DEGRADED,
            fallback_data={
                "required": required,
                "available": available,
                "fallback": "reduced_batch_size"
            }
        )


class DriverError(GPUAccessError):
    """GPU driver related errors."""
    
    def __init__(self, message: str, gpu_id: Optional[int] = None):
        super().__init__(
            f"Driver error: {message}",
            gpu_id=gpu_id,
            error_type=ErrorType.CRITICAL,
            fallback_data={"fallback": "update_drivers"}
        )


class ThermalThrottlingError(MonitoringError):
    """Thermal throttling detected."""
    
    def __init__(self, temperature: float, threshold: float):
        super().__init__(
            f"Thermal throttling detected: {temperature}°C > {threshold}°C",
            metric_type="temperature",
            error_type=ErrorType.DEGRADED,
            fallback_data={
                "temperature": temperature,
                "threshold": threshold,
                "fallback": "reduce_workload"
            }
        )


class PowerLimitError(MonitoringError):
    """Power limit exceeded."""
    
    def __init__(self, power_usage: float, power_limit: float):
        super().__init__(
            f"Power limit exceeded: {power_usage}W > {power_limit}W",
            metric_type="power",
            error_type=ErrorType.DEGRADED,
            fallback_data={
                "power_usage": power_usage,
                "power_limit": power_limit,
                "fallback": "reduce_power_limit"
            }
        )


# Legacy aliases for backward compatibility
RecoverableError = BaseBenchmarkError
CriticalError = BaseBenchmarkError
