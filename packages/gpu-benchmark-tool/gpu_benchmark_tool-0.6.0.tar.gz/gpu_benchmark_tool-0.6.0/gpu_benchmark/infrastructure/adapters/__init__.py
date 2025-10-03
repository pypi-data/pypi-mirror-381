"""Adapters for integrating existing backends with new architecture.

This package provides adapters that bridge the gap between the existing
GPU backends and the new domain-driven architecture.
"""

from .gpu_backend_adapter import GPUBackendAdapter
from .legacy_backend_factory import LegacyBackendFactory

__all__ = [
    "GPUBackendAdapter",
    "LegacyBackendFactory"
]
