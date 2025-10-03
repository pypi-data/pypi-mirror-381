"""Dependency Injection container for GPU Benchmark Tool.

This package provides a simple dependency injection container
for managing dependencies and their lifecycle.
"""

from .container import DIContainer
from .providers import (
    RepositoryProvider,
    ServiceProvider,
    UseCaseProvider
)

__all__ = [
    "DIContainer",
    "RepositoryProvider",
    "ServiceProvider", 
    "UseCaseProvider"
]
