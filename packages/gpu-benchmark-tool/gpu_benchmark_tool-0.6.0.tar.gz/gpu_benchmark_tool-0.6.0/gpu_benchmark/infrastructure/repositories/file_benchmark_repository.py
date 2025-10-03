"""File-based Benchmark Repository implementation.

This implementation stores benchmark results in JSON files.
"""

import json
import os
import uuid
from datetime import datetime
from typing import List, Optional, Dict, Any
from pathlib import Path

from ...domain.repositories.benchmark_repository import BenchmarkRepository
from ...domain.models.benchmark_result import BenchmarkResult


class FileBenchmarkRepository(BenchmarkRepository):
    """File-based implementation of BenchmarkRepository.
    
    This implementation stores benchmark results as JSON files in a
    configurable directory. It provides basic CRUD operations and
    simple querying capabilities.
    """
    
    def __init__(self, storage_dir: str = "benchmark_results"):
        """Initialize the file-based repository.
        
        Args:
            storage_dir: Directory to store benchmark result files.
        """
        self._storage_dir = Path(storage_dir)
        self._storage_dir.mkdir(parents=True, exist_ok=True)
    
    def save_benchmark_result(self, result: BenchmarkResult) -> str:
        """Save a benchmark result to a JSON file.
        
        Args:
            result: The benchmark result to save.
            
        Returns:
            str: The unique identifier for the saved result.
            
        Raises:
            PersistenceError: If saving fails.
        """
        try:
            # Generate unique ID if not present
            if not result.metadata.benchmark_id:
                benchmark_id = str(uuid.uuid4())
                # Create new metadata with ID
                from ...domain.models.benchmark_result import BenchmarkMetadata
                metadata = BenchmarkMetadata(
                    benchmark_id=benchmark_id,
                    version=result.metadata.version,
                    timestamp=result.metadata.timestamp,
                    duration_seconds=result.metadata.duration_seconds,
                    gpu_device_id=result.metadata.gpu_device_id,
                    benchmark_type=result.metadata.benchmark_type,
                    configuration=result.metadata.configuration
                )
                # Create new result with ID
                result = BenchmarkResult(
                    metadata=metadata,
                    gpu_device=result.gpu_device,
                    health_score=result.health_score,
                    stress_test_results=result.stress_test_results,
                    performance_metrics=result.performance_metrics,
                    warnings=result.warnings,
                    errors=result.errors,
                    status=result.status
                )
            else:
                benchmark_id = result.metadata.benchmark_id
            
            # Create filename
            timestamp = result.metadata.timestamp.strftime("%Y%m%d_%H%M%S")
            filename = f"benchmark_{benchmark_id}_{timestamp}.json"
            filepath = self._storage_dir / filename
            
            # Convert to dictionary and save
            data = result.to_dict()
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)
            
            return benchmark_id
            
        except Exception as e:
            raise PersistenceError(f"Failed to save benchmark result: {e}") from e
    
    def load_benchmark_result(self, benchmark_id: str) -> Optional[BenchmarkResult]:
        """Load a benchmark result by ID.
        
        Args:
            benchmark_id: The unique identifier of the benchmark result.
            
        Returns:
            Optional[BenchmarkResult]: The benchmark result if found, None otherwise.
            
        Raises:
            PersistenceError: If loading fails.
        """
        try:
            # Find file with matching ID
            for filepath in self._storage_dir.glob(f"benchmark_{benchmark_id}_*.json"):
                with open(filepath, 'r') as f:
                    data = json.load(f)
                    return BenchmarkResult.from_dict(data)
            
            return None
            
        except Exception as e:
            raise PersistenceError(f"Failed to load benchmark result {benchmark_id}: {e}") from e
    
    def list_benchmark_results(self, 
                              device_id: Optional[int] = None,
                              start_date: Optional[datetime] = None,
                              end_date: Optional[datetime] = None,
                              limit: Optional[int] = None) -> List[BenchmarkResult]:
        """List benchmark results with optional filtering.
        
        Args:
            device_id: Filter by GPU device ID.
            start_date: Filter results after this date.
            end_date: Filter results before this date.
            limit: Maximum number of results to return.
            
        Returns:
            List[BenchmarkResult]: List of matching benchmark results.
            
        Raises:
            PersistenceError: If querying fails.
        """
        try:
            results = []
            
            # Load all benchmark files
            for filepath in self._storage_dir.glob("benchmark_*.json"):
                try:
                    with open(filepath, 'r') as f:
                        data = json.load(f)
                        result = BenchmarkResult.from_dict(data)
                        
                        # Apply filters
                        if device_id is not None and result.metadata.gpu_device_id != device_id:
                            continue
                        
                        if start_date is not None and result.metadata.timestamp < start_date:
                            continue
                        
                        if end_date is not None and result.metadata.timestamp > end_date:
                            continue
                        
                        results.append(result)
                        
                except Exception as e:
                    # Skip corrupted files
                    continue
            
            # Sort by timestamp (newest first)
            results.sort(key=lambda r: r.metadata.timestamp, reverse=True)
            
            # Apply limit
            if limit is not None:
                results = results[:limit]
            
            return results
            
        except Exception as e:
            raise PersistenceError(f"Failed to list benchmark results: {e}") from e
    
    def delete_benchmark_result(self, benchmark_id: str) -> bool:
        """Delete a benchmark result.
        
        Args:
            benchmark_id: The unique identifier of the benchmark result.
            
        Returns:
            bool: True if deleted successfully, False if not found.
            
        Raises:
            PersistenceError: If deletion fails.
        """
        try:
            # Find and delete file with matching ID
            for filepath in self._storage_dir.glob(f"benchmark_{benchmark_id}_*.json"):
                filepath.unlink()
                return True
            
            return False
            
        except Exception as e:
            raise PersistenceError(f"Failed to delete benchmark result {benchmark_id}: {e}") from e
    
    def get_benchmark_statistics(self, 
                                device_id: Optional[int] = None,
                                days: int = 30) -> Dict[str, Any]:
        """Get benchmark statistics for a device.
        
        Args:
            device_id: The GPU device ID to get statistics for.
            days: Number of days to include in statistics.
            
        Returns:
            Dict[str, Any]: Statistics including average scores, trends, etc.
            
        Raises:
            PersistenceError: If querying fails.
        """
        try:
            # Get results from the last N days
            end_date = datetime.utcnow()
            start_date = datetime(end_date.year, end_date.month, end_date.day - days)
            
            results = self.list_benchmark_results(
                device_id=device_id,
                start_date=start_date,
                end_date=end_date
            )
            
            if not results:
                return {
                    "total_benchmarks": 0,
                    "average_health_score": 0.0,
                    "health_score_trend": "no_data",
                    "most_common_status": "unknown"
                }
            
            # Calculate statistics
            health_scores = [r.health_score.score for r in results]
            statuses = [r.health_score.status.value for r in results]
            
            # Calculate trend
            if len(health_scores) >= 2:
                recent_avg = sum(health_scores[:len(health_scores)//2]) / (len(health_scores)//2)
                older_avg = sum(health_scores[len(health_scores)//2:]) / (len(health_scores) - len(health_scores)//2)
                if recent_avg > older_avg:
                    trend = "improving"
                elif recent_avg < older_avg:
                    trend = "declining"
                else:
                    trend = "stable"
            else:
                trend = "insufficient_data"
            
            # Most common status
            status_counts = {}
            for status in statuses:
                status_counts[status] = status_counts.get(status, 0) + 1
            most_common_status = max(status_counts, key=status_counts.get)
            
            return {
                "total_benchmarks": len(results),
                "average_health_score": sum(health_scores) / len(health_scores),
                "min_health_score": min(health_scores),
                "max_health_score": max(health_scores),
                "health_score_trend": trend,
                "most_common_status": most_common_status,
                "status_distribution": status_counts,
                "date_range": {
                    "start": start_date.isoformat(),
                    "end": end_date.isoformat()
                }
            }
            
        except Exception as e:
            raise PersistenceError(f"Failed to get benchmark statistics: {e}") from e
    
    def export_benchmark_results(self, 
                                results: List[BenchmarkResult],
                                format: str = "json",
                                file_path: Optional[str] = None) -> str:
        """Export benchmark results to a file.
        
        Args:
            results: List of benchmark results to export.
            format: Export format ("json", "csv", "yaml").
            file_path: Optional file path. If None, generates a filename.
            
        Returns:
            str: The file path where results were exported.
            
        Raises:
            ExportError: If export fails.
        """
        try:
            if file_path is None:
                timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
                file_path = f"benchmark_export_{timestamp}.{format}"
            
            if format == "json":
                data = [result.to_dict() for result in results]
                with open(file_path, 'w') as f:
                    json.dump(data, f, indent=2)
            
            elif format == "csv":
                import csv
                with open(file_path, 'w', newline='') as f:
                    if results:
                        # Get fieldnames from first result
                        fieldnames = list(results[0].to_dict().keys())
                        writer = csv.DictWriter(f, fieldnames=fieldnames)
                        writer.writeheader()
                        for result in results:
                            writer.writerow(result.to_dict())
            
            elif format == "yaml":
                import yaml
                data = [result.to_dict() for result in results]
                with open(file_path, 'w') as f:
                    yaml.dump(data, f, default_flow_style=False)
            
            else:
                raise ValueError(f"Unsupported export format: {format}")
            
            return file_path
            
        except Exception as e:
            raise ExportError(f"Failed to export benchmark results: {e}") from e
    
    def import_benchmark_results(self, file_path: str) -> List[BenchmarkResult]:
        """Import benchmark results from a file.
        
        Args:
            file_path: Path to the file to import.
            
        Returns:
            List[BenchmarkResult]: List of imported benchmark results.
            
        Raises:
            ImportError: If import fails.
        """
        try:
            file_path = Path(file_path)
            
            if not file_path.exists():
                raise FileNotFoundError(f"File not found: {file_path}")
            
            if file_path.suffix.lower() == '.json':
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        return [BenchmarkResult.from_dict(item) for item in data]
                    else:
                        return [BenchmarkResult.from_dict(data)]
            
            elif file_path.suffix.lower() == '.yaml':
                import yaml
                with open(file_path, 'r') as f:
                    data = yaml.safe_load(f)
                    if isinstance(data, list):
                        return [BenchmarkResult.from_dict(item) for item in data]
                    else:
                        return [BenchmarkResult.from_dict(data)]
            
            else:
                raise ValueError(f"Unsupported import format: {file_path.suffix}")
            
        except Exception as e:
            raise ImportError(f"Failed to import benchmark results from {file_path}: {e}") from e
    
    def get_latest_benchmark_result(self, device_id: int) -> Optional[BenchmarkResult]:
        """Get the most recent benchmark result for a device.
        
        Args:
            device_id: The GPU device ID.
            
        Returns:
            Optional[BenchmarkResult]: The most recent result if found, None otherwise.
            
        Raises:
            PersistenceError: If querying fails.
        """
        try:
            results = self.list_benchmark_results(device_id=device_id, limit=1)
            return results[0] if results else None
            
        except Exception as e:
            raise PersistenceError(f"Failed to get latest benchmark result for device {device_id}: {e}") from e
    
    def compare_benchmark_results(self, 
                                 result1_id: str, 
                                 result2_id: str) -> Dict[str, Any]:
        """Compare two benchmark results.
        
        Args:
            result1_id: ID of the first benchmark result.
            result2_id: ID of the second benchmark result.
            
        Returns:
            Dict[str, Any]: Comparison data including differences and improvements.
            
        Raises:
            PersistenceError: If loading results fails.
        """
        try:
            result1 = self.load_benchmark_result(result1_id)
            result2 = self.load_benchmark_result(result2_id)
            
            if not result1 or not result2:
                raise ValueError("One or both benchmark results not found")
            
            # Compare health scores
            health_comparison = {
                "score1": result1.health_score.score,
                "score2": result2.health_score.score,
                "score_difference": result2.health_score.score - result1.health_score.score,
                "status1": result1.health_score.status.value,
                "status2": result2.health_score.status.value
            }
            
            # Compare performance metrics
            performance_comparison = {}
            if result1.performance_metrics and result2.performance_metrics:
                for key in set(result1.performance_metrics.keys()) | set(result2.performance_metrics.keys()):
                    val1 = result1.performance_metrics.get(key, 0)
                    val2 = result2.performance_metrics.get(key, 0)
                    if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
                        performance_comparison[key] = {
                            "value1": val1,
                            "value2": val2,
                            "difference": val2 - val1,
                            "improvement_percent": ((val2 - val1) / val1 * 100) if val1 != 0 else 0
                        }
            
            return {
                "result1_id": result1_id,
                "result2_id": result2_id,
                "health_comparison": health_comparison,
                "performance_comparison": performance_comparison,
                "timestamp1": result1.metadata.timestamp.isoformat(),
                "timestamp2": result2.metadata.timestamp.isoformat()
            }
            
        except Exception as e:
            raise PersistenceError(f"Failed to compare benchmark results: {e}") from e


# Custom exceptions
class PersistenceError(Exception):
    """Raised when data persistence operations fail."""
    pass


class ExportError(Exception):
    """Raised when export operations fail."""
    pass


class ImportError(Exception):
    """Raised when import operations fail."""
    pass
