"""Tests for use cases."""

import unittest
from unittest.mock import Mock, patch
from datetime import datetime

from gpu_benchmark.domain.models.gpu_device import GPUDevice, GPUInfo, GPUMetrics, GPUType, GPUStatus
from gpu_benchmark.domain.models.benchmark_result import BenchmarkResult, BenchmarkMetadata, BenchmarkStatus
from gpu_benchmark.domain.models.health_score import HealthScore, HealthScoreBreakdown, HealthStatus
from gpu_benchmark.domain.models.configuration import BenchmarkConfig, BenchmarkType
from gpu_benchmark.domain.services.health_scoring_service import HealthScoringService
from gpu_benchmark.application.use_cases.assess_gpu_health import AssessGPUHealthUseCase
from gpu_benchmark.application.use_cases.run_benchmark import RunBenchmarkUseCase


class TestAssessGPUHealthUseCase(unittest.TestCase):
    """Test assess GPU health use case."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.gpu_repository = Mock()
        self.benchmark_repository = Mock()
        self.health_scoring_service = Mock()
        
        self.use_case = AssessGPUHealthUseCase(
            gpu_repository=self.gpu_repository,
            benchmark_repository=self.benchmark_repository,
            health_scoring_service=self.health_scoring_service
        )
        
        # Create test GPU device
        self.gpu_info = GPUInfo(
            name="Test GPU",
            device_id=0,
            gpu_type=GPUType.NVIDIA,
            memory_total_mb=8192,
            memory_used_mb=2048
        )
        
        self.gpu_metrics = GPUMetrics(
            temperature_celsius=75.0,
            power_usage_watts=150.0,
            utilization_percent=95.0
        )
        
        self.gpu_device = GPUDevice(info=self.gpu_info)
        self.gpu_device.update_metrics(self.gpu_metrics)
        
        # Create test health score
        self.health_score = HealthScore.create(
            breakdown=HealthScoreBreakdown(
                temperature=20.0,
                baseline_temperature=10.0,
                power_efficiency=10.0,
                utilization=10.0,
                throttling=20.0,
                errors=20.0,
                temperature_stability=10.0
            ),
            recommendation="GPU is healthy"
        )
    
    def test_execute_successful_health_assessment(self):
        """Test successful health assessment execution."""
        # Setup mocks
        self.gpu_repository.get_device_by_id.return_value = self.gpu_device
        self.benchmark_repository.get_latest_benchmark_result.return_value = None
        self.health_scoring_service.calculate_health_score.return_value = self.health_score
        
        # Execute use case
        result = self.use_case.execute(device_id=0)
        
        # Verify result
        self.assertEqual(result.score, 100.0)
        self.assertEqual(result.status, HealthStatus.HEALTHY)
        
        # Verify repository calls
        self.gpu_repository.get_device_by_id.assert_called_once_with(0)
        self.health_scoring_service.calculate_health_score.assert_called_once()
    
    def test_execute_gpu_not_found(self):
        """Test health assessment when GPU is not found."""
        # Setup mocks
        self.gpu_repository.get_device_by_id.return_value = None
        
        # Execute use case and expect exception
        with self.assertRaises(Exception):  # GPUAccessError
            self.use_case.execute(device_id=0)
    
    def test_execute_with_stress_test_data(self):
        """Test health assessment with stress test data."""
        # Setup mocks
        self.gpu_repository.get_device_by_id.return_value = self.gpu_device
        
        # Mock stress test results
        stress_test_results = {
            "compute_test": {
                "throttling_events": 0,
                "errors_count": 0
            }
        }
        
        mock_benchmark_result = Mock()
        mock_benchmark_result.stress_test_results = stress_test_results
        self.benchmark_repository.get_latest_benchmark_result.return_value = mock_benchmark_result
        
        self.health_scoring_service.calculate_health_score.return_value = self.health_score
        
        # Execute use case
        result = self.use_case.execute(device_id=0, include_stress_test_data=True)
        
        # Verify result
        self.assertEqual(result.score, 100.0)
        
        # Verify stress test data was passed to scoring service
        call_args = self.health_scoring_service.calculate_health_score.call_args
        self.assertEqual(call_args[1]['stress_test_results'], stress_test_results)
    
    def test_execute_with_benchmark_data(self):
        """Test health assessment using existing benchmark data."""
        # Create benchmark result
        metadata = BenchmarkMetadata(
            benchmark_id="test-123",
            timestamp=datetime.utcnow(),
            duration_seconds=60.0,
            gpu_device_id=0
        )
        
        benchmark_result = BenchmarkResult(
            metadata=metadata,
            gpu_device=self.gpu_device,
            health_score=self.health_score
        )
        
        self.health_scoring_service.calculate_health_score.return_value = self.health_score
        
        # Execute use case
        result = self.use_case.execute_with_benchmark_data(benchmark_result)
        
        # Verify result
        self.assertEqual(result.score, 100.0)
        
        # Verify scoring service was called with benchmark data
        self.health_scoring_service.calculate_health_score.assert_called_once()
    
    def test_compare_health_scores(self):
        """Test health score comparison."""
        # Setup mocks
        self.gpu_repository.get_device_by_id.return_value = self.gpu_device
        self.benchmark_repository.get_latest_benchmark_result.return_value = None
        self.health_scoring_service.calculate_health_score.return_value = self.health_score
        
        # Mock historical results
        historical_result = Mock()
        historical_result.health_score = self.health_score
        self.benchmark_repository.list_benchmark_results.return_value = [historical_result]
        
        # Execute use case
        result = self.use_case.compare_health_scores(device_id=0, days_back=7)
        
        # Verify result structure
        self.assertIn("current_health", result)
        self.assertIn("historical_health", result)
        self.assertIn("comparison", result)
        self.assertIn("trend", result)
    
    def test_get_workload_recommendations(self):
        """Test getting workload recommendations."""
        # Setup mocks
        self.gpu_repository.get_device_by_id.return_value = self.gpu_device
        self.benchmark_repository.get_latest_benchmark_result.return_value = None
        self.health_scoring_service.calculate_health_score.return_value = self.health_score
        self.health_scoring_service.get_workload_recommendations.return_value = {
            "ai_training": True,
            "gaming": True,
            "inference": True
        }
        
        # Execute use case
        result = self.use_case.get_workload_recommendations(device_id=0)
        
        # Verify result structure
        self.assertIn("gpu_info", result)
        self.assertIn("health_score", result)
        self.assertIn("workload_suitability", result)
        self.assertIn("recommendations", result)


class TestRunBenchmarkUseCase(unittest.TestCase):
    """Test run benchmark use case."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.gpu_repository = Mock()
        self.benchmark_repository = Mock()
        self.configuration_repository = Mock()
        self.health_scoring_service = Mock()
        
        self.use_case = RunBenchmarkUseCase(
            gpu_repository=self.gpu_repository,
            benchmark_repository=self.benchmark_repository,
            configuration_repository=self.configuration_repository,
            health_scoring_service=self.health_scoring_service
        )
        
        # Create test GPU device
        self.gpu_info = GPUInfo(
            name="Test GPU",
            device_id=0,
            gpu_type=GPUType.NVIDIA,
            memory_total_mb=8192,
            memory_used_mb=2048
        )
        
        self.gpu_device = GPUDevice(info=self.gpu_info)
        
        # Create test health score
        self.health_score = HealthScore.create(
            breakdown=HealthScoreBreakdown(),
            recommendation="GPU is healthy"
        )
        
        # Create test configuration
        self.config = BenchmarkConfig(
            benchmark_type=BenchmarkType.STANDARD,
            duration_seconds=60,
            include_stress_tests=True,
            include_health_scoring=True
        )
    
    def test_execute_successful_benchmark(self):
        """Test successful benchmark execution."""
        # Setup mocks
        self.gpu_repository.get_device_by_id.return_value = self.gpu_device
        self.configuration_repository.validate_configuration.return_value = []
        self.health_scoring_service.calculate_health_score.return_value = self.health_score
        self.benchmark_repository.save_benchmark_result.return_value = "test-123"
        
        # Execute use case
        result = self.use_case.execute(device_id=0, config=self.config)
        
        # Verify result
        self.assertEqual(result.status, BenchmarkStatus.SUCCESS)
        self.assertIsNotNone(result.health_score)
        self.assertGreater(result.metadata.duration_seconds, 0)
        
        # Verify repository calls
        self.gpu_repository.get_device_by_id.assert_called_once_with(0)
        self.benchmark_repository.save_benchmark_result.assert_called_once()
    
    def test_execute_gpu_not_found(self):
        """Test benchmark execution when GPU is not found."""
        # Setup mocks
        self.gpu_repository.get_device_by_id.return_value = None
        
        # Execute use case and expect exception
        with self.assertRaises(Exception):  # BenchmarkError
            self.use_case.execute(device_id=0, config=self.config)
    
    def test_execute_gpu_not_available(self):
        """Test benchmark execution when GPU is not available."""
        # Setup mocks
        self.gpu_device.is_available = Mock(return_value=False)
        self.gpu_repository.get_device_by_id.return_value = self.gpu_device
        
        # Execute use case and expect exception
        with self.assertRaises(Exception):  # BenchmarkError
            self.use_case.execute(device_id=0, config=self.config)
    
    def test_execute_invalid_configuration(self):
        """Test benchmark execution with invalid configuration."""
        # Setup mocks
        self.gpu_repository.get_device_by_id.return_value = self.gpu_device
        self.configuration_repository.validate_configuration.return_value = ["Invalid duration"]
        
        # Execute use case and expect exception
        with self.assertRaises(Exception):  # BenchmarkError
            self.use_case.execute(device_id=0, config=self.config)
    
    def test_execute_quick_benchmark(self):
        """Test quick benchmark execution."""
        # Setup mocks
        self.gpu_repository.get_device_by_id.return_value = self.gpu_device
        self.configuration_repository.validate_configuration.return_value = []
        self.health_scoring_service.calculate_health_score.return_value = self.health_score
        self.benchmark_repository.save_benchmark_result.return_value = "test-123"
        
        # Execute use case
        result = self.use_case.execute_quick_benchmark(device_id=0)
        
        # Verify result
        self.assertEqual(result.status, BenchmarkStatus.SUCCESS)
        self.assertIsNotNone(result.health_score)
    
    def test_execute_comprehensive_benchmark(self):
        """Test comprehensive benchmark execution."""
        # Setup mocks
        self.gpu_repository.get_device_by_id.return_value = self.gpu_device
        self.configuration_repository.validate_configuration.return_value = []
        self.health_scoring_service.calculate_health_score.return_value = self.health_score
        self.benchmark_repository.save_benchmark_result.return_value = "test-123"
        
        # Execute use case
        result = self.use_case.execute_comprehensive_benchmark(device_id=0)
        
        # Verify result
        self.assertEqual(result.status, BenchmarkStatus.SUCCESS)
        self.assertIsNotNone(result.health_score)
    
    def test_execute_without_export(self):
        """Test benchmark execution without exporting results."""
        # Setup mocks
        self.gpu_repository.get_device_by_id.return_value = self.gpu_device
        self.configuration_repository.validate_configuration.return_value = []
        self.health_scoring_service.calculate_health_score.return_value = self.health_score
        
        # Execute use case
        result = self.use_case.execute(device_id=0, config=self.config, export_results=False)
        
        # Verify result
        self.assertEqual(result.status, BenchmarkStatus.SUCCESS)
        
        # Verify save was not called
        self.benchmark_repository.save_benchmark_result.assert_not_called()
    
    def test_get_benchmark_history(self):
        """Test getting benchmark history."""
        # Setup mocks
        mock_results = [Mock(), Mock()]
        self.benchmark_repository.list_benchmark_results.return_value = mock_results
        
        # Execute use case
        results = self.use_case.get_benchmark_history(device_id=0, limit=10)
        
        # Verify result
        self.assertEqual(len(results), 2)
        self.benchmark_repository.list_benchmark_results.assert_called_once_with(
            device_id=0, limit=10
        )
    
    def test_compare_benchmarks(self):
        """Test comparing benchmarks."""
        # Setup mocks
        mock_comparison = {
            "result1_id": "test-123",
            "result2_id": "test-456",
            "health_comparison": {},
            "performance_comparison": {}
        }
        self.benchmark_repository.compare_benchmark_results.return_value = mock_comparison
        
        # Execute use case
        comparison = self.use_case.compare_benchmarks("test-123", "test-456")
        
        # Verify result
        self.assertEqual(comparison["result1_id"], "test-123")
        self.assertEqual(comparison["result2_id"], "test-456")
        self.benchmark_repository.compare_benchmark_results.assert_called_once_with(
            "test-123", "test-456"
        )


if __name__ == '__main__':
    unittest.main()
