"""Error Boundary implementation.

This module provides error boundary functionality to catch and handle
errors gracefully with fallback strategies.
"""

import logging
from typing import Callable, Any, Optional, Type, Union, List
from functools import wraps

from .error_types import (
    BaseBenchmarkError, ErrorType, GPUAccessError, 
    HealthAssessmentError, PersistenceError
)
from .fallback_strategies import FallbackStrategy


class ErrorBoundary:
    """Error boundary for catching and handling errors gracefully.
    
    This class provides a way to wrap operations with error handling
    and fallback strategies to ensure the application continues to
    function even when individual components fail.
    """
    
    def __init__(self, 
                 fallback_strategy: Optional[FallbackStrategy] = None,
                 logger: Optional[logging.Logger] = None,
                 allowed_exceptions: Optional[List[Type[Exception]]] = None):
        """Initialize the error boundary.
        
        Args:
            fallback_strategy: Strategy to use when errors occur.
            logger: Logger for error reporting.
            allowed_exceptions: List of exception types to catch.
        """
        self._fallback_strategy = fallback_strategy
        self._logger = logger or logging.getLogger(__name__)
        self._allowed_exceptions = allowed_exceptions or [BaseBenchmarkError, Exception]
    
    def execute_with_fallback(self, 
                            operation: Callable, 
                            *args, 
                            **kwargs) -> Any:
        """Execute an operation with fallback error handling.
        
        Args:
            operation: The operation to execute.
            *args: Positional arguments for the operation.
            **kwargs: Keyword arguments for the operation.
            
        Returns:
            Any: Result of the operation or fallback result.
        """
        try:
            return operation(*args, **kwargs)
        
        except Exception as e:
            # Check if this is an allowed exception type
            if not any(isinstance(e, exc_type) for exc_type in self._allowed_exceptions):
                # Re-raise if not an allowed exception
                raise
            
            # Log the error
            self._logger.warning(f"Operation failed, using fallback: {e}")
            
            # Handle based on error type
            if isinstance(e, BaseBenchmarkError):
                return self._handle_benchmark_error(e, operation, *args, **kwargs)
            else:
                return self._handle_generic_error(e, operation, *args, **kwargs)
    
    def _handle_benchmark_error(self, 
                              error: BaseBenchmarkError,
                              operation: Callable,
                              *args, **kwargs) -> Any:
        """Handle benchmark-specific errors."""
        if error.is_critical():
            # Critical errors cannot be recovered from
            self._logger.error(f"Critical error occurred: {error.message}")
            raise error
        
        elif error.is_degraded():
            # Try fallback strategy
            if self._fallback_strategy:
                try:
                    return self._fallback_strategy.execute(*args, **kwargs)
                except Exception as fallback_error:
                    self._logger.error(f"Fallback strategy also failed: {fallback_error}")
                    # Return a safe default based on error type
                    return self._get_safe_default(error)
            else:
                return self._get_safe_default(error)
        
        else:
            # Recoverable error - try fallback
            if self._fallback_strategy:
                try:
                    return self._fallback_strategy.execute(*args, **kwargs)
                except Exception as fallback_error:
                    self._logger.warning(f"Fallback failed: {fallback_error}")
                    return self._get_safe_default(error)
            else:
                return self._get_safe_default(error)
    
    def _handle_generic_error(self, 
                            error: Exception,
                            operation: Callable,
                            *args, **kwargs) -> Any:
        """Handle generic errors."""
        self._logger.error(f"Unexpected error: {error}")
        
        # Try fallback if available
        if self._fallback_strategy:
            try:
                return self._fallback_strategy.execute(*args, **kwargs)
            except Exception as fallback_error:
                self._logger.error(f"Fallback strategy failed: {fallback_error}")
        
        # Return safe default
        return self._get_safe_default(error)
    
    def _get_safe_default(self, error: Exception) -> Any:
        """Get a safe default value based on error type."""
        if isinstance(error, GPUAccessError):
            # Return mock GPU info
            return {
                "name": "Mock GPU",
                "device_id": 0,
                "gpu_type": "mock",
                "memory_total_mb": 8192,
                "memory_used_mb": 0,
                "is_mock": True
            }
        
        elif isinstance(error, HealthAssessmentError):
            # Return default health score
            return {
                "score": 50.0,
                "status": "unknown",
                "recommendation": "Unable to assess health - using default values"
            }
        
        elif isinstance(error, PersistenceError):
            # Return empty result
            return None
        
        else:
            # Generic safe default
            return None
    
    def wrap_function(self, func: Callable) -> Callable:
        """Wrap a function with error boundary handling.
        
        Args:
            func: Function to wrap.
            
        Returns:
            Callable: Wrapped function with error handling.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            return self.execute_with_fallback(func, *args, **kwargs)
        
        return wrapper
    
    def wrap_method(self, method: Callable) -> Callable:
        """Wrap a method with error boundary handling.
        
        Args:
            method: Method to wrap.
            
        Returns:
            Callable: Wrapped method with error handling.
        """
        @wraps(method)
        def wrapper(self_instance, *args, **kwargs):
            return self.execute_with_fallback(method, self_instance, *args, **kwargs)
        
        return wrapper


class GPUErrorBoundary(ErrorBoundary):
    """Specialized error boundary for GPU operations."""
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """Initialize GPU error boundary."""
        from .fallback_strategies import MockGPUFallback
        super().__init__(
            fallback_strategy=MockGPUFallback(),
            logger=logger,
            allowed_exceptions=[GPUAccessError, Exception]
        )
    
    def _get_safe_default(self, error: Exception) -> Any:
        """Get GPU-specific safe defaults."""
        if isinstance(error, GPUAccessError):
            # Return mock GPU device
            from ...domain.models.gpu_device import GPUDevice, GPUInfo, GPUType, GPUStatus
            from ...domain.models.gpu_device import GPUMetrics
            
            mock_info = GPUInfo(
                name="Mock GPU",
                device_id=0,
                gpu_type=GPUType.MOCK,
                memory_total_mb=8192,
                memory_used_mb=0,
                driver_version="Mock Driver",
                cuda_version="Mock CUDA",
                is_mock=True
            )
            
            mock_metrics = GPUMetrics(
                temperature_celsius=45.0,
                power_usage_watts=0.0,
                utilization_percent=0.0
            )
            
            mock_device = GPUDevice(
                info=mock_info,
                current_metrics=mock_metrics,
                status=GPUStatus.HEALTHY
            )
            
            return mock_device
        
        return super()._get_safe_default(error)


class BenchmarkErrorBoundary(ErrorBoundary):
    """Specialized error boundary for benchmark operations."""
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """Initialize benchmark error boundary."""
        super().__init__(
            fallback_strategy=None,  # No default fallback for benchmarks
            logger=logger,
            allowed_exceptions=[BaseBenchmarkError, Exception]
        )
    
    def _get_safe_default(self, error: Exception) -> Any:
        """Get benchmark-specific safe defaults."""
        if isinstance(error, (GPUAccessError, HealthAssessmentError)):
            # Return partial benchmark result
            from ...domain.models.benchmark_result import BenchmarkResult, BenchmarkMetadata, BenchmarkStatus
            from ...domain.models.health_score import HealthScore, HealthScoreBreakdown
            
            metadata = BenchmarkMetadata(
                benchmark_id="error_fallback",
                timestamp=datetime.utcnow(),
                duration_seconds=0.0,
                gpu_device_id=0,
                benchmark_type="error_fallback"
            )
            
            # Create default health score
            breakdown = HealthScoreBreakdown()
            health_score = HealthScore.create(
                breakdown=breakdown,
                recommendation="Benchmark failed - using default values"
            )
            
            # Create mock GPU device
            mock_device = self._create_mock_gpu_device()
            
            result = BenchmarkResult(
                metadata=metadata,
                gpu_device=mock_device,
                health_score=health_score,
                status=BenchmarkStatus.PARTIAL_SUCCESS
            )
            
            result.add_warning(f"Benchmark failed: {error}")
            
            return result
        
        return super()._get_safe_default(error)
    
    def _create_mock_gpu_device(self):
        """Create a mock GPU device for error fallback."""
        from ...domain.models.gpu_device import GPUDevice, GPUInfo, GPUType, GPUStatus
        from ...domain.models.gpu_device import GPUMetrics
        
        mock_info = GPUInfo(
            name="Mock GPU (Error Fallback)",
            device_id=0,
            gpu_type=GPUType.MOCK,
            memory_total_mb=8192,
            memory_used_mb=0,
            driver_version="Mock Driver",
            cuda_version="Mock CUDA",
            is_mock=True
        )
        
        mock_metrics = GPUMetrics(
            temperature_celsius=45.0,
            power_usage_watts=0.0,
            utilization_percent=0.0
        )
        
        return GPUDevice(
            info=mock_info,
            current_metrics=mock_metrics,
            status=GPUStatus.HEALTHY
        )


# Decorator functions for easy use
def with_error_boundary(fallback_strategy: Optional[FallbackStrategy] = None,
                       logger: Optional[logging.Logger] = None):
    """Decorator to wrap a function with error boundary handling.
    
    Args:
        fallback_strategy: Fallback strategy to use.
        logger: Logger for error reporting.
    """
    def decorator(func: Callable) -> Callable:
        boundary = ErrorBoundary(fallback_strategy, logger)
        return boundary.wrap_function(func)
    
    return decorator


def with_gpu_error_boundary(logger: Optional[logging.Logger] = None):
    """Decorator to wrap a function with GPU error boundary handling."""
    def decorator(func: Callable) -> Callable:
        boundary = GPUErrorBoundary(logger)
        return boundary.wrap_function(func)
    
    return decorator


def with_benchmark_error_boundary(logger: Optional[logging.Logger] = None):
    """Decorator to wrap a function with benchmark error boundary handling."""
    def decorator(func: Callable) -> Callable:
        boundary = BenchmarkErrorBoundary(logger)
        return boundary.wrap_function(func)
    
    return decorator
