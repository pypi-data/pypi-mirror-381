"""Stress Test Adapter.

This adapter wraps the legacy stress test infrastructure to work with
the new domain-driven architecture.
"""

import logging
from typing import Dict, Any, Optional
from datetime import datetime

try:
    import torch
    TORCH_AVAILABLE = True
except ImportError:
    TORCH_AVAILABLE = False


class StressTestAdapter:
    """Adapter for running GPU stress tests.

    This adapter bridges the legacy stress test modules with the new architecture,
    providing a clean interface for running compute, memory, and mixed precision tests.
    """

    def __init__(self, logger: Optional[logging.Logger] = None):
        """Initialize the stress test adapter.

        Args:
            logger: Logger for operations.
        """
        self._logger = logger or logging.getLogger(__name__)

    def run_stress_tests(self,
                        device_id: int,
                        duration: float = 60,
                        monitor = None) -> Dict[str, Any]:
        """Run comprehensive stress tests on a GPU device.

        Args:
            device_id: GPU device ID to test.
            duration: Duration of stress tests in seconds.
            monitor: GPU monitor object (from backend).

        Returns:
            Dict containing stress test results.
        """
        if not TORCH_AVAILABLE:
            self._logger.warning("PyTorch not available, cannot run stress tests")
            return self._get_fallback_results()

        try:
            # Import legacy stress test infrastructure
            from ...monitor import enhanced_stress_test

            if monitor is None:
                self._logger.warning("No monitor provided, using fallback results")
                return self._get_fallback_results()

            # Run the legacy enhanced stress test
            self._logger.info(f"Running stress tests on device {device_id} for {duration}s")
            results = enhanced_stress_test(monitor, duration, device_id)

            # Transform results to match new architecture format
            return self._transform_stress_test_results(results)

        except Exception as e:
            self._logger.error(f"Stress test failed: {e}", exc_info=True)
            return self._get_fallback_results(error=str(e))

    def _transform_stress_test_results(self, legacy_results: Dict[str, Any]) -> Dict[str, Any]:
        """Transform legacy stress test results to new format.

        Args:
            legacy_results: Results from legacy enhanced_stress_test().

        Returns:
            Transformed results matching new architecture format.
        """
        # Extract stress test results from legacy format
        stress_test_results = legacy_results.get("stress_test_results", {})

        # Get telemetry data
        max_temp = legacy_results.get("max_temp", 0)
        max_power = legacy_results.get("max_power", 0)
        avg_utilization = legacy_results.get("avg_utilization", 0)
        throttle_events = legacy_results.get("throttle_events", [])
        errors = legacy_results.get("errors", [])

        # Build transformed result
        transformed = {
            "compute_test": self._extract_compute_results(stress_test_results),
            "memory_test": self._extract_memory_results(stress_test_results),
            "mixed_precision_test": self._extract_mixed_precision_results(stress_test_results),
            "telemetry": {
                "max_temperature": max_temp,
                "max_power_watts": max_power,
                "average_utilization": avg_utilization,
                "throttle_events_count": len(throttle_events),
                "errors_count": len(errors),
                "throttle_events": throttle_events,
                "errors": errors
            },
            "baseline_metrics": {
                "baseline_temp": legacy_results.get("baseline_temp", 0),
                "baseline_power": legacy_results.get("baseline_power", 0)
            },
            "stability": {
                "temperature_stability": legacy_results.get("temperature_stability", {}),
                "throttled": len(throttle_events) > 0,
                "has_errors": len(errors) > 0
            }
        }

        return transformed

    def _extract_compute_results(self, stress_results: Dict[str, Any]) -> Dict[str, Any]:
        """Extract compute test results."""
        matrix_mult = stress_results.get("matrix_multiply", {})

        if not matrix_mult:
            return {"status": "not_run"}

        return {
            "status": "success" if matrix_mult.get("tflops", 0) > 0 else "failed",
            "tflops": matrix_mult.get("tflops", 0),
            "iterations": matrix_mult.get("iterations", 0),
            "avg_time_per_iter": matrix_mult.get("avg_time_per_iter", 0),
            "matrix_size": matrix_mult.get("matrix_size", 0)
        }

    def _extract_memory_results(self, stress_results: Dict[str, Any]) -> Dict[str, Any]:
        """Extract memory test results."""
        memory_bw = stress_results.get("memory_bandwidth", {})
        vram_stress = stress_results.get("vram_stress", {})

        result = {
            "status": "success" if memory_bw or vram_stress else "not_run"
        }

        if memory_bw:
            result.update({
                "bandwidth_gbps": memory_bw.get("bandwidth_gbps", 0),
                "read_bandwidth": memory_bw.get("read_bandwidth", 0),
                "write_bandwidth": memory_bw.get("write_bandwidth", 0)
            })

        if vram_stress:
            result.update({
                "vram_status": vram_stress.get("status", "unknown"),
                "allocations_successful": vram_stress.get("allocations_successful", 0),
                "peak_memory_gb": vram_stress.get("peak_memory_gb", 0)
            })

        return result

    def _extract_mixed_precision_results(self, stress_results: Dict[str, Any]) -> Dict[str, Any]:
        """Extract mixed precision test results."""
        mixed_precision = stress_results.get("mixed_precision", {})

        if not mixed_precision:
            return {"status": "not_run"}

        result = {
            "status": "success",
            "fp32": mixed_precision.get("fp32", {}),
            "fp16": mixed_precision.get("fp16", {}),
            "bf16": mixed_precision.get("bf16", {}),
            "int8": mixed_precision.get("int8", {})
        }

        # Add speedup metrics if available
        if "fp16_speedup" in mixed_precision:
            result["fp16_speedup"] = mixed_precision["fp16_speedup"]
        if "bf16_speedup" in mixed_precision:
            result["bf16_speedup"] = mixed_precision["bf16_speedup"]
        if "int8_speedup" in mixed_precision:
            result["int8_speedup"] = mixed_precision["int8_speedup"]

        return result

    def _get_fallback_results(self, error: Optional[str] = None) -> Dict[str, Any]:
        """Get fallback results when stress tests cannot run.

        Args:
            error: Optional error message.

        Returns:
            Fallback results structure.
        """
        return {
            "compute_test": {
                "status": "not_available",
                "error": error or "PyTorch not available or no GPU monitor"
            },
            "memory_test": {
                "status": "not_available"
            },
            "mixed_precision_test": {
                "status": "not_available"
            },
            "telemetry": {
                "max_temperature": 0,
                "max_power_watts": 0,
                "average_utilization": 0,
                "throttle_events_count": 0,
                "errors_count": 0,
                "throttle_events": [],
                "errors": []
            },
            "baseline_metrics": {
                "baseline_temp": 0,
                "baseline_power": 0
            },
            "stability": {
                "temperature_stability": {},
                "throttled": False,
                "has_errors": False
            }
        }