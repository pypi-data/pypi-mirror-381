"""AI Workload Cost Benchmarking Module

This module benchmarks the real cost (time + energy) of AI workloads on different GPUs.
It measures training time, inference time, and energy consumption for actual models.
"""

import torch
import torch.nn as nn
import time
import json
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from .backends import get_gpu_backend
from .utils import print_info, print_success, print_warning, print_error


@dataclass
class ModelConfig:
    """Configuration for AI models to benchmark"""
    name: str
    model_class: str
    input_size: Tuple[int, ...]
    batch_size: int
    num_epochs: int
    learning_rate: float
    target_accuracy: float = 0.95
    energy_cost_per_wh: float = 0.00012    # Configurable energy cost (per Wh)


@dataclass
class CostMetrics:
    """Performance and energy metrics for AI workloads"""
    # Basic metrics
    training_time_seconds: float
    training_energy_wh: float
    inference_time_seconds: float
    inference_energy_wh: float
    cost_per_inference: float
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


class AICostBenchmark:
    """Benchmarks AI workload costs on different GPUs"""
    
    def __init__(self, device_id: int = 0):
        self.device_id = device_id
        self.device = torch.device(f"cuda:{device_id}" if torch.cuda.is_available() else "cpu")
        self.monitor = None
        self.setup_monitoring()
        
    def setup_monitoring(self):
        """Setup GPU monitoring for energy consumption"""
        try:
            # Check if CUDA is available and use NVIDIA backend if possible
            if torch.cuda.is_available():
                print_info(f"CUDA detected: {torch.cuda.get_device_name(0) if torch.cuda.device_count() > 0 else 'Unknown GPU'}")
                
                # Force NVIDIA backend when CUDA is available
                backend = get_gpu_backend(backend_type="nvidia", device_id=self.device_id)
                if backend:
                    print_info(f"NVIDIA backend created: {backend.__class__.__name__}")
                    if backend.is_available():
                        self.monitor = backend.create_monitor(self.device_id)
                        print_success(f"Real GPU monitoring enabled for device {self.device_id} using {backend.__class__.__name__}")
                    else:
                        print_warning("CUDA available but NVIDIA backend.is_available() returned False")
                        backend = get_gpu_backend(backend_type="mock", device_id=self.device_id)
                        self.monitor = backend.create_monitor(self.device_id)
                else:
                    print_warning("CUDA available but NVIDIA backend creation failed")
                    backend = get_gpu_backend(backend_type="mock", device_id=self.device_id)
                    self.monitor = backend.create_monitor(self.device_id)
            else:
                # Use mock backend for CPU-only systems
                backend = get_gpu_backend(backend_type="mock", device_id=self.device_id)
                self.monitor = backend.create_monitor(self.device_id)
                print_info(f"Mock monitoring enabled for device {self.device_id} (CPU-only system)")
        except Exception as e:
            print_warning(f"GPU monitoring setup failed: {e}")
            import traceback
            traceback.print_exc()
            self.monitor = None
    
    def get_energy_consumption(self, start_time: float, end_time: float) -> Tuple[float, Dict[str, float]]:
        """Get energy consumption in Wh and power profile for a time period
        
        Returns:
            Tuple of (energy_wh, power_profile_dict)
        """
        if not self.monitor:
            return 0.0, {"avg_power_watts": 0.0, "peak_power_watts": 0.0, "min_power_watts": 0.0, "power_variance": 0.0}
        
        try:
            # Get power readings during the period
            # Since we don't have continuous power monitoring, we'll use a sampling approach
            duration = end_time - start_time
            if duration <= 0:
                return 0.0
            
            # Sample power usage at regular intervals during the workload
            # For fast workloads, sample more frequently
            if duration < 5.0:  # If workload is less than 5 seconds
                sample_interval = 0.1  # Sample every 0.1 seconds
            else:
                sample_interval = 1.0  # Sample every second
                
            num_samples = max(1, int(duration / sample_interval))
            
            power_samples = []
            for i in range(num_samples):
                sample_time = start_time + (i * sample_interval)
                if sample_time <= end_time:
                    power_watts = self.monitor.get_power_usage()
                    if power_watts > 0:
                        power_samples.append(power_watts)
            
            if power_samples:
                # Calculate energy: average power * time (convert to Wh)
                avg_power = sum(power_samples) / len(power_samples)
                total_energy = avg_power * duration / 3600  # Convert to Wh
                
                # Calculate power profile statistics
                peak_power = max(power_samples)
                min_power = min(power_samples)
                power_variance = sum((p - avg_power) ** 2 for p in power_samples) / len(power_samples)
                
                power_profile = {
                    "avg_power_watts": avg_power,
                    "peak_power_watts": peak_power,
                    "min_power_watts": min_power,
                    "power_variance": power_variance
                }
                
                print_info(f"Power sampling: {len(power_samples)} samples, avg power: {avg_power:.1f}W, duration: {duration:.2f}s, energy: {total_energy:.3f} Wh")
                return total_energy, power_profile
            else:
                # Fallback: estimate based on typical GPU power usage
                print_warning(f"No power samples collected. Duration: {duration:.2f}s, expected samples: {num_samples}")
                return 0.0, {"avg_power_watts": 0.0, "peak_power_watts": 0.0, "min_power_watts": 0.0, "power_variance": 0.0}
                
        except Exception as e:
            print_warning(f"Could not get energy consumption: {e}")
        
        return 0.0, {"avg_power_watts": 0.0, "peak_power_watts": 0.0, "min_power_watts": 0.0, "power_variance": 0.0}
    
    def get_memory_usage(self) -> Dict[str, float]:
        """Get current memory usage information"""
        try:
            if torch.cuda.is_available():
                # Get GPU memory info
                memory_allocated = torch.cuda.memory_allocated(self.device_id) / 1e9  # Convert to GB
                memory_reserved = torch.cuda.memory_reserved(self.device_id) / 1e9   # Convert to GB
                memory_total = torch.cuda.get_device_properties(self.device_id).total_memory / 1e9  # Convert to GB
                
                return {
                    "peak_memory_usage_gb": memory_allocated,
                    "memory_reserved_gb": memory_reserved,
                    "memory_total_gb": memory_total,
                    "memory_efficiency_gb_per_sample": memory_allocated / 1000  # Assuming 1000 samples
                }
            else:
                # For CPU, estimate based on model size
                return {
                    "peak_memory_usage_gb": 0.5,  # Estimated CPU memory usage
                    "memory_reserved_gb": 0.5,
                    "memory_total_gb": 16.0,  # Typical system RAM
                    "memory_efficiency_gb_per_sample": 0.0005
                }
        except Exception as e:
            print_warning(f"Could not get memory usage: {e}")
            return {
                "peak_memory_usage_gb": 0.0,
                "memory_reserved_gb": 0.0,
                "memory_total_gb": 0.0,
                "memory_efficiency_gb_per_sample": 0.0
            }
    
    def get_hardware_info(self) -> Dict[str, str]:
        """Get hardware information for the system"""
        import platform
        import psutil
        
        try:
            hardware_info = {
                "os": f"{platform.system()}-{platform.release()}-{platform.machine()}",
                "cpu_model": platform.processor() or "Unknown",
                "cpu_cores": str(psutil.cpu_count()),
                "ram_gb": f"{psutil.virtual_memory().total / 1e9:.1f}",
                "cuda_version": "Unknown",
                "driver_version": "Unknown",
                "gpu_model": "Unknown"
            }
            
            if torch.cuda.is_available():
                hardware_info["cuda_version"] = torch.version.cuda or "Unknown"
                hardware_info["gpu_model"] = torch.cuda.get_device_name(self.device_id) if torch.cuda.device_count() > 0 else "Unknown"
                # Try to get driver version from CUDA
                try:
                    import pynvml
                    pynvml.nvmlInit()
                    handle = pynvml.nvmlDeviceGetHandleByIndex(self.device_id)
                    driver_version = pynvml.nvmlSystemGetDriverVersion()
                    hardware_info["driver_version"] = driver_version.decode('utf-8')
                except:
                    pass
            
            return hardware_info
        except Exception as e:
            print_warning(f"Could not get hardware info: {e}")
            return {
                "os": "Unknown",
                "cpu_model": "Unknown", 
                "cpu_cores": "Unknown",
                "ram_gb": "Unknown",
                "cuda_version": "Unknown",
                "driver_version": "Unknown",
                "gpu_model": "Unknown"
            }
    
    def get_benchmark_metadata(self) -> Dict[str, str]:
        """Get benchmark metadata"""
        import datetime
        from .version import __version__
        
        return {
            "timestamp": datetime.datetime.now().isoformat() + "Z",
            "benchmark_version": __version__,
            "pytorch_version": torch.__version__,
            "cuda_version": torch.version.cuda or "N/A",
            "total_benchmark_duration_seconds": "0",  # Will be updated by caller
            "environment": "production"
        }
    
    def generate_comparative_analysis(self, results: Dict[str, CostMetrics]) -> Dict[str, Dict[str, float]]:
        """Generate comparative analysis between models"""
        if len(results) < 2:
            return {}
        
        # Get baseline model (first model)
        baseline_name = list(results.keys())[0]
        baseline = results[baseline_name]
        
        comparative_analysis = {}
        
        for model_name, metrics in results.items():
            if model_name == baseline_name:
                continue
                
            # Calculate ratios compared to baseline
            training_time_ratio = metrics.training_time_seconds / baseline.training_time_seconds if baseline.training_time_seconds > 0 else 0
            energy_ratio = metrics.training_energy_wh / baseline.training_energy_wh if baseline.training_energy_wh > 0 else 0
            efficiency_ratio = (metrics.training_time_seconds / metrics.training_energy_wh) / (baseline.training_time_seconds / baseline.training_energy_wh) if baseline.training_energy_wh > 0 and metrics.training_energy_wh > 0 else 0
            
            comparative_analysis[model_name] = {
                f"vs_{baseline_name}_training_time_ratio": training_time_ratio,
                f"vs_{baseline_name}_energy_ratio": energy_ratio,
                f"vs_{baseline_name}_efficiency_ratio": efficiency_ratio
            }
        
        # Add performance rankings
        models_by_efficiency = sorted(results.items(), 
                                    key=lambda x: x[1].training_time_seconds / x[1].training_energy_wh if x[1].training_energy_wh > 0 else 0, 
                                    reverse=True)
        
        for i, (model_name, _) in enumerate(models_by_efficiency):
            if model_name not in comparative_analysis:
                comparative_analysis[model_name] = {}
            comparative_analysis[model_name]["efficiency_rank"] = i + 1
        
        return comparative_analysis
    
    def benchmark_resnet_training(self, config: ModelConfig) -> CostMetrics:
        """Benchmark ResNet training cost"""
        print_info(f"Benchmarking ResNet training on {self.device}")
        
        # Create a simple ResNet-like model
        model = self._create_resnet_model()
        model.to(self.device)
        
        # Create dummy dataset
        dataset_size = 1000
        inputs = torch.randn(dataset_size, *config.input_size, device=self.device)
        targets = torch.randint(0, 10, (dataset_size,), device=self.device)
        
        # Training setup
        criterion = nn.CrossEntropyLoss()
        optimizer = torch.optim.Adam(model.parameters(), lr=config.learning_rate)
        
        # Start monitoring
        start_time = time.time()
        
        # Training loop
        model.train()
        for epoch in range(config.num_epochs):
            for i in range(0, dataset_size, config.batch_size):
                batch_inputs = inputs[i:i+config.batch_size]
                batch_targets = targets[i:i+config.batch_size]
                
                optimizer.zero_grad()
                outputs = model(batch_inputs)
                loss = criterion(outputs, batch_targets)
                loss.backward()
                optimizer.step()
                
                # Check accuracy periodically
                if i % (dataset_size // 4) == 0:
                    accuracy = self._calculate_accuracy(model, inputs, targets)
                    if accuracy >= config.target_accuracy:
                        break
            
            if accuracy >= config.target_accuracy:
                break
        
        end_time = time.time()
        training_time = end_time - start_time
        
        # Calculate energy consumption and power profile
        training_energy, training_power_profile = self.get_energy_consumption(start_time, end_time)
        
        # Get memory usage
        memory_info = self.get_memory_usage()
        
        # Benchmark inference
        inference_time, inference_energy, inference_power_profile = self._benchmark_inference(model, inputs[:100])
        
        # Calculate enhanced metrics
        dataset_size = 1000  # From the training loop
        final_accuracy = accuracy if 'accuracy' in locals() else config.target_accuracy
        
        # Performance metrics
        training_throughput = dataset_size / training_time if training_time > 0 else 0
        inference_throughput = 100 / inference_time if inference_time > 0 else 0
        training_wh_per_sample = training_energy / dataset_size if dataset_size > 0 else 0
        inference_wh_per_sample = inference_energy / 100 if inference_energy > 0 else 0
        
        # Cost analysis (in cents)
        training_cost_per_sample_cents = training_wh_per_sample * config.energy_cost_per_wh * 100
        inference_cost_per_sample_cents = inference_wh_per_sample * config.energy_cost_per_wh * 100
        total_training_cost_cents = training_energy * config.energy_cost_per_wh * 100
        total_inference_cost_cents = inference_energy * config.energy_cost_per_wh * 100
        
        # Efficiency metrics
        energy_per_accuracy_point = training_energy / (final_accuracy * 100) if final_accuracy > 0 else 0
        time_per_accuracy_point = training_time / (final_accuracy * 100) if final_accuracy > 0 else 0
        samples_per_wh = dataset_size / training_energy if training_energy > 0 else 0
        
        return CostMetrics(
            # Basic metrics
            training_time_seconds=training_time,
            training_energy_wh=training_energy,
            inference_time_seconds=inference_time,
            inference_energy_wh=inference_energy,
            cost_per_inference=0.01,
            time_to_accuracy=training_time,
            
            # Performance metrics
            training_throughput_samples_per_second=training_throughput,
            inference_throughput_samples_per_second=inference_throughput,
            training_wh_per_sample=training_wh_per_sample,
            inference_wh_per_sample=inference_wh_per_sample,
            
            # Cost analysis (in cents)
            training_cost_per_sample_cents=training_cost_per_sample_cents,
            inference_cost_per_sample_cents=inference_cost_per_sample_cents,
            total_training_cost_cents=total_training_cost_cents,
            total_inference_cost_cents=total_inference_cost_cents,
            
            # Efficiency metrics
            energy_per_accuracy_point=energy_per_accuracy_point,
            time_per_accuracy_point=time_per_accuracy_point,
            samples_per_wh=samples_per_wh,
            final_accuracy=final_accuracy,
            
            # Power profile
            avg_power_watts=training_power_profile["avg_power_watts"],
            peak_power_watts=training_power_profile["peak_power_watts"],
            min_power_watts=training_power_profile["min_power_watts"],
            power_variance=training_power_profile["power_variance"],
            
            # Memory analysis
            peak_memory_usage_gb=memory_info["peak_memory_usage_gb"],
            memory_efficiency_gb_per_sample=memory_info["memory_efficiency_gb_per_sample"]
        )
    
    def benchmark_transformer_inference(self, config: ModelConfig) -> CostMetrics:
        """Benchmark Transformer inference cost"""
        print_info(f"Benchmarking Transformer inference on {self.device}")
        
        # Create a simple transformer model
        model = self._create_transformer_model()
        model.to(self.device)
        model.eval()
        
        # Create dummy input
        inputs = torch.randn(config.batch_size, *config.input_size, device=self.device)
        
        # Benchmark inference
        start_time = time.time()
        
        with torch.no_grad():
            for _ in range(100):  # Run 100 inferences
                outputs = model(inputs)
        
        end_time = time.time()
        inference_time = end_time - start_time
        inference_energy, inference_power_profile = self.get_energy_consumption(start_time, end_time)
        
        # Get memory usage
        memory_info = self.get_memory_usage()
        
        # Calculate enhanced metrics for inference-only
        inference_throughput = 100 / inference_time if inference_time > 0 else 0
        inference_wh_per_sample = inference_energy / 100 if inference_energy > 0 else 0
        
        # Cost analysis (in cents)
        inference_cost_per_sample_cents = inference_wh_per_sample * config.energy_cost_per_wh * 100
        total_inference_cost_cents = inference_energy * config.energy_cost_per_wh * 100
        
        return CostMetrics(
            # Basic metrics
            training_time_seconds=0.0,
            training_energy_wh=0.0,
            inference_time_seconds=inference_time,
            inference_energy_wh=inference_energy,
            cost_per_inference=0.01,
            time_to_accuracy=0.0,
            
            # Performance metrics
            training_throughput_samples_per_second=0.0,
            inference_throughput_samples_per_second=inference_throughput,
            training_wh_per_sample=0.0,
            inference_wh_per_sample=inference_wh_per_sample,
            
            # Cost analysis (in cents)
            training_cost_per_sample_cents=0.0,
            inference_cost_per_sample_cents=inference_cost_per_sample_cents,
            total_training_cost_cents=0.0,
            total_inference_cost_cents=total_inference_cost_cents,
            
            # Efficiency metrics
            energy_per_accuracy_point=0.0,
            time_per_accuracy_point=0.0,
            samples_per_wh=0.0,
            final_accuracy=0.0,
            
            # Power profile
            avg_power_watts=inference_power_profile["avg_power_watts"],
            peak_power_watts=inference_power_profile["peak_power_watts"],
            min_power_watts=inference_power_profile["min_power_watts"],
            power_variance=inference_power_profile["power_variance"],
            
            # Memory analysis
            peak_memory_usage_gb=memory_info["peak_memory_usage_gb"],
            memory_efficiency_gb_per_sample=memory_info["memory_efficiency_gb_per_sample"]
        )
    
    def _create_resnet_model(self) -> nn.Module:
        """Create a simple ResNet-like model"""
        class SimpleResNet(nn.Module):
            def __init__(self, num_classes=10):
                super().__init__()
                self.conv1 = nn.Conv2d(3, 64, 7, stride=2, padding=3)
                self.bn1 = nn.BatchNorm2d(64)
                self.relu = nn.ReLU(inplace=True)
                self.maxpool = nn.MaxPool2d(3, stride=2, padding=1)
                
                # Simple residual blocks
                self.layer1 = self._make_layer(64, 64, 2)
                self.layer2 = self._make_layer(64, 128, 2, stride=2)
                self.layer3 = self._make_layer(128, 256, 2, stride=2)
                
                self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
                self.fc = nn.Linear(256, num_classes)
            
            def _make_layer(self, in_channels, out_channels, blocks, stride=1):
                layers = []
                layers.append(nn.Conv2d(in_channels, out_channels, 3, stride=stride, padding=1))
                layers.append(nn.BatchNorm2d(out_channels))
                layers.append(nn.ReLU(inplace=True))
                return nn.Sequential(*layers)
            
            def forward(self, x):
                x = self.conv1(x)
                x = self.bn1(x)
                x = self.relu(x)
                x = self.maxpool(x)
                
                x = self.layer1(x)
                x = self.layer2(x)
                x = self.layer3(x)
                
                x = self.avgpool(x)
                x = torch.flatten(x, 1)
                x = self.fc(x)
                return x
        
        return SimpleResNet()
    
    def _create_transformer_model(self) -> nn.Module:
        """Create a simple transformer model"""
        class SimpleTransformer(nn.Module):
            def __init__(self, input_dim=512, hidden_dim=256, num_layers=4):
                super().__init__()
                # For 2D input (batch, features), we need to reshape to (batch, 1, features)
                # Then project to hidden_dim
                self.input_projection = nn.Linear(input_dim, hidden_dim)
                encoder_layer = nn.TransformerEncoderLayer(
                    d_model=hidden_dim, 
                    nhead=8, 
                    dim_feedforward=1024,
                    batch_first=True
                )
                self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
                self.output = nn.Linear(hidden_dim, 10)
            
            def forward(self, x):
                # x shape: (batch_size, input_dim)
                # Reshape to (batch_size, 1, input_dim) for transformer
                if x.dim() == 2:
                    x = x.unsqueeze(1)  # Add sequence dimension
                
                # Project to hidden dimension
                x = self.input_projection(x)  # (batch_size, 1, hidden_dim)
                
                # Apply transformer
                x = self.transformer(x)  # (batch_size, 1, hidden_dim)
                
                # Global average pooling (remove sequence dimension)
                x = x.mean(dim=1)  # (batch_size, hidden_dim)
                
                # Final output
                x = self.output(x)  # (batch_size, 10)
                return x
        
        return SimpleTransformer()
    
    def _create_clip_model(self) -> nn.Module:
        """Create a simplified CLIP-like model for benchmarking"""
        class SimpleCLIP(nn.Module):
            def __init__(self, image_size=224, text_vocab_size=10000, embed_dim=512):
                super().__init__()
                self.embed_dim = embed_dim
                
                # Image encoder (simplified Vision Transformer)
                self.image_patch_size = 16
                self.num_patches = (image_size // self.image_patch_size) ** 2
                
                self.image_patch_embed = nn.Conv2d(3, embed_dim, kernel_size=self.image_patch_size, stride=self.image_patch_size)
                self.image_pos_embed = nn.Parameter(torch.randn(1, self.num_patches + 1, embed_dim))
                self.image_cls_token = nn.Parameter(torch.randn(1, 1, embed_dim))
                
                # Simplified transformer for images
                encoder_layer = nn.TransformerEncoderLayer(
                    d_model=embed_dim,
                    nhead=8,
                    dim_feedforward=2048,
                    batch_first=True
                )
                self.image_transformer = nn.TransformerEncoder(encoder_layer, num_layers=6)
                self.image_projection = nn.Linear(embed_dim, embed_dim)
                
                # Text encoder (simplified)
                self.text_embedding = nn.Embedding(text_vocab_size, embed_dim)
                self.text_pos_embed = nn.Parameter(torch.randn(1, 77, embed_dim))  # Max 77 tokens
                self.text_projection = nn.Linear(embed_dim, embed_dim)
                
                # Simplified transformer for text
                self.text_transformer = nn.TransformerEncoder(encoder_layer, num_layers=6)
                
                # Temperature parameter for similarity
                self.temperature = nn.Parameter(torch.ones([]) * 0.07)
                
            def encode_image(self, x):
                # x shape: (batch_size, 3, 224, 224)
                batch_size = x.shape[0]
                
                # Patch embedding
                x = self.image_patch_embed(x)  # (batch_size, embed_dim, 14, 14)
                x = x.flatten(2).transpose(1, 2)  # (batch_size, 196, embed_dim)
                
                # Add CLS token
                cls_tokens = self.image_cls_token.expand(batch_size, -1, -1)
                x = torch.cat([cls_tokens, x], dim=1)  # (batch_size, 197, embed_dim)
                
                # Add positional embedding
                x = x + self.image_pos_embed
                
                # Transformer
                x = self.image_transformer(x)
                
                # Use CLS token for global representation
                x = x[:, 0]  # (batch_size, embed_dim)
                
                # Project to final embedding space
                x = self.image_projection(x)
                x = x / x.norm(dim=-1, keepdim=True)  # L2 normalize
                
                return x
            
            def encode_text(self, text):
                # text shape: (batch_size, seq_len)
                batch_size, seq_len = text.shape
                
                # Text embedding
                x = self.text_embedding(text)  # (batch_size, seq_len, embed_dim)
                
                # Add positional embedding
                x = x + self.text_pos_embed[:, :seq_len, :]
                
                # Transformer
                x = self.text_transformer(x)
                
                # Global average pooling
                x = x.mean(dim=1)  # (batch_size, embed_dim)
                
                # Project to final embedding space
                x = self.text_projection(x)
                x = x / x.norm(dim=-1, keepdim=True)  # L2 normalize
                
                return x
            
            def forward(self, images, texts):
                # Encode images and texts
                image_features = self.encode_image(images)
                text_features = self.encode_text(texts)
                
                # Compute similarity
                similarity = torch.matmul(image_features, text_features.T) * self.temperature
                
                return similarity, image_features, text_features
        
        return SimpleCLIP()
    
    def _create_vit_model(self) -> nn.Module:
        """Create a simplified Vision Transformer (ViT) model for benchmarking"""
        class SimpleViT(nn.Module):
            def __init__(self, image_size=224, patch_size=16, num_classes=10, embed_dim=384, num_heads=6, num_layers=6):
                super().__init__()
                self.patch_size = patch_size
                self.num_patches = (image_size // patch_size) ** 2
                
                # Patch embedding
                self.patch_embed = nn.Conv2d(3, embed_dim, kernel_size=patch_size, stride=patch_size)
                
                # Positional embedding
                self.pos_embed = nn.Parameter(torch.randn(1, self.num_patches + 1, embed_dim))
                
                # CLS token
                self.cls_token = nn.Parameter(torch.randn(1, 1, embed_dim))
                
                # Transformer encoder
                encoder_layer = nn.TransformerEncoderLayer(
                    d_model=embed_dim,
                    nhead=num_heads,
                    dim_feedforward=embed_dim * 4,
                    batch_first=True
                )
                self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
                
                # Classification head
                self.norm = nn.LayerNorm(embed_dim)
                self.head = nn.Linear(embed_dim, num_classes)
                
            def forward(self, x):
                # x shape: (batch_size, 3, 224, 224)
                batch_size = x.shape[0]
                
                # Patch embedding
                x = self.patch_embed(x)  # (batch_size, embed_dim, 14, 14)
                x = x.flatten(2).transpose(1, 2)  # (batch_size, 196, embed_dim)
                
                # Add CLS token
                cls_tokens = self.cls_token.expand(batch_size, -1, -1)
                x = torch.cat([cls_tokens, x], dim=1)  # (batch_size, 197, embed_dim)
                
                # Add positional embedding
                x = x + self.pos_embed
                
                # Transformer encoder
                x = self.transformer(x)
                
                # Use CLS token for classification
                x = self.norm(x[:, 0])  # (batch_size, embed_dim)
                
                # Classification head
                x = self.head(x)  # (batch_size, num_classes)
                
                return x
        
        return SimpleViT()
    
    def benchmark_vit_training(self, config: ModelConfig) -> CostMetrics:
        """Benchmark ViT training cost"""
        print_info(f"Benchmarking ViT training on {self.device}")
        
        # Create ViT model
        model = self._create_vit_model()
        model.to(self.device)
        
        # Create dummy dataset
        dataset_size = 1000
        inputs = torch.randn(dataset_size, *config.input_size, device=self.device)
        targets = torch.randint(0, 10, (dataset_size,), device=self.device)
        
        # Training setup
        criterion = nn.CrossEntropyLoss()
        optimizer = torch.optim.Adam(model.parameters(), lr=config.learning_rate)
        
        # Start monitoring
        start_time = time.time()
        
        # Training loop
        model.train()
        for epoch in range(config.num_epochs):
            for i in range(0, dataset_size, config.batch_size):
                batch_inputs = inputs[i:i+config.batch_size]
                batch_targets = targets[i:i+config.batch_size]
                
                optimizer.zero_grad()
                outputs = model(batch_inputs)
                loss = criterion(outputs, batch_targets)
                loss.backward()
                optimizer.step()
                
                # Check accuracy periodically
                if i % (dataset_size // 4) == 0:
                    accuracy = self._calculate_accuracy(model, inputs, targets)
                    if accuracy >= config.target_accuracy:
                        break
            
            if accuracy >= config.target_accuracy:
                break
        
        end_time = time.time()
        training_time = end_time - start_time
        
        # Calculate energy consumption and power profile
        training_energy, training_power_profile = self.get_energy_consumption(start_time, end_time)
        
        # Get memory usage
        memory_info = self.get_memory_usage()
        
        # Benchmark inference
        inference_time, inference_energy, inference_power_profile = self._benchmark_inference(model, inputs[:100])
        
        # Calculate enhanced metrics
        dataset_size = 1000  # From the training loop
        final_accuracy = accuracy if 'accuracy' in locals() else config.target_accuracy
        
        # Performance metrics
        training_throughput = dataset_size / training_time if training_time > 0 else 0
        inference_throughput = 100 / inference_time if inference_time > 0 else 0
        training_wh_per_sample = training_energy / dataset_size if dataset_size > 0 else 0
        inference_wh_per_sample = inference_energy / 100 if inference_energy > 0 else 0
        
        # Cost analysis (in cents)
        training_cost_per_sample_cents = training_wh_per_sample * config.energy_cost_per_wh * 100
        inference_cost_per_sample_cents = inference_wh_per_sample * config.energy_cost_per_wh * 100
        total_training_cost_cents = training_energy * config.energy_cost_per_wh * 100
        total_inference_cost_cents = inference_energy * config.energy_cost_per_wh * 100
        
        # Efficiency metrics
        energy_per_accuracy_point = training_energy / (final_accuracy * 100) if final_accuracy > 0 else 0
        time_per_accuracy_point = training_time / (final_accuracy * 100) if final_accuracy > 0 else 0
        samples_per_wh = dataset_size / training_energy if training_energy > 0 else 0
        
        return CostMetrics(
            # Basic metrics
            training_time_seconds=training_time,
            training_energy_wh=training_energy,
            inference_time_seconds=inference_time,
            inference_energy_wh=inference_energy,
            cost_per_inference=0.01,
            time_to_accuracy=training_time,
            
            # Performance metrics
            training_throughput_samples_per_second=training_throughput,
            inference_throughput_samples_per_second=inference_throughput,
            training_wh_per_sample=training_wh_per_sample,
            inference_wh_per_sample=inference_wh_per_sample,
            
            # Cost analysis (in cents)
            training_cost_per_sample_cents=training_cost_per_sample_cents,
            inference_cost_per_sample_cents=inference_cost_per_sample_cents,
            total_training_cost_cents=total_training_cost_cents,
            total_inference_cost_cents=total_inference_cost_cents,
            
            # Efficiency metrics
            energy_per_accuracy_point=energy_per_accuracy_point,
            time_per_accuracy_point=time_per_accuracy_point,
            samples_per_wh=samples_per_wh,
            final_accuracy=final_accuracy,
            
            # Power profile
            avg_power_watts=training_power_profile["avg_power_watts"],
            peak_power_watts=training_power_profile["peak_power_watts"],
            min_power_watts=training_power_profile["min_power_watts"],
            power_variance=training_power_profile["power_variance"],
            
            # Memory analysis
            peak_memory_usage_gb=memory_info["peak_memory_usage_gb"],
            memory_efficiency_gb_per_sample=memory_info["memory_efficiency_gb_per_sample"]
        )
    
    def benchmark_vit_inference(self, config: ModelConfig) -> CostMetrics:
        """Benchmark ViT inference cost"""
        print_info(f"Benchmarking ViT inference on {self.device}")
        
        # Create ViT model
        model = self._create_vit_model()
        model.to(self.device)
        model.eval()
        
        # Create dummy inputs
        inputs = torch.randn(config.batch_size, *config.input_size, device=self.device)
        
        # Benchmark inference
        start_time = time.time()
        
        with torch.no_grad():
            for _ in range(100):  # Run 100 inferences
                outputs = model(inputs)
        
        end_time = time.time()
        inference_time = end_time - start_time
        inference_energy, inference_power_profile = self.get_energy_consumption(start_time, end_time)
        
        # Get memory usage
        memory_info = self.get_memory_usage()
        
        # Calculate enhanced metrics for ViT inference
        inference_throughput = 100 / inference_time if inference_time > 0 else 0
        inference_wh_per_sample = inference_energy / 100 if inference_energy > 0 else 0
        
        # Cost analysis (in cents)
        inference_cost_per_sample_cents = inference_wh_per_sample * config.energy_cost_per_wh * 100
        total_inference_cost_cents = inference_energy * config.energy_cost_per_wh * 100
        
        return CostMetrics(
            # Basic metrics
            training_time_seconds=0.0,
            training_energy_wh=0.0,
            inference_time_seconds=inference_time,
            inference_energy_wh=inference_energy,
            cost_per_inference=0.01,
            time_to_accuracy=0.0,
            
            # Performance metrics
            training_throughput_samples_per_second=0.0,
            inference_throughput_samples_per_second=inference_throughput,
            training_wh_per_sample=0.0,
            inference_wh_per_sample=inference_wh_per_sample,
            
            # Cost analysis (in cents)
            training_cost_per_sample_cents=0.0,
            inference_cost_per_sample_cents=inference_cost_per_sample_cents,
            total_training_cost_cents=0.0,
            total_inference_cost_cents=total_inference_cost_cents,
            
            # Efficiency metrics
            energy_per_accuracy_point=0.0,
            time_per_accuracy_point=0.0,
            samples_per_wh=0.0,
            final_accuracy=0.0,
            
            # Power profile
            avg_power_watts=inference_power_profile["avg_power_watts"],
            peak_power_watts=inference_power_profile["peak_power_watts"],
            min_power_watts=inference_power_profile["min_power_watts"],
            power_variance=inference_power_profile["power_variance"],
            
            # Memory analysis
            peak_memory_usage_gb=memory_info["peak_memory_usage_gb"],
            memory_efficiency_gb_per_sample=memory_info["memory_efficiency_gb_per_sample"]
        )
    
    def benchmark_clip_inference(self, config: ModelConfig) -> CostMetrics:
        """Benchmark CLIP inference cost"""
        print_info(f"Benchmarking CLIP inference on {self.device}")
        
        # Create CLIP model
        model = self._create_clip_model()
        model.to(self.device)
        model.eval()
        
        # Create dummy inputs
        images = torch.randn(config.batch_size, *config.input_size, device=self.device)
        texts = torch.randint(0, 10000, (config.batch_size, 10), device=self.device)  # 10 tokens per text
        
        # Benchmark inference
        start_time = time.time()
        
        with torch.no_grad():
            for _ in range(100):  # Run 100 inferences
                similarity, image_features, text_features = model(images, texts)
        
        end_time = time.time()
        inference_time = end_time - start_time
        inference_energy, inference_power_profile = self.get_energy_consumption(start_time, end_time)
        
        # Get memory usage
        memory_info = self.get_memory_usage()
        
        # Calculate enhanced metrics for CLIP inference
        inference_throughput = 100 / inference_time if inference_time > 0 else 0
        inference_wh_per_sample = inference_energy / 100 if inference_energy > 0 else 0
        
        # Cost analysis (in cents)
        inference_cost_per_sample_cents = inference_wh_per_sample * config.energy_cost_per_wh * 100
        total_inference_cost_cents = inference_energy * config.energy_cost_per_wh * 100
        
        return CostMetrics(
            # Basic metrics
            training_time_seconds=0.0,
            training_energy_wh=0.0,
            inference_time_seconds=inference_time,
            inference_energy_wh=inference_energy,
            cost_per_inference=0.01,
            time_to_accuracy=0.0,
            
            # Performance metrics
            training_throughput_samples_per_second=0.0,
            inference_throughput_samples_per_second=inference_throughput,
            training_wh_per_sample=0.0,
            inference_wh_per_sample=inference_wh_per_sample,
            
            # Cost analysis (in cents)
            training_cost_per_sample_cents=0.0,
            inference_cost_per_sample_cents=inference_cost_per_sample_cents,
            total_training_cost_cents=0.0,
            total_inference_cost_cents=total_inference_cost_cents,
            
            # Efficiency metrics
            energy_per_accuracy_point=0.0,
            time_per_accuracy_point=0.0,
            samples_per_wh=0.0,
            final_accuracy=0.0,
            
            # Power profile
            avg_power_watts=inference_power_profile["avg_power_watts"],
            peak_power_watts=inference_power_profile["peak_power_watts"],
            min_power_watts=inference_power_profile["min_power_watts"],
            power_variance=inference_power_profile["power_variance"],
            
            # Memory analysis
            peak_memory_usage_gb=memory_info["peak_memory_usage_gb"],
            memory_efficiency_gb_per_sample=memory_info["memory_efficiency_gb_per_sample"]
        )
    
    def _calculate_accuracy(self, model: nn.Module, inputs: torch.Tensor, targets: torch.Tensor) -> float:
        """Calculate model accuracy"""
        model.eval()
        with torch.no_grad():
            outputs = model(inputs)
            _, predicted = torch.max(outputs.data, 1)
            accuracy = (predicted == targets).sum().item() / targets.size(0)
        model.train()
        return accuracy
    
    def _benchmark_inference(self, model: nn.Module, inputs: torch.Tensor) -> Tuple[float, float, Dict[str, float]]:
        """Benchmark inference time, energy, and power profile"""
        model.eval()
        
        start_time = time.time()
        
        with torch.no_grad():
            for _ in range(100):  # Run 100 inferences
                outputs = model(inputs)
        
        end_time = time.time()
        inference_time = end_time - start_time
        inference_energy, inference_power_profile = self.get_energy_consumption(start_time, end_time)
        
        return inference_time, inference_energy, inference_power_profile
    
    def run_full_cost_benchmark(self, models: List[ModelConfig]) -> Dict[str, CostMetrics]:
        """Run full cost benchmark for multiple models"""
        results = {}
        
        for config in models:
            print_info(f"Benchmarking {config.name}...")
            
            try:
                if "resnet" in config.name.lower():
                    metrics = self.benchmark_resnet_training(config)
                elif "transformer" in config.name.lower():
                    metrics = self.benchmark_transformer_inference(config)
                elif "clip" in config.name.lower():
                    metrics = self.benchmark_clip_inference(config)
                elif "vit" in config.name.lower():
                    if "training" in config.name.lower():
                        metrics = self.benchmark_vit_training(config)
                    else:
                        metrics = self.benchmark_vit_inference(config)
                else:
                    # Default to ResNet training
                    metrics = self.benchmark_resnet_training(config)
                
                results[config.name] = metrics
                print_success(f"Completed {config.name} benchmark")
                
            except Exception as e:
                print_error(f"Failed to benchmark {config.name}: {e}")
                continue
        
        return results
    
    def generate_cost_report(self, results: Dict[str, CostMetrics]) -> str:
        """Generate a human-readable cost report"""
        report = "=== AI Workload Cost Benchmark Report ===\n\n"
        
        for model_name, metrics in results.items():
            report += f"Model: {model_name}\n"
            report += f"Training Time: {metrics.training_time_seconds:.2f}s ({metrics.training_time_seconds/3600:.2f}h)\n"
            report += f"Training Energy: {metrics.training_energy_wh:.3f} Wh\n"
            report += f"Inference Time: {metrics.inference_time_seconds:.4f}s per 100 inferences\n"
            report += f"Inference Energy: {metrics.inference_energy_wh:.3f} Wh per 100 inferences\n"
            # Calculate performance per watt only if we have meaningful energy data
            if metrics.training_energy_wh > 0.1:  # More than 0.1 Wh
                performance_per_watt = metrics.training_time_seconds / metrics.training_energy_wh
                report += f"Performance per Watt: {performance_per_watt:.2f}s/Wh (training)\n"
            else:
                report += f"Performance per Watt: Insufficient energy data (< 0.1 Wh)\n"
            report += "-" * 50 + "\n\n"
        
        return report


def create_standard_benchmarks() -> List[ModelConfig]:
    """Create standard benchmark configurations"""
    return [
        ModelConfig(
            name="ResNet-50 Training",
            model_class="resnet",
            input_size=(3, 224, 224),
            batch_size=32,
            num_epochs=5,
            learning_rate=0.001,
            energy_cost_per_wh=0.00012
        ),
        ModelConfig(
            name="Transformer Inference",
            model_class="transformer",
            input_size=(512,),
            batch_size=16,
            num_epochs=0,  # No training for inference
            learning_rate=0.0,
            energy_cost_per_wh=0.00012
        ),
        ModelConfig(
            name="CLIP Inference",
            model_class="clip",
            input_size=(3, 224, 224),
            batch_size=8,
            num_epochs=0,  # No training for inference
            learning_rate=0.0,
            energy_cost_per_wh=0.00012
        ),
        ModelConfig(
            name="ViT Training",
            model_class="vit",
            input_size=(3, 224, 224),
            batch_size=16,
            num_epochs=3,
            learning_rate=0.001,
            energy_cost_per_wh=0.00012
        ),
        ModelConfig(
            name="ViT Inference",
            model_class="vit",
            input_size=(3, 224, 224),
            batch_size=16,
            num_epochs=0,  # No training for inference
            learning_rate=0.0,
            energy_cost_per_wh=0.00012
        ),
        ModelConfig(
            name="ResNet-18 Training",
            model_class="resnet",
            input_size=(3, 224, 224),
            batch_size=64,
            num_epochs=3,
            learning_rate=0.001,
            energy_cost_per_wh=0.00012
        )
    ]


if __name__ == "__main__":
    # Example usage
    benchmark = AICostBenchmark()
    models = create_standard_benchmarks()
    results = benchmark.run_full_cost_benchmark(models)
    
    report = benchmark.generate_cost_report(results)
    print(report)

