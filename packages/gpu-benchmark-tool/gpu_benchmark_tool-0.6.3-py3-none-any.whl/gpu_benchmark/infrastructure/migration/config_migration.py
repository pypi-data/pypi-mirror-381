"""Configuration Migration Utility.

This utility helps migrate existing configurations to the new system.
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, Optional, List
import logging

from ...domain.models.configuration import BenchmarkConfig, BenchmarkType, UseCase, ScoringThresholds


class ConfigMigration:
    """Utility for migrating configurations to the new system."""
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """Initialize the configuration migration utility.
        
        Args:
            logger: Logger for migration operations.
        """
        self._logger = logger or logging.getLogger(__name__)
    
    def migrate_legacy_config(self, legacy_config: Dict[str, Any]) -> BenchmarkConfig:
        """Migrate a legacy configuration to the new format.
        
        Args:
            legacy_config: Legacy configuration dictionary.
            
        Returns:
            BenchmarkConfig: New configuration object.
        """
        try:
            # Map legacy configuration to new format
            benchmark_type = self._map_benchmark_type(legacy_config.get("type", "standard"))
            use_case = self._map_use_case(legacy_config.get("use_case", "general"))
            duration = legacy_config.get("duration", 60)
            device_id = legacy_config.get("gpu_id", 0)
            
            # Create new configuration
            config = BenchmarkConfig(
                benchmark_type=benchmark_type,
                use_case=use_case,
                duration_seconds=duration,
                gpu_device_id=device_id,
                include_ai_benchmarks=legacy_config.get("include_ai", False),
                include_stress_tests=legacy_config.get("include_stress_tests", True),
                include_health_scoring=legacy_config.get("include_health_scoring", True),
                export_results=legacy_config.get("export_results", True),
                export_format=legacy_config.get("export_format", "json"),
                export_path=legacy_config.get("export_path")
            )
            
            self._logger.info(f"Migrated legacy config: {legacy_config.get('name', 'unnamed')}")
            return config
            
        except Exception as e:
            self._logger.error(f"Failed to migrate legacy config: {e}")
            # Return default configuration as fallback
            return BenchmarkConfig()
    
    def _map_benchmark_type(self, legacy_type: str) -> BenchmarkType:
        """Map legacy benchmark type to new enum."""
        type_mapping = {
            "quick": BenchmarkType.QUICK,
            "standard": BenchmarkType.STANDARD,
            "comprehensive": BenchmarkType.COMPREHENSIVE,
            "ai_workload": BenchmarkType.AI_WORKLOAD,
            "custom": BenchmarkType.CUSTOM
        }
        return type_mapping.get(legacy_type.lower(), BenchmarkType.STANDARD)
    
    def _map_use_case(self, legacy_use_case: str) -> UseCase:
        """Map legacy use case to new enum."""
        use_case_mapping = {
            "gaming": UseCase.GAMING,
            "ai_training": UseCase.AI_TRAINING,
            "ai_inference": UseCase.AI_INFERENCE,
            "mining": UseCase.MINING,
            "rendering": UseCase.RENDERING,
            "general": UseCase.GENERAL
        }
        return use_case_mapping.get(legacy_use_case.lower(), UseCase.GENERAL)
    
    def migrate_scoring_thresholds(self, legacy_thresholds: Dict[str, Any]) -> ScoringThresholds:
        """Migrate legacy scoring thresholds to new format.
        
        Args:
            legacy_thresholds: Legacy thresholds dictionary.
            
        Returns:
            ScoringThresholds: New thresholds object.
        """
        try:
            thresholds = ScoringThresholds(
                healthy_min=legacy_thresholds.get("healthy_min", 85.0),
                good_min=legacy_thresholds.get("good_min", 70.0),
                degraded_min=legacy_thresholds.get("degraded_min", 55.0),
                warning_min=legacy_thresholds.get("warning_min", 40.0),
                critical_min=legacy_thresholds.get("critical_min", 0.0),
                temperature_weight=legacy_thresholds.get("temperature_weight", 0.2),
                baseline_temperature_weight=legacy_thresholds.get("baseline_temperature_weight", 0.1),
                power_efficiency_weight=legacy_thresholds.get("power_efficiency_weight", 0.1),
                utilization_weight=legacy_thresholds.get("utilization_weight", 0.1),
                throttling_weight=legacy_thresholds.get("throttling_weight", 0.2),
                errors_weight=legacy_thresholds.get("errors_weight", 0.2),
                temperature_stability_weight=legacy_thresholds.get("temperature_stability_weight", 0.1)
            )
            
            self._logger.info("Migrated legacy scoring thresholds")
            return thresholds
            
        except Exception as e:
            self._logger.error(f"Failed to migrate scoring thresholds: {e}")
            # Return default thresholds as fallback
            return ScoringThresholds()
    
    def migrate_config_file(self, legacy_file_path: str, new_file_path: str) -> bool:
        """Migrate a configuration file from legacy to new format.
        
        Args:
            legacy_file_path: Path to legacy configuration file.
            new_file_path: Path to save new configuration file.
            
        Returns:
            bool: True if migration successful, False otherwise.
        """
        try:
            # Read legacy configuration
            with open(legacy_file_path, 'r') as f:
                legacy_config = json.load(f)
            
            # Migrate configuration
            new_config = self.migrate_legacy_config(legacy_config)
            
            # Save new configuration
            with open(new_file_path, 'w') as f:
                json.dump(new_config.to_dict(), f, indent=2)
            
            self._logger.info(f"Migrated config file: {legacy_file_path} -> {new_file_path}")
            return True
            
        except Exception as e:
            self._logger.error(f"Failed to migrate config file {legacy_file_path}: {e}")
            return False
    
    def migrate_directory(self, legacy_dir: str, new_dir: str) -> Dict[str, Any]:
        """Migrate all configuration files in a directory.
        
        Args:
            legacy_dir: Directory containing legacy configurations.
            new_dir: Directory to save new configurations.
            
        Returns:
            Dict with migration results.
        """
        legacy_path = Path(legacy_dir)
        new_path = Path(new_dir)
        
        # Create new directory if it doesn't exist
        new_path.mkdir(parents=True, exist_ok=True)
        
        results = {
            "total_files": 0,
            "successful_migrations": 0,
            "failed_migrations": 0,
            "errors": []
        }
        
        # Find all JSON files in legacy directory
        for legacy_file in legacy_path.glob("*.json"):
            results["total_files"] += 1
            
            new_file = new_path / legacy_file.name
            
            if self.migrate_config_file(str(legacy_file), str(new_file)):
                results["successful_migrations"] += 1
            else:
                results["failed_migrations"] += 1
                results["errors"].append(f"Failed to migrate {legacy_file.name}")
        
        self._logger.info(f"Migration complete: {results['successful_migrations']}/{results['total_files']} files migrated")
        return results
    
    def create_default_configs(self, config_dir: str) -> None:
        """Create default configuration files for the new system.
        
        Args:
            config_dir: Directory to create default configs in.
        """
        config_path = Path(config_dir)
        config_path.mkdir(parents=True, exist_ok=True)
        
        # Create default benchmark configurations
        default_configs = {
            "quick": BenchmarkConfig(
                benchmark_type=BenchmarkType.QUICK,
                use_case=UseCase.GENERAL,
                duration_seconds=30
            ),
            "standard": BenchmarkConfig(
                benchmark_type=BenchmarkType.STANDARD,
                use_case=UseCase.GENERAL,
                duration_seconds=60
            ),
            "comprehensive": BenchmarkConfig(
                benchmark_type=BenchmarkType.COMPREHENSIVE,
                use_case=UseCase.AI_TRAINING,
                duration_seconds=120,
                include_ai_benchmarks=True
            ),
            "gaming": BenchmarkConfig(
                benchmark_type=BenchmarkType.QUICK,
                use_case=UseCase.GAMING,
                duration_seconds=30,
                include_ai_benchmarks=False
            ),
            "ai_training": BenchmarkConfig(
                benchmark_type=BenchmarkType.COMPREHENSIVE,
                use_case=UseCase.AI_TRAINING,
                duration_seconds=120,
                include_ai_benchmarks=True
            )
        }
        
        # Save default configurations
        for name, config in default_configs.items():
            config_file = config_path / f"{name}.json"
            with open(config_file, 'w') as f:
                json.dump(config.to_dict(), f, indent=2)
        
        # Create default scoring thresholds
        thresholds_file = config_path / "scoring_thresholds.json"
        with open(thresholds_file, 'w') as f:
            json.dump(ScoringThresholds().to_dict(), f, indent=2)
        
        self._logger.info(f"Created default configurations in {config_dir}")
    
    def validate_migrated_config(self, config: BenchmarkConfig) -> List[str]:
        """Validate a migrated configuration.
        
        Args:
            config: Configuration to validate.
            
        Returns:
            List of validation errors (empty if valid).
        """
        errors = []
        
        try:
            config.validate()
        except ValueError as e:
            errors.append(str(e))
        
        # Additional custom validations
        if config.duration_seconds <= 0:
            errors.append("Duration must be positive")
        
        if config.gpu_device_id < 0:
            errors.append("GPU device ID must be non-negative")
        
        if config.export_format not in ["json", "yaml", "csv"]:
            errors.append("Export format must be json, yaml, or csv")
        
        return errors
