"""Tests for dependency injection container."""

import unittest
from unittest.mock import Mock

from gpu_benchmark.application.di.container import DIContainer, DependencyResolutionError
from gpu_benchmark.application.di.providers import (
    RepositoryProvider,
    ServiceProvider,
    UseCaseProvider,
    create_container,
    create_test_container
)


class TestDIContainer(unittest.TestCase):
    """Test dependency injection container."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.container = DIContainer()
    
    def test_register_singleton(self):
        """Test registering singleton services."""
        class Interface:
            pass
        
        class Implementation(Interface):
            pass
        
        self.container.register_singleton(Interface, Implementation)
        
        # Verify registration
        self.assertTrue(self.container.is_registered(Interface))
        
        # Get registered services info
        services = self.container.get_registered_services()
        self.assertIn("Interface", services)
        self.assertIn("singleton", services["Interface"])
    
    def test_register_factory(self):
        """Test registering factory functions."""
        class Interface:
            pass
        
        def factory():
            return Interface()
        
        self.container.register_factory(Interface, factory)
        
        # Verify registration
        self.assertTrue(self.container.is_registered(Interface))
        
        # Get registered services info
        services = self.container.get_registered_services()
        self.assertIn("Interface", services)
        self.assertIn("factory", services["Interface"])
    
    def test_register_instance(self):
        """Test registering specific instances."""
        class Interface:
            pass
        
        instance = Interface()
        self.container.register_instance(Interface, instance)
        
        # Verify registration
        self.assertTrue(self.container.is_registered(Interface))
        
        # Get registered services info
        services = self.container.get_registered_services()
        self.assertIn("Interface", services)
        self.assertIn("instance", services["Interface"])
    
    def test_resolve_singleton(self):
        """Test resolving singleton services."""
        class Interface:
            def __init__(self):
                self.value = "test"
        
        class Implementation(Interface):
            pass
        
        self.container.register_singleton(Interface, Implementation)
        
        # Resolve service
        instance1 = self.container.resolve(Interface)
        instance2 = self.container.resolve(Interface)
        
        # Verify it's the same instance (singleton)
        self.assertIs(instance1, instance2)
        self.assertIsInstance(instance1, Implementation)
    
    def test_resolve_factory(self):
        """Test resolving factory services."""
        class Interface:
            def __init__(self):
                self.value = "test"
        
        def factory():
            return Interface()
        
        self.container.register_factory(Interface, factory)
        
        # Resolve service
        instance = self.container.resolve(Interface)
        
        # Verify it's the correct type
        self.assertIsInstance(instance, Interface)
    
    def test_resolve_instance(self):
        """Test resolving registered instances."""
        class Interface:
            def __init__(self):
                self.value = "test"
        
        instance = Interface()
        self.container.register_instance(Interface, instance)
        
        # Resolve service
        resolved = self.container.resolve(Interface)
        
        # Verify it's the same instance
        self.assertIs(resolved, instance)
    
    def test_resolve_concrete_class(self):
        """Test resolving concrete classes directly."""
        class ConcreteClass:
            def __init__(self):
                self.value = "test"
        
        # Resolve without registration
        instance = self.container.resolve(ConcreteClass)
        
        # Verify it's the correct type
        self.assertIsInstance(instance, ConcreteClass)
    
    def test_resolve_with_dependencies(self):
        """Test resolving classes with dependencies."""
        class Dependency:
            def __init__(self):
                self.value = "dependency"
        
        class Service:
            def __init__(self, dependency: Dependency):
                self.dependency = dependency
        
        # Register dependency
        self.container.register_singleton(Dependency, Dependency)
        
        # Resolve service with dependency
        service = self.container.resolve(Service)
        
        # Verify dependency injection worked
        self.assertIsInstance(service, Service)
        self.assertIsInstance(service.dependency, Dependency)
        self.assertEqual(service.dependency.value, "dependency")
    
    def test_resolve_nonexistent_service(self):
        """Test resolving non-existent services."""
        class NonExistentInterface:
            pass
        
        # Try to resolve non-existent service
        with self.assertRaises(DependencyResolutionError):
            self.container.resolve(NonExistentInterface)
    
    def test_resolve_with_missing_dependency(self):
        """Test resolving services with missing dependencies."""
        class MissingDependency:
            pass
        
        class Service:
            def __init__(self, missing: MissingDependency):
                self.missing = missing
        
        # Try to resolve service with missing dependency
        with self.assertRaises(DependencyResolutionError):
            self.container.resolve(Service)
    
    def test_resolve_with_default_parameters(self):
        """Test resolving services with default parameters."""
        class Service:
            def __init__(self, optional_param: str = "default"):
                self.optional_param = optional_param
        
        # Resolve service with default parameter
        service = self.container.resolve(Service)
        
        # Verify default parameter was used
        self.assertEqual(service.optional_param, "default")
    
    def test_clear_dependencies(self):
        """Test clearing all dependencies."""
        class Interface:
            pass
        
        class Implementation(Interface):
            pass
        
        # Register some dependencies
        self.container.register_singleton(Interface, Implementation)
        self.assertTrue(self.container.is_registered(Interface))
        
        # Clear dependencies
        self.container.clear()
        self.assertFalse(self.container.is_registered(Interface))
    
    def test_get_registered_services(self):
        """Test getting information about registered services."""
        class Interface1:
            pass
        
        class Interface2:
            pass
        
        class Implementation1(Interface1):
            pass
        
        def factory():
            return Interface2()
        
        # Register different types of services
        self.container.register_singleton(Interface1, Implementation1)
        self.container.register_factory(Interface2, factory)
        
        # Get registered services info
        services = self.container.get_registered_services()
        
        # Verify info is correct
        self.assertIn("Interface1", services)
        self.assertIn("Interface2", services)
        self.assertIn("singleton", services["Interface1"])
        self.assertIn("factory", services["Interface2"])


class TestProviders(unittest.TestCase):
    """Test dependency providers."""
    
    def test_repository_provider(self):
        """Test repository provider registration."""
        container = DIContainer()
        
        # Register repositories
        RepositoryProvider.register_repositories(container)
        
        # Verify repositories are registered
        from gpu_benchmark.domain.repositories.gpu_repository import GPURepository
        from gpu_benchmark.domain.repositories.benchmark_repository import BenchmarkRepository
        from gpu_benchmark.domain.repositories.configuration_repository import ConfigurationRepository
        
        self.assertTrue(container.is_registered(GPURepository))
        self.assertTrue(container.is_registered(BenchmarkRepository))
        self.assertTrue(container.is_registered(ConfigurationRepository))
    
    def test_service_provider(self):
        """Test service provider registration."""
        container = DIContainer()
        
        # Register services
        ServiceProvider.register_services(container)
        
        # Verify services are registered
        from gpu_benchmark.domain.services.health_scoring_service import HealthScoringService
        
        self.assertTrue(container.is_registered(HealthScoringService))
    
    def test_use_case_provider(self):
        """Test use case provider registration."""
        container = DIContainer()
        
        # Register repositories and services first
        RepositoryProvider.register_repositories(container)
        ServiceProvider.register_services(container)
        
        # Register use cases
        UseCaseProvider.register_use_cases(container)
        
        # Verify use cases are registered
        from gpu_benchmark.application.use_cases.assess_gpu_health import AssessGPUHealthUseCase
        from gpu_benchmark.application.use_cases.run_benchmark import RunBenchmarkUseCase
        
        self.assertTrue(container.is_registered(AssessGPUHealthUseCase))
        self.assertTrue(container.is_registered(RunBenchmarkUseCase))
    
    def test_create_container(self):
        """Test creating a complete container."""
        container = create_container()
        
        # Verify all major components are registered
        from gpu_benchmark.domain.repositories.gpu_repository import GPURepository
        from gpu_benchmark.domain.repositories.benchmark_repository import BenchmarkRepository
        from gpu_benchmark.domain.services.health_scoring_service import HealthScoringService
        from gpu_benchmark.application.use_cases.assess_gpu_health import AssessGPUHealthUseCase
        from gpu_benchmark.application.use_cases.run_benchmark import RunBenchmarkUseCase
        
        self.assertTrue(container.is_registered(GPURepository))
        self.assertTrue(container.is_registered(BenchmarkRepository))
        self.assertTrue(container.is_registered(HealthScoringService))
        self.assertTrue(container.is_registered(AssessGPUHealthUseCase))
        self.assertTrue(container.is_registered(RunBenchmarkUseCase))
    
    def test_create_test_container(self):
        """Test creating a test container."""
        container = create_test_container()
        
        # Verify all major components are registered
        from gpu_benchmark.domain.repositories.gpu_repository import GPURepository
        from gpu_benchmark.domain.repositories.benchmark_repository import BenchmarkRepository
        from gpu_benchmark.domain.services.health_scoring_service import HealthScoringService
        from gpu_benchmark.application.use_cases.assess_gpu_health import AssessGPUHealthUseCase
        from gpu_benchmark.application.use_cases.run_benchmark import RunBenchmarkUseCase
        
        self.assertTrue(container.is_registered(GPURepository))
        self.assertTrue(container.is_registered(BenchmarkRepository))
        self.assertTrue(container.is_registered(HealthScoringService))
        self.assertTrue(container.is_registered(AssessGPUHealthUseCase))
        self.assertTrue(container.is_registered(RunBenchmarkUseCase))
    
    def test_resolve_use_cases(self):
        """Test resolving use cases with dependencies."""
        container = create_test_container()
        
        # Resolve use cases
        from gpu_benchmark.application.use_cases.assess_gpu_health import AssessGPUHealthUseCase
        from gpu_benchmark.application.use_cases.run_benchmark import RunBenchmarkUseCase
        
        assess_use_case = container.resolve(AssessGPUHealthUseCase)
        benchmark_use_case = container.resolve(RunBenchmarkUseCase)
        
        # Verify use cases are resolved correctly
        self.assertIsInstance(assess_use_case, AssessGPUHealthUseCase)
        self.assertIsInstance(benchmark_use_case, RunBenchmarkUseCase)
        
        # Verify dependencies are injected
        self.assertIsNotNone(assess_use_case._gpu_repository)
        self.assertIsNotNone(assess_use_case._benchmark_repository)
        self.assertIsNotNone(assess_use_case._health_scoring_service)
        
        self.assertIsNotNone(benchmark_use_case._gpu_repository)
        self.assertIsNotNone(benchmark_use_case._benchmark_repository)
        self.assertIsNotNone(benchmark_use_case._configuration_repository)
        self.assertIsNotNone(benchmark_use_case._health_scoring_service)


if __name__ == '__main__':
    unittest.main()
