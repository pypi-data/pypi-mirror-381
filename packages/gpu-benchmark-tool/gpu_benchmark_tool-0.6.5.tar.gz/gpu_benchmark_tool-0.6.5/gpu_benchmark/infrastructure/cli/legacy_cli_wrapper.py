"""Legacy CLI Wrapper.

This wrapper maintains the exact same CLI interface as the original
while using the new architecture underneath.
"""

import logging
from typing import Dict, Any, Optional, List

from .cli_adapter import CLIBenchmarkAdapter


class LegacyCLIWrapper:
    """Wrapper that maintains the exact same CLI interface as the original.
    
    This class provides the same function signatures and return formats
    as the original CLI functions, but uses the new architecture underneath.
    """
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """Initialize the legacy CLI wrapper.
        
        Args:
            logger: Logger for CLI operations.
        """
        self._logger = logger or logging.getLogger(__name__)
        self._adapter = CLIBenchmarkAdapter(logger)
    
    # Maintain the exact same function signatures as the original CLI
    
    def run_full_benchmark(self, 
                          device_id: int = 0,
                          duration: int = 60,
                          include_ai: bool = False,
                          export_format: str = "json",
                          export_path: Optional[str] = None) -> Dict[str, Any]:
        """Run a full GPU benchmark - same interface as original."""
        return self._adapter.run_full_benchmark(
            device_id=device_id,
            duration=duration,
            include_ai=include_ai,
            export_format=export_format,
            export_path=export_path
        )
    
    def run_quick_benchmark(self, device_id: int = 0) -> Dict[str, Any]:
        """Run a quick GPU benchmark - same interface as original."""
        return self._adapter.run_quick_benchmark(device_id)
    
    def run_comprehensive_benchmark(self, device_id: int = 0) -> Dict[str, Any]:
        """Run a comprehensive GPU benchmark - same interface as original."""
        return self._adapter.run_comprehensive_benchmark(device_id)
    
    def assess_gpu_health(self, device_id: int = 0) -> Dict[str, Any]:
        """Assess GPU health - same interface as original."""
        return self._adapter.assess_gpu_health(device_id)
    
    def get_gpu_info(self, device_id: int = 0) -> Dict[str, Any]:
        """Get GPU information - same interface as original."""
        return self._adapter.get_gpu_info(device_id)
    
    def get_available_devices(self) -> List[Dict[str, Any]]:
        """Get list of available GPU devices - same interface as original."""
        return self._adapter.get_available_devices()
    
    def get_benchmark_history(self, device_id: int, limit: int = 10) -> List[Dict[str, Any]]:
        """Get benchmark history - same interface as original."""
        return self._adapter.get_benchmark_history(device_id, limit)
    
    def compare_benchmarks(self, benchmark_id1: str, benchmark_id2: str) -> Dict[str, Any]:
        """Compare benchmark results - same interface as original."""
        return self._adapter.compare_benchmarks(benchmark_id1, benchmark_id2)

    def run_multi_gpu_benchmark(self,
                                duration: int = 60,
                                enhanced: bool = True,
                                export_results: bool = False) -> Dict[str, Any]:
        """Run benchmarks on all available GPUs - same interface as original."""
        return self._adapter.run_multi_gpu_benchmark(
            duration=duration,
            enhanced=enhanced,
            export_results=export_results
        )

    def export_results(self, results: Dict[str, Any], filename: Optional[str] = None) -> str:
        """Export benchmark results to JSON file - same interface as original."""
        return self._adapter.export_results(results, filename)


# Create a global instance for easy import
_legacy_cli_wrapper = None

def get_legacy_cli_wrapper(logger: Optional[logging.Logger] = None) -> LegacyCLIWrapper:
    """Get the global legacy CLI wrapper instance.
    
    Args:
        logger: Logger for CLI operations.
        
    Returns:
        LegacyCLIWrapper: The global CLI wrapper instance.
    """
    global _legacy_cli_wrapper
    if _legacy_cli_wrapper is None:
        _legacy_cli_wrapper = LegacyCLIWrapper(logger)
    return _legacy_cli_wrapper


# Convenience functions that maintain the exact same interface as the original
def run_full_benchmark(device_id: int = 0,
                      duration: int = 60,
                      include_ai: bool = False,
                      export_format: str = "json",
                      export_path: Optional[str] = None) -> Dict[str, Any]:
    """Run a full GPU benchmark - same interface as original."""
    return get_legacy_cli_wrapper().run_full_benchmark(
        device_id=device_id,
        duration=duration,
        include_ai=include_ai,
        export_format=export_format,
        export_path=export_path
    )


def run_quick_benchmark(device_id: int = 0) -> Dict[str, Any]:
    """Run a quick GPU benchmark - same interface as original."""
    return get_legacy_cli_wrapper().run_quick_benchmark(device_id)


def run_comprehensive_benchmark(device_id: int = 0) -> Dict[str, Any]:
    """Run a comprehensive GPU benchmark - same interface as original."""
    return get_legacy_cli_wrapper().run_comprehensive_benchmark(device_id)


def assess_gpu_health(device_id: int = 0) -> Dict[str, Any]:
    """Assess GPU health - same interface as original."""
    return get_legacy_cli_wrapper().assess_gpu_health(device_id)


def get_gpu_info(device_id: int = 0) -> Dict[str, Any]:
    """Get GPU information - same interface as original."""
    return get_legacy_cli_wrapper().get_gpu_info(device_id)


def get_available_devices() -> List[Dict[str, Any]]:
    """Get list of available GPU devices - same interface as original."""
    return get_legacy_cli_wrapper().get_available_devices()


def get_benchmark_history(device_id: int, limit: int = 10) -> List[Dict[str, Any]]:
    """Get benchmark history - same interface as original."""
    return get_legacy_cli_wrapper().get_benchmark_history(device_id, limit)


def compare_benchmarks(benchmark_id1: str, benchmark_id2: str) -> Dict[str, Any]:
    """Compare benchmark results - same interface as original."""
    return get_legacy_cli_wrapper().compare_benchmarks(benchmark_id1, benchmark_id2)


def run_multi_gpu_benchmark(duration: int = 60,
                            enhanced: bool = True,
                            export_results: bool = False) -> Dict[str, Any]:
    """Run benchmarks on all available GPUs - same interface as original."""
    return get_legacy_cli_wrapper().run_multi_gpu_benchmark(
        duration=duration,
        enhanced=enhanced,
        export_results=export_results
    )


def export_results(results: Dict[str, Any], filename: Optional[str] = None) -> str:
    """Export benchmark results to JSON file - same interface as original."""
    return get_legacy_cli_wrapper().export_results(results, filename)


# Diagnostic functions
def print_system_info() -> None:
    """Print system information - maintains legacy interface."""
    # Use new architecture through DiagnosticsUseCase
    wrapper = get_legacy_cli_wrapper()
    diagnostics = wrapper._adapter.run_diagnostics()

    # Print system info from diagnostics
    if 'system' in diagnostics:
        system = diagnostics['system']
        print("\nSystem Information:")
        print("-" * 30)
        for key, value in system.items():
            print(f"{key}: {value}")


def print_enhanced_monitoring_status() -> None:
    """Print enhanced monitoring status - maintains legacy interface."""
    wrapper = get_legacy_cli_wrapper()
    diagnostics = wrapper._adapter.run_diagnostics()

    # Print enhanced monitoring status
    if 'requirements' in diagnostics:
        reqs = diagnostics['requirements']
        print("\nEnhanced Monitoring Status:")
        print("-" * 30)
        for key, value in reqs.items():
            status = "✓" if value else "✗"
            print(f"{status} {key}: {value}")


def print_comprehensive_diagnostics() -> None:
    """Print comprehensive diagnostics - maintains legacy interface."""
    wrapper = get_legacy_cli_wrapper()
    diagnostics = wrapper._adapter.run_diagnostics()

    # Print comprehensive diagnostics
    import json
    print("\nComprehensive Diagnostics:")
    print("=" * 60)
    print(json.dumps(diagnostics, indent=2))
