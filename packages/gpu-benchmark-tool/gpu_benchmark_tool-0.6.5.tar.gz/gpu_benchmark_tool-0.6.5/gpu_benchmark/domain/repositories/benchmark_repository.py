"""Benchmark Repository interface.

This module defines the contract for benchmark result data access operations.
"""

from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from datetime import datetime

from ..models.benchmark_result import BenchmarkResult


class BenchmarkRepository(ABC):
    """Abstract repository for benchmark result operations.
    
    This interface defines the contract for persisting and retrieving
    benchmark results. Implementations should handle the specific details
    of data storage, serialization, and retrieval.
    """
    
    @abstractmethod
    def save_benchmark_result(self, result: BenchmarkResult) -> str:
        """Save a benchmark result.
        
        Args:
            result: The benchmark result to save.
            
        Returns:
            str: The unique identifier for the saved result.
            
        Raises:
            PersistenceError: If saving fails.
        """
        pass
    
    @abstractmethod
    def load_benchmark_result(self, benchmark_id: str) -> Optional[BenchmarkResult]:
        """Load a benchmark result by ID.
        
        Args:
            benchmark_id: The unique identifier of the benchmark result.
            
        Returns:
            Optional[BenchmarkResult]: The benchmark result if found, None otherwise.
            
        Raises:
            PersistenceError: If loading fails.
        """
        pass
    
    @abstractmethod
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
        pass
    
    @abstractmethod
    def delete_benchmark_result(self, benchmark_id: str) -> bool:
        """Delete a benchmark result.
        
        Args:
            benchmark_id: The unique identifier of the benchmark result.
            
        Returns:
            bool: True if deleted successfully, False if not found.
            
        Raises:
            PersistenceError: If deletion fails.
        """
        pass
    
    @abstractmethod
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
        pass
    
    @abstractmethod
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
        pass
    
    @abstractmethod
    def import_benchmark_results(self, file_path: str) -> List[BenchmarkResult]:
        """Import benchmark results from a file.
        
        Args:
            file_path: Path to the file to import.
            
        Returns:
            List[BenchmarkResult]: List of imported benchmark results.
            
        Raises:
            ImportError: If import fails.
        """
        pass
    
    @abstractmethod
    def get_latest_benchmark_result(self, device_id: int) -> Optional[BenchmarkResult]:
        """Get the most recent benchmark result for a device.
        
        Args:
            device_id: The GPU device ID.
            
        Returns:
            Optional[BenchmarkResult]: The most recent result if found, None otherwise.
            
        Raises:
            PersistenceError: If querying fails.
        """
        pass
    
    @abstractmethod
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
        pass
