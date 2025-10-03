"""Fallback strategies for error handling.

This module provides various fallback strategies for handling errors
gracefully and maintaining system functionality.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
import logging

from ...domain.models.gpu_device import GPUDevice, GPUInfo, GPUMetrics, GPUType, GPUStatus


class FallbackStrategy(ABC):
    """Abstract base class for fallback strategies."""
    
    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        """Execute the fallback strategy.
        
        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.
            
        Returns:
            Any: Fallback result.
        """
        pass


class MockGPUFallback(FallbackStrategy):
    """Fallback strategy that returns mock GPU data."""
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """Initialize mock GPU fallback.
        
        Args:
            logger: Logger for fallback operations.
        """
        self._logger = logger or logging.getLogger(__name__)
    
    def execute(self, device_id: int = 0, **kwargs) -> GPUDevice:
        """Execute mock GPU fallback.
        
        Args:
            device_id: GPU device ID.
            **kwargs: Additional arguments.
            
        Returns:
            GPUDevice: Mock GPU device.
        """
        self._logger.info(f"Using mock GPU fallback for device {device_id}")
        
        # Create mock GPU info
        mock_info = GPUInfo(
            name=f"Mock GPU {device_id}",
            device_id=device_id,
            gpu_type=GPUType.MOCK,
            memory_total_mb=8192,
            memory_used_mb=0,
            driver_version="Mock Driver",
            cuda_version="Mock CUDA",
            is_mock=True
        )
        
        # Create mock metrics
        mock_metrics = GPUMetrics(
            temperature_celsius=45.0,
            power_usage_watts=0.0,
            utilization_percent=0.0,
            fan_speed_percent=0.0,
            clock_speed_mhz=0.0,
            memory_clock_mhz=0.0
        )
        
        # Create mock device
        mock_device = GPUDevice(
            info=mock_info,
            current_metrics=mock_metrics,
            status=GPUStatus.HEALTHY
        )
        
        return mock_device


class ReducedBatchSizeFallback(FallbackStrategy):
    """Fallback strategy that reduces batch size for memory operations."""
    
    def __init__(self, reduction_factor: float = 0.5, logger: Optional[logging.Logger] = None):
        """Initialize reduced batch size fallback.
        
        Args:
            reduction_factor: Factor to reduce batch size by (0.0 to 1.0).
            logger: Logger for fallback operations.
        """
        self._reduction_factor = max(0.1, min(1.0, reduction_factor))
        self._logger = logger or logging.getLogger(__name__)
    
    def execute(self, original_batch_size: int, **kwargs) -> int:
        """Execute reduced batch size fallback.
        
        Args:
            original_batch_size: Original batch size.
            **kwargs: Additional arguments.
            
        Returns:
            int: Reduced batch size.
        """
        reduced_size = max(1, int(original_batch_size * self._reduction_factor))
        self._logger.info(f"Reducing batch size from {original_batch_size} to {reduced_size}")
        return reduced_size


class CloudStorageFallback(FallbackStrategy):
    """Fallback strategy that saves data to cloud storage."""
    
    def __init__(self, cloud_provider: str = "aws_s3", logger: Optional[logging.Logger] = None):
        """Initialize cloud storage fallback.
        
        Args:
            cloud_provider: Cloud storage provider.
            logger: Logger for fallback operations.
        """
        self._cloud_provider = cloud_provider
        self._logger = logger or logging.getLogger(__name__)
    
    def execute(self, data: Dict[str, Any], **kwargs) -> str:
        """Execute cloud storage fallback.
        
        Args:
            data: Data to save to cloud storage.
            **kwargs: Additional arguments.
            
        Returns:
            str: Cloud storage URL or identifier.
        """
        # This is a mock implementation
        # In a real implementation, this would upload to actual cloud storage
        self._logger.info(f"Saving data to {self._cloud_provider} cloud storage")
        
        # Mock cloud storage URL
        cloud_url = f"https://{self._cloud_provider}.com/benchmark_results/{data.get('id', 'unknown')}"
        return cloud_url


class EstimatedMetricsFallback(FallbackStrategy):
    """Fallback strategy that provides estimated metrics."""
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """Initialize estimated metrics fallback.
        
        Args:
            logger: Logger for fallback operations.
        """
        self._logger = logger or logging.getLogger(__name__)
    
    def execute(self, metric_type: str, **kwargs) -> Dict[str, Any]:
        """Execute estimated metrics fallback.
        
        Args:
            metric_type: Type of metric to estimate.
            **kwargs: Additional arguments.
            
        Returns:
            Dict[str, Any]: Estimated metrics.
        """
        self._logger.info(f"Providing estimated metrics for {metric_type}")
        
        # Provide safe estimated values based on metric type
        if metric_type == "temperature":
            return {
                "temperature_celsius": 45.0,
                "is_estimated": True,
                "confidence": "low"
            }
        elif metric_type == "power":
            return {
                "power_usage_watts": 0.0,
                "is_estimated": True,
                "confidence": "low"
            }
        elif metric_type == "utilization":
            return {
                "utilization_percent": 0.0,
                "is_estimated": True,
                "confidence": "low"
            }
        elif metric_type == "memory":
            return {
                "memory_used_mb": 0,
                "memory_total_mb": 8192,
                "is_estimated": True,
                "confidence": "low"
            }
        else:
            return {
                "value": 0.0,
                "is_estimated": True,
                "confidence": "low"
            }


class SkipTestFallback(FallbackStrategy):
    """Fallback strategy that skips failed tests."""
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """Initialize skip test fallback.
        
        Args:
            logger: Logger for fallback operations.
        """
        self._logger = logger or logging.getLogger(__name__)
    
    def execute(self, test_name: str, **kwargs) -> Dict[str, Any]:
        """Execute skip test fallback.
        
        Args:
            test_name: Name of the test to skip.
            **kwargs: Additional arguments.
            
        Returns:
            Dict[str, Any]: Skipped test result.
        """
        self._logger.warning(f"Skipping test: {test_name}")
        
        return {
            "test_name": test_name,
            "status": "skipped",
            "reason": "Test failed and was skipped",
            "duration_seconds": 0.0,
            "iterations_completed": 0,
            "success_rate": 0.0,
            "is_skipped": True
        }


class DefaultHealthScoreFallback(FallbackStrategy):
    """Fallback strategy that provides default health scores."""
    
    def __init__(self, default_score: float = 50.0, logger: Optional[logging.Logger] = None):
        """Initialize default health score fallback.
        
        Args:
            default_score: Default health score to return.
            logger: Logger for fallback operations.
        """
        self._default_score = max(0.0, min(100.0, default_score))
        self._logger = logger or logging.getLogger(__name__)
    
    def execute(self, **kwargs) -> Dict[str, Any]:
        """Execute default health score fallback.
        
        Args:
            **kwargs: Additional arguments.
            
        Returns:
            Dict[str, Any]: Default health score.
        """
        self._logger.info(f"Using default health score: {self._default_score}")
        
        return {
            "score": self._default_score,
            "status": "unknown",
            "recommendation": "Unable to calculate health score - using default value",
            "breakdown": {
                "temperature": 0.0,
                "baseline_temperature": 0.0,
                "power_efficiency": 0.0,
                "utilization": 0.0,
                "throttling": 0.0,
                "errors": 0.0,
                "temperature_stability": 0.0
            },
            "is_default": True
        }


class FallbackStrategyFactory:
    """Factory for creating fallback strategies."""
    
    @staticmethod
    def create_strategy(strategy_type: str, **kwargs) -> FallbackStrategy:
        """Create a fallback strategy by type.
        
        Args:
            strategy_type: Type of strategy to create.
            **kwargs: Additional arguments for strategy creation.
            
        Returns:
            FallbackStrategy: Created strategy instance.
        """
        strategies = {
            "mock_gpu": MockGPUFallback,
            "reduced_batch_size": ReducedBatchSizeFallback,
            "cloud_storage": CloudStorageFallback,
            "estimated_metrics": EstimatedMetricsFallback,
            "skip_test": SkipTestFallback,
            "default_health_score": DefaultHealthScoreFallback
        }
        
        if strategy_type not in strategies:
            raise ValueError(f"Unknown fallback strategy type: {strategy_type}")
        
        strategy_class = strategies[strategy_type]
        return strategy_class(**kwargs)
    
    @staticmethod
    def create_gpu_fallback(**kwargs) -> MockGPUFallback:
        """Create a GPU fallback strategy."""
        return MockGPUFallback(**kwargs)
    
    @staticmethod
    def create_memory_fallback(reduction_factor: float = 0.5, **kwargs) -> ReducedBatchSizeFallback:
        """Create a memory fallback strategy."""
        return ReducedBatchSizeFallback(reduction_factor=reduction_factor, **kwargs)
    
    @staticmethod
    def create_storage_fallback(cloud_provider: str = "aws_s3", **kwargs) -> CloudStorageFallback:
        """Create a storage fallback strategy."""
        return CloudStorageFallback(cloud_provider=cloud_provider, **kwargs)
    
    @staticmethod
    def create_metrics_fallback(**kwargs) -> EstimatedMetricsFallback:
        """Create a metrics fallback strategy."""
        return EstimatedMetricsFallback(**kwargs)
    
    @staticmethod
    def create_test_fallback(**kwargs) -> SkipTestFallback:
        """Create a test fallback strategy."""
        return SkipTestFallback(**kwargs)
    
    @staticmethod
    def create_health_fallback(default_score: float = 50.0, **kwargs) -> DefaultHealthScoreFallback:
        """Create a health score fallback strategy."""
        return DefaultHealthScoreFallback(default_score=default_score, **kwargs)
