"""Tests for repository implementations."""

import unittest
import tempfile
import shutil
from datetime import datetime
from pathlib import Path

from gpu_benchmark.domain.models.gpu_device import GPUDevice, GPUInfo, GPUMetrics, GPUType, GPUStatus
from gpu_benchmark.domain.models.benchmark_result import BenchmarkResult, BenchmarkMetadata, BenchmarkStatus
from gpu_benchmark.domain.models.health_score import HealthScore, HealthScoreBreakdown
from gpu_benchmark.infrastructure.repositories.memory_gpu_repository import MemoryGPURepository
from gpu_benchmark.infrastructure.repositories.file_benchmark_repository import FileBenchmarkRepository


class TestMemoryGPURepository(unittest.TestCase):
    """Test memory-based GPU repository."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.repository = MemoryGPURepository()
    
    def test_initial_state(self):
        """Test initial repository state."""
        self.assertEqual(self.repository.get_device_count(), 0)
        self.assertEqual(len(self.repository.get_available_devices()), 0)
    
    def test_add_device(self):
        """Test adding a device to the repository."""
        gpu_info = GPUInfo(
            name="Test GPU",
            device_id=0,
            gpu_type=GPUType.NVIDIA,
            memory_total_mb=8192,
            memory_used_mb=2048
        )
        
        device = GPUDevice(info=gpu_info)
        device_id = self.repository.add_device(device)
        
        self.assertEqual(device_id, 0)
        self.assertEqual(self.repository.get_device_count(), 1)
        
        retrieved_device = self.repository.get_device_by_id(device_id)
        self.assertIsNotNone(retrieved_device)
        self.assertEqual(retrieved_device.info.name, "Test GPU")
    
    def test_get_device_by_id(self):
        """Test getting device by ID."""
        # Add a device
        device_id = self.repository.create_mock_device("Test GPU")
        
        # Get the device
        device = self.repository.get_device_by_id(device_id)
        self.assertIsNotNone(device)
        self.assertEqual(device.info.name, "Test GPU")
        
        # Get non-existent device
        device = self.repository.get_device_by_id(999)
        self.assertIsNone(device)
    
    def test_update_device_metrics(self):
        """Test updating device metrics."""
        device_id = self.repository.create_mock_device("Test GPU")
        
        metrics = GPUMetrics(
            temperature_celsius=75.0,
            power_usage_watts=150.0,
            utilization_percent=95.0
        )
        
        self.repository.update_device_metrics(device_id, metrics)
        
        device = self.repository.get_device_by_id(device_id)
        self.assertEqual(device.current_metrics.temperature_celsius, 75.0)
        self.assertEqual(device.status, GPUStatus.HEALTHY)
    
    def test_device_availability(self):
        """Test device availability checking."""
        device_id = self.repository.create_mock_device("Test GPU")
        
        # Initially available (mock device has metrics)
        self.assertTrue(self.repository.is_device_available(device_id))
        
        # Non-existent device
        self.assertFalse(self.repository.is_device_available(999))
    
    def test_device_capabilities(self):
        """Test getting device capabilities."""
        device_id = self.repository.create_mock_device("Test GPU")
        
        capabilities = self.repository.get_device_capabilities(device_id)
        
        self.assertIn("gpu_type", capabilities)
        self.assertIn("memory_total_mb", capabilities)
        self.assertIn("status", capabilities)
        self.assertIn("is_available", capabilities)
    
    def test_save_and_load_device_profile(self):
        """Test saving and loading device profiles."""
        device_id = self.repository.create_mock_device("Test GPU")
        device = self.repository.get_device_by_id(device_id)
        
        # Save profile
        self.repository.save_device_profile(device)
        
        # Load profile
        loaded_device = self.repository.load_device_profile(device_id)
        self.assertIsNotNone(loaded_device)
        self.assertEqual(loaded_device.info.name, "Test GPU")
    
    def test_create_mock_device(self):
        """Test creating mock devices."""
        device_id = self.repository.create_mock_device("Mock GPU", 4096)
        
        device = self.repository.get_device_by_id(device_id)
        self.assertEqual(device.info.name, "Mock GPU")
        self.assertEqual(device.info.memory_total_mb, 4096)
        self.assertEqual(device.info.gpu_type, GPUType.MOCK)
        self.assertTrue(device.info.is_mock)
    
    def test_create_nvidia_device(self):
        """Test creating NVIDIA devices."""
        device_id = self.repository.create_nvidia_device("RTX 4090", 24576, "12.0")
        
        device = self.repository.get_device_by_id(device_id)
        self.assertEqual(device.info.name, "RTX 4090")
        self.assertEqual(device.info.memory_total_mb, 24576)
        self.assertEqual(device.info.gpu_type, GPUType.NVIDIA)
        self.assertEqual(device.info.driver_version, "12.0")
    
    def test_remove_device(self):
        """Test removing devices."""
        device_id = self.repository.create_mock_device("Test GPU")
        self.assertEqual(self.repository.get_device_count(), 1)
        
        # Remove device
        result = self.repository.remove_device(device_id)
        self.assertTrue(result)
        self.assertEqual(self.repository.get_device_count(), 0)
        
        # Remove non-existent device
        result = self.repository.remove_device(999)
        self.assertFalse(result)
    
    def test_clear_all_devices(self):
        """Test clearing all devices."""
        self.repository.create_mock_device("GPU 1")
        self.repository.create_mock_device("GPU 2")
        self.assertEqual(self.repository.get_device_count(), 2)
        
        self.repository.clear_all_devices()
        self.assertEqual(self.repository.get_device_count(), 0)
    
    def test_device_statistics(self):
        """Test getting device statistics."""
        # Empty repository
        stats = self.repository.get_device_statistics()
        self.assertEqual(stats["total_devices"], 0)
        
        # Add some devices
        self.repository.create_mock_device("Mock GPU")
        self.repository.create_nvidia_device("RTX 4090", 24576)
        
        stats = self.repository.get_device_statistics()
        self.assertEqual(stats["total_devices"], 2)
        self.assertIn("device_types", stats)
        self.assertIn("status_distribution", stats)


class TestFileBenchmarkRepository(unittest.TestCase):
    """Test file-based benchmark repository."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.repository = FileBenchmarkRepository(self.temp_dir)
        
        # Create test data
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
        
        self.metadata = BenchmarkMetadata(
            benchmark_id="test-123",
            timestamp=datetime.utcnow(),
            duration_seconds=60.0,
            gpu_device_id=0
        )
        
        self.benchmark_result = BenchmarkResult(
            metadata=self.metadata,
            gpu_device=self.gpu_device,
            health_score=self.health_score
        )
    
    def tearDown(self):
        """Clean up test fixtures."""
        shutil.rmtree(self.temp_dir)
    
    def test_save_benchmark_result(self):
        """Test saving benchmark results."""
        result_id = self.repository.save_benchmark_result(self.benchmark_result)
        
        self.assertEqual(result_id, "test-123")
        
        # Check that file was created
        files = list(Path(self.temp_dir).glob("benchmark_*.json"))
        self.assertEqual(len(files), 1)
    
    def test_load_benchmark_result(self):
        """Test loading benchmark results."""
        # Save result
        result_id = self.repository.save_benchmark_result(self.benchmark_result)
        
        # Load result
        loaded_result = self.repository.load_benchmark_result(result_id)
        
        self.assertIsNotNone(loaded_result)
        self.assertEqual(loaded_result.metadata.benchmark_id, "test-123")
        self.assertEqual(loaded_result.gpu_device.info.name, "Test GPU")
    
    def test_load_nonexistent_result(self):
        """Test loading non-existent benchmark result."""
        result = self.repository.load_benchmark_result("nonexistent")
        self.assertIsNone(result)
    
    def test_list_benchmark_results(self):
        """Test listing benchmark results."""
        # Save multiple results
        self.repository.save_benchmark_result(self.benchmark_result)
        
        # Create another result
        metadata2 = BenchmarkMetadata(
            benchmark_id="test-456",
            timestamp=datetime.utcnow(),
            duration_seconds=30.0,
            gpu_device_id=0
        )
        
        result2 = BenchmarkResult(
            metadata=metadata2,
            gpu_device=self.gpu_device,
            health_score=self.health_score
        )
        
        self.repository.save_benchmark_result(result2)
        
        # List all results
        results = self.repository.list_benchmark_results()
        self.assertEqual(len(results), 2)
        
        # List with limit
        results = self.repository.list_benchmark_results(limit=1)
        self.assertEqual(len(results), 1)
    
    def test_list_benchmark_results_with_filters(self):
        """Test listing benchmark results with filters."""
        # Save result
        self.repository.save_benchmark_result(self.benchmark_result)
        
        # Filter by device ID
        results = self.repository.list_benchmark_results(device_id=0)
        self.assertEqual(len(results), 1)
        
        results = self.repository.list_benchmark_results(device_id=999)
        self.assertEqual(len(results), 0)
    
    def test_delete_benchmark_result(self):
        """Test deleting benchmark results."""
        # Save result
        result_id = self.repository.save_benchmark_result(self.benchmark_result)
        
        # Delete result
        result = self.repository.delete_benchmark_result(result_id)
        self.assertTrue(result)
        
        # Try to load deleted result
        loaded_result = self.repository.load_benchmark_result(result_id)
        self.assertIsNone(loaded_result)
        
        # Delete non-existent result
        result = self.repository.delete_benchmark_result("nonexistent")
        self.assertFalse(result)
    
    def test_get_benchmark_statistics(self):
        """Test getting benchmark statistics."""
        # No results
        stats = self.repository.get_benchmark_statistics()
        self.assertEqual(stats["total_benchmarks"], 0)
        
        # Save result
        self.repository.save_benchmark_result(self.benchmark_result)
        
        # Get statistics
        stats = self.repository.get_benchmark_statistics()
        self.assertEqual(stats["total_benchmarks"], 1)
        self.assertIn("average_health_score", stats)
        self.assertIn("health_score_trend", stats)
    
    def test_export_benchmark_results(self):
        """Test exporting benchmark results."""
        # Save result
        self.repository.save_benchmark_result(self.benchmark_result)
        
        # Export to JSON
        results = self.repository.list_benchmark_results()
        file_path = self.repository.export_benchmark_results(results, "json")
        
        self.assertTrue(Path(file_path).exists())
        
        # Export to CSV
        file_path = self.repository.export_benchmark_results(results, "csv")
        self.assertTrue(Path(file_path).exists())
    
    def test_import_benchmark_results(self):
        """Test importing benchmark results."""
        # Export results first
        self.repository.save_benchmark_result(self.benchmark_result)
        results = self.repository.list_benchmark_results()
        file_path = self.repository.export_benchmark_results(results, "json")
        
        # Import results
        imported_results = self.repository.import_benchmark_results(file_path)
        self.assertEqual(len(imported_results), 1)
        self.assertEqual(imported_results[0].metadata.benchmark_id, "test-123")
    
    def test_get_latest_benchmark_result(self):
        """Test getting latest benchmark result."""
        # No results
        result = self.repository.get_latest_benchmark_result(0)
        self.assertIsNone(result)
        
        # Save result
        self.repository.save_benchmark_result(self.benchmark_result)
        
        # Get latest result
        result = self.repository.get_latest_benchmark_result(0)
        self.assertIsNotNone(result)
        self.assertEqual(result.metadata.benchmark_id, "test-123")
    
    def test_compare_benchmark_results(self):
        """Test comparing benchmark results."""
        # Save two results
        result_id1 = self.repository.save_benchmark_result(self.benchmark_result)
        
        metadata2 = BenchmarkMetadata(
            benchmark_id="test-456",
            timestamp=datetime.utcnow(),
            duration_seconds=30.0,
            gpu_device_id=0
        )
        
        result2 = BenchmarkResult(
            metadata=metadata2,
            gpu_device=self.gpu_device,
            health_score=self.health_score
        )
        
        result_id2 = self.repository.save_benchmark_result(result2)
        
        # Compare results
        comparison = self.repository.compare_benchmark_results(result_id1, result_id2)
        
        self.assertIn("result1_id", comparison)
        self.assertIn("result2_id", comparison)
        self.assertIn("health_comparison", comparison)
        self.assertIn("performance_comparison", comparison)


if __name__ == '__main__':
    unittest.main()
