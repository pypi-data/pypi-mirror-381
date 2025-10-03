"""Run Benchmark Use Case.

This use case handles the complete benchmark workflow including
GPU detection, stress testing, health scoring, and result storage.
"""

import uuid
import logging
from datetime import datetime
from typing import Optional, Dict, Any

from ...domain.models.gpu_device import GPUDevice
from ...domain.models.benchmark_result import BenchmarkResult, BenchmarkMetadata, BenchmarkStatus
from ...domain.models.configuration import BenchmarkConfig
from ...domain.repositories.gpu_repository import GPURepository
from ...domain.repositories.benchmark_repository import BenchmarkRepository
from ...domain.repositories.configuration_repository import ConfigurationRepository
from ...domain.services.health_scoring_service import HealthScoringService
from ...infrastructure.adapters.stress_test_adapter import StressTestAdapter


class RunBenchmarkUseCase:
    """Use case for running complete GPU benchmarks.
    
    This use case orchestrates the entire benchmark process including
    GPU detection, stress testing, health assessment, and result storage.
    """
    
    def __init__(self,
                 gpu_repository: GPURepository,
                 benchmark_repository: BenchmarkRepository,
                 configuration_repository: ConfigurationRepository,
                 health_scoring_service: HealthScoringService,
                 logger: Optional[logging.Logger] = None):
        """Initialize the use case.

        Args:
            gpu_repository: Repository for GPU device operations.
            benchmark_repository: Repository for benchmark results.
            configuration_repository: Repository for configuration data.
            health_scoring_service: Service for health score calculations.
            logger: Logger for operations.
        """
        self._gpu_repository = gpu_repository
        self._benchmark_repository = benchmark_repository
        self._configuration_repository = configuration_repository
        self._health_scoring_service = health_scoring_service
        self._logger = logger or logging.getLogger(__name__)
        self._stress_test_adapter = StressTestAdapter(logger=self._logger)
    
    def execute(self, 
                device_id: int,
                config: Optional[BenchmarkConfig] = None,
                export_results: bool = True) -> BenchmarkResult:
        """Execute a complete GPU benchmark.
        
        Args:
            device_id: The GPU device ID to benchmark.
            config: Optional benchmark configuration. If None, uses defaults.
            export_results: Whether to save results to repository.
            
        Returns:
            BenchmarkResult: The complete benchmark result.
            
        Raises:
            BenchmarkError: If benchmark execution fails.
        """
        try:
            # Use default config if none provided
            if config is None:
                config = self._configuration_repository.get_default_benchmark_config()
            
            # Validate configuration
            validation_errors = self._configuration_repository.validate_configuration(config)
            if validation_errors:
                raise BenchmarkError(f"Invalid configuration: {', '.join(validation_errors)}")
            
            # Get GPU device
            gpu_device = self._gpu_repository.get_device_by_id(device_id)
            if not gpu_device:
                raise BenchmarkError(f"GPU device {device_id} not found")
            
            # Check if device is available
            if not gpu_device.is_available():
                raise BenchmarkError(f"GPU device {device_id} is not available for benchmarking")
            
            # Create benchmark metadata
            benchmark_id = str(uuid.uuid4())
            start_time = datetime.utcnow()
            
            metadata = BenchmarkMetadata(
                benchmark_id=benchmark_id,
                version="1.0.0",
                timestamp=start_time,
                duration_seconds=0.0,  # Will be updated at the end
                gpu_device_id=device_id,
                benchmark_type=config.benchmark_type.value,
                configuration=config.to_dict()
            )
            
            # Initialize result
            result = BenchmarkResult(
                metadata=metadata,
                gpu_device=gpu_device,
                health_score=None,  # Will be calculated
                status=BenchmarkStatus.SUCCESS
            )
            
            # Execute benchmark steps
            try:
                # Step 1: Collect baseline GPU info
                self._collect_baseline_info(result)
                
                # Step 2: Run stress tests if configured
                if config.include_stress_tests:
                    self._run_stress_tests(result, config)
                
                # Step 3: Calculate health score if configured
                if config.include_health_scoring:
                    self._calculate_health_score(result)
                
                # Step 4: Update metadata with final duration
                end_time = datetime.utcnow()
                duration = (end_time - start_time).total_seconds()
                
                # Create updated metadata
                updated_metadata = BenchmarkMetadata(
                    benchmark_id=metadata.benchmark_id,
                    version=metadata.version,
                    timestamp=metadata.timestamp,
                    duration_seconds=duration,
                    gpu_device_id=metadata.gpu_device_id,
                    benchmark_type=metadata.benchmark_type,
                    configuration=metadata.configuration
                )
                
                # Update result with new metadata
                result = BenchmarkResult(
                    metadata=updated_metadata,
                    gpu_device=result.gpu_device,
                    health_score=result.health_score,
                    stress_test_results=result.stress_test_results,
                    performance_metrics=result.performance_metrics,
                    warnings=result.warnings,
                    errors=result.errors,
                    status=result.status
                )
                
            except Exception as e:
                # Mark as partial success if we got some data
                if result.health_score or result.stress_test_results:
                    result.status = BenchmarkStatus.PARTIAL_SUCCESS
                    result.add_warning(f"Benchmark completed with errors: {e}")
                else:
                    result.status = BenchmarkStatus.FAILED
                    result.add_error(f"Benchmark failed: {e}")
            
            # Save results if requested
            if export_results:
                try:
                    saved_id = self._benchmark_repository.save_benchmark_result(result)
                    result.add_warning(f"Results saved with ID: {saved_id}")
                except Exception as e:
                    result.add_warning(f"Failed to save results: {e}")
            
            return result
            
        except Exception as e:
            if isinstance(e, BenchmarkError):
                raise
            else:
                raise BenchmarkError(f"Benchmark execution failed: {e}") from e
    
    def execute_quick_benchmark(self, device_id: int) -> BenchmarkResult:
        """Execute a quick benchmark with minimal configuration.
        
        Args:
            device_id: The GPU device ID to benchmark.
            
        Returns:
            BenchmarkResult: The benchmark result.
        """
        # Create quick benchmark configuration
        from ...domain.models.configuration import BenchmarkConfig, BenchmarkType
        
        quick_config = BenchmarkConfig(
            benchmark_type=BenchmarkType.QUICK,
            duration_seconds=30,
            include_stress_tests=True,
            include_health_scoring=True,
            include_ai_benchmarks=False
        )
        
        return self.execute(device_id, config=quick_config)
    
    def execute_comprehensive_benchmark(self, device_id: int) -> BenchmarkResult:
        """Execute a comprehensive benchmark with full testing.
        
        Args:
            device_id: The GPU device ID to benchmark.
            
        Returns:
            BenchmarkResult: The benchmark result.
        """
        # Create comprehensive benchmark configuration
        from ...domain.models.configuration import BenchmarkConfig, BenchmarkType
        
        comprehensive_config = BenchmarkConfig(
            benchmark_type=BenchmarkType.COMPREHENSIVE,
            duration_seconds=120,
            include_stress_tests=True,
            include_health_scoring=True,
            include_ai_benchmarks=True
        )
        
        return self.execute(device_id, config=comprehensive_config)
    
    def _collect_baseline_info(self, result: BenchmarkResult) -> None:
        """Collect baseline GPU information."""
        try:
            # Update GPU metrics if available
            gpu_device = result.gpu_device
            if gpu_device.current_metrics:
                # Metrics already available
                pass
            else:
                # Try to get current metrics
                try:
                    # This would typically call the GPU backend to get current metrics
                    # For now, we'll add a warning that no current metrics are available
                    result.add_warning("No current GPU metrics available")
                except Exception as e:
                    result.add_warning(f"Could not collect current GPU metrics: {e}")
            
        except Exception as e:
            result.add_warning(f"Baseline info collection failed: {e}")
    
    def _run_stress_tests(self, result: BenchmarkResult, config: BenchmarkConfig) -> None:
        """Run stress tests on the GPU."""
        try:
            device_id = result.gpu_device.info.device_id

            # Get a monitor for the GPU from the backend
            monitor = self._get_gpu_monitor(device_id)

            if monitor is None:
                result.add_warning("No GPU monitor available, skipping stress tests")
                return

            # Run real stress tests using the adapter
            self._logger.info(f"Running stress tests on device {device_id} for {config.duration_seconds}s")
            stress_test_results = self._stress_test_adapter.run_stress_tests(
                device_id=device_id,
                duration=config.duration_seconds,
                monitor=monitor
            )

            # Store results
            result.stress_test_results = stress_test_results

            # Update performance metrics from stress test results
            if stress_test_results.get("compute_test", {}).get("status") == "success":
                result.performance_metrics = {
                    "compute_tflops": stress_test_results["compute_test"].get("tflops", 0),
                    "memory_bandwidth_gbps": stress_test_results.get("memory_test", {}).get("bandwidth_gbps", 0),
                    "mixed_precision_support": stress_test_results.get("mixed_precision_test", {})
                }

            # Update GPU device with latest metrics from telemetry
            telemetry = stress_test_results.get("telemetry", {})
            if telemetry:
                self._update_gpu_metrics_from_telemetry(result.gpu_device, telemetry)

            self._logger.info(f"Stress tests completed successfully for device {device_id}")

        except Exception as e:
            self._logger.error(f"Stress test execution failed: {e}", exc_info=True)
            result.add_warning(f"Stress test execution failed: {e}")
    
    def _calculate_health_score(self, result: BenchmarkResult) -> None:
        """Calculate health score for the GPU."""
        try:
            health_score = self._health_scoring_service.calculate_health_score(
                gpu_device=result.gpu_device,
                stress_test_results=result.stress_test_results,
                baseline_metrics=None
            )

            result.health_score = health_score

        except Exception as e:
            self._logger.error(f"Health score calculation failed: {e}", exc_info=True)
            result.add_warning(f"Health score calculation failed: {e}")

    def _get_gpu_monitor(self, device_id: int):
        """Get a GPU monitor for the specified device.

        Args:
            device_id: GPU device ID.

        Returns:
            GPU monitor object or None if not available.
        """
        try:
            # Check if GPUBackendAdapter is available and has the method
            if hasattr(self._gpu_repository, '_backends'):
                # Get the backend for this device
                device = self._gpu_repository.get_device_by_id(device_id)
                if not device:
                    return None

                # Map GPU type to backend name
                backend_map = {
                    "nvidia": "nvidia",
                    "amd": "amd",
                    "intel": "intel",
                    "mock": "mock"
                }

                backend_name = backend_map.get(device.info.gpu_type.value)
                if not backend_name:
                    return None

                # Get the backend and create monitor
                backends = self._gpu_repository._backends
                if backend_name in backends:
                    backend = backends[backend_name]
                    monitor = backend.create_monitor(device_id)
                    return monitor

            return None

        except Exception as e:
            self._logger.error(f"Failed to get GPU monitor: {e}", exc_info=True)
            return None

    def _update_gpu_metrics_from_telemetry(self, gpu_device: GPUDevice, telemetry: Dict[str, Any]) -> None:
        """Update GPU device metrics from stress test telemetry.

        Args:
            gpu_device: GPU device to update.
            telemetry: Telemetry data from stress tests.
        """
        try:
            from ...domain.models.gpu_device import GPUMetrics

            # Create metrics from telemetry
            metrics = GPUMetrics(
                temperature_celsius=telemetry.get("max_temperature", 0),
                power_usage_watts=telemetry.get("max_power_watts", 0),
                utilization_percent=telemetry.get("average_utilization", 0),
                fan_speed_percent=None,
                clock_speed_mhz=None,
                memory_clock_mhz=None,
                timestamp=datetime.utcnow()
            )

            # Update device
            gpu_device.update_metrics(metrics)

        except Exception as e:
            self._logger.warning(f"Failed to update GPU metrics: {e}")
    
    def get_benchmark_history(self, device_id: int, limit: int = 10) -> list:
        """Get benchmark history for a device.
        
        Args:
            device_id: The GPU device ID.
            limit: Maximum number of results to return.
            
        Returns:
            list: List of benchmark results.
        """
        try:
            return self._benchmark_repository.list_benchmark_results(
                device_id=device_id,
                limit=limit
            )
        except Exception as e:
            raise BenchmarkError(f"Failed to get benchmark history: {e}") from e
    
    def compare_benchmarks(self, benchmark_id1: str, benchmark_id2: str) -> Dict[str, Any]:
        """Compare two benchmark results.

        Args:
            benchmark_id1: ID of the first benchmark.
            benchmark_id2: ID of the second benchmark.

        Returns:
            Dict[str, Any]: Comparison data.
        """
        try:
            return self._benchmark_repository.compare_benchmark_results(
                benchmark_id1, benchmark_id2
            )
        except Exception as e:
            raise BenchmarkError(f"Failed to compare benchmarks: {e}") from e

    def execute_multi_gpu_benchmark(self,
                                    duration: int = 60,
                                    enhanced: bool = True,
                                    export_results: bool = False) -> Dict[str, Any]:
        """Execute benchmarks on all available GPUs.

        Args:
            duration: Benchmark duration in seconds.
            enhanced: Whether to run enhanced benchmarks.
            export_results: Whether to save results.

        Returns:
            Dict containing results for all GPUs with summary.
        """
        try:
            # Get all available devices
            devices = self._gpu_repository.get_available_devices()
            device_count = len(devices)

            if device_count == 0:
                return {
                    "error": "No GPU devices found",
                    "device_count": 0,
                    "results": {}
                }

            self._logger.info(f"Running multi-GPU benchmark on {device_count} device(s)")

            # Create configuration
            from ...domain.models.configuration import BenchmarkConfig, BenchmarkType, UseCase

            config = BenchmarkConfig(
                benchmark_type=BenchmarkType.STANDARD if not enhanced else BenchmarkType.COMPREHENSIVE,
                use_case=UseCase.GENERAL,
                duration_seconds=duration,
                include_stress_tests=enhanced,
                include_health_scoring=True,
                include_ai_benchmarks=False,
                export_results=export_results
            )

            # Run benchmark on each device
            results = {}
            for device in devices:
                device_id = device.info.device_id
                self._logger.info(f"Benchmarking GPU {device_id}: {device.info.name}")

                try:
                    result = self.execute(device_id=device_id, config=config, export_results=export_results)
                    results[device_id] = result
                except Exception as e:
                    self._logger.error(f"Benchmark failed for GPU {device_id}: {e}")
                    results[device_id] = {
                        "error": str(e),
                        "device_id": device_id,
                        "device_name": device.info.name
                    }

            # Generate summary
            summary = self._generate_multi_gpu_summary(results, device_count)

            return {
                "device_count": device_count,
                "results": results,
                "summary": summary
            }

        except Exception as e:
            self._logger.error(f"Multi-GPU benchmark failed: {e}", exc_info=True)
            return {
                "error": f"Multi-GPU benchmark failed: {e}",
                "device_count": 0,
                "results": {}
            }

    def _generate_multi_gpu_summary(self, results: Dict, device_count: int) -> Dict[str, Any]:
        """Generate summary statistics for multi-GPU benchmark.

        Args:
            results: Dictionary of benchmark results keyed by device_id.
            device_count: Total number of devices.

        Returns:
            Summary dictionary.
        """
        healthy_count = 0
        total_score = 0
        warnings = []

        for device_id, result in results.items():
            # Handle error results
            if isinstance(result, dict) and "error" in result:
                warnings.append(f"GPU {device_id}: Benchmark failed - {result['error']}")
                continue

            # Count healthy GPUs and accumulate scores
            if hasattr(result, 'health_score') and result.health_score:
                score = result.health_score.score
                total_score += score

                if score >= 70:  # Threshold for "healthy"
                    healthy_count += 1
                elif score < 55:
                    warnings.append(f"GPU {device_id}: Health score below recommended threshold ({score}/100)")

        # Calculate percentage
        health_percentage = (healthy_count / device_count * 100) if device_count > 0 else 0

        return {
            "total_gpus": device_count,
            "healthy_gpus": healthy_count,
            "health_percentage": health_percentage,
            "average_score": total_score / device_count if device_count > 0 else 0,
            "warnings": warnings
        }


# Custom exceptions
class BenchmarkError(Exception):
    """Raised when benchmark operations fail."""
    pass
