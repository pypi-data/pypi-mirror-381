"""File-based Configuration Repository implementation.

This implementation stores configuration data in JSON files.
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, Optional, List

from ...domain.repositories.configuration_repository import ConfigurationRepository
from ...domain.models.configuration import (
    BenchmarkConfig, ScoringThresholds, SystemContext,
    BenchmarkType, UseCase, StressTestConfig
)


class FileConfigurationRepository(ConfigurationRepository):
    """File-based implementation of ConfigurationRepository.
    
    This implementation stores configuration data in JSON files
    in a configurable directory.
    """
    
    def __init__(self, config_dir: str = "config"):
        """Initialize the file-based configuration repository.
        
        Args:
            config_dir: Directory to store configuration files.
        """
        self._config_dir = Path(config_dir)
        self._config_dir.mkdir(parents=True, exist_ok=True)
        
        # Default file paths
        self._benchmark_configs_dir = self._config_dir / "benchmark_configs"
        self._benchmark_configs_dir.mkdir(exist_ok=True)
        
        self._scoring_thresholds_file = self._config_dir / "scoring_thresholds.json"
        self._system_context_file = self._config_dir / "system_context.json"
        self._user_preferences_file = self._config_dir / "user_preferences.json"
        self._installation_type_file = self._config_dir / "installation_type.json"
    
    def get_default_benchmark_config(self) -> BenchmarkConfig:
        """Get the default benchmark configuration.
        
        Returns:
            BenchmarkConfig: The default benchmark configuration.
        """
        return BenchmarkConfig()
    
    def get_benchmark_config(self, config_name: str) -> Optional[BenchmarkConfig]:
        """Get a named benchmark configuration.
        
        Args:
            config_name: The name of the configuration.
            
        Returns:
            Optional[BenchmarkConfig]: The configuration if found, None otherwise.
        """
        try:
            config_file = self._benchmark_configs_dir / f"{config_name}.json"
            if not config_file.exists():
                return None
            
            with open(config_file, 'r') as f:
                data = json.load(f)
                return self._deserialize_benchmark_config(data)
                
        except Exception:
            return None
    
    def save_benchmark_config(self, config: BenchmarkConfig, config_name: str) -> None:
        """Save a benchmark configuration.
        
        Args:
            config: The benchmark configuration to save.
            config_name: The name to save the configuration under.
        """
        try:
            config_file = self._benchmark_configs_dir / f"{config_name}.json"
            data = self._serialize_benchmark_config(config)
            
            with open(config_file, 'w') as f:
                json.dump(data, f, indent=2)
                
        except Exception as e:
            raise ConfigurationError(f"Failed to save benchmark config {config_name}: {e}") from e
    
    def list_benchmark_configs(self) -> List[str]:
        """List all available benchmark configuration names.
        
        Returns:
            List[str]: List of configuration names.
        """
        try:
            config_names = []
            for config_file in self._benchmark_configs_dir.glob("*.json"):
                config_names.append(config_file.stem)
            return config_names
            
        except Exception as e:
            raise ConfigurationError(f"Failed to list benchmark configs: {e}") from e
    
    def delete_benchmark_config(self, config_name: str) -> bool:
        """Delete a benchmark configuration.
        
        Args:
            config_name: The name of the configuration to delete.
            
        Returns:
            bool: True if deleted successfully, False if not found.
        """
        try:
            config_file = self._benchmark_configs_dir / f"{config_name}.json"
            if config_file.exists():
                config_file.unlink()
                return True
            return False
            
        except Exception as e:
            raise ConfigurationError(f"Failed to delete benchmark config {config_name}: {e}") from e
    
    def get_scoring_thresholds(self) -> ScoringThresholds:
        """Get the scoring thresholds configuration.
        
        Returns:
            ScoringThresholds: The scoring thresholds configuration.
        """
        try:
            if self._scoring_thresholds_file.exists():
                with open(self._scoring_thresholds_file, 'r') as f:
                    data = json.load(f)
                    return self._deserialize_scoring_thresholds(data)
            else:
                # Return default thresholds
                return ScoringThresholds()
                
        except Exception as e:
            raise ConfigurationError(f"Failed to load scoring thresholds: {e}") from e
    
    def save_scoring_thresholds(self, thresholds: ScoringThresholds) -> None:
        """Save the scoring thresholds configuration.
        
        Args:
            thresholds: The scoring thresholds to save.
        """
        try:
            data = self._serialize_scoring_thresholds(thresholds)
            with open(self._scoring_thresholds_file, 'w') as f:
                json.dump(data, f, indent=2)
                
        except Exception as e:
            raise ConfigurationError(f"Failed to save scoring thresholds: {e}") from e
    
    def get_system_context(self) -> SystemContext:
        """Get the current system context.
        
        Returns:
            SystemContext: The current system context.
        """
        try:
            if self._system_context_file.exists():
                with open(self._system_context_file, 'r') as f:
                    data = json.load(f)
                    return self._deserialize_system_context(data)
            else:
                # Try to detect system context
                return self._detect_system_context()
                
        except Exception as e:
            raise ConfigurationError(f"Failed to load system context: {e}") from e
    
    def save_system_context(self, context: SystemContext) -> None:
        """Save the system context.
        
        Args:
            context: The system context to save.
        """
        try:
            data = self._serialize_system_context(context)
            with open(self._system_context_file, 'w') as f:
                json.dump(data, f, indent=2)
                
        except Exception as e:
            raise ConfigurationError(f"Failed to save system context: {e}") from e
    
    def get_user_preferences(self) -> Dict[str, Any]:
        """Get user preferences.
        
        Returns:
            Dict[str, Any]: User preferences dictionary.
        """
        try:
            if self._user_preferences_file.exists():
                with open(self._user_preferences_file, 'r') as f:
                    return json.load(f)
            else:
                return {}
                
        except Exception as e:
            raise ConfigurationError(f"Failed to load user preferences: {e}") from e
    
    def save_user_preferences(self, preferences: Dict[str, Any]) -> None:
        """Save user preferences.
        
        Args:
            preferences: User preferences dictionary.
        """
        try:
            with open(self._user_preferences_file, 'w') as f:
                json.dump(preferences, f, indent=2)
                
        except Exception as e:
            raise ConfigurationError(f"Failed to save user preferences: {e}") from e
    
    def get_installation_type(self) -> str:
        """Get the installation type.
        
        Returns:
            str: Installation type ("nvidia", "amd", "intel", "all", "basic").
        """
        try:
            if self._installation_type_file.exists():
                with open(self._installation_type_file, 'r') as f:
                    data = json.load(f)
                    return data.get("installation_type", "basic")
            else:
                # Try to detect installation type
                return self._detect_installation_type()
                
        except Exception:
            return "basic"
    
    def validate_configuration(self, config: BenchmarkConfig) -> List[str]:
        """Validate a benchmark configuration.
        
        Args:
            config: The configuration to validate.
            
        Returns:
            List[str]: List of validation errors. Empty list if valid.
        """
        errors = []
        
        try:
            config.validate()
        except ValueError as e:
            errors.append(str(e))
        
        # Additional custom validations
        if config.duration_seconds > 3600:  # 1 hour
            errors.append("Duration too long (max 1 hour)")
        
        if config.gpu_device_id < 0:
            errors.append("GPU device ID must be non-negative")
        
        return errors
    
    def get_recommended_config(self, use_case: str, system_context: SystemContext) -> BenchmarkConfig:
        """Get recommended configuration for a use case.
        
        Args:
            use_case: The intended use case.
            system_context: The current system context.
            
        Returns:
            BenchmarkConfig: Recommended configuration.
        """
        # Base configuration
        config = BenchmarkConfig()
        
        # Adjust based on use case
        if use_case == "gaming":
            config = BenchmarkConfig(
                benchmark_type=BenchmarkType.QUICK,
                use_case=UseCase.GAMING,
                duration_seconds=30,
                include_ai_benchmarks=False
            )
        elif use_case == "ai_training":
            config = BenchmarkConfig(
                benchmark_type=BenchmarkType.COMPREHENSIVE,
                use_case=UseCase.AI_TRAINING,
                duration_seconds=120,
                include_ai_benchmarks=True
            )
        elif use_case == "ai_inference":
            config = BenchmarkConfig(
                benchmark_type=BenchmarkType.STANDARD,
                use_case=UseCase.AI_INFERENCE,
                duration_seconds=60,
                include_ai_benchmarks=True
            )
        elif use_case == "mining":
            config = BenchmarkConfig(
                benchmark_type=BenchmarkType.COMPREHENSIVE,
                use_case=UseCase.MINING,
                duration_seconds=180,
                include_ai_benchmarks=False
            )
        
        # Adjust based on system context
        if system_context.available_memory_gb < 8:
            config = BenchmarkConfig(
                benchmark_type=BenchmarkType.QUICK,
                duration_seconds=30
            )
        elif system_context.available_memory_gb > 32:
            config = BenchmarkConfig(
                benchmark_type=BenchmarkType.COMPREHENSIVE,
                duration_seconds=120
            )
        
        return config
    
    def _serialize_benchmark_config(self, config: BenchmarkConfig) -> Dict[str, Any]:
        """Serialize benchmark config to dictionary."""
        data = config.to_dict()
        
        # Convert enums to strings
        if "benchmark_type" in data:
            data["benchmark_type"] = data["benchmark_type"]
        if "use_case" in data:
            data["use_case"] = data["use_case"]
        
        return data
    
    def _deserialize_benchmark_config(self, data: Dict[str, Any]) -> BenchmarkConfig:
        """Deserialize benchmark config from dictionary."""
        # Convert string enums back to enum objects
        if "benchmark_type" in data:
            data["benchmark_type"] = BenchmarkType(data["benchmark_type"])
        if "use_case" in data:
            data["use_case"] = UseCase(data["use_case"])
        
        # Handle stress test config
        if data.get("stress_test_config"):
            stress_data = data["stress_test_config"]
            data["stress_test_config"] = StressTestConfig(
                duration_seconds=stress_data["duration_seconds"],
                include_compute_test=stress_data["include_compute_test"],
                include_memory_test=stress_data["include_memory_test"],
                include_mixed_precision_test=stress_data["include_mixed_precision_test"],
                compute_test_weight=stress_data["compute_test_weight"],
                memory_test_weight=stress_data["memory_test_weight"],
                mixed_precision_test_weight=stress_data["mixed_precision_test_weight"],
                target_utilization=stress_data["target_utilization"],
                max_temperature=stress_data["max_temperature"]
            )
        
        # Handle scoring thresholds
        if data.get("scoring_thresholds"):
            thresholds_data = data["scoring_thresholds"]
            data["scoring_thresholds"] = ScoringThresholds(
                healthy_min=thresholds_data["healthy_min"],
                good_min=thresholds_data["good_min"],
                degraded_min=thresholds_data["degraded_min"],
                warning_min=thresholds_data["warning_min"],
                critical_min=thresholds_data["critical_min"],
                temperature_weight=thresholds_data["temperature_weight"],
                baseline_temperature_weight=thresholds_data["baseline_temperature_weight"],
                power_efficiency_weight=thresholds_data["power_efficiency_weight"],
                utilization_weight=thresholds_data["utilization_weight"],
                throttling_weight=thresholds_data["throttling_weight"],
                errors_weight=thresholds_data["errors_weight"],
                temperature_stability_weight=thresholds_data["temperature_stability_weight"]
            )
        
        return BenchmarkConfig(**data)
    
    def _serialize_scoring_thresholds(self, thresholds: ScoringThresholds) -> Dict[str, Any]:
        """Serialize scoring thresholds to dictionary."""
        return thresholds.to_dict()
    
    def _deserialize_scoring_thresholds(self, data: Dict[str, Any]) -> ScoringThresholds:
        """Deserialize scoring thresholds from dictionary."""
        return ScoringThresholds(**data)
    
    def _serialize_system_context(self, context: SystemContext) -> Dict[str, Any]:
        """Serialize system context to dictionary."""
        return context.to_dict()
    
    def _deserialize_system_context(self, data: Dict[str, Any]) -> SystemContext:
        """Deserialize system context from dictionary."""
        from datetime import datetime
        data["timestamp"] = datetime.fromisoformat(data["timestamp"])
        return SystemContext(**data)
    
    def _detect_system_context(self) -> SystemContext:
        """Detect current system context."""
        import platform
        import psutil
        
        return SystemContext(
            os_name=platform.system(),
            os_version=platform.release(),
            architecture=platform.machine(),
            python_version=platform.python_version(),
            gpu_backend_type="unknown",
            installation_type=self._detect_installation_type(),
            available_memory_gb=psutil.virtual_memory().total / (1024**3),
            cpu_cores=psutil.cpu_count()
        )
    
    def _detect_installation_type(self) -> str:
        """Detect installation type based on available packages."""
        try:
            import pynvml
            nvidia_available = True
        except ImportError:
            nvidia_available = False
        
        try:
            import torch
            torch_cuda_available = torch.cuda.is_available()
        except ImportError:
            torch_cuda_available = False
        
        try:
            import intel_extension_for_pytorch
            intel_available = True
        except ImportError:
            intel_available = False
        
        # Determine installation type
        if nvidia_available and torch_cuda_available and intel_available:
            return "all"
        elif nvidia_available and torch_cuda_available:
            return "nvidia"
        elif intel_available:
            return "intel"
        else:
            return "basic"


# Custom exceptions
class ConfigurationError(Exception):
    """Raised when configuration operations fail."""
    pass
