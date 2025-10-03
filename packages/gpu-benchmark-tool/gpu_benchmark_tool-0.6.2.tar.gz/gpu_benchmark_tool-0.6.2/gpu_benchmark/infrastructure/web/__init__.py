"""Web interface infrastructure for GPU Benchmark Tool.

This package provides web interface adapters that bridge the new architecture
with the existing Flask web interface.
"""

from .flask_adapter import FlaskWebAdapter
from .api_routes import APIRoutes

__all__ = [
    "FlaskWebAdapter",
    "APIRoutes"
]
