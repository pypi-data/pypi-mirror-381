"""Configuration Repository interface.

This module defines the contract for configuration data access operations.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List

from ..models.configuration import BenchmarkConfig, ScoringThresholds, SystemContext


class ConfigurationRepository(ABC):
    """Abstract repository for configuration operations.
    
    This interface defines the contract for managing configuration data
    including benchmark settings, scoring thresholds, and system context.
    """
    
    @abstractmethod
    def get_default_benchmark_config(self) -> BenchmarkConfig:
        """Get the default benchmark configuration.
        
        Returns:
            BenchmarkConfig: The default benchmark configuration.
            
        Raises:
            ConfigurationError: If configuration cannot be loaded.
        """
        pass
    
    @abstractmethod
    def get_benchmark_config(self, config_name: str) -> Optional[BenchmarkConfig]:
        """Get a named benchmark configuration.
        
        Args:
            config_name: The name of the configuration.
            
        Returns:
            Optional[BenchmarkConfig]: The configuration if found, None otherwise.
            
        Raises:
            ConfigurationError: If configuration cannot be loaded.
        """
        pass
    
    @abstractmethod
    def save_benchmark_config(self, config: BenchmarkConfig, config_name: str) -> None:
        """Save a benchmark configuration.
        
        Args:
            config: The benchmark configuration to save.
            config_name: The name to save the configuration under.
            
        Raises:
            ConfigurationError: If saving fails.
        """
        pass
    
    @abstractmethod
    def list_benchmark_configs(self) -> List[str]:
        """List all available benchmark configuration names.
        
        Returns:
            List[str]: List of configuration names.
            
        Raises:
            ConfigurationError: If listing fails.
        """
        pass
    
    @abstractmethod
    def delete_benchmark_config(self, config_name: str) -> bool:
        """Delete a benchmark configuration.
        
        Args:
            config_name: The name of the configuration to delete.
            
        Returns:
            bool: True if deleted successfully, False if not found.
            
        Raises:
            ConfigurationError: If deletion fails.
        """
        pass
    
    @abstractmethod
    def get_scoring_thresholds(self) -> ScoringThresholds:
        """Get the scoring thresholds configuration.
        
        Returns:
            ScoringThresholds: The scoring thresholds configuration.
            
        Raises:
            ConfigurationError: If configuration cannot be loaded.
        """
        pass
    
    @abstractmethod
    def save_scoring_thresholds(self, thresholds: ScoringThresholds) -> None:
        """Save the scoring thresholds configuration.
        
        Args:
            thresholds: The scoring thresholds to save.
            
        Raises:
            ConfigurationError: If saving fails.
        """
        pass
    
    @abstractmethod
    def get_system_context(self) -> SystemContext:
        """Get the current system context.
        
        Returns:
            SystemContext: The current system context.
            
        Raises:
            ConfigurationError: If system context cannot be determined.
        """
        pass
    
    @abstractmethod
    def save_system_context(self, context: SystemContext) -> None:
        """Save the system context.
        
        Args:
            context: The system context to save.
            
        Raises:
            ConfigurationError: If saving fails.
        """
        pass
    
    @abstractmethod
    def get_user_preferences(self) -> Dict[str, Any]:
        """Get user preferences.
        
        Returns:
            Dict[str, Any]: User preferences dictionary.
            
        Raises:
            ConfigurationError: If preferences cannot be loaded.
        """
        pass
    
    @abstractmethod
    def save_user_preferences(self, preferences: Dict[str, Any]) -> None:
        """Save user preferences.
        
        Args:
            preferences: User preferences dictionary.
            
        Raises:
            ConfigurationError: If saving fails.
        """
        pass
    
    @abstractmethod
    def get_installation_type(self) -> str:
        """Get the installation type.
        
        Returns:
            str: Installation type ("nvidia", "amd", "intel", "all", "basic").
            
        Raises:
            ConfigurationError: If installation type cannot be determined.
        """
        pass
    
    @abstractmethod
    def validate_configuration(self, config: BenchmarkConfig) -> List[str]:
        """Validate a benchmark configuration.
        
        Args:
            config: The configuration to validate.
            
        Returns:
            List[str]: List of validation errors. Empty list if valid.
        """
        pass
    
    @abstractmethod
    def get_recommended_config(self, use_case: str, system_context: SystemContext) -> BenchmarkConfig:
        """Get recommended configuration for a use case.
        
        Args:
            use_case: The intended use case.
            system_context: The current system context.
            
        Returns:
            BenchmarkConfig: Recommended configuration.
            
        Raises:
            ConfigurationError: If recommendation cannot be generated.
        """
        pass
