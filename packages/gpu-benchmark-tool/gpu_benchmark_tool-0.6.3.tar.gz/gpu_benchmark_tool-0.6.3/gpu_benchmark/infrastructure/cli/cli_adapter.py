"""CLI Adapter for new architecture.

This adapter provides the same CLI interface as the original while
using the new domain-driven architecture underneath.
"""

import logging
from typing import Dict, Any, Optional, List
from datetime import datetime

from ...application.di.providers import create_container
from ...application.use_cases.run_benchmark import RunBenchmarkUseCase
from ...application.use_cases.assess_gpu_health import AssessGPUHealthUseCase
from ...domain.models.configuration import BenchmarkConfig, BenchmarkType, UseCase
from ...domain.models.benchmark_result import BenchmarkResult
from ...domain.repositories.gpu_repository import GPURepository
from ...domain.error_handling.error_boundary import with_benchmark_error_boundary


class CLIBenchmarkAdapter:
    """Adapter that provides the same CLI interface using the new architecture.
    
    This class maintains compatibility with the existing CLI while using
    the new domain-driven architecture for all operations.
    """
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """Initialize the CLI adapter.
        
        Args:
            logger: Logger for CLI operations.
        """
        self._logger = logger or logging.getLogger(__name__)
        self._container = create_container(logger=self._logger)
        self._benchmark_use_case = self._container.resolve(RunBenchmarkUseCase)
        self._health_use_case = self._container.resolve(AssessGPUHealthUseCase)

        # Lazy-load diagnostics use case (may not always be needed)
        self._diagnostics_use_case = None
    
    def run_full_benchmark(self, 
                          device_id: int = 0,
                          duration: int = 60,
                          include_ai: bool = False,
                          export_format: str = "json",
                          export_path: Optional[str] = None) -> Dict[str, Any]:
        """Run a full GPU benchmark.
        
        Args:
            device_id: GPU device ID to benchmark.
            duration: Benchmark duration in seconds.
            include_ai: Whether to include AI workload benchmarks.
            export_format: Export format for results.
            export_path: Path to export results.
            
        Returns:
            Dict containing benchmark results.
        """
        try:
            # Create benchmark configuration
            config = BenchmarkConfig(
                benchmark_type=BenchmarkType.STANDARD,
                use_case=UseCase.AI_TRAINING if include_ai else UseCase.GENERAL,
                duration_seconds=duration,
                gpu_device_id=device_id,
                include_ai_benchmarks=include_ai,
                include_stress_tests=True,
                include_health_scoring=True,
                export_results=True,
                export_format=export_format,
                export_path=export_path
            )
            
            # Run benchmark using new architecture
            result = self._benchmark_use_case.execute(
                device_id=device_id,
                config=config,
                export_results=True
            )
            
            # Convert to legacy format for compatibility
            return self._convert_benchmark_result_to_legacy_format(result)
            
        except Exception as e:
            self._logger.error(f"Benchmark failed: {e}")
            return {
                "success": False,
                "error": str(e),
                "gpu_info": {},
                "health_score": {},
                "performance_metrics": {}
            }
    
    def run_quick_benchmark(self, device_id: int = 0) -> Dict[str, Any]:
        """Run a quick GPU benchmark.
        
        Args:
            device_id: GPU device ID to benchmark.
            
        Returns:
            Dict containing benchmark results.
        """
        try:
            # Run quick benchmark using new architecture
            result = self._benchmark_use_case.execute_quick_benchmark(device_id)
            
            # Convert to legacy format
            return self._convert_benchmark_result_to_legacy_format(result)
            
        except Exception as e:
            self._logger.error(f"Quick benchmark failed: {e}")
            return {
                "success": False,
                "error": str(e),
                "gpu_info": {},
                "health_score": {},
                "performance_metrics": {}
            }
    
    def run_comprehensive_benchmark(self, device_id: int = 0) -> Dict[str, Any]:
        """Run a comprehensive GPU benchmark.
        
        Args:
            device_id: GPU device ID to benchmark.
            
        Returns:
            Dict containing benchmark results.
        """
        try:
            # Run comprehensive benchmark using new architecture
            result = self._benchmark_use_case.execute_comprehensive_benchmark(device_id)
            
            # Convert to legacy format
            return self._convert_benchmark_result_to_legacy_format(result)
            
        except Exception as e:
            self._logger.error(f"Comprehensive benchmark failed: {e}")
            return {
                "success": False,
                "error": str(e),
                "gpu_info": {},
                "health_score": {},
                "performance_metrics": {}
            }
    
    def assess_gpu_health(self, device_id: int = 0) -> Dict[str, Any]:
        """Assess GPU health.
        
        Args:
            device_id: GPU device ID to assess.
            
        Returns:
            Dict containing health assessment.
        """
        try:
            # Assess health using new architecture
            health_score = self._health_use_case.execute(device_id)
            
            # Convert to legacy format
            return self._convert_health_score_to_legacy_format(health_score)
            
        except Exception as e:
            self._logger.error(f"Health assessment failed: {e}")
            return {
                "score": 0,
                "status": "unknown",
                "recommendation": f"Health assessment failed: {e}",
                "details": {
                    "breakdown": {},
                    "specific_recommendations": []
                }
            }
    
    def get_gpu_info(self, device_id: int = 0) -> Dict[str, Any]:
        """Get GPU information.
        
        Args:
            device_id: GPU device ID.
            
        Returns:
            Dict containing GPU information.
        """
        try:
            gpu_repository = self._container.resolve(GPURepository)
            device = gpu_repository.get_device_by_id(device_id)
            
            if not device:
                return {
                    "name": "Unknown GPU",
                    "device_id": device_id,
                    "gpu_type": "unknown",
                    "memory_total_mb": 0,
                    "memory_used_mb": 0,
                    "driver_version": "Unknown",
                    "cuda_version": "Unknown",
                    "is_mock": True
                }
            
            return {
                "name": device.info.name,
                "device_id": device.info.device_id,
                "gpu_type": device.info.gpu_type.value,
                "memory_total_mb": device.info.memory_total_mb,
                "memory_used_mb": device.info.memory_used_mb,
                "driver_version": device.info.driver_version or "Unknown",
                "cuda_version": device.info.cuda_version or "Unknown",
                "is_mock": device.info.is_mock
            }
            
        except Exception as e:
            self._logger.error(f"Failed to get GPU info: {e}")
            return {
                "name": "Error",
                "device_id": device_id,
                "gpu_type": "unknown",
                "memory_total_mb": 0,
                "memory_used_mb": 0,
                "driver_version": "Error",
                "cuda_version": "Error",
                "is_mock": True
            }
    
    def get_available_devices(self) -> List[Dict[str, Any]]:
        """Get list of available GPU devices.
        
        Returns:
            List of device information dictionaries.
        """
        try:
            gpu_repository = self._container.resolve(GPURepository)
            devices = gpu_repository.get_available_devices()
            
            return [
                {
                    "name": device.info.name,
                    "device_id": device.info.device_id,
                    "gpu_type": device.info.gpu_type.value,
                    "memory_total_mb": device.info.memory_total_mb,
                    "memory_used_mb": device.info.memory_used_mb,
                    "driver_version": device.info.driver_version or "Unknown",
                    "cuda_version": device.info.cuda_version or "Unknown",
                    "is_mock": device.info.is_mock,
                    "status": device.status.value,
                    "is_available": device.is_available()
                }
                for device in devices
            ]
            
        except Exception as e:
            self._logger.error(f"Failed to get available devices: {e}")
            return []
    
    def _convert_benchmark_result_to_legacy_format(self, result) -> Dict[str, Any]:
        """Convert new benchmark result to legacy format for CLI compatibility."""
        return {
            "success": result.is_successful(),
            "gpu_info": {
                "name": result.gpu_device.info.name,
                "device_id": result.gpu_device.info.device_id,
                "gpu_type": result.gpu_device.info.gpu_type.value,
                "memory_total_mb": result.gpu_device.info.memory_total_mb,
                "memory_used_mb": result.gpu_device.info.memory_used_mb,
                "driver_version": result.gpu_device.info.driver_version or "Unknown",
                "cuda_version": result.gpu_device.info.cuda_version or "Unknown",
                "is_mock": result.gpu_device.info.is_mock
            },
            "health_score": self._convert_health_score_to_legacy_format(result.health_score),
            "performance_metrics": result.performance_metrics or {},
            "stress_test_results": result.stress_test_results or {},
            "warnings": result.warnings,
            "errors": result.errors,
            "duration_seconds": result.metadata.duration_seconds,
            "timestamp": result.metadata.timestamp.isoformat()
        }
    
    def _convert_health_score_to_legacy_format(self, health_score) -> Dict[str, Any]:
        """Convert new health score to legacy format for CLI compatibility."""
        return {
            "score": health_score.score,
            "status": health_score.status.value,
            "recommendation": health_score.recommendation,
            "details": {
                "breakdown": health_score.breakdown.to_dict(),
                "specific_recommendations": health_score.specific_recommendations
            }
        }
    
    def get_benchmark_history(self, device_id: int, limit: int = 10) -> List[Dict[str, Any]]:
        """Get benchmark history for a device.
        
        Args:
            device_id: GPU device ID.
            limit: Maximum number of results to return.
            
        Returns:
            List of benchmark result dictionaries.
        """
        try:
            results = self._benchmark_use_case.get_benchmark_history(device_id, limit)
            return [self._convert_benchmark_result_to_legacy_format(result) for result in results]
            
        except Exception as e:
            self._logger.error(f"Failed to get benchmark history: {e}")
            return []
    
    def compare_benchmarks(self, benchmark_id1: str, benchmark_id2: str) -> Dict[str, Any]:
        """Compare two benchmark results.
        
        Args:
            benchmark_id1: ID of the first benchmark.
            benchmark_id2: ID of the second benchmark.
            
        Returns:
            Dict containing comparison data.
        """
        try:
            return self._benchmark_use_case.compare_benchmarks(benchmark_id1, benchmark_id2)
            
        except Exception as e:
            self._logger.error(f"Failed to compare benchmarks: {e}")
            return {
                "error": str(e),
                "result1_id": benchmark_id1,
                "result2_id": benchmark_id2
            }

    def run_multi_gpu_benchmark(self,
                                duration: int = 60,
                                enhanced: bool = True,
                                export_results: bool = False) -> Dict[str, Any]:
        """Run benchmarks on all available GPUs.

        Args:
            duration: Benchmark duration in seconds.
            enhanced: Whether to run enhanced benchmarks.
            export_results: Whether to save results.

        Returns:
            Dict containing results for all GPUs with summary.
        """
        try:
            # Run multi-GPU benchmark using new architecture
            results = self._benchmark_use_case.execute_multi_gpu_benchmark(
                duration=duration,
                enhanced=enhanced,
                export_results=export_results
            )

            # Convert results to legacy format for CLI compatibility
            if "results" in results and isinstance(results["results"], dict):
                converted_results = {}
                for device_id, result in results["results"].items():
                    if isinstance(result, BenchmarkResult):
                        converted_results[device_id] = self._convert_benchmark_result_to_legacy_format(result)
                    else:
                        # Already a dict (likely an error result)
                        converted_results[device_id] = result

                results["results"] = converted_results

            return results

        except Exception as e:
            self._logger.error(f"Multi-GPU benchmark failed: {e}")
            return {
                "error": str(e),
                "device_count": 0,
                "results": {}
            }

    def export_results(self, results: Dict[str, Any], filename: Optional[str] = None) -> str:
        """Export benchmark results to JSON file.

        Args:
            results: Benchmark results to export.
            filename: Optional output filename. If None, generates timestamped name.

        Returns:
            str: The filename to which results were exported.
        """
        try:
            import json
            from datetime import datetime

            if filename is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"gpu_benchmark_{timestamp}.json"

            # Convert any non-serializable objects
            serializable_results = self._make_serializable(results)

            with open(filename, 'w') as f:
                json.dump(serializable_results, f, indent=2)

            self._logger.info(f"Results exported to {filename}")
            return filename

        except Exception as e:
            self._logger.error(f"Failed to export results: {e}")
            raise

    def _make_serializable(self, obj: Any) -> Any:
        """Convert objects to JSON-serializable format.

        Args:
            obj: Object to convert.

        Returns:
            JSON-serializable version of the object.
        """
        if isinstance(obj, dict):
            return {k: self._make_serializable(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._make_serializable(item) for item in obj]
        elif hasattr(obj, 'to_dict'):
            return obj.to_dict()
        elif hasattr(obj, '__dict__'):
            return self._make_serializable(obj.__dict__)
        elif isinstance(obj, (str, int, float, bool, type(None))):
            return obj
        else:
            return str(obj)

    def run_diagnostics(self) -> Dict[str, Any]:
        """Run comprehensive diagnostics.

        Returns:
            Dict containing diagnostic information.
        """
        try:
            # Lazy-load diagnostics use case
            if self._diagnostics_use_case is None:
                from ...application.use_cases.run_diagnostics import RunDiagnosticsUseCase
                self._diagnostics_use_case = self._container.resolve(RunDiagnosticsUseCase)

            # Run diagnostics
            return self._diagnostics_use_case.run_comprehensive_diagnostics()

        except Exception as e:
            self._logger.error(f"Diagnostics failed: {e}")
            return {
                "error": str(e),
                "system": {},
                "gpus": [],
                "backends": {}
            }
