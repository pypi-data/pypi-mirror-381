"""Migration utilities for GPU Benchmark Tool.

This package provides utilities for migrating from the old architecture
to the new domain-driven architecture.
"""

from .config_migration import ConfigMigration
from .data_migration import DataMigration

__all__ = [
    "ConfigMigration",
    "DataMigration"
]
