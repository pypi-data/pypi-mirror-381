"""Run AI Cost Benchmark Use Case.

This use case wraps the AI cost benchmarking functionality for the new architecture.
Note: This currently wraps the legacy AI cost benchmark implementation.
TODO: Fully migrate AI cost benchmarking to new architecture in future iteration.
"""

import logging
from typing import Dict, Any, List, Optional

from ...domain.repositories.gpu_repository import GPURepository


class RunAICostBenchmarkUseCase:
    """Use case for running AI workload cost benchmarks.

    This use case provides AI-specific benchmarking including training time,
    inference time, and energy consumption measurements for various model types.

    Note: Currently wraps the legacy implementation to maintain functionality.
    """

    def __init__(self,
                 gpu_repository: GPURepository,
                 logger: Optional[logging.Logger] = None):
        """Initialize the AI cost benchmark use case.

        Args:
            gpu_repository: Repository for GPU device operations.
            logger: Logger for operations.
        """
        self._gpu_repository = gpu_repository
        self._logger = logger or logging.getLogger(__name__)

    def execute(self,
                device_id: int,
                model_names: List[str],
                export_path: Optional[str] = None) -> Dict[str, Any]:
        """Execute AI cost benchmarks.

        Args:
            device_id: GPU device ID to benchmark.
            model_names: List of model names to benchmark.
            export_path: Optional path to export results.

        Returns:
            Dict containing AI benchmark results.
        """
        try:
            # Import legacy AI cost benchmark
            from ...ai_cost_benchmark import (
                AICostBenchmark,
                create_standard_benchmarks
            )

            self._logger.info(f"Running AI cost benchmarks on device {device_id}")
            self._logger.info(f"Models: {', '.join(model_names)}")

            # Create benchmark instance
            benchmark = AICostBenchmark(device_id=device_id)

            # Get standard model configurations
            all_models = create_standard_benchmarks()

            # Filter selected models
            selected_models = []
            for model_name in model_names:
                matching_models = [
                    m for m in all_models
                    if model_name.lower() in m.name.lower()
                ]
                selected_models.extend(matching_models)

            if not selected_models:
                raise AICostBenchmarkError(
                    f"No valid models selected. Available: resnet, transformer, clip, vit"
                )

            # Run benchmarks
            self._logger.info(f"Running benchmarks for {len(selected_models)} model(s)...")
            results = benchmark.run_full_cost_benchmark(selected_models)

            if not results:
                raise AICostBenchmarkError("No benchmarks completed successfully")

            # Generate report
            report = benchmark.generate_cost_report(results)

            # Get additional metadata
            hardware_info = benchmark.get_hardware_info()
            benchmark_metadata = benchmark.get_benchmark_metadata()
            comparative_analysis = benchmark.generate_comparative_analysis(results)

            # Build comprehensive result
            result = {
                "success": True,
                "device_id": device_id,
                "benchmark_metadata": benchmark_metadata,
                "hardware_info": hardware_info,
                "model_results": self._convert_results_to_dict(results),
                "comparative_analysis": comparative_analysis,
                "report": report
            }

            # Export if requested
            if export_path:
                self._export_results(result, export_path)

            return result

        except Exception as e:
            self._logger.error(f"AI cost benchmark failed: {e}", exc_info=True)
            return {
                "success": False,
                "error": str(e),
                "device_id": device_id
            }

    def _convert_results_to_dict(self, results: Dict) -> Dict[str, Any]:
        """Convert results to dictionary format.

        Args:
            results: Raw results from benchmark.

        Returns:
            Dict representation of results.
        """
        converted = {}
        for model_name, metrics in results.items():
            converted[model_name] = {
                "training_time_seconds": metrics.training_time_seconds,
                "training_energy_wh": metrics.training_energy_wh,
                "inference_time_seconds": metrics.inference_time_seconds,
                "inference_energy_wh": metrics.inference_energy_wh,
                "time_to_accuracy": metrics.time_to_accuracy,
                "training_throughput_samples_per_second": metrics.training_throughput_samples_per_second,
                "inference_throughput_samples_per_second": metrics.inference_throughput_samples_per_second,
                "training_wh_per_sample": metrics.training_wh_per_sample,
                "inference_wh_per_sample": metrics.inference_wh_per_sample,
                "training_cost_per_sample_cents": metrics.training_cost_per_sample_cents,
                "inference_cost_per_sample_cents": metrics.inference_cost_per_sample_cents,
                "total_training_cost_cents": metrics.total_training_cost_cents,
                "total_inference_cost_cents": metrics.total_inference_cost_cents,
                "energy_per_accuracy_point": metrics.energy_per_accuracy_point,
                "time_per_accuracy_point": metrics.time_per_accuracy_point,
                "samples_per_wh": metrics.samples_per_wh,
                "final_accuracy": metrics.final_accuracy,
                "avg_power_watts": metrics.avg_power_watts,
                "peak_power_watts": metrics.peak_power_watts,
                "min_power_watts": metrics.min_power_watts,
                "power_variance": metrics.power_variance,
                "peak_memory_usage_gb": metrics.peak_memory_usage_gb,
                "memory_efficiency_gb_per_sample": metrics.memory_efficiency_gb_per_sample
            }
        return converted

    def _export_results(self, results: Dict[str, Any], filepath: str) -> None:
        """Export results to file.

        Args:
            results: Results to export.
            filepath: Path to export file.
        """
        try:
            import json

            with open(filepath, 'w') as f:
                json.dump(results, f, indent=2)

            self._logger.info(f"Results exported to: {filepath}")

        except Exception as e:
            self._logger.error(f"Failed to export results: {e}")
            raise


class AICostBenchmarkError(Exception):
    """Exception raised when AI cost benchmark operations fail."""
    pass