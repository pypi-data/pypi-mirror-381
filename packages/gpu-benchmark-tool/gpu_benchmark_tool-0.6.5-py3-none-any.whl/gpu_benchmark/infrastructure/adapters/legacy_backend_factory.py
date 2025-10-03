"""Legacy Backend Factory.

This factory creates and manages the existing GPU backends for integration
with the new architecture.
"""

import logging
from typing import Dict, Any, Optional

from ...domain.error_handling.error_boundary import ErrorBoundary
from ...domain.error_handling.fallback_strategies import MockGPUFallback


class LegacyBackendFactory:
    """Factory for creating and managing legacy GPU backends.
    
    This factory provides a unified interface to the existing GPU backend system
    while maintaining compatibility with the new domain architecture.
    """
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """Initialize the legacy backend factory.
        
        Args:
            logger: Logger for factory operations.
        """
        self._logger = logger or logging.getLogger(__name__)
        self._backends: Dict[str, Any] = {}
        self._error_boundary = ErrorBoundary(
            fallback_strategy=MockGPUFallback(),
            logger=self._logger
        )
        self._initialized = False
    
    def get_available_backends(self) -> Dict[str, Any]:
        """Get all available GPU backends.
        
        Returns:
            Dict[str, Any]: Dictionary mapping backend names to backend instances.
        """
        if not self._initialized:
            self._initialize_backends()
        
        return self._backends.copy()
    
    def _initialize_backends(self) -> None:
        """Initialize all available GPU backends."""
        self._logger.info("Initializing legacy GPU backends...")
        
        # Initialize NVIDIA backend
        self._initialize_nvidia_backend()
        
        # Initialize AMD backend
        self._initialize_amd_backend()
        
        # Initialize Intel backend
        self._initialize_intel_backend()
        
        # Initialize Mock backend
        self._initialize_mock_backend()
        
        self._initialized = True
        
        available_count = len([b for b in self._backends.values() if b.is_available()])
        self._logger.info(f"Initialized {len(self._backends)} backends, {available_count} available")
    
    def _initialize_nvidia_backend(self) -> None:
        """Initialize NVIDIA backend."""
        try:
            from ...backends.nvidia import NVIDIABackend
            backend = NVIDIABackend()
            self._backends["nvidia"] = backend
            self._logger.debug("NVIDIA backend initialized")
        except Exception as e:
            self._logger.warning(f"Failed to initialize NVIDIA backend: {e}")
            # Don't add to backends if initialization failed
    
    def _initialize_amd_backend(self) -> None:
        """Initialize AMD backend."""
        try:
            from ...backends.amd import AMDBackend
            backend = AMDBackend()
            self._backends["amd"] = backend
            self._logger.debug("AMD backend initialized")
        except Exception as e:
            self._logger.warning(f"Failed to initialize AMD backend: {e}")
            # Don't add to backends if initialization failed
    
    def _initialize_intel_backend(self) -> None:
        """Initialize Intel backend."""
        try:
            from ...backends.intel import IntelBackend
            backend = IntelBackend()
            self._backends["intel"] = backend
            self._logger.debug("Intel backend initialized")
        except Exception as e:
            self._logger.warning(f"Failed to initialize Intel backend: {e}")
            # Don't add to backends if initialization failed
    
    def _initialize_mock_backend(self) -> None:
        """Initialize Mock backend."""
        try:
            from ...backends.mock import MockBackend
            backend = MockBackend()
            self._backends["mock"] = backend
            self._logger.debug("Mock backend initialized")
        except Exception as e:
            self._logger.warning(f"Failed to initialize Mock backend: {e}")
            # Create a fallback mock backend only for mock type
            self._backends["mock"] = self._create_mock_backend("mock")
    
    def _create_mock_backend(self, backend_type: str):
        """Create a mock backend for fallback purposes."""
        class MockBackend:
            def __init__(self, backend_type: str):
                self.backend_type = backend_type
                self._device_count = 1 if backend_type == "mock" else 0
            
            def is_available(self) -> bool:
                return self.backend_type == "mock"
            
            def get_device_count(self) -> int:
                return self._device_count
            
            def get_device_info(self, device_id: int) -> Dict[str, Any]:
                return {
                    "name": f"Mock {self.backend_type.upper()} GPU",
                    "memory_total_mb": 8192,
                    "memory_used_mb": 0,
                    "driver_version": f"Mock {self.backend_type} Driver",
                    "cuda_version": "Mock CUDA" if self.backend_type == "nvidia" else None
                }
            
            def create_monitor(self, device_id: int):
                return self._create_mock_monitor()
            
            def _create_mock_monitor(self):
                class MockMonitor:
                    def get_temperature(self) -> float:
                        return 45.0
                    
                    def get_power_usage(self) -> float:
                        return 0.0
                    
                    def get_memory_info(self) -> Dict[str, float]:
                        return {
                            "used_mb": 0,
                            "total_mb": 8192,
                            "free_mb": 8192,
                            "utilization_pct": 0
                        }
                    
                    def get_utilization(self) -> float:
                        return 0.0
                    
                    def check_throttling(self):
                        return False, []
                
                return MockMonitor()
        
        return MockBackend(backend_type)
    
    def get_backend(self, backend_name: str) -> Optional[Any]:
        """Get a specific backend by name.
        
        Args:
            backend_name: Name of the backend to get.
            
        Returns:
            Backend instance if found, None otherwise.
        """
        if not self._initialized:
            self._initialize_backends()
        
        return self._backends.get(backend_name)
    
    def get_available_backend_names(self) -> list:
        """Get list of available backend names.
        
        Returns:
            List of backend names that are available.
        """
        if not self._initialized:
            self._initialize_backends()
        
        return [name for name, backend in self._backends.items() if backend.is_available()]
    
    def get_backend_status(self) -> Dict[str, Any]:
        """Get status information about all backends.
        
        Returns:
            Dictionary with backend status information.
        """
        if not self._initialized:
            self._initialize_backends()
        
        status = {
            "initialized": self._initialized,
            "backends": {}
        }
        
        for name, backend in self._backends.items():
            try:
                status["backends"][name] = {
                    "available": backend.is_available(),
                    "device_count": backend.get_device_count() if backend.is_available() else 0
                }
            except Exception as e:
                status["backends"][name] = {
                    "available": False,
                    "error": str(e)
                }
        
        return status
    
    def refresh_backends(self) -> None:
        """Refresh backend initialization."""
        self._logger.info("Refreshing GPU backends...")
        self._backends.clear()
        self._initialized = False
        self._initialize_backends()
    
    def create_backend_adapter(self, backend_name: str) -> Optional[Any]:
        """Create a backend adapter for a specific backend.
        
        Args:
            backend_name: Name of the backend to create adapter for.
            
        Returns:
            Backend adapter if successful, None otherwise.
        """
        backend = self.get_backend(backend_name)
        if not backend:
            return None
        
        # Create a simple adapter wrapper
        class BackendAdapter:
            def __init__(self, backend):
                self.backend = backend
            
            def is_available(self) -> bool:
                return self.backend.is_available()
            
            def get_device_count(self) -> int:
                return self.backend.get_device_count()
            
            def get_device_info(self, device_id: int) -> Dict[str, Any]:
                return self.backend.get_device_info(device_id)
            
            def create_monitor(self, device_id: int):
                return self.backend.create_monitor(device_id)
        
        return BackendAdapter(backend)
