"""Data Migration Utility.

This utility helps migrate existing benchmark results to the new format.
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, Optional, List
from datetime import datetime
import logging

from ...domain.models.benchmark_result import BenchmarkResult, BenchmarkMetadata, BenchmarkStatus
from ...domain.models.gpu_device import GPUDevice, GPUInfo, GPUMetrics, GPUType, GPUStatus
from ...domain.models.health_score import HealthScore, HealthScoreBreakdown, HealthStatus


class DataMigration:
    """Utility for migrating benchmark data to the new system."""
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """Initialize the data migration utility.
        
        Args:
            logger: Logger for migration operations.
        """
        self._logger = logger or logging.getLogger(__name__)
    
    def migrate_legacy_benchmark_result(self, legacy_result: Dict[str, Any]) -> BenchmarkResult:
        """Migrate a legacy benchmark result to the new format.
        
        Args:
            legacy_result: Legacy benchmark result dictionary.
            
        Returns:
            BenchmarkResult: New benchmark result object.
        """
        try:
            # Extract metadata
            metadata = self._migrate_metadata(legacy_result)
            
            # Extract GPU device information
            gpu_device = self._migrate_gpu_device(legacy_result.get("gpu_info", {}))
            
            # Extract health score
            health_score = self._migrate_health_score(legacy_result.get("health_score", {}))
            
            # Extract stress test results
            stress_test_results = legacy_result.get("stress_test_results", {})
            
            # Extract performance metrics
            performance_metrics = legacy_result.get("performance_metrics", {})
            
            # Extract warnings and errors
            warnings = legacy_result.get("warnings", [])
            errors = legacy_result.get("errors", [])
            
            # Determine status
            status = self._determine_status(legacy_result, warnings, errors)
            
            # Create new benchmark result
            result = BenchmarkResult(
                metadata=metadata,
                gpu_device=gpu_device,
                health_score=health_score,
                stress_test_results=stress_test_results,
                performance_metrics=performance_metrics,
                warnings=warnings,
                errors=errors,
                status=status
            )
            
            self._logger.info(f"Migrated legacy benchmark result: {metadata.benchmark_id}")
            return result
            
        except Exception as e:
            self._logger.error(f"Failed to migrate legacy benchmark result: {e}")
            # Return a minimal result as fallback
            return self._create_fallback_result(legacy_result)
    
    def _migrate_metadata(self, legacy_result: Dict[str, Any]) -> BenchmarkMetadata:
        """Migrate metadata from legacy format."""
        # Extract timestamp
        timestamp = legacy_result.get("timestamp")
        if isinstance(timestamp, str):
            timestamp = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
        elif timestamp is None:
            timestamp = datetime.utcnow()
        
        # Extract duration
        duration = legacy_result.get("duration_seconds", 0.0)
        
        # Extract device ID
        device_id = legacy_result.get("gpu_info", {}).get("device_id", 0)
        
        # Generate benchmark ID if not present
        benchmark_id = legacy_result.get("benchmark_id", f"migrated_{timestamp.strftime('%Y%m%d_%H%M%S')}")
        
        return BenchmarkMetadata(
            benchmark_id=benchmark_id,
            version="1.0.0",
            timestamp=timestamp,
            duration_seconds=duration,
            gpu_device_id=device_id,
            benchmark_type="migrated",
            configuration=legacy_result.get("configuration", {})
        )
    
    def _migrate_gpu_device(self, legacy_gpu_info: Dict[str, Any]) -> GPUDevice:
        """Migrate GPU device information from legacy format."""
        # Map GPU type
        gpu_type_str = legacy_gpu_info.get("gpu_type", "unknown").lower()
        gpu_type_map = {
            "nvidia": GPUType.NVIDIA,
            "amd": GPUType.AMD,
            "intel": GPUType.INTEL,
            "mock": GPUType.MOCK
        }
        gpu_type = gpu_type_map.get(gpu_type_str, GPUType.UNKNOWN)
        
        # Create GPU info
        gpu_info = GPUInfo(
            name=legacy_gpu_info.get("name", "Unknown GPU"),
            device_id=legacy_gpu_info.get("device_id", 0),
            gpu_type=gpu_type,
            memory_total_mb=legacy_gpu_info.get("memory_total_mb", 0),
            memory_used_mb=legacy_gpu_info.get("memory_used_mb", 0),
            driver_version=legacy_gpu_info.get("driver_version"),
            cuda_version=legacy_gpu_info.get("cuda_version"),
            is_mock=legacy_gpu_info.get("is_mock", False)
        )
        
        # Create GPU device
        gpu_device = GPUDevice(info=gpu_info, status=GPUStatus.UNKNOWN)
        
        # Add metrics if available
        if "current_metrics" in legacy_gpu_info:
            metrics_data = legacy_gpu_info["current_metrics"]
            metrics = GPUMetrics(
                temperature_celsius=metrics_data.get("temperature_celsius", 45.0),
                power_usage_watts=metrics_data.get("power_usage_watts", 0.0),
                utilization_percent=metrics_data.get("utilization_percent", 0.0),
                fan_speed_percent=metrics_data.get("fan_speed_percent"),
                clock_speed_mhz=metrics_data.get("clock_speed_mhz"),
                memory_clock_mhz=metrics_data.get("memory_clock_mhz")
            )
            gpu_device.update_metrics(metrics)
        
        return gpu_device
    
    def _migrate_health_score(self, legacy_health: Dict[str, Any]) -> HealthScore:
        """Migrate health score from legacy format."""
        # Extract basic health information
        score = legacy_health.get("score", 0.0)
        status_str = legacy_health.get("status", "unknown").lower()
        
        # Map status
        status_map = {
            "healthy": HealthStatus.HEALTHY,
            "good": HealthStatus.GOOD,
            "degraded": HealthStatus.DEGRADED,
            "warning": HealthStatus.WARNING,
            "critical": HealthStatus.CRITICAL
        }
        status = status_map.get(status_str, HealthStatus.UNKNOWN)
        
        # Extract breakdown
        breakdown_data = legacy_health.get("details", {}).get("breakdown", {})
        breakdown = HealthScoreBreakdown(
            temperature=breakdown_data.get("temperature", 0.0),
            baseline_temperature=breakdown_data.get("baseline_temperature", 0.0),
            power_efficiency=breakdown_data.get("power_efficiency", 0.0),
            utilization=breakdown_data.get("utilization", 0.0),
            throttling=breakdown_data.get("throttling", 0.0),
            errors=breakdown_data.get("errors", 0.0),
            temperature_stability=breakdown_data.get("temperature_stability", 0.0)
        )
        
        # Extract recommendation
        recommendation = legacy_health.get("recommendation", "No recommendation available")
        
        # Extract specific recommendations
        specific_recommendations = legacy_health.get("details", {}).get("specific_recommendations", [])
        
        # Create health score
        health_score = HealthScore(
            score=score,
            status=status,
            breakdown=breakdown,
            recommendation=recommendation,
            specific_recommendations=specific_recommendations
        )
        
        return health_score
    
    def _determine_status(self, legacy_result: Dict[str, Any], warnings: List[str], errors: List[str]) -> BenchmarkStatus:
        """Determine benchmark status from legacy data."""
        if errors:
            return BenchmarkStatus.FAILED
        elif warnings:
            return BenchmarkStatus.PARTIAL_SUCCESS
        else:
            return BenchmarkStatus.SUCCESS
    
    def _create_fallback_result(self, legacy_result: Dict[str, Any]) -> BenchmarkResult:
        """Create a fallback result when migration fails."""
        # Create minimal metadata
        metadata = BenchmarkMetadata(
            benchmark_id=f"fallback_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}",
            timestamp=datetime.utcnow(),
            duration_seconds=0.0,
            gpu_device_id=0,
            benchmark_type="fallback"
        )
        
        # Create minimal GPU device
        gpu_info = GPUInfo(
            name="Unknown GPU (Migration Failed)",
            device_id=0,
            gpu_type=GPUType.UNKNOWN,
            memory_total_mb=0,
            memory_used_mb=0,
            is_mock=True
        )
        gpu_device = GPUDevice(info=gpu_info, status=GPUStatus.UNKNOWN)
        
        # Create minimal health score
        breakdown = HealthScoreBreakdown()
        health_score = HealthScore.create(
            breakdown=breakdown,
            recommendation="Migration failed - using default values"
        )
        
        return BenchmarkResult(
            metadata=metadata,
            gpu_device=gpu_device,
            health_score=health_score,
            status=BenchmarkStatus.FAILED,
            errors=["Migration failed"]
        )
    
    def migrate_benchmark_file(self, legacy_file_path: str, new_file_path: str) -> bool:
        """Migrate a benchmark result file from legacy to new format.
        
        Args:
            legacy_file_path: Path to legacy benchmark file.
            new_file_path: Path to save new benchmark file.
            
        Returns:
            bool: True if migration successful, False otherwise.
        """
        try:
            # Read legacy benchmark result
            with open(legacy_file_path, 'r') as f:
                legacy_result = json.load(f)
            
            # Migrate benchmark result
            new_result = self.migrate_legacy_benchmark_result(legacy_result)
            
            # Save new benchmark result
            with open(new_file_path, 'w') as f:
                json.dump(new_result.to_dict(), f, indent=2)
            
            self._logger.info(f"Migrated benchmark file: {legacy_file_path} -> {new_file_path}")
            return True
            
        except Exception as e:
            self._logger.error(f"Failed to migrate benchmark file {legacy_file_path}: {e}")
            return False
    
    def migrate_directory(self, legacy_dir: str, new_dir: str) -> Dict[str, Any]:
        """Migrate all benchmark files in a directory.
        
        Args:
            legacy_dir: Directory containing legacy benchmark files.
            new_dir: Directory to save new benchmark files.
            
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
            
            # Create new filename with migrated prefix
            new_file = new_path / f"migrated_{legacy_file.name}"
            
            if self.migrate_benchmark_file(str(legacy_file), str(new_file)):
                results["successful_migrations"] += 1
            else:
                results["failed_migrations"] += 1
                results["errors"].append(f"Failed to migrate {legacy_file.name}")
        
        self._logger.info(f"Migration complete: {results['successful_migrations']}/{results['total_files']} files migrated")
        return results
    
    def validate_migrated_result(self, result: BenchmarkResult) -> List[str]:
        """Validate a migrated benchmark result.
        
        Args:
            result: Benchmark result to validate.
            
        Returns:
            List of validation errors (empty if valid).
        """
        errors = []
        
        # Validate metadata
        if not result.metadata.benchmark_id:
            errors.append("Missing benchmark ID")
        
        if result.metadata.duration_seconds < 0:
            errors.append("Invalid duration")
        
        # Validate GPU device
        if not result.gpu_device.info.name:
            errors.append("Missing GPU name")
        
        if result.gpu_device.info.memory_total_mb <= 0:
            errors.append("Invalid memory total")
        
        # Validate health score
        if not 0 <= result.health_score.score <= 100:
            errors.append("Invalid health score")
        
        return errors
    
    def create_migration_report(self, migration_results: Dict[str, Any]) -> str:
        """Create a migration report.
        
        Args:
            migration_results: Results from migration operations.
            
        Returns:
            str: Formatted migration report.
        """
        report = []
        report.append("=" * 60)
        report.append("GPU Benchmark Tool - Data Migration Report")
        report.append("=" * 60)
        report.append(f"Total files processed: {migration_results['total_files']}")
        report.append(f"Successful migrations: {migration_results['successful_migrations']}")
        report.append(f"Failed migrations: {migration_results['failed_migrations']}")
        report.append("")
        
        if migration_results['errors']:
            report.append("Errors encountered:")
            for error in migration_results['errors']:
                report.append(f"  - {error}")
            report.append("")
        
        success_rate = (migration_results['successful_migrations'] / migration_results['total_files'] * 100) if migration_results['total_files'] > 0 else 0
        report.append(f"Success rate: {success_rate:.1f}%")
        report.append("=" * 60)
        
        return "\n".join(report)
