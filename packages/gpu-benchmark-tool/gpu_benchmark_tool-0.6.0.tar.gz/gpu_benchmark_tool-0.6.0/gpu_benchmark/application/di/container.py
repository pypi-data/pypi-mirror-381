"""Dependency Injection Container.

This module provides a simple dependency injection container
for managing dependencies and their lifecycle.
"""

from typing import Dict, Any, Type, TypeVar, Callable, Optional, Union
import logging

T = TypeVar('T')


class DIContainer:
    """Simple dependency injection container.
    
    This container manages the registration and resolution of dependencies
    using a simple registry pattern with support for singletons and factories.
    """
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """Initialize the DI container.
        
        Args:
            logger: Logger for container operations.
        """
        self._logger = logger or logging.getLogger(__name__)
        self._services: Dict[Type, Any] = {}
        self._factories: Dict[Type, Callable] = {}
        self._singletons: Dict[Type, Any] = {}
        self._instances: Dict[Type, Any] = {}
    
    def register_singleton(self, interface: Type[T], implementation: Type[T]) -> None:
        """Register a singleton service.
        
        Args:
            interface: The interface or abstract type.
            implementation: The concrete implementation class.
        """
        self._services[interface] = implementation
        self._logger.debug(f"Registered singleton: {interface.__name__} -> {implementation.__name__}")
    
    def register_factory(self, interface: Type[T], factory: Callable[[], T]) -> None:
        """Register a factory function for a service.
        
        Args:
            interface: The interface or abstract type.
            factory: Factory function that creates instances.
        """
        self._factories[interface] = factory
        self._logger.debug(f"Registered factory: {interface.__name__}")
    
    def register_instance(self, interface: Type[T], instance: T) -> None:
        """Register a specific instance.
        
        Args:
            interface: The interface or abstract type.
            instance: The instance to register.
        """
        self._instances[interface] = instance
        self._logger.debug(f"Registered instance: {interface.__name__}")
    
    def resolve(self, interface: Type[T]) -> T:
        """Resolve a dependency.
        
        Args:
            interface: The interface or type to resolve.
            
        Returns:
            T: The resolved instance.
            
        Raises:
            DependencyResolutionError: If dependency cannot be resolved.
        """
        # Check for registered instance first
        if interface in self._instances:
            return self._instances[interface]
        
        # Check for singleton
        if interface in self._singletons:
            return self._singletons[interface]
        
        # Check for factory
        if interface in self._factories:
            instance = self._factories[interface]()
            self._singletons[interface] = instance
            return instance
        
        # Check for service registration
        if interface in self._services:
            implementation = self._services[interface]
            instance = self._create_instance(implementation)
            self._singletons[interface] = instance
            return instance
        
        # Try to create instance directly if it's a concrete class
        if self._is_concrete_class(interface):
            instance = self._create_instance(interface)
            self._singletons[interface] = instance
            return instance
        
        raise DependencyResolutionError(f"Cannot resolve dependency: {interface.__name__}")
    
    def _create_instance(self, implementation: Type[T]) -> T:
        """Create an instance of a class with dependency injection.
        
        Args:
            implementation: The class to instantiate.
            
        Returns:
            T: The created instance.
        """
        try:
            # Get constructor signature
            import inspect
            sig = inspect.signature(implementation.__init__)
            
            # Build arguments
            args = {}
            for param_name, param in sig.parameters.items():
                if param_name == 'self':
                    continue
                
                # Try to resolve the parameter type
                if param.annotation != inspect.Parameter.empty:
                    try:
                        args[param_name] = self.resolve(param.annotation)
                    except DependencyResolutionError:
                        # If we can't resolve the dependency, try to use default value
                        if param.default != inspect.Parameter.empty:
                            args[param_name] = param.default
                        else:
                            raise DependencyResolutionError(
                                f"Cannot resolve parameter '{param_name}' of type {param.annotation.__name__}"
                            )
                else:
                    # No type annotation, try to use default value
                    if param.default != inspect.Parameter.empty:
                        args[param_name] = param.default
                    else:
                        raise DependencyResolutionError(
                            f"Parameter '{param_name}' has no type annotation and no default value"
                        )
            
            return implementation(**args)
            
        except Exception as e:
            raise DependencyResolutionError(f"Failed to create instance of {implementation.__name__}: {e}") from e
    
    def _is_concrete_class(self, cls: Type) -> bool:
        """Check if a class is concrete (can be instantiated).
        
        Args:
            cls: The class to check.
            
        Returns:
            bool: True if the class is concrete.
        """
        import inspect
        return (
            inspect.isclass(cls) and
            not inspect.isabstract(cls) and
            not cls.__name__.startswith('ABC')
        )
    
    def is_registered(self, interface: Type) -> bool:
        """Check if a dependency is registered.
        
        Args:
            interface: The interface to check.
            
        Returns:
            bool: True if the dependency is registered.
        """
        return (
            interface in self._services or
            interface in self._factories or
            interface in self._instances or
            self._is_concrete_class(interface)
        )
    
    def clear(self) -> None:
        """Clear all registered dependencies."""
        self._services.clear()
        self._factories.clear()
        self._singletons.clear()
        self._instances.clear()
        self._logger.debug("Cleared all dependencies")
    
    def get_registered_services(self) -> Dict[str, str]:
        """Get information about registered services.
        
        Returns:
            Dict[str, str]: Dictionary mapping service names to their types.
        """
        services = {}
        
        for interface, implementation in self._services.items():
            services[interface.__name__] = f"singleton -> {implementation.__name__}"
        
        for interface in self._factories:
            services[interface.__name__] = "factory"
        
        for interface in self._instances:
            services[interface.__name__] = "instance"
        
        return services


class DependencyResolutionError(Exception):
    """Raised when a dependency cannot be resolved."""
    pass
