"""Dependency providers for GPU Benchmark Tool.

This module provides factory functions and providers for setting up
dependencies in the DI container.
"""

import logging
from typing import Optional

from .container import DIContainer

# Import domain interfaces
from ...domain.repositories.gpu_repository import GPURepository
from ...domain.repositories.benchmark_repository import BenchmarkRepository
from ...domain.repositories.configuration_repository import ConfigurationRepository
from ...domain.services.health_scoring_service import HealthScoringService

# Import infrastructure implementations
from ...infrastructure.repositories.memory_gpu_repository import MemoryGPURepository
from ...infrastructure.repositories.file_benchmark_repository import FileBenchmarkRepository
from ...infrastructure.repositories.file_configuration_repository import FileConfigurationRepository
from ...infrastructure.adapters.gpu_backend_adapter import GPUBackendAdapter
from ...infrastructure.adapters.legacy_backend_factory import LegacyBackendFactory

# Import use cases
from ..use_cases.assess_gpu_health import AssessGPUHealthUseCase
from ..use_cases.run_benchmark import RunBenchmarkUseCase
from ..use_cases.run_diagnostics import RunDiagnosticsUseCase


class RepositoryProvider:
    """Provider for repository dependencies."""
    
    @staticmethod
    def register_repositories(container: DIContainer, 
                            storage_dir: str = "benchmark_results",
                            config_dir: str = "config",
                            use_legacy_backends: bool = True) -> None:
        """Register repository dependencies.
        
        Args:
            container: The DI container.
            storage_dir: Directory for benchmark result storage.
            config_dir: Directory for configuration storage.
            use_legacy_backends: Whether to use legacy GPU backends.
        """
        # Register GPU repository
        if use_legacy_backends:
            # Use adapter that integrates with existing backends
            container.register_factory(
                GPURepository,
                lambda: GPUBackendAdapter(
                    backend_factory=LegacyBackendFactory(),
                    logger=container._logger
                )
            )
        else:
            # Use memory-based repository for testing
            container.register_factory(
                GPURepository,
                lambda: MemoryGPURepository()
            )
        
        # Register benchmark repository
        container.register_factory(
            BenchmarkRepository,
            lambda: FileBenchmarkRepository(storage_dir)
        )
        
        # Register configuration repository
        container.register_factory(
            ConfigurationRepository,
            lambda: FileConfigurationRepository(config_dir)
        )


class ServiceProvider:
    """Provider for domain service dependencies."""
    
    @staticmethod
    def register_services(container: DIContainer) -> None:
        """Register domain service dependencies.
        
        Args:
            container: The DI container.
        """
        # Register health scoring service
        container.register_factory(
            HealthScoringService,
            lambda: HealthScoringService()
        )


class UseCaseProvider:
    """Provider for use case dependencies."""
    
    @staticmethod
    def register_use_cases(container: DIContainer) -> None:
        """Register use case dependencies.
        
        Args:
            container: The DI container.
        """
        # Register assess GPU health use case
        container.register_factory(
            AssessGPUHealthUseCase,
            lambda: AssessGPUHealthUseCase(
                gpu_repository=container.resolve(GPURepository),
                benchmark_repository=container.resolve(BenchmarkRepository),
                health_scoring_service=container.resolve(HealthScoringService)
            )
        )
        
        # Register run benchmark use case
        container.register_factory(
            RunBenchmarkUseCase,
            lambda: RunBenchmarkUseCase(
                gpu_repository=container.resolve(GPURepository),
                benchmark_repository=container.resolve(BenchmarkRepository),
                configuration_repository=container.resolve(ConfigurationRepository),
                health_scoring_service=container.resolve(HealthScoringService)
            )
        )

        # Register run diagnostics use case
        container.register_factory(
            RunDiagnosticsUseCase,
            lambda: RunDiagnosticsUseCase(
                gpu_repository=container.resolve(GPURepository)
            )
        )


class ApplicationProvider:
    """Provider for the complete application setup."""
    
    @staticmethod
    def setup_application(container: DIContainer,
                         storage_dir: str = "benchmark_results",
                         config_dir: str = "config",
                         logger: Optional[logging.Logger] = None,
                         use_legacy_backends: bool = True) -> None:
        """Set up the complete application with all dependencies.
        
        Args:
            container: The DI container.
            storage_dir: Directory for benchmark result storage.
            config_dir: Directory for configuration storage.
            logger: Logger for the application.
            use_legacy_backends: Whether to use legacy GPU backends.
        """
        if logger:
            container._logger = logger
        
        # Register all dependencies
        RepositoryProvider.register_repositories(container, storage_dir, config_dir, use_legacy_backends)
        ServiceProvider.register_services(container)
        UseCaseProvider.register_use_cases(container)
        
        if logger:
            logger.info("Application dependencies registered successfully")


def create_container(storage_dir: str = "benchmark_results",
                    config_dir: str = "config",
                    logger: Optional[logging.Logger] = None,
                    use_legacy_backends: bool = True) -> DIContainer:
    """Create and configure a DI container with all dependencies.
    
    Args:
        storage_dir: Directory for benchmark result storage.
        config_dir: Directory for configuration storage.
        logger: Logger for the container.
        use_legacy_backends: Whether to use legacy GPU backends.
        
    Returns:
        DIContainer: Configured DI container.
    """
    container = DIContainer(logger)
    ApplicationProvider.setup_application(container, storage_dir, config_dir, logger, use_legacy_backends)
    return container


def create_test_container() -> DIContainer:
    """Create a DI container configured for testing.
    
    Returns:
        DIContainer: Test-configured DI container.
    """
    container = DIContainer()
    
    # Use in-memory repositories for testing
    container.register_instance(GPURepository, MemoryGPURepository())
    container.register_instance(BenchmarkRepository, FileBenchmarkRepository("test_results"))
    container.register_instance(ConfigurationRepository, FileConfigurationRepository("test_config"))
    
    # Register services
    ServiceProvider.register_services(container)
    
    # Register use cases
    UseCaseProvider.register_use_cases(container)
    
    return container
