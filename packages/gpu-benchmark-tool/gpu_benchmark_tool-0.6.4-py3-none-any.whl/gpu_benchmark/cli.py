#!/usr/bin/env python3
"""Command Line Interface for GPU Benchmark Tool.

This module provides the command-line interface for running GPU benchmarks, diagnostics, and monitoring.
"""

import argparse
import json
import sys
import platform
from datetime import datetime, timezone

# Import from new architecture while maintaining same interface
from .infrastructure.cli.legacy_cli_wrapper import (
    run_full_benchmark,
    run_quick_benchmark,
    run_comprehensive_benchmark,
    assess_gpu_health,
    get_gpu_info,
    get_available_devices,
    get_benchmark_history,
    compare_benchmarks,
    run_multi_gpu_benchmark,
    export_results,
    print_system_info,
    print_enhanced_monitoring_status,
    print_comprehensive_diagnostics
)
from .backends import list_available_backends
from .utils import print_success, print_warning, print_error, print_info

from . import __version__

try:
    import pynvml
    PYNVML_AVAILABLE = True
except ImportError:
    PYNVML_AVAILABLE = False


def print_banner():
    """Prints the tool banner with version information."""
    print("=" * 60)
    print(f"GPU Benchmark Tool v{__version__}")
    print("=" * 60)


def print_gpu_info(info, mock_mode=False):
    """Pretty prints GPU information.

    Args:
        info (dict): Dictionary containing GPU information to display.
        mock_mode (bool): Whether we're in mock mode (affects the indicators).
    """
    print("\nGPU Information:")
    print("-" * 30)
    for key, value in info.items():
        # Add indicator for mock mode only
        if mock_mode:
            indicator = "🔴 SIMULATED" if "Mock" in str(value) else "🟢 REAL"
            print(f"{key:.<25} {value} {indicator}")
        else:
            print(f"{key:.<25} {value}")


def print_health_score(health, mock_mode=False):
    """Pretty prints the health score with color coding.

    Args:
        health (dict): Health assessment dictionary with score, status, recommendation, and details.
        mock_mode (bool): Whether we're in mock mode (affects the indicator).
    """
    score = health["score"]
    status = health["status"]
    
    # Use our color utility functions
    from .utils import print_success, print_warning, print_error, print_info
    
    print("\nHealth Assessment:")
    print("-" * 30)
    
    # Health scoring is simulated in mock mode, real otherwise
    mock_indicator = "🔴 SIMULATED" if mock_mode else ""
    
    # Color-code the score based on status
    if status in ["healthy", "good"]:
        print_success(f"Score: {score}/100", bold=True)
        print_success(f"Status: {status.upper()}", bold=True)
    elif status in ["degraded", "warning"]:
        print_warning(f"Score: {score}/100", bold=True)
        print_warning(f"Status: {status.upper()}", bold=True)
    elif status == "critical":
        print_error(f"Score: {score}/100", bold=True)
        print_error(f"Status: {status.upper()}", bold=True)
    else:
        print_info(f"Score: {score}/100", bold=True)
        print_info(f"Status: {status.upper()}", bold=True)
    
    print(f"Recommendation: {health['recommendation']}{' ' + mock_indicator if mock_mode else ''}")
    
    if "details" in health and "breakdown" in health["details"]:
        print("\nScore Breakdown:")
        for component, points in health["details"]["breakdown"].items():
            print(f"  {component:.<25} {points} points")
    
    if "details" in health and "specific_recommendations" in health["details"]:
        recs = health["details"]["specific_recommendations"]
        if recs:
            print("\nSpecific Recommendations:")
            for rec in recs:
                print(f"  • {rec}")


def print_test_results(results, mock_mode=False):
    """Pretty prints stress test results.

    Args:
        results (dict): Dictionary containing results from various stress tests.
        mock_mode (bool): Whether we're in mock mode (affects the indicators).
    """
    if "matrix_multiply" in results:
        print("\nMatrix Multiplication Test:")
        mm = results["matrix_multiply"]
        indicator = " 🟢 REAL" if mock_mode else ""
        print(f"  Performance: {mm['tflops']:.2f} TFLOPS{indicator}")
        print(f"  Iterations: {mm['iterations']}{indicator}")
    
    if "memory_bandwidth" in results:
        print("\nMemory Bandwidth Test:")
        mb = results["memory_bandwidth"]
        indicator = " 🟢 REAL" if mock_mode else ""
        print(f"  Bandwidth: {mb['bandwidth_gbps']:.2f} GB/s{indicator}")
    
    if "mixed_precision" in results:
        print("\nMixed Precision Support:")
        mp = results["mixed_precision"]
        
        # FP32 is always real
        if mp.get("fp32", {}).get("supported"):
            tflops = mp["fp32"].get("tflops", 0)
            indicator = " 🟢 REAL" if mock_mode else ""
            print(f"  FP32: Baseline ({tflops:.2f} TFLOPS){indicator}")
        else:
            indicator = " 🟢 REAL" if mock_mode else ""
            print(f"  FP32: Not available{indicator}")
        
        # FP16 - check hardware and runtime support
        fp16 = mp.get("fp16", {})
        hw_supported = fp16.get("hardware_supported", False)
        rt_supported = fp16.get("runtime_supported", False)
        
        if hw_supported and rt_supported:
            tflops = fp16.get("tflops", 0)
            speedup = mp.get("fp16_speedup", 0)
            indicator = " 🟡 HARDWARE-DEPENDENT" if mock_mode else ""
            print(f"  FP16: Hardware ✅ Runtime ✅ ({speedup:.2f}x speedup, {tflops:.2f} TFLOPS){indicator}")
        elif hw_supported and not rt_supported:
            error = fp16.get("error", "Runtime failed")
            indicator = " 🟡 HARDWARE-DEPENDENT" if mock_mode else ""
            print(f"  FP16: Hardware ✅ Runtime ❌ ({error}){indicator}")
        else:
            indicator = " 🟡 HARDWARE-DEPENDENT" if mock_mode else ""
            print(f"  FP16: Hardware ❌ Runtime ❌ (Not supported){indicator}")
        
        # BF16 - check hardware and runtime support
        bf16 = mp.get("bf16", {})
        hw_supported = bf16.get("hardware_supported", False)
        rt_supported = bf16.get("runtime_supported", False)
        
        if hw_supported and rt_supported:
            tflops = bf16.get("tflops", 0)
            speedup = mp.get("bf16_speedup", 0)
            indicator = " 🟡 HARDWARE-DEPENDENT" if mock_mode else ""
            print(f"  BF16: Hardware ✅ Runtime ✅ ({speedup:.2f}x speedup, {tflops:.2f} TFLOPS){indicator}")
        elif hw_supported and not rt_supported:
            error = bf16.get("error", "Runtime failed")
            indicator = " 🟡 HARDWARE-DEPENDENT" if mock_mode else ""
            print(f"  BF16: Hardware ✅ Runtime ❌ ({error}){indicator}")
        else:
            indicator = " 🟡 HARDWARE-DEPENDENT" if mock_mode else ""
            print(f"  BF16: Hardware ❌ Runtime ❌ (Not supported){indicator}")
        
        # INT8 - check hardware and runtime support
        int8 = mp.get("int8", {})
        hw_supported = int8.get("hardware_supported", False)
        rt_supported = int8.get("runtime_supported", False)
        method = int8.get("method", "unknown")
        
        if hw_supported and rt_supported:
            tflops = int8.get("tflops", 0)
            speedup = mp.get("int8_speedup", 0)
            note = int8.get("note", "")
            indicator = " 🟡 HARDWARE-DEPENDENT" if mock_mode else ""
            print(f"  INT8: Hardware ✅ Runtime ✅ ({speedup:.2f}x speedup, {tflops:.2f} TFLOPS via {method}){indicator}")
            if note and mock_mode:
                print(f"           📝 Note: {note}")
        elif hw_supported and not rt_supported:
            error = int8.get("error", "Runtime failed")
            solution = int8.get("solution", "")
            note = int8.get("note", "")
            indicator = " 🟡 HARDWARE-DEPENDENT" if mock_mode else ""
            print(f"  INT8: Hardware ✅ Runtime ❌ ({error}){indicator}")
            if note and mock_mode:
                print(f"           📝 Note: {note}")
            if solution and mock_mode:
                print(f"           💡 Solution: {solution}")
        else:
            indicator = " 🟡 HARDWARE-DEPENDENT" if mock_mode else ""
            print(f"  INT8: Hardware ❌ Runtime ❌ (Not supported){indicator}")


def run_mock_benchmark(args):
    """Runs the benchmark in mock mode (simulated GPU).

    Args:
        args (argparse.Namespace): Parsed command-line arguments.

    Returns:
        int: Exit code (0 for success, 1 for error).
    """
    print("\nRunning in mock mode (simulated GPU)...")
    print("=" * 60)
    print("🔴 SIMULATED: GPU monitoring, health scoring")
    print("🟢 REAL: Computational performance, memory bandwidth")
    print("🟡 HARDWARE-DEPENDENT: Mixed precision (FP32=real, FP16/BF16/INT8=hardware-dependent)")
    print("=" * 60)
    print("Running simulated stress tests...")
    print("(This will take about {} seconds)".format(args.duration))

    try:
        # Use new architecture with mock backend
        # The GPUBackendAdapter will automatically create a mock device if no real GPU is found
        result = run_full_benchmark(
            device_id=0,
            duration=args.duration,
            include_ai=not args.basic,
            export_format="json",
            export_path=None
        )

        # Check if benchmark was successful
        if not result.get("success", False):
            error_msg = result.get("error", "Unknown error")
            print_error(f"Mock benchmark failed: {error_msg}")
            return 1

        # Print results
        gpu_info = result.get("gpu_info", {})
        if gpu_info:
            print_gpu_info(gpu_info, mock_mode=True)

        health_score = result.get("health_score", {})
        if health_score and "score" in health_score:
            print_health_score(health_score, mock_mode=True)

        if not args.basic and "performance_metrics" in result:
            print_test_results(result["performance_metrics"], mock_mode=True)

        # Export if requested
        if args.export is not None:
            if args.export == '':
                # Auto-generate filename
                filename = export_results(result)
            else:
                # Use provided filename
                filename = export_results(result, args.export)
            print(f"\nResults exported to {filename}")

        return 0

    except Exception as e:
        print_error(f"Mock benchmark failed: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


def cmd_benchmark(args):
    """Runs the benchmark command.

    Args:
        args (argparse.Namespace): Parsed command-line arguments.

    Returns:
        int: Exit code (0 for success, 1 for error).
    """
    
    # Handle mock mode separately
    if args.mock:
        return run_mock_benchmark(args)
    
    # Real GPU benchmark
    if not PYNVML_AVAILABLE:
        print("Error: pynvml is required for GPU benchmarking")
        print("Install with: pip install nvidia-ml-py torch")
        print("Or use --mock flag for simulation mode")
        return 1
    
    # Check for enhanced monitoring requirements
    if args.enhanced:
        try:
            import torch
            if not torch.cuda.is_available():
                print("Warning: Enhanced monitoring requires CUDA support")
                print("Install PyTorch with CUDA: pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118")
                print("Continuing with basic monitoring...")
                args.enhanced = False
        except ImportError:
            print("Warning: PyTorch not available for enhanced monitoring")
            print("Install with: pip install torch")
            print("Continuing with basic monitoring...")
            args.enhanced = False
    
    try:
        pynvml.nvmlInit()
    except pynvml.NVMLError as e:
        print_error(f"Error initializing NVML: {e}")
        
        # Platform-specific guidance
        if platform.system() == "Darwin":
            print_error("NVIDIA GPU support is not available on macOS")
            print_info("Use --mock flag for simulation mode")
            print_info("For real GPU testing, consider using Linux or Windows")
        else:
            print_error("Make sure NVIDIA drivers are installed and nvidia-smi works")
            print_info("Or use --mock flag for simulation mode")
        
        return 1
    
    # All imports now from new architecture via legacy_cli_wrapper
    from .backends import list_available_backends
    
    # Single GPU benchmark
    if args.gpu_id is not None:
        device_count = pynvml.nvmlDeviceGetCount()
        if args.gpu_id >= device_count:
            print_error(f"Error: GPU {args.gpu_id} not found. Found {device_count} GPU(s)")
            return 1
        
        print(f"\nBenchmarking GPU {args.gpu_id}...")
        handle = pynvml.nvmlDeviceGetHandleByIndex(args.gpu_id)

        # Temperature thresholds are now monitored by the new architecture
        # Verbose output is included in diagnostics command
        
        # Run benchmark using new architecture
        enhanced_mode = args.enhanced or (not args.basic)
        result = run_full_benchmark(
            device_id=args.gpu_id,
            duration=args.duration,
            include_ai=enhanced_mode
        )
        
        # Print results
        print_gpu_info(result["gpu_info"], mock_mode=False)
        print_health_score(result["health_score"], mock_mode=False)
        
        if not args.basic and "performance_metrics" in result:
            print_test_results(result["performance_metrics"], mock_mode=False)
        
        # Export if requested
        if args.export is not None:
            if args.export == '':
                # Auto-generate filename
                filename = export_results(result)
            else:
                # Use provided filename
                filename = export_results(result, args.export)
            print(f"\nResults exported to: {filename}")
    
    # Multi-GPU benchmark
    else:
        print("\nBenchmarking all GPUs...")
        enhanced_mode = args.enhanced or (not args.basic)
        # Use new architecture for multi-GPU
        results = run_multi_gpu_benchmark(
            duration=args.duration,
            enhanced=enhanced_mode,
            export_results=False
        )
        
        if "error" in results:
            print_error(f"Error: {results['error']}")
            return 1
            
        print(f"\nFound {results['device_count']} GPU(s)")
        
        for gpu_id, result in results["results"].items():
            print(f"\n{'='*60}")
            print(f"GPU {gpu_id}")
            print('='*60)
            
            if "error" in result:
                print(f"Error: {result['error']}")
                continue
            
            print_gpu_info(result["gpu_info"], mock_mode=False)
            print_health_score(result["health_score"], mock_mode=False)
            
            if not args.basic and "performance_tests" in result:
                print_test_results(result["performance_tests"], mock_mode=False)
        
        # Print summary
        summary = results["summary"]
        print(f"\n{'='*60}")
        print("SUMMARY")
        print('='*60)
        print(f"Total GPUs: {summary['total_gpus']}")
        print(f"Healthy GPUs: {summary['healthy_gpus']} ({summary['health_percentage']:.1f}%)")
        
        if summary["warnings"]:
            print("\nWarnings:")
            for warning in summary["warnings"]:
                print(f"  • {warning}")
        
        # Export if requested
        if args.export is not None:
            if args.export == '':
                # Auto-generate filename
                filename = export_results(results)
            else:
                # Use provided filename
                filename = export_results(results, args.export)
            print(f"\nResults exported to: {filename}")
    
    return 0


def cmd_list(args):
    """Lists available GPUs and backends."""
    from .backends import list_available_backends
    backends = list_available_backends()
    if not backends:
        print("No supported GPU backends found!")
        print("\nOptions:")
        print("  1. Install NVIDIA support: pip install gpu-benchmark-tool[nvidia]")
        print("  2. Use mock mode: gpu-benchmark benchmark --mock")
        return 1
    for backend in backends:
        print(f"\n{backend['type'].upper()} Backend:")
        print(f"  Devices: {backend['device_count']}")
    
    # Use new architecture to get device information
    try:
        devices = get_available_devices()
        if devices:
            print("\nAvailable GPUs:")
            for device in devices:
                print(f"  [{device['device_id']}] {device['name']} ({device['memory_total_mb'] / 1024:.1f} GB)")
                if device['is_mock']:
                    print("    🔴 Mock GPU (simulation mode)")
                else:
                    print("    🟢 Real GPU")
        else:
            print("\nNo GPUs detected")
    except Exception as e:
        print(f"\nError getting device information: {e}")
        # Fallback to old method
        if PYNVML_AVAILABLE:
            try:
                pynvml.nvmlInit()
                count = pynvml.nvmlDeviceGetCount()
                print("\nNVIDIA GPUs (fallback):")
                for i in range(count):
                    handle = pynvml.nvmlDeviceGetHandleByIndex(i)
                    name = pynvml.nvmlDeviceGetName(handle)
                    if isinstance(name, bytes):
                        name = name.decode('utf-8')
                    mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
                    print(f"  [{i}] {name} ({mem_info.total / 1e9:.1f} GB)")
            except pynvml.NVMLError:
                pass
    return 0


def cmd_ai_cost_benchmark(args):
    """Run AI workload cost benchmark.

    Args:
        args: Parsed command line arguments.

    Returns:
        int: Exit code (0 for success, 1 for error).
    """
    try:
        # Import from legacy for now - AI cost benchmark uses legacy implementation
        from .ai_cost_benchmark import AICostBenchmark, create_standard_benchmarks

        print_info("🚀 Starting AI Workload Cost Benchmark...")
        print_info(f"Target GPU: {args.gpu_id}")
        print_info(f"Models to benchmark: {', '.join(args.models)}")

        # Create benchmark instance
        benchmark = AICostBenchmark(device_id=args.gpu_id)
        
        # Create model configurations based on user selection
        all_models = create_standard_benchmarks()
        selected_models = []
        
        for model_name in args.models:
            if model_name.lower() == 'resnet':
                selected_models.extend([m for m in all_models if 'resnet' in m.name.lower()])
            elif model_name.lower() == 'transformer':
                selected_models.extend([m for m in all_models if 'transformer' in m.name.lower()])
            elif model_name.lower() == 'clip':
                selected_models.extend([m for m in all_models if 'clip' in m.name.lower()])
            elif model_name.lower() == 'vit':
                selected_models.extend([m for m in all_models if 'vit' in m.name.lower()])
        
        if not selected_models:
            print_error("No valid models selected. Available: resnet, transformer, clip, vit")
            return 1
        
        print_info(f"Running benchmarks for {len(selected_models)} model(s)...")
        
        # Show workload summary
        print_info("📋 Workload Summary:")
        for model in selected_models:
            if model.num_epochs > 0:
                workload_type = f"Training + Inference ({model.num_epochs} epochs)"
            else:
                workload_type = "Inference Only"
            print_info(f"  • {model.name}: {workload_type}")
        
        print_info("")  # Empty line for readability
        
        # Run benchmarks
        results = benchmark.run_full_cost_benchmark(selected_models)
        
        if not results:
            print_error("No benchmarks completed successfully")
            return 1
        
        # Generate and display report
        report = benchmark.generate_cost_report(results)
        print("\n" + report)
        
        # Export results if requested
        if args.export is not None:
            filename = args.export if args.export else f"ai_cost_benchmark_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
            # Get hardware info and metadata
            hardware_info = benchmark.get_hardware_info()
            benchmark_metadata = benchmark.get_benchmark_metadata()
            comparative_analysis = benchmark.generate_comparative_analysis(results)
            
            # Calculate total benchmark duration
            total_time = sum(metrics.training_time_seconds + metrics.inference_time_seconds for metrics in results.values())
            benchmark_metadata["total_benchmark_duration_seconds"] = str(total_time)
            
            export_data = {
                "benchmark_metadata": benchmark_metadata,
                "hardware_info": hardware_info,
                "model_results": {},
                "comparative_analysis": comparative_analysis
            }
            
            for model_name, metrics in results.items():
                export_data["model_results"][model_name] = {
                    # Basic metrics
                    "training_time_seconds": metrics.training_time_seconds,
                    "training_energy_wh": metrics.training_energy_wh,
                    "inference_time_seconds": metrics.inference_time_seconds,
                    "inference_energy_wh": metrics.inference_energy_wh,
                    "time_to_accuracy": metrics.time_to_accuracy,
                    "performance_per_watt": metrics.training_time_seconds/metrics.training_energy_wh if metrics.training_energy_wh > 0 else 0,
                    
                    # Performance metrics
                    "training_throughput_samples_per_second": metrics.training_throughput_samples_per_second,
                    "inference_throughput_samples_per_second": metrics.inference_throughput_samples_per_second,
                    "training_wh_per_sample": metrics.training_wh_per_sample,
                    "inference_wh_per_sample": metrics.inference_wh_per_sample,
                    
                    # Cost analysis (in cents)
                    "training_cost_per_sample_cents": metrics.training_cost_per_sample_cents,
                    "inference_cost_per_sample_cents": metrics.inference_cost_per_sample_cents,
                    "total_training_cost_cents": metrics.total_training_cost_cents,
                    "total_inference_cost_cents": metrics.total_inference_cost_cents,
                    
                    # Efficiency metrics
                    "energy_per_accuracy_point": metrics.energy_per_accuracy_point,
                    "time_per_accuracy_point": metrics.time_per_accuracy_point,
                    "samples_per_wh": metrics.samples_per_wh,
                    "final_accuracy": metrics.final_accuracy,
                    
                    # Power profile
                    "avg_power_watts": metrics.avg_power_watts,
                    "peak_power_watts": metrics.peak_power_watts,
                    "min_power_watts": metrics.min_power_watts,
                    "power_variance": metrics.power_variance,
                    
                    # Memory analysis
                    "peak_memory_usage_gb": metrics.peak_memory_usage_gb,
                    "memory_efficiency_gb_per_sample": metrics.memory_efficiency_gb_per_sample
                }
            
            with open(filename, 'w') as f:
                json.dump(export_data, f, indent=2)
            
            print_success(f"Enhanced results exported to: {filename}")
        
        # Summary
        total_time = sum(metrics.training_time_seconds + metrics.inference_time_seconds for metrics in results.values())
        total_energy = sum(metrics.training_energy_wh + metrics.inference_energy_wh for metrics in results.values())
        print_info(f"\n⏱️ Total Time Across All Models: {total_time:.2f}s ({total_time/60:.2f} minutes)")
        print_info(f"⚡ Total Energy Across All Models: {total_energy:.3f} Wh")
        print_info("✅ AI Performance & Energy Benchmark completed successfully!")
        
        return 0
        
    except Exception as e:
        print_error(f"AI Cost Benchmark failed: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


def cmd_monitor(args):
    """Real-time monitoring (basic version).

    Args:
        args (argparse.Namespace): Parsed command-line arguments.

    Returns:
        int: Exit code (0 for success, 1 for error).
    """
    import time
    
    try:
        # Use new architecture to get device information
        device_id = args.gpu_id or 0
        gpu_info = get_gpu_info(device_id)
        
        if gpu_info['is_mock']:
            print("Mock monitoring mode - showing simulated data")
        else:
            print(f"Monitoring GPU {device_id} (Press Ctrl+C to stop)...")
        
        print("-" * 60)
        
        while True:
            # Get current GPU info using new architecture
            current_info = get_gpu_info(device_id)
            
            # For now, we'll show static info since we don't have real-time monitoring yet
            # In a full implementation, we'd refresh metrics here
            print(f"\rGPU: {current_info['name']} | "
                  f"Type: {current_info['gpu_type']} | "
                  f"Memory: {current_info['memory_used_mb']}/{current_info['memory_total_mb']} MB", 
                  end='', flush=True)
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n\nMonitoring stopped.")
    except Exception as e:
        print(f"\nError: {e}")
        return 1
    
    return 0


def main():
    """Main CLI entry point.

    Returns:
        int: Exit code (0 for success, 1 for error).
    """
    parser = argparse.ArgumentParser(
        description="GPU Benchmark Tool - Comprehensive GPU health monitoring and optimization"
    )
    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Benchmark command
    bench_parser = subparsers.add_parser('benchmark', help='Run GPU benchmark')
    bench_parser.add_argument(
        '--gpu-id', '-g', type=int, 
        help='Specific GPU to benchmark (default: all GPUs)'
    )
    bench_parser.add_argument(
        '--duration', '-d', type=int, default=60,
        help='Test duration in seconds (default: 60)'
    )
    bench_parser.add_argument(
        '--basic', '-b', action='store_true',
        help='Run basic tests only (faster)'
    )
    bench_parser.add_argument(
        '--enhanced', '-E', action='store_true',
        help='Force enhanced monitoring (comprehensive stress tests)'
    )
    bench_parser.add_argument(
        '--export', '-e', type=str, nargs='?', const='',
        help='Export results to JSON file (auto-generates filename if not provided)'
    )
    bench_parser.add_argument(
        '--verbose', '-v', action='store_true',
        help='Verbose output'
    )
    bench_parser.add_argument(
        '--mock', '-m', action='store_true',
        help='Use mock GPU (for testing/development)'
    )
    bench_parser.set_defaults(func=cmd_benchmark)
    
    # List command
    list_parser = subparsers.add_parser('list', help='List available GPUs')
    list_parser.set_defaults(func=cmd_list)
    
    # Monitor command
    monitor_parser = subparsers.add_parser('monitor', help='Real-time GPU monitoring')
    monitor_parser.add_argument(
        '--gpu-id', '-g', type=int,
        help='GPU to monitor (default: 0)'
    )
    monitor_parser.add_argument(
        '--mock', '-m', action='store_true',
        help='Use mock GPU (for testing/development)'
    )
    monitor_parser.set_defaults(func=cmd_monitor)
    
    # System info command
    sysinfo_parser = subparsers.add_parser('system-info', help='Show baseline system information')
    sysinfo_parser.set_defaults(func=lambda args: print_system_info() or 0)
    
    # Enhanced monitoring status command
    enhanced_parser = subparsers.add_parser('enhanced-status', help='Check enhanced monitoring requirements')
    enhanced_parser.set_defaults(func=lambda args: print_enhanced_monitoring_status() or 0)
    
    # Comprehensive diagnostics command
    comprehensive_parser = subparsers.add_parser('diagnostics', help='Comprehensive GPU diagnostics and version check')
    comprehensive_parser.set_defaults(func=lambda args: print_comprehensive_diagnostics() or 0)
    
    # AI Cost Benchmark command
    ai_cost_parser = subparsers.add_parser('ai-cost', help='Benchmark AI workload costs (training/inference time + energy)')
    ai_cost_parser.add_argument(
        '--gpu-id', '-g', type=int, default=0,
        help='GPU to benchmark (default: 0)'
    )
    ai_cost_parser.add_argument(
        '--models', '-m', type=str, nargs='+',
        default=['resnet', 'transformer'],
        help='Models to benchmark: resnet, transformer (default: both)'
    )
    ai_cost_parser.add_argument(
        '--export', '-e', type=str, nargs='?', const='',
        help='Export results to JSON file (auto-generates filename if not provided)'
    )
    ai_cost_parser.add_argument(
        '--verbose', '-v', action='store_true',
        help='Verbose output'
    )
    ai_cost_parser.set_defaults(func=cmd_ai_cost_benchmark)
    
    # Parse arguments
    args = parser.parse_args()
    
    # Print banner and system info at the start
    print_banner()
    print_system_info()
    
    # Add note about system info being real
    print("\n📊 System Information: All data is REAL (hardware detection)")
    
    # Execute command
    if args.command is None:
        parser.print_help()
        return 0
    
    # For system-info, just print and exit
    if args.command == 'system-info':
        return 0
    
    return args.func(args)


if __name__ == '__main__':
    sys.exit(main())
