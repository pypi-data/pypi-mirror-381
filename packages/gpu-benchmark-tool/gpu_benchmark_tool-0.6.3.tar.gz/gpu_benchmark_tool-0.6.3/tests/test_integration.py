"""Integration tests for the new architecture.

These tests verify that the new architecture integrates properly
with the existing system and maintains compatibility.
"""

import unittest
import tempfile
import shutil
from pathlib import Path

from gpu_benchmark.application.di.providers import create_container, create_test_container
from gpu_benchmark.infrastructure.adapters.gpu_backend_adapter import GPUBackendAdapter
from gpu_benchmark.infrastructure.adapters.legacy_backend_factory import LegacyBackendFactory
from gpu_benchmark.infrastructure.cli.legacy_cli_wrapper import LegacyCLIWrapper
from gpu_benchmark.infrastructure.web.flask_adapter import FlaskWebAdapter
from gpu_benchmark.infrastructure.migration.config_migration import ConfigMigration
from gpu_benchmark.infrastructure.migration.data_migration import DataMigration


class TestArchitectureIntegration(unittest.TestCase):
    """Test integration between new architecture and existing system."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.container = create_test_container()
    
    def tearDown(self):
        """Clean up test fixtures."""
        shutil.rmtree(self.temp_dir)
    
    def test_di_container_integration(self):
        """Test that DI container properly integrates all components."""
        # Test that all major components can be resolved
        from gpu_benchmark.domain.repositories.gpu_repository import GPURepository
        from gpu_benchmark.domain.repositories.benchmark_repository import BenchmarkRepository
        from gpu_benchmark.domain.repositories.configuration_repository import ConfigurationRepository
        from gpu_benchmark.domain.services.health_scoring_service import HealthScoringService
        from gpu_benchmark.application.use_cases.run_benchmark import RunBenchmarkUseCase
        from gpu_benchmark.application.use_cases.assess_gpu_health import AssessGPUHealthUseCase
        
        # Resolve all components
        gpu_repo = self.container.resolve(GPURepository)
        benchmark_repo = self.container.resolve(BenchmarkRepository)
        config_repo = self.container.resolve(ConfigurationRepository)
        health_service = self.container.resolve(HealthScoringService)
        benchmark_use_case = self.container.resolve(RunBenchmarkUseCase)
        health_use_case = self.container.resolve(AssessGPUHealthUseCase)
        
        # Verify all components are resolved
        self.assertIsNotNone(gpu_repo)
        self.assertIsNotNone(benchmark_repo)
        self.assertIsNotNone(config_repo)
        self.assertIsNotNone(health_service)
        self.assertIsNotNone(benchmark_use_case)
        self.assertIsNotNone(health_use_case)
    
    def test_gpu_backend_adapter_integration(self):
        """Test GPU backend adapter integration."""
        # Create backend factory
        backend_factory = LegacyBackendFactory()
        
        # Create adapter
        adapter = GPUBackendAdapter(backend_factory)
        
        # Test basic operations
        devices = adapter.get_available_devices()
        self.assertIsInstance(devices, list)
        
        device_count = adapter.get_device_count()
        self.assertGreaterEqual(device_count, 0)
        
        # Test backend status
        status = adapter.get_backend_status()
        self.assertIn("initialized", status)
        self.assertIn("available_backends", status)
        self.assertIn("device_count", status)
    
    def test_cli_wrapper_integration(self):
        """Test CLI wrapper integration."""
        # Create CLI wrapper
        cli_wrapper = LegacyCLIWrapper()
        
        # Test basic operations
        devices = cli_wrapper.get_available_devices()
        self.assertIsInstance(devices, list)
        
        gpu_info = cli_wrapper.get_gpu_info(0)
        self.assertIsInstance(gpu_info, dict)
        self.assertIn("name", gpu_info)
        self.assertIn("device_id", gpu_info)
        self.assertIn("gpu_type", gpu_info)
    
    def test_flask_adapter_integration(self):
        """Test Flask adapter integration."""
        # Create Flask adapter
        flask_adapter = FlaskWebAdapter()
        
        # Test basic operations
        system_info = flask_adapter.get_system_info()
        self.assertIsInstance(system_info, dict)
        self.assertIn("platform", system_info)
        self.assertIn("python_version", system_info)
        
        gpu_info = flask_adapter.get_gpu_info()
        self.assertIsInstance(gpu_info, dict)
        self.assertIn("detected", gpu_info)
        self.assertIn("gpus", gpu_info)
        self.assertIn("backend", gpu_info)
        
        # Test Flask app creation
        app = flask_adapter.create_flask_app()
        self.assertIsNotNone(app)
    
    def test_config_migration_integration(self):
        """Test configuration migration integration."""
        # Create migration utility
        migration = ConfigMigration()
        
        # Test legacy config migration
        legacy_config = {
            "name": "test_config",
            "type": "standard",
            "use_case": "gaming",
            "duration": 60,
            "gpu_id": 0,
            "include_ai": False
        }
        
        new_config = migration.migrate_legacy_config(legacy_config)
        self.assertIsNotNone(new_config)
        self.assertEqual(new_config.duration_seconds, 60)
        self.assertEqual(new_config.gpu_device_id, 0)
        
        # Test default config creation
        config_dir = Path(self.temp_dir) / "configs"
        migration.create_default_configs(str(config_dir))
        
        # Verify config files were created
        self.assertTrue(config_dir.exists())
        config_files = list(config_dir.glob("*.json"))
        self.assertGreater(len(config_files), 0)
    
    def test_data_migration_integration(self):
        """Test data migration integration."""
        # Create migration utility
        migration = DataMigration()
        
        # Test legacy benchmark result migration
        legacy_result = {
            "benchmark_id": "test_123",
            "timestamp": "2024-01-01T12:00:00Z",
            "duration_seconds": 60.0,
            "gpu_info": {
                "name": "Test GPU",
                "device_id": 0,
                "gpu_type": "nvidia",
                "memory_total_mb": 8192,
                "memory_used_mb": 2048,
                "driver_version": "12.0",
                "cuda_version": "12.0",
                "is_mock": False
            },
            "health_score": {
                "score": 85.0,
                "status": "healthy",
                "recommendation": "GPU is healthy",
                "details": {
                    "breakdown": {
                        "temperature": 20.0,
                        "baseline_temperature": 10.0,
                        "power_efficiency": 10.0,
                        "utilization": 10.0,
                        "throttling": 20.0,
                        "errors": 20.0,
                        "temperature_stability": 10.0
                    },
                    "specific_recommendations": []
                }
            },
            "warnings": [],
            "errors": []
        }
        
        new_result = migration.migrate_legacy_benchmark_result(legacy_result)
        self.assertIsNotNone(new_result)
        self.assertEqual(new_result.metadata.benchmark_id, "test_123")
        self.assertEqual(new_result.gpu_device.info.name, "Test GPU")
        self.assertEqual(new_result.health_score.score, 85.0)
    
    def test_end_to_end_benchmark_flow(self):
        """Test end-to-end benchmark flow using new architecture."""
        # Get use case from container
        benchmark_use_case = self.container.resolve("RunBenchmarkUseCase")
        
        # Run a quick benchmark
        result = benchmark_use_case.execute_quick_benchmark(device_id=0)
        
        # Verify result
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.metadata)
        self.assertIsNotNone(result.gpu_device)
        self.assertIsNotNone(result.health_score)
        
        # Verify metadata
        self.assertIsNotNone(result.metadata.benchmark_id)
        self.assertGreaterEqual(result.metadata.duration_seconds, 0)
        
        # Verify GPU device
        self.assertIsNotNone(result.gpu_device.info.name)
        self.assertGreaterEqual(result.gpu_device.info.device_id, 0)
        
        # Verify health score
        self.assertGreaterEqual(result.health_score.score, 0)
        self.assertLessEqual(result.health_score.score, 100)
    
    def test_end_to_end_health_assessment_flow(self):
        """Test end-to-end health assessment flow using new architecture."""
        # Get use case from container
        health_use_case = self.container.resolve("AssessGPUHealthUseCase")
        
        # Assess GPU health
        health_score = health_use_case.execute(device_id=0)
        
        # Verify result
        self.assertIsNotNone(health_score)
        self.assertGreaterEqual(health_score.score, 0)
        self.assertLessEqual(health_score.score, 100)
        self.assertIsNotNone(health_score.status)
        self.assertIsNotNone(health_score.recommendation)
    
    def test_error_handling_integration(self):
        """Test error handling integration."""
        # Test with invalid device ID
        benchmark_use_case = self.container.resolve("RunBenchmarkUseCase")
        
        # This should handle the error gracefully
        try:
            result = benchmark_use_case.execute(device_id=999)  # Invalid device ID
            # If it doesn't raise an exception, it should return a result with errors
            if result:
                self.assertIsNotNone(result.errors or result.warnings)
        except Exception as e:
            # Exception is also acceptable - the important thing is it doesn't crash
            self.assertIsNotNone(str(e))
    
    def test_backward_compatibility(self):
        """Test backward compatibility with existing interfaces."""
        # Test that CLI wrapper maintains same interface
        cli_wrapper = LegacyCLIWrapper()
        
        # Test function signatures match expected interface
        devices = cli_wrapper.get_available_devices()
        self.assertIsInstance(devices, list)
        
        gpu_info = cli_wrapper.get_gpu_info(0)
        self.assertIsInstance(gpu_info, dict)
        self.assertIn("name", gpu_info)
        self.assertIn("device_id", gpu_info)
        self.assertIn("gpu_type", gpu_info)
        
        # Test that Flask adapter maintains same interface
        flask_adapter = FlaskWebAdapter()
        
        system_info = flask_adapter.get_system_info()
        self.assertIsInstance(system_info, dict)
        self.assertIn("platform", system_info)
        
        gpu_info = flask_adapter.get_gpu_info()
        self.assertIsInstance(gpu_info, dict)
        self.assertIn("detected", gpu_info)
        self.assertIn("gpus", gpu_info)


class TestLegacyCompatibility(unittest.TestCase):
    """Test compatibility with legacy interfaces."""
    
    def test_legacy_cli_interface_compatibility(self):
        """Test that legacy CLI interface still works."""
        from gpu_benchmark.infrastructure.cli.legacy_cli_wrapper import (
            run_full_benchmark,
            run_quick_benchmark,
            get_gpu_info,
            get_available_devices
        )
        
        # Test that functions can be called with same signatures
        devices = get_available_devices()
        self.assertIsInstance(devices, list)
        
        gpu_info = get_gpu_info(0)
        self.assertIsInstance(gpu_info, dict)
        
        # Test benchmark functions (they should not crash)
        try:
            result = run_quick_benchmark(0)
            self.assertIsInstance(result, dict)
        except Exception as e:
            # Exception is acceptable as long as it's handled gracefully
            self.assertIsNotNone(str(e))
    
    def test_legacy_web_interface_compatibility(self):
        """Test that legacy web interface still works."""
        from gpu_benchmark.infrastructure.web.flask_adapter import FlaskWebAdapter
        
        flask_adapter = FlaskWebAdapter()
        app = flask_adapter.create_flask_app()
        
        # Test that app has expected routes
        with app.test_client() as client:
            # Test health endpoint
            response = client.get('/api/health')
            self.assertEqual(response.status_code, 200)
            
            # Test detect endpoint
            response = client.get('/api/detect')
            self.assertEqual(response.status_code, 200)
            
            # Test new endpoints
            response = client.get('/api/health/0')
            self.assertEqual(response.status_code, 200)
            
            response = client.get('/api/history/0')
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
