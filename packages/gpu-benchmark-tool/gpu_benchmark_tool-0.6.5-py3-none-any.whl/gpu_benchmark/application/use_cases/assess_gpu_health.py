"""Assess GPU Health Use Case.

This use case handles the business workflow for assessing GPU health
based on current metrics and stress test results.
"""

from typing import Optional, Dict, Any
from datetime import datetime

from ...domain.models.gpu_device import GPUDevice
from ...domain.models.health_score import HealthScore
from ...domain.models.benchmark_result import BenchmarkResult
from ...domain.repositories.gpu_repository import GPURepository
from ...domain.repositories.benchmark_repository import BenchmarkRepository
from ...domain.services.health_scoring_service import HealthScoringService


class AssessGPUHealthUseCase:
    """Use case for assessing GPU health.
    
    This use case orchestrates the process of collecting GPU metrics,
    calculating health scores, and generating recommendations.
    """
    
    def __init__(self,
                 gpu_repository: GPURepository,
                 benchmark_repository: BenchmarkRepository,
                 health_scoring_service: HealthScoringService):
        """Initialize the use case.
        
        Args:
            gpu_repository: Repository for GPU device operations.
            benchmark_repository: Repository for benchmark results.
            health_scoring_service: Service for health score calculations.
        """
        self._gpu_repository = gpu_repository
        self._benchmark_repository = benchmark_repository
        self._health_scoring_service = health_scoring_service
    
    def execute(self, device_id: int, include_stress_test_data: bool = True) -> HealthScore:
        """Execute the GPU health assessment.
        
        Args:
            device_id: The GPU device ID to assess.
            include_stress_test_data: Whether to include stress test data in assessment.
            
        Returns:
            HealthScore: The calculated health score and recommendations.
            
        Raises:
            GPUAccessError: If GPU access fails.
            HealthAssessmentError: If health assessment fails.
        """
        try:
            # Get GPU device
            gpu_device = self._gpu_repository.get_device_by_id(device_id)
            if not gpu_device:
                raise GPUAccessError(f"GPU device {device_id} not found")
            
            # Get stress test results if requested
            stress_test_results = None
            if include_stress_test_data:
                stress_test_results = self._get_latest_stress_test_results(device_id)
            
            # Get baseline metrics from previous benchmark
            baseline_metrics = self._get_baseline_metrics(device_id)
            
            # Calculate health score
            health_score = self._health_scoring_service.calculate_health_score(
                gpu_device=gpu_device,
                stress_test_results=stress_test_results,
                baseline_metrics=baseline_metrics
            )
            
            return health_score
            
        except Exception as e:
            if isinstance(e, (GPUAccessError, HealthAssessmentError)):
                raise
            else:
                raise HealthAssessmentError(f"Health assessment failed: {e}") from e
    
    def execute_with_benchmark_data(self, benchmark_result: BenchmarkResult) -> HealthScore:
        """Execute health assessment using existing benchmark data.
        
        Args:
            benchmark_result: The benchmark result containing GPU and test data.
            
        Returns:
            HealthScore: The calculated health score and recommendations.
        """
        try:
            # Calculate health score using benchmark data
            health_score = self._health_scoring_service.calculate_health_score(
                gpu_device=benchmark_result.gpu_device,
                stress_test_results=benchmark_result.stress_test_results,
                baseline_metrics=None  # Could extract from benchmark metadata
            )
            
            return health_score
            
        except Exception as e:
            raise HealthAssessmentError(f"Health assessment from benchmark data failed: {e}") from e
    
    def compare_health_scores(self, device_id: int, days_back: int = 7) -> Dict[str, Any]:
        """Compare current health score with historical scores.
        
        Args:
            device_id: The GPU device ID.
            days_back: Number of days to look back for comparison.
            
        Returns:
            Dict[str, Any]: Comparison data including trends and improvements.
        """
        try:
            # Get current health score
            current_health = self.execute(device_id, include_stress_test_data=True)
            
            # Get historical benchmark results
            end_date = datetime.utcnow()
            start_date = datetime(end_date.year, end_date.month, end_date.day - days_back)
            
            historical_results = self._benchmark_repository.list_benchmark_results(
                device_id=device_id,
                start_date=start_date,
                end_date=end_date,
                limit=10
            )
            
            if not historical_results:
                return {
                    "current_health": current_health.to_dict(),
                    "historical_comparison": "no_historical_data",
                    "trend": "unknown"
                }
            
            # Get the most recent historical health score
            latest_historical = historical_results[0]
            historical_health = latest_historical.health_score
            
            # Compare health scores
            comparison = self._health_scoring_service.compare_health_scores(
                current_health, historical_health
            )
            
            # Calculate trend over time
            trend = self._calculate_health_trend(historical_results)
            
            return {
                "current_health": current_health.to_dict(),
                "historical_health": historical_health.to_dict(),
                "comparison": comparison,
                "trend": trend,
                "historical_data_points": len(historical_results)
            }
            
        except Exception as e:
            raise HealthAssessmentError(f"Health score comparison failed: {e}") from e
    
    def get_workload_recommendations(self, device_id: int) -> Dict[str, Any]:
        """Get workload suitability recommendations for a GPU.
        
        Args:
            device_id: The GPU device ID.
            
        Returns:
            Dict[str, Any]: Workload recommendations and suitability scores.
        """
        try:
            # Get current health score
            health_score = self.execute(device_id, include_stress_test_data=True)
            
            # Get workload recommendations
            workload_suitability = self._health_scoring_service.get_workload_recommendations(
                health_score
            )
            
            # Get GPU device info
            gpu_device = self._gpu_repository.get_device_by_id(device_id)
            if not gpu_device:
                raise GPUAccessError(f"GPU device {device_id} not found")
            
            return {
                "gpu_info": {
                    "name": gpu_device.info.name,
                    "gpu_type": gpu_device.info.gpu_type.value,
                    "memory_total_mb": gpu_device.info.memory_total_mb,
                    "status": gpu_device.status.value
                },
                "health_score": health_score.to_dict(),
                "workload_suitability": workload_suitability,
                "recommendations": health_score.get_improvement_suggestions()
            }
            
        except Exception as e:
            raise HealthAssessmentError(f"Workload recommendations failed: {e}") from e
    
    def _get_latest_stress_test_results(self, device_id: int) -> Optional[Dict[str, Any]]:
        """Get the most recent stress test results for a device."""
        try:
            latest_result = self._benchmark_repository.get_latest_benchmark_result(device_id)
            if latest_result and latest_result.stress_test_results:
                return latest_result.stress_test_results
            return None
        except Exception:
            return None
    
    def _get_baseline_metrics(self, device_id: int) -> Optional[Any]:
        """Get baseline metrics from previous benchmark."""
        try:
            latest_result = self._benchmark_repository.get_latest_benchmark_result(device_id)
            if latest_result and latest_result.gpu_device.current_metrics:
                return latest_result.gpu_device.current_metrics
            return None
        except Exception:
            return None
    
    def _calculate_health_trend(self, historical_results) -> str:
        """Calculate health trend from historical results."""
        if len(historical_results) < 2:
            return "insufficient_data"
        
        # Get health scores from historical results
        scores = [result.health_score.score for result in historical_results]
        
        # Calculate trend (newest first, so we want to see if scores are improving)
        recent_avg = sum(scores[:len(scores)//2]) / (len(scores)//2)
        older_avg = sum(scores[len(scores)//2:]) / (len(scores) - len(scores)//2)
        
        if recent_avg > older_avg + 5:  # 5 point improvement threshold
            return "improving"
        elif recent_avg < older_avg - 5:  # 5 point decline threshold
            return "declining"
        else:
            return "stable"


# Custom exceptions
class GPUAccessError(Exception):
    """Raised when GPU access operations fail."""
    pass


class HealthAssessmentError(Exception):
    """Raised when health assessment operations fail."""
    pass
