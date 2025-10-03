"""CLI infrastructure for GPU Benchmark Tool.

This package provides CLI adapters that bridge the new architecture
with the existing CLI interface.
"""

from .cli_adapter import CLIBenchmarkAdapter
from .legacy_cli_wrapper import LegacyCLIWrapper

__all__ = [
    "CLIBenchmarkAdapter",
    "LegacyCLIWrapper"
]
