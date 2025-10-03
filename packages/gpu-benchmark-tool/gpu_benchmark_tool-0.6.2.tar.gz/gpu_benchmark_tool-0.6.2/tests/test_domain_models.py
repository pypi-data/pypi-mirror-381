"""Tests for domain models."""

import unittest
from datetime import datetime
from unittest.mock import Mock

from gpu_benchmark.domain.models.gpu_device import GPUDevice, GPUInfo, GPUMetrics, GPUType, GPUStatus
from gpu_benchmark.domain.models.health_score import HealthScore, HealthScoreBreakdown, HealthStatus
from gpu_benchmark.domain.models.benchmark_result import BenchmarkResult, BenchmarkMetadata, BenchmarkStatus
from gpu_benchmark.domain.models.configuration import BenchmarkConfig, BenchmarkType, UseCase


class TestGPUDevice(unittest.TestCase):
    """Test GPU device domain model."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.gpu_info = GPUInfo(
            name="Test GPU",
            device_id=0,
            gpu_type=GPUType.NVIDIA,
            memory_total_mb=8192,
            memory_used_mb=2048,
            driver_version="12.0",
            cuda_version="12.0"
        )
        
        self.gpu_metrics = GPUMetrics(
            temperature_celsius=75.0,
            power_usage_watts=150.0,
            utilization_percent=95.0,
            fan_speed_percent=80.0
        )
    
    def test_gpu_info_properties(self):
        """Test GPU info calculated properties."""
        self.assertEqual(self.gpu_info.memory_available_mb, 6144)
        self.assertEqual(self.gpu_info.memory_usage_percent, 25.0)
    
    def test_gpu_metrics_validation(self):
        """Test GPU metrics validation."""
        # Valid metrics
        self.assertTrue(self.gpu_metrics.is_valid())
        
        # Invalid temperature
        invalid_metrics = GPUMetrics(
            temperature_celsius=200.0,  # Too high
            power_usage_watts=150.0,
            utilization_percent=95.0
        )
        self.assertFalse(invalid_metrics.is_valid())
    
    def test_gpu_device_creation(self):
        """Test GPU device creation."""
        device = GPUDevice(info=self.gpu_info)
        self.assertEqual(device.info.name, "Test GPU")
        self.assertEqual(device.status, GPUStatus.UNKNOWN)
    
    def test_gpu_device_metrics_update(self):
        """Test GPU device metrics update."""
        device = GPUDevice(info=self.gpu_info)
        device.update_metrics(self.gpu_metrics)
        
        self.assertEqual(device.current_metrics.temperature_celsius, 75.0)
        self.assertEqual(device.status, GPUStatus.HEALTHY)
    
    def test_gpu_device_availability(self):
        """Test GPU device availability check."""
        device = GPUDevice(info=self.gpu_info)
        self.assertFalse(device.is_available())  # No metrics yet
        
        device.update_metrics(self.gpu_metrics)
        self.assertTrue(device.is_available())
    
    def test_thermal_throttling_risk(self):
        """Test thermal throttling risk calculation."""
        device = GPUDevice(info=self.gpu_info)
        device.update_metrics(self.gpu_metrics)
        
        risk = device.get_thermal_throttling_risk()
        self.assertEqual(risk, 0.0)  # 75°C is below 80°C threshold
        
        # Test high temperature
        high_temp_metrics = GPUMetrics(
            temperature_celsius=85.0,
            power_usage_watts=150.0,
            utilization_percent=95.0
        )
        device.update_metrics(high_temp_metrics)
        risk = device.get_thermal_throttling_risk()
        self.assertEqual(risk, 0.5)  # 85°C is 50% of the way to 90°C
    
    def test_power_efficiency_score(self):
        """Test power efficiency score calculation."""
        device = GPUDevice(info=self.gpu_info)
        device.update_metrics(self.gpu_metrics)
        
        efficiency = device.get_power_efficiency_score()
        self.assertGreater(efficiency, 0.0)
        self.assertLessEqual(efficiency, 1.0)


class TestHealthScore(unittest.TestCase):
    """Test health score domain model."""
    
    def test_health_score_breakdown(self):
        """Test health score breakdown calculation."""
        breakdown = HealthScoreBreakdown(
            temperature=20.0,
            baseline_temperature=10.0,
            power_efficiency=10.0,
            utilization=10.0,
            throttling=20.0,
            errors=20.0,
            temperature_stability=10.0
        )
        
        self.assertEqual(breakdown.total_score, 100.0)
    
    def test_health_score_creation(self):
        """Test health score creation."""
        breakdown = HealthScoreBreakdown(
            temperature=20.0,
            baseline_temperature=10.0,
            power_efficiency=10.0,
            utilization=10.0,
            throttling=20.0,
            errors=20.0,
            temperature_stability=10.0
        )
        
        health_score = HealthScore.create(
            breakdown=breakdown,
            recommendation="GPU is healthy"
        )
        
        self.assertEqual(health_score.score, 100.0)
        self.assertEqual(health_score.status, HealthStatus.HEALTHY)
    
    def test_health_score_status_determination(self):
        """Test health score status determination."""
        # Test different score ranges
        test_cases = [
            (95.0, HealthStatus.HEALTHY),
            (75.0, HealthStatus.GOOD),
            (60.0, HealthStatus.DEGRADED),
            (45.0, HealthStatus.WARNING),
            (25.0, HealthStatus.CRITICAL)
        ]
        
        for score, expected_status in test_cases:
            breakdown = HealthScoreBreakdown(
                temperature=score * 0.2,
                baseline_temperature=score * 0.1,
                power_efficiency=score * 0.1,
                utilization=score * 0.1,
                throttling=score * 0.2,
                errors=score * 0.2,
                temperature_stability=score * 0.1
            )
            
            health_score = HealthScore.create(
                breakdown=breakdown,
                recommendation="Test"
            )
            
            self.assertEqual(health_score.status, expected_status)
    
    def test_workload_suitability(self):
        """Test workload suitability checking."""
        breakdown = HealthScoreBreakdown(
            temperature=20.0,
            baseline_temperature=10.0,
            power_efficiency=10.0,
            utilization=10.0,
            throttling=20.0,
            errors=20.0,
            temperature_stability=10.0
        )
        
        health_score = HealthScore.create(
            breakdown=breakdown,
            recommendation="GPU is healthy"
        )
        
        # Healthy GPU should be suitable for all workloads
        self.assertTrue(health_score.is_suitable_for_workload("ai_training"))
        self.assertTrue(health_score.is_suitable_for_workload("gaming"))
        self.assertTrue(health_score.is_suitable_for_workload("inference"))


class TestBenchmarkResult(unittest.TestCase):
    """Test benchmark result domain model."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.metadata = BenchmarkMetadata(
            benchmark_id="test-123",
            timestamp=datetime.utcnow(),
            duration_seconds=60.0,
            gpu_device_id=0
        )
        
        self.gpu_info = GPUInfo(
            name="Test GPU",
            device_id=0,
            gpu_type=GPUType.NVIDIA,
            memory_total_mb=8192,
            memory_used_mb=2048
        )
        
        self.gpu_device = GPUDevice(info=self.gpu_info)
        
        self.health_score = HealthScore.create(
            breakdown=HealthScoreBreakdown(),
            recommendation="Test recommendation"
        )
    
    def test_benchmark_result_creation(self):
        """Test benchmark result creation."""
        result = BenchmarkResult(
            metadata=self.metadata,
            gpu_device=self.gpu_device,
            health_score=self.health_score
        )
        
        self.assertEqual(result.metadata.benchmark_id, "test-123")
        self.assertTrue(result.is_successful())
        self.assertFalse(result.has_warnings())
        self.assertFalse(result.has_errors())
    
    def test_benchmark_result_warnings_and_errors(self):
        """Test benchmark result warnings and errors."""
        result = BenchmarkResult(
            metadata=self.metadata,
            gpu_device=self.gpu_device,
            health_score=self.health_score
        )
        
        result.add_warning("Test warning")
        result.add_error("Test error")
        
        self.assertTrue(result.has_warnings())
        self.assertTrue(result.has_errors())
        self.assertEqual(len(result.warnings), 1)
        self.assertEqual(len(result.errors), 1)
    
    def test_benchmark_result_summary(self):
        """Test benchmark result summary generation."""
        result = BenchmarkResult(
            metadata=self.metadata,
            gpu_device=self.gpu_device,
            health_score=self.health_score
        )
        
        summary = result.get_summary()
        
        self.assertIn("status", summary)
        self.assertIn("health_score", summary)
        self.assertIn("gpu_name", summary)
        self.assertIn("duration_seconds", summary)
    
    def test_benchmark_result_recommendations(self):
        """Test benchmark result recommendations."""
        result = BenchmarkResult(
            metadata=self.metadata,
            gpu_device=self.gpu_device,
            health_score=self.health_score
        )
        
        recommendations = result.get_recommendations()
        self.assertIsInstance(recommendations, list)
        self.assertGreater(len(recommendations), 0)


class TestBenchmarkConfig(unittest.TestCase):
    """Test benchmark configuration domain model."""
    
    def test_default_benchmark_config(self):
        """Test default benchmark configuration."""
        config = BenchmarkConfig()
        
        self.assertEqual(config.benchmark_type, BenchmarkType.STANDARD)
        self.assertEqual(config.use_case, UseCase.GENERAL)
        self.assertEqual(config.duration_seconds, 60)
        self.assertTrue(config.include_stress_tests)
        self.assertTrue(config.include_health_scoring)
    
    def test_benchmark_config_validation(self):
        """Test benchmark configuration validation."""
        # Valid config
        config = BenchmarkConfig()
        config.validate()  # Should not raise
        
        # Invalid duration
        config.duration_seconds = -1
        with self.assertRaises(ValueError):
            config.validate()
    
    def test_benchmark_config_effective_duration(self):
        """Test benchmark config effective duration calculation."""
        # Quick benchmark
        config = BenchmarkConfig(benchmark_type=BenchmarkType.QUICK, duration_seconds=60)
        self.assertEqual(config.get_effective_duration(), 30)
        
        # Comprehensive benchmark
        config = BenchmarkConfig(benchmark_type=BenchmarkType.COMPREHENSIVE, duration_seconds=60)
        self.assertEqual(config.get_effective_duration(), 120)
        
        # Standard benchmark
        config = BenchmarkConfig(benchmark_type=BenchmarkType.STANDARD, duration_seconds=60)
        self.assertEqual(config.get_effective_duration(), 60)
    
    def test_benchmark_config_test_inclusion(self):
        """Test benchmark config test inclusion logic."""
        config = BenchmarkConfig()
        
        # Should include tests by default
        self.assertTrue(config.should_include_test("compute"))
        self.assertTrue(config.should_include_test("memory"))
        
        # Quick benchmark should only include compute
        config.benchmark_type = BenchmarkType.QUICK
        self.assertTrue(config.should_include_test("compute"))
        self.assertFalse(config.should_include_test("memory"))


if __name__ == '__main__':
    unittest.main()
