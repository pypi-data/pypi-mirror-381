"""Health Scoring Service.

This service contains the business logic for calculating GPU health scores.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime

from ..models.gpu_device import GPUDevice, GPUMetrics
from ..models.health_score import HealthScore, HealthScoreBreakdown, HealthStatus
from ..models.configuration import ScoringThresholds


class HealthScoringService:
    """Service for calculating GPU health scores.
    
    This service encapsulates the business logic for determining GPU health
    based on various metrics and thresholds. It provides methods for
    calculating health scores, generating recommendations, and determining
    workload suitability.
    """
    
    def __init__(self, thresholds: Optional[ScoringThresholds] = None):
        """Initialize the health scoring service.
        
        Args:
            thresholds: Custom scoring thresholds. If None, uses defaults.
        """
        self._thresholds = thresholds or ScoringThresholds()
    
    def calculate_health_score(self, 
                             gpu_device: GPUDevice,
                             stress_test_results: Optional[Dict[str, Any]] = None,
                             baseline_metrics: Optional[GPUMetrics] = None) -> HealthScore:
        """Calculate health score for a GPU device.
        
        Args:
            gpu_device: The GPU device to score.
            stress_test_results: Optional stress test results.
            baseline_metrics: Optional baseline metrics for comparison.
            
        Returns:
            HealthScore: The calculated health score.
        """
        if not gpu_device.current_metrics:
            # If no current metrics, return a default low score
            breakdown = HealthScoreBreakdown()
            return HealthScore.create(
                breakdown=breakdown,
                recommendation="No GPU metrics available. Run a benchmark to get health assessment.",
                specific_recommendations=["Run GPU benchmark to collect metrics"]
            )
        
        # Calculate individual component scores
        breakdown = self._calculate_score_breakdown(
            gpu_device, stress_test_results, baseline_metrics
        )
        
        # Generate recommendations
        recommendation = self._generate_recommendation(breakdown, gpu_device)
        specific_recommendations = self._generate_specific_recommendations(
            breakdown, gpu_device, stress_test_results
        )
        
        return HealthScore.create(
            breakdown=breakdown,
            recommendation=recommendation,
            specific_recommendations=specific_recommendations
        )
    
    def _calculate_score_breakdown(self,
                                 gpu_device: GPUDevice,
                                 stress_test_results: Optional[Dict[str, Any]],
                                 baseline_metrics: Optional[GPUMetrics]) -> HealthScoreBreakdown:
        """Calculate the breakdown of health score components."""
        metrics = gpu_device.current_metrics
        
        # Temperature scoring (20 points max)
        temp_score = self._calculate_temperature_score(metrics.temperature_celsius)
        
        # Baseline temperature scoring (10 points max)
        baseline_score = 0.0
        if baseline_metrics:
            baseline_score = self._calculate_baseline_temperature_score(
                baseline_metrics.temperature_celsius
            )
        
        # Power efficiency scoring (10 points max)
        power_score = self._calculate_power_efficiency_score(metrics)
        
        # Utilization scoring (10 points max)
        util_score = self._calculate_utilization_score(metrics.utilization_percent)
        
        # Throttling scoring (20 points max)
        throttle_score = self._calculate_throttling_score(stress_test_results)
        
        # Errors scoring (20 points max)
        error_score = self._calculate_error_score(stress_test_results)
        
        # Temperature stability scoring (10 points max)
        stability_score = self._calculate_temperature_stability_score(
            stress_test_results, metrics.temperature_celsius
        )
        
        return HealthScoreBreakdown(
            temperature=temp_score,
            baseline_temperature=baseline_score,
            power_efficiency=power_score,
            utilization=util_score,
            throttling=throttle_score,
            errors=error_score,
            temperature_stability=stability_score
        )
    
    def _calculate_temperature_score(self, temperature: float) -> float:
        """Calculate temperature component score."""
        if temperature < 80:
            return 20.0
        elif temperature < 85:
            return 15.0
        elif temperature < 90:
            return 10.0
        else:
            return 5.0
    
    def _calculate_baseline_temperature_score(self, baseline_temp: float) -> float:
        """Calculate baseline temperature component score."""
        if baseline_temp < 50:
            return 10.0
        elif baseline_temp < 60:
            return 5.0
        else:
            return 0.0
    
    def _calculate_power_efficiency_score(self, metrics: GPUMetrics) -> float:
        """Calculate power efficiency component score."""
        # Simple efficiency calculation based on utilization vs power
        if metrics.power_usage_watts == 0:
            return 0.0
        
        efficiency = metrics.utilization_percent / metrics.power_usage_watts
        
        # Score based on efficiency ratio
        if efficiency > 2.0:
            return 10.0
        elif efficiency > 1.5:
            return 7.0
        elif efficiency > 1.0:
            return 5.0
        else:
            return 2.0
    
    def _calculate_utilization_score(self, utilization: float) -> float:
        """Calculate utilization component score."""
        if utilization >= 99:
            return 10.0
        elif utilization >= 90:
            return 5.0
        else:
            return 0.0
    
    def _calculate_throttling_score(self, stress_test_results: Optional[Dict[str, Any]]) -> float:
        """Calculate throttling component score."""
        if not stress_test_results:
            return 20.0  # Assume no throttling if no stress test data
        
        # Check for throttling events in stress test results
        throttle_events = 0
        for test_name, test_data in stress_test_results.items():
            if isinstance(test_data, dict) and "throttling_events" in test_data:
                throttle_events += test_data["throttling_events"]
        
        if throttle_events == 0:
            return 20.0
        elif throttle_events <= 2:
            return 15.0
        elif throttle_events <= 5:
            return 10.0
        else:
            return 5.0
    
    def _calculate_error_score(self, stress_test_results: Optional[Dict[str, Any]]) -> float:
        """Calculate error component score."""
        if not stress_test_results:
            return 20.0  # Assume no errors if no stress test data
        
        # Check for errors in stress test results
        total_errors = 0
        for test_name, test_data in stress_test_results.items():
            if isinstance(test_data, dict) and "errors_count" in test_data:
                total_errors += test_data["errors_count"]
        
        if total_errors == 0:
            return 20.0
        elif total_errors <= 2:
            return 15.0
        elif total_errors <= 5:
            return 10.0
        else:
            return 5.0
    
    def _calculate_temperature_stability_score(self, 
                                             stress_test_results: Optional[Dict[str, Any]],
                                             current_temp: float) -> float:
        """Calculate temperature stability component score."""
        if not stress_test_results:
            return 10.0  # Assume stable if no stress test data
        
        # Look for temperature stability data
        for test_name, test_data in stress_test_results.items():
            if isinstance(test_data, dict) and "temperature_stability" in test_data:
                stability_data = test_data["temperature_stability"]
                if "stability_score" in stability_data:
                    return min(10.0, stability_data["stability_score"] / 10.0)
        
        # Fallback: estimate based on current temperature
        if current_temp < 70:
            return 10.0
        elif current_temp < 80:
            return 8.0
        elif current_temp < 90:
            return 5.0
        else:
            return 2.0
    
    def _generate_recommendation(self, 
                               breakdown: HealthScoreBreakdown,
                               gpu_device: GPUDevice) -> str:
        """Generate overall health recommendation."""
        total_score = breakdown.total_score
        
        if total_score >= 85:
            return "GPU is in excellent condition and suitable for all workloads including AI training."
        elif total_score >= 70:
            return "GPU is in good condition and suitable for most workloads."
        elif total_score >= 55:
            return "GPU shows some degradation. Limit to inference or light compute workloads."
        elif total_score >= 40:
            return "GPU requires attention. Monitor closely and avoid heavy workloads."
        else:
            return "GPU is in critical condition. Do not use for production workloads."
    
    def _generate_specific_recommendations(self,
                                         breakdown: HealthScoreBreakdown,
                                         gpu_device: GPUDevice,
                                         stress_test_results: Optional[Dict[str, Any]]) -> List[str]:
        """Generate specific recommendations based on score breakdown."""
        recommendations = []
        
        # Temperature recommendations
        if breakdown.temperature < 15:
            recommendations.append("Improve cooling system - GPU temperature is high")
        
        # Baseline temperature recommendations
        if breakdown.baseline_temperature < 5:
            recommendations.append("Check idle temperature - may indicate cooling issues")
        
        # Power efficiency recommendations
        if breakdown.power_efficiency < 5:
            recommendations.append("Optimize power settings and GPU utilization")
        
        # Utilization recommendations
        if breakdown.utilization < 5:
            recommendations.append("Check GPU utilization during workloads")
        
        # Throttling recommendations
        if breakdown.throttling < 15:
            recommendations.append("Address thermal or power throttling issues")
        
        # Error recommendations
        if breakdown.errors < 15:
            recommendations.append("Investigate GPU errors and stability issues")
        
        # Stability recommendations
        if breakdown.temperature_stability < 7:
            recommendations.append("Improve temperature stability during workloads")
        
        # GPU-specific recommendations
        if gpu_device.info.is_mock:
            recommendations.append("Using mock GPU - install proper GPU drivers for real testing")
        
        return recommendations
    
    def is_suitable_for_workload(self, 
                               health_score: HealthScore,
                               workload_type: str) -> bool:
        """Check if GPU is suitable for a specific workload type."""
        return health_score.is_suitable_for_workload(workload_type)
    
    def get_workload_recommendations(self, 
                                   health_score: HealthScore) -> Dict[str, bool]:
        """Get workload suitability recommendations."""
        workloads = {
            "ai_training": health_score.is_suitable_for_workload("ai_training"),
            "ai_inference": health_score.is_suitable_for_workload("inference"),
            "gaming": health_score.is_suitable_for_workload("gaming"),
            "mining": health_score.is_suitable_for_workload("mining"),
            "rendering": health_score.is_suitable_for_workload("rendering"),
            "light_compute": health_score.is_suitable_for_workload("light_compute")
        }
        
        return workloads
    
    def compare_health_scores(self, 
                            score1: HealthScore,
                            score2: HealthScore) -> Dict[str, Any]:
        """Compare two health scores."""
        return {
            "score1": {
                "score": score1.score,
                "status": score1.status.value,
                "breakdown": score1.breakdown.to_dict()
            },
            "score2": {
                "score": score2.score,
                "status": score2.status.value,
                "breakdown": score2.breakdown.to_dict()
            },
            "improvement": {
                "score_difference": score2.score - score1.score,
                "status_improvement": self._get_status_improvement(score1.status, score2.status),
                "component_improvements": self._get_component_improvements(
                    score1.breakdown, score2.breakdown
                )
            }
        }
    
    def _get_status_improvement(self, status1: HealthStatus, status2: HealthStatus) -> str:
        """Get status improvement description."""
        status_order = [
            HealthStatus.CRITICAL,
            HealthStatus.WARNING,
            HealthStatus.DEGRADED,
            HealthStatus.GOOD,
            HealthStatus.HEALTHY
        ]
        
        index1 = status_order.index(status1)
        index2 = status_order.index(status2)
        
        if index2 > index1:
            return f"Improved from {status1.value} to {status2.value}"
        elif index2 < index1:
            return f"Degraded from {status1.value} to {status2.value}"
        else:
            return f"Status unchanged: {status1.value}"
    
    def _get_component_improvements(self, 
                                  breakdown1: HealthScoreBreakdown,
                                  breakdown2: HealthScoreBreakdown) -> Dict[str, float]:
        """Get component score improvements."""
        return {
            "temperature": breakdown2.temperature - breakdown1.temperature,
            "baseline_temperature": breakdown2.baseline_temperature - breakdown1.baseline_temperature,
            "power_efficiency": breakdown2.power_efficiency - breakdown1.power_efficiency,
            "utilization": breakdown2.utilization - breakdown1.utilization,
            "throttling": breakdown2.throttling - breakdown1.throttling,
            "errors": breakdown2.errors - breakdown1.errors,
            "temperature_stability": breakdown2.temperature_stability - breakdown1.temperature_stability
        }
