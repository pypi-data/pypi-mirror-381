"""Flask Web Adapter.

This adapter provides the same web interface as the original Flask app
while using the new domain-driven architecture underneath.
"""

import logging
from typing import Dict, Any, Optional, List
from flask import Flask, render_template, jsonify, request

from ...application.di.providers import create_container
from ...application.use_cases.run_benchmark import RunBenchmarkUseCase
from ...application.use_cases.assess_gpu_health import AssessGPUHealthUseCase


class FlaskWebAdapter:
    """Adapter that provides the same web interface using the new architecture.
    
    This class maintains compatibility with the existing Flask web interface
    while using the new domain-driven architecture for all operations.
    """
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """Initialize the Flask web adapter.
        
        Args:
            logger: Logger for web operations.
        """
        self._logger = logger or logging.getLogger(__name__)
        self._container = create_container(logger=self._logger)
        self._benchmark_use_case = self._container.resolve(RunBenchmarkUseCase)
        self._health_use_case = self._container.resolve(AssessGPUHealthUseCase)
        self._gpu_repository = self._container.resolve("GPURepository")
    
    def get_system_info(self) -> Dict[str, Any]:
        """Get system information - same interface as original."""
        import platform
        import psutil
        
        return {
            "platform": platform.system(),
            "platform_version": platform.version(),
            "architecture": platform.machine(),
            "processor": platform.processor(),
            "python_version": platform.python_version(),
            "memory_gb": psutil.virtual_memory().total / (1024**3),
            "cpu_cores": psutil.cpu_count()
        }
    
    def get_gpu_info(self) -> Dict[str, Any]:
        """Get GPU information - same interface as original."""
        try:
            devices = self._gpu_repository.get_available_devices()
            
            gpu_info = {
                "detected": len(devices) > 0,
                "gpus": [],
                "backend": "new_architecture",
                "error": None
            }
            
            for device in devices:
                gpu_data = {
                    "name": device.info.name,
                    "memory_gb": device.info.memory_total_mb / 1024,
                    "driver_version": device.info.driver_version or "Unknown",
                    "cuda_version": device.info.cuda_version or "Unknown",
                    "type": device.info.gpu_type.value.upper(),
                    "device_id": device.info.device_id,
                    "is_mock": device.info.is_mock,
                    "status": device.status.value
                }
                gpu_info["gpus"].append(gpu_data)
            
            return gpu_info
            
        except Exception as e:
            self._logger.error(f"Failed to get GPU info: {e}")
            return {
                "detected": False,
                "gpus": [],
                "backend": "error",
                "error": str(e)
            }
    
    def run_benchmark(self, device_id: int = 0, duration: int = 60) -> Dict[str, Any]:
        """Run a benchmark - new web interface method."""
        try:
            result = self._benchmark_use_case.execute_quick_benchmark(device_id)
            
            return {
                "success": result.is_successful(),
                "gpu_info": {
                    "name": result.gpu_device.info.name,
                    "device_id": result.gpu_device.info.device_id,
                    "gpu_type": result.gpu_device.info.gpu_type.value,
                    "memory_total_mb": result.gpu_device.info.memory_total_mb,
                    "driver_version": result.gpu_device.info.driver_version or "Unknown"
                },
                "health_score": {
                    "score": result.health_score.score,
                    "status": result.health_score.status.value,
                    "recommendation": result.health_score.recommendation
                },
                "duration_seconds": result.metadata.duration_seconds,
                "timestamp": result.metadata.timestamp.isoformat(),
                "warnings": result.warnings,
                "errors": result.errors
            }
            
        except Exception as e:
            self._logger.error(f"Benchmark failed: {e}")
            return {
                "success": False,
                "error": str(e),
                "gpu_info": {},
                "health_score": {}
            }
    
    def assess_health(self, device_id: int = 0) -> Dict[str, Any]:
        """Assess GPU health - new web interface method."""
        try:
            health_score = self._health_use_case.execute(device_id)
            
            return {
                "score": health_score.score,
                "status": health_score.status.value,
                "recommendation": health_score.recommendation,
                "breakdown": health_score.breakdown.to_dict(),
                "specific_recommendations": health_score.specific_recommendations
            }
            
        except Exception as e:
            self._logger.error(f"Health assessment failed: {e}")
            return {
                "score": 0,
                "status": "unknown",
                "recommendation": f"Health assessment failed: {e}",
                "breakdown": {},
                "specific_recommendations": []
            }
    
    def get_benchmark_history(self, device_id: int = 0, limit: int = 10) -> List[Dict[str, Any]]:
        """Get benchmark history - new web interface method."""
        try:
            results = self._benchmark_use_case.get_benchmark_history(device_id, limit)
            
            return [
                {
                    "benchmark_id": result.metadata.benchmark_id,
                    "timestamp": result.metadata.timestamp.isoformat(),
                    "duration_seconds": result.metadata.duration_seconds,
                    "health_score": result.health_score.score,
                    "status": result.health_score.status.value,
                    "success": result.is_successful()
                }
                for result in results
            ]
            
        except Exception as e:
            self._logger.error(f"Failed to get benchmark history: {e}")
            return []
    
    def get_device_capabilities(self, device_id: int = 0) -> Dict[str, Any]:
        """Get device capabilities - new web interface method."""
        try:
            capabilities = self._gpu_repository.get_device_capabilities(device_id)
            return capabilities
            
        except Exception as e:
            self._logger.error(f"Failed to get device capabilities: {e}")
            return {
                "error": str(e),
                "device_id": device_id
            }
    
    def create_flask_app(self) -> Flask:
        """Create a Flask app with the new architecture.
        
        Returns:
            Flask: Configured Flask application.
        """
        app = Flask(__name__)
        
        @app.route('/')
        def index():
            """Main page - same interface as original."""
            return render_template('index.html')
        
        @app.route('/api/detect')
        def detect_gpu():
            """API endpoint to detect GPU - same interface as original."""
            try:
                system_info = self.get_system_info()
                gpu_info = self.get_gpu_info()
                
                return jsonify({
                    "system": system_info,
                    "gpu": gpu_info
                })
            except Exception as e:
                self._logger.error(f"GPU detection failed: {e}")
                return jsonify({
                    "error": str(e),
                    "system": self.get_system_info(),
                    "gpu": {
                        "detected": False,
                        "gpus": [],
                        "backend": "error",
                        "error": str(e)
                    }
                }), 500
        
        @app.route('/api/health')
        def health():
            """Health check endpoint - same interface as original."""
            return jsonify({"status": "healthy"})
        
        # New API endpoints using the new architecture
        @app.route('/api/benchmark', methods=['POST'])
        def run_benchmark_api():
            """Run a benchmark via API."""
            try:
                data = request.get_json() or {}
                device_id = data.get('device_id', 0)
                duration = data.get('duration', 60)
                
                result = self.run_benchmark(device_id, duration)
                return jsonify(result)
                
            except Exception as e:
                self._logger.error(f"Benchmark API failed: {e}")
                return jsonify({"error": str(e)}), 500
        
        @app.route('/api/health/<int:device_id>')
        def assess_health_api(device_id):
            """Assess GPU health via API."""
            try:
                result = self.assess_health(device_id)
                return jsonify(result)
                
            except Exception as e:
                self._logger.error(f"Health assessment API failed: {e}")
                return jsonify({"error": str(e)}), 500
        
        @app.route('/api/history/<int:device_id>')
        def get_history_api(device_id):
            """Get benchmark history via API."""
            try:
                limit = request.args.get('limit', 10, type=int)
                results = self.get_benchmark_history(device_id, limit)
                return jsonify({"history": results})
                
            except Exception as e:
                self._logger.error(f"History API failed: {e}")
                return jsonify({"error": str(e)}), 500
        
        @app.route('/api/capabilities/<int:device_id>')
        def get_capabilities_api(device_id):
            """Get device capabilities via API."""
            try:
                capabilities = self.get_device_capabilities(device_id)
                return jsonify(capabilities)
                
            except Exception as e:
                self._logger.error(f"Capabilities API failed: {e}")
                return jsonify({"error": str(e)}), 500
        
        return app
