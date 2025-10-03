"""AI Workload domain model.

This module defines AI workload results and related value objects.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
from enum import Enum


class WorkloadType(Enum):
    """Types of AI workloads."""
    TRAINING = "training"
    INFERENCE = "inference"
    FINE_TUNING = "fine_tuning"
    EVALUATION = "evaluation"


class ModelType(Enum):
    """Types of AI models."""
    RESNET = "resnet"
    TRANSFORMER = "transformer"
    VIT = "vit"
    CLIP = "clip"
    CUSTOM = "custom"


@dataclass(frozen=True)
class ModelConfig:
    """Immutable model configuration value object."""
    name: str
    model_type: ModelType
    input_size: Tuple[int, ...]
    batch_size: int
    num_epochs: int
    learning_rate: float
    target_accuracy: float = 0.95
    energy_cost_per_wh: float = 0.00012  # Cost per Wh in dollars
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "name": self.name,
            "model_type": self.model_type.value,
            "input_size": list(self.input_size),
            "batch_size": self.batch_size,
            "num_epochs": self.num_epochs,
            "learning_rate": self.learning_rate,
            "target_accuracy": self.target_accuracy,
            "energy_cost_per_wh": self.energy_cost_per_wh
        }


@dataclass(frozen=True)
class CostMetrics:
    """Immutable cost metrics value object."""
    # Basic metrics
    training_time_seconds: float
    training_energy_wh: float
    inference_time_seconds: float
    inference_energy_wh: float
    time_to_accuracy: float
    
    # Performance metrics
    training_throughput_samples_per_second: float
    inference_throughput_samples_per_second: float
    training_wh_per_sample: float
    inference_wh_per_sample: float
    
    # Cost analysis (in cents for better readability)
    training_cost_per_sample_cents: float
    inference_cost_per_sample_cents: float
    total_training_cost_cents: float
    total_inference_cost_cents: float
    
    # Efficiency metrics
    energy_per_accuracy_point: float
    time_per_accuracy_point: float
    samples_per_wh: float
    final_accuracy: float
    
    # Power profile
    avg_power_watts: float
    peak_power_watts: float
    min_power_watts: float
    power_variance: float
    
    # Memory analysis
    peak_memory_usage_gb: float
    memory_efficiency_gb_per_sample: float
    
    def get_efficiency_score(self) -> float:
        """Calculate overall efficiency score (0.0 to 1.0)."""
        # Combine multiple efficiency metrics
        time_efficiency = 1.0 / (1.0 + self.time_per_accuracy_point / 1000.0)
        energy_efficiency = 1.0 / (1.0 + self.energy_per_accuracy_point / 100.0)
        throughput_efficiency = min(1.0, self.training_throughput_samples_per_second / 1000.0)
        
        return (time_efficiency + energy_efficiency + throughput_efficiency) / 3.0
    
    def get_cost_effectiveness(self) -> float:
        """Calculate cost effectiveness score (higher is better)."""
        if self.total_training_cost_cents == 0:
            return 0.0
        
        # Cost effectiveness = accuracy / cost
        return (self.final_accuracy * 100) / self.total_training_cost_cents
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            # Basic metrics
            "training_time_seconds": self.training_time_seconds,
            "training_energy_wh": self.training_energy_wh,
            "inference_time_seconds": self.inference_time_seconds,
            "inference_energy_wh": self.inference_energy_wh,
            "time_to_accuracy": self.time_to_accuracy,
            
            # Performance metrics
            "training_throughput_samples_per_second": self.training_throughput_samples_per_second,
            "inference_throughput_samples_per_second": self.inference_throughput_samples_per_second,
            "training_wh_per_sample": self.training_wh_per_sample,
            "inference_wh_per_sample": self.inference_wh_per_sample,
            
            # Cost analysis
            "training_cost_per_sample_cents": self.training_cost_per_sample_cents,
            "inference_cost_per_sample_cents": self.inference_cost_per_sample_cents,
            "total_training_cost_cents": self.total_training_cost_cents,
            "total_inference_cost_cents": self.total_inference_cost_cents,
            
            # Efficiency metrics
            "energy_per_accuracy_point": self.energy_per_accuracy_point,
            "time_per_accuracy_point": self.time_per_accuracy_point,
            "samples_per_wh": self.samples_per_wh,
            "final_accuracy": self.final_accuracy,
            
            # Power profile
            "avg_power_watts": self.avg_power_watts,
            "peak_power_watts": self.peak_power_watts,
            "min_power_watts": self.min_power_watts,
            "power_variance": self.power_variance,
            
            # Memory analysis
            "peak_memory_usage_gb": self.peak_memory_usage_gb,
            "memory_efficiency_gb_per_sample": self.memory_efficiency_gb_per_sample,
            
            # Calculated metrics
            "efficiency_score": self.get_efficiency_score(),
            "cost_effectiveness": self.get_cost_effectiveness()
        }


@dataclass
class AIWorkloadResult:
    """AI Workload Result domain entity.
    
    This entity represents the result of an AI workload benchmark,
    including performance metrics, cost analysis, and efficiency scores.
    """
    model_config: ModelConfig
    workload_type: WorkloadType
    cost_metrics: CostMetrics
    execution_status: str = "success"
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    timestamp: datetime = field(default_factory=datetime.utcnow)
    
    def add_warning(self, warning: str) -> None:
        """Add a warning message."""
        if warning not in self.warnings:
            self.warnings.append(warning)
    
    def add_error(self, error: str) -> None:
        """Add an error message."""
        if error not in self.errors:
            self.errors.append(error)
    
    def is_successful(self) -> bool:
        """Check if workload execution was successful."""
        return self.execution_status == "success" and len(self.errors) == 0
    
    def get_performance_summary(self) -> Dict[str, Any]:
        """Get performance summary."""
        return {
            "model_name": self.model_config.name,
            "workload_type": self.workload_type.value,
            "final_accuracy": self.cost_metrics.final_accuracy,
            "training_time_hours": self.cost_metrics.training_time_seconds / 3600.0,
            "inference_time_ms": self.cost_metrics.inference_time_seconds * 1000.0,
            "total_cost_cents": self.cost_metrics.total_training_cost_cents + self.cost_metrics.total_inference_cost_cents,
            "efficiency_score": self.cost_metrics.get_efficiency_score(),
            "cost_effectiveness": self.cost_metrics.get_cost_effectiveness(),
            "peak_memory_gb": self.cost_metrics.peak_memory_usage_gb,
            "avg_power_watts": self.cost_metrics.avg_power_watts
        }
    
    def get_cost_breakdown(self) -> Dict[str, float]:
        """Get detailed cost breakdown."""
        return {
            "training_cost_cents": self.cost_metrics.total_training_cost_cents,
            "inference_cost_cents": self.cost_metrics.total_inference_cost_cents,
            "total_cost_cents": self.cost_metrics.total_training_cost_cents + self.cost_metrics.total_inference_cost_cents,
            "cost_per_training_sample_cents": self.cost_metrics.training_cost_per_sample_cents,
            "cost_per_inference_sample_cents": self.cost_metrics.inference_cost_per_sample_cents,
            "energy_cost_per_wh": self.model_config.energy_cost_per_wh
        }
    
    def get_efficiency_metrics(self) -> Dict[str, float]:
        """Get efficiency metrics."""
        return {
            "training_throughput_samples_per_second": self.cost_metrics.training_throughput_samples_per_second,
            "inference_throughput_samples_per_second": self.cost_metrics.inference_throughput_samples_per_second,
            "training_wh_per_sample": self.cost_metrics.training_wh_per_sample,
            "inference_wh_per_sample": self.cost_metrics.inference_wh_per_sample,
            "samples_per_wh": self.cost_metrics.samples_per_wh,
            "energy_per_accuracy_point": self.cost_metrics.energy_per_accuracy_point,
            "time_per_accuracy_point": self.cost_metrics.time_per_accuracy_point,
            "efficiency_score": self.cost_metrics.get_efficiency_score()
        }
    
    def compare_with(self, other: 'AIWorkloadResult') -> Dict[str, Any]:
        """Compare with another AI workload result."""
        if self.model_config.name != other.model_config.name:
            raise ValueError("Cannot compare results from different models")
        
        return {
            "model_name": self.model_config.name,
            "this_result": {
                "efficiency_score": self.cost_metrics.get_efficiency_score(),
                "total_cost_cents": self.cost_metrics.total_training_cost_cents + self.cost_metrics.total_inference_cost_cents,
                "training_time_hours": self.cost_metrics.training_time_seconds / 3600.0,
                "final_accuracy": self.cost_metrics.final_accuracy
            },
            "other_result": {
                "efficiency_score": other.cost_metrics.get_efficiency_score(),
                "total_cost_cents": other.cost_metrics.total_training_cost_cents + other.cost_metrics.total_inference_cost_cents,
                "training_time_hours": other.cost_metrics.training_time_seconds / 3600.0,
                "final_accuracy": other.cost_metrics.final_accuracy
            },
            "improvements": {
                "efficiency_improvement": self.cost_metrics.get_efficiency_score() - other.cost_metrics.get_efficiency_score(),
                "cost_reduction_cents": (other.cost_metrics.total_training_cost_cents + other.cost_metrics.total_inference_cost_cents) - 
                                      (self.cost_metrics.total_training_cost_cents + self.cost_metrics.total_inference_cost_cents),
                "time_reduction_hours": (other.cost_metrics.training_time_seconds - self.cost_metrics.training_time_seconds) / 3600.0,
                "accuracy_improvement": self.cost_metrics.final_accuracy - other.cost_metrics.final_accuracy
            }
        }
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "model_config": self.model_config.to_dict(),
            "workload_type": self.workload_type.value,
            "cost_metrics": self.cost_metrics.to_dict(),
            "execution_status": self.execution_status,
            "warnings": self.warnings,
            "errors": self.errors,
            "timestamp": self.timestamp.isoformat(),
            "performance_summary": self.get_performance_summary(),
            "cost_breakdown": self.get_cost_breakdown(),
            "efficiency_metrics": self.get_efficiency_metrics()
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'AIWorkloadResult':
        """Create AIWorkloadResult from dictionary."""
        config_data = data["model_config"]
        model_config = ModelConfig(
            name=config_data["name"],
            model_type=ModelType(config_data["model_type"]),
            input_size=tuple(config_data["input_size"]),
            batch_size=config_data["batch_size"],
            num_epochs=config_data["num_epochs"],
            learning_rate=config_data["learning_rate"],
            target_accuracy=config_data.get("target_accuracy", 0.95),
            energy_cost_per_wh=config_data.get("energy_cost_per_wh", 0.00012)
        )
        
        metrics_data = data["cost_metrics"]
        cost_metrics = CostMetrics(
            training_time_seconds=metrics_data["training_time_seconds"],
            training_energy_wh=metrics_data["training_energy_wh"],
            inference_time_seconds=metrics_data["inference_time_seconds"],
            inference_energy_wh=metrics_data["inference_energy_wh"],
            time_to_accuracy=metrics_data["time_to_accuracy"],
            training_throughput_samples_per_second=metrics_data["training_throughput_samples_per_second"],
            inference_throughput_samples_per_second=metrics_data["inference_throughput_samples_per_second"],
            training_wh_per_sample=metrics_data["training_wh_per_sample"],
            inference_wh_per_sample=metrics_data["inference_wh_per_sample"],
            training_cost_per_sample_cents=metrics_data["training_cost_per_sample_cents"],
            inference_cost_per_sample_cents=metrics_data["inference_cost_per_sample_cents"],
            total_training_cost_cents=metrics_data["total_training_cost_cents"],
            total_inference_cost_cents=metrics_data["total_inference_cost_cents"],
            energy_per_accuracy_point=metrics_data["energy_per_accuracy_point"],
            time_per_accuracy_point=metrics_data["time_per_accuracy_point"],
            samples_per_wh=metrics_data["samples_per_wh"],
            final_accuracy=metrics_data["final_accuracy"],
            avg_power_watts=metrics_data["avg_power_watts"],
            peak_power_watts=metrics_data["peak_power_watts"],
            min_power_watts=metrics_data["min_power_watts"],
            power_variance=metrics_data["power_variance"],
            peak_memory_usage_gb=metrics_data["peak_memory_usage_gb"],
            memory_efficiency_gb_per_sample=metrics_data["memory_efficiency_gb_per_sample"]
        )
        
        return cls(
            model_config=model_config,
            workload_type=WorkloadType(data["workload_type"]),
            cost_metrics=cost_metrics,
            execution_status=data.get("execution_status", "success"),
            warnings=data.get("warnings", []),
            errors=data.get("errors", []),
            timestamp=datetime.fromisoformat(data["timestamp"])
        )
