#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Maniq - Manim Quality Stress Testing Tool

Supports quality levels:
- low (-ql): 480p
- medium (-qm): 720p  
- high (-qh): 1080p
- 2k (-qp): 1440p
- 4k (-qk): 2160p
"""

# Import dataclass first
from dataclasses import dataclass, asdict

import os
import sys
import subprocess
import time
import psutil
import threading
import argparse
from pathlib import Path
from datetime import datetime
import logging
from typing import List, Dict, Tuple, Optional
import json
import statistics
import traceback
import re

# Configure detailed logging
def setup_logging(log_file: str = 'manim_quality_stress_test.log'):
    """Setup detailed logging configuration"""
    log_path = Path(log_file)
    log_path.parent.mkdir(exist_ok=True)
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)
    
    return root_logger

logger = setup_logging()

@dataclass
class VideoInfo:
    """Video file information"""
    file_path: str
    file_size_bytes: int
    file_size_mb: float
    duration_seconds: float
    resolution: str
    fps: float

@dataclass
class RenderResult:
    """Single render task result"""
    file_name: str
    quality: str
    task_id: int
    start_time: float
    end_time: float
    duration: float
    success: bool
    returncode: int
    timeout: bool
    cpu_usage_start: float
    cpu_usage_end: float
    memory_usage_start: float
    memory_usage_end: float
    memory_available_start: float
    memory_available_end: float
    stdout: str
    stderr: str
    command: List[str]
    video_info: Optional[VideoInfo] = None
    estimated_cpu_usage: float = 0.0

@dataclass
class QualityTestResult:
    """Quality level test result"""
    quality: str
    max_concurrent_tasks: int
    total_tasks_started: int
    successful_tasks: int
    failed_tasks: int
    success_rate: float
    task_durations: List[float]
    avg_duration: float
    min_duration: float
    max_duration: float
    median_duration: float
    std_duration: float
    video_durations: List[float]
    avg_video_duration: float
    min_video_duration: float
    max_video_duration: float
    video_file_sizes: List[float]
    avg_file_size: float
    min_file_size: float
    max_file_size: float
    resource_usage: List[Dict]
    final_system_resources: Dict
    test_duration: float
    tasks_per_second: float
    individual_results: List[RenderResult]
    cpu_usage_history: List[float]

class ManimQualityStressTester:
    def __init__(self, code_dir: str, output_dir: str = "manim_quality_output", 
                 log_output_dir: str = "manim_task_logs", launch_interval: float = 1.0):
        self.code_dir = Path(code_dir)
        self.output_dir = Path(output_dir)
        self.log_output_dir = Path(log_output_dir)
        self.launch_interval = launch_interval
        self.output_dir.mkdir(exist_ok=True)
        self.log_output_dir.mkdir(exist_ok=True)
        
        self.manim_files = sorted(list(self.code_dir.glob("*.py")))
        if not self.manim_files:
            raise ValueError(f"No .py files found in directory {code_dir}")
        
        logger.info(f"Found {len(self.manim_files)} Manim code files")
        logger.info(f"Sample files: {[f.name for f in self.manim_files[:5]]}")
        logger.info(f"Task launch interval: {launch_interval} seconds")
        
        self.quality_configs = {
            'low': {'flag': '-ql', 'description': 'Low quality (480p)'},
            'medium': {'flag': '-qm', 'description': 'Medium quality (720p)'},
            'high': {'flag': '-qh', 'description': 'High quality (1080p)'},
            '2k': {'flag': '-qp', 'description': '2K quality (1440p)'},
            '4k': {'flag': '-qk', 'description': '4K quality (2160p)'}
        }
        
        self.system_monitor_data = []
        self.system_monitor_stop = threading.Event()
        self.completed_tasks = []
        
        for quality in self.quality_configs:
            (self.log_output_dir / quality).mkdir(exist_ok=True)
    
    def get_system_resources(self) -> Dict:
        """Get current system resource usage"""
        memory = psutil.virtual_memory()
        return {
            'timestamp': time.time(),
            'cpu_percent': psutil.cpu_percent(interval=0.1),
            'memory_percent': memory.percent,
            'memory_available_gb': memory.available / (1024**3),
            'memory_total_gb': memory.total / (1024**3),
            'disk_usage_percent': psutil.disk_usage('/').percent,
            'active_processes': len(psutil.pids())
        }
    
    def system_monitor_thread(self):
        """System monitoring thread"""
        while not self.system_monitor_stop.is_set():
            try:
                resources = self.get_system_resources()
                self.system_monitor_data.append(resources)
                time.sleep(1)
            except Exception as e:
                logger.warning(f"System monitor thread error: {e}")
                time.sleep(1)
    
    def get_video_info(self, video_path: Path) -> Optional[VideoInfo]:
        """Get video file information"""
        try:
            if not video_path.exists():
                return None
            
            file_size_bytes = video_path.stat().st_size
            file_size_mb = file_size_bytes / (1024**2)
            
            try:
                cmd = [
                    'ffprobe', '-v', 'quiet', '-print_format', 'json',
                    '-show_format', '-show_streams', str(video_path)
                ]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                
                if result.returncode == 0:
                    probe_data = json.loads(result.stdout)
                    duration = float(probe_data.get('format', {}).get('duration', 0))
                    
                    resolution = "unknown"
                    fps = 0.0
                    for stream in probe_data.get('streams', []):
                        if stream.get('codec_type') == 'video':
                            width = stream.get('width', 0)
                            height = stream.get('height', 0)
                            if width and height:
                                resolution = f"{width}x{height}"
                            avg_frame_rate = stream.get('avg_frame_rate', '0/1')
                            if '/' in avg_frame_rate:
                                num, den = avg_frame_rate.split('/')
                                if den != '0':
                                    fps = float(num) / float(den)
                            break
                    
                    return VideoInfo(
                        file_path=str(video_path),
                        file_size_bytes=file_size_bytes,
                        file_size_mb=file_size_mb,
                        duration_seconds=duration,
                        resolution=resolution,
                        fps=fps
                    )
            except (subprocess.SubprocessError, json.JSONDecodeError, ValueError, FileNotFoundError):
                pass
            
            return VideoInfo(
                file_path=str(video_path),
                file_size_bytes=file_size_bytes,
                file_size_mb=file_size_mb,
                duration_seconds=0.0,
                resolution="unknown",
                fps=0.0
            )
            
        except Exception as e:
            logger.warning(f"Failed to get video info {video_path}: {e}")
            return None
    
    def find_rendered_video(self, output_dir: Path) -> Optional[Path]:
        """Find rendered video file in output directory"""
        try:
            video_extensions = ['.mp4', '.mov', '.avi', '.mkv', '.webm']
            for ext in video_extensions:
                video_files = list(output_dir.rglob(f"*{ext}"))
                if video_files:
                    return max(video_files, key=lambda f: f.stat().st_mtime)
        except Exception as e:
            logger.warning(f"Failed to find video file {output_dir}: {e}")
        return None
    
    def render_single_file(self, file_path: Path, quality: str, task_id: int) -> RenderResult:
        """Render single Manim file"""
        start_time = time.time()
        quality_flag = self.quality_configs[quality]['flag']
        output_subdir = f"{quality}_{task_id}"
        output_path = self.output_dir / output_subdir
        output_path.mkdir(exist_ok=True)
        
        start_resources = self.get_system_resources()
        
        cmd = [
            "manim",
            quality_flag,
            "--disable_caching",
            "--media_dir", str(output_path),
            str(file_path)
        ]
        
        task_log_file = self.log_output_dir / quality / f"task_{task_id:03d}.log"
        
        try:
            logger.info(f"[{quality.upper()} #{task_id}] Starting command: {' '.join(cmd)}")
            
            with open(task_log_file, 'w', encoding='utf-8') as log_f:
                log_f.write(f"Task ID: {task_id}\n")
                log_f.write(f"Quality: {quality} ({self.quality_configs[quality]['description']})\n")
                log_f.write(f"File path: {file_path}\n")
                log_f.write(f"Command: {' '.join(cmd)}\n")
                log_f.write(f"Start time: {datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')}\n")
                log_f.write(f"Initial resources: CPU={start_resources['cpu_percent']:.1f}%, "
                           f"Memory={start_resources['memory_percent']:.1f}%, "
                           f"Available memory={start_resources['memory_available_gb']:.2f}GB\n")
                log_f.write("-" * 80 + "\n")
                log_f.write("Standard output and error output:\n")
                log_f.write("-" * 80 + "\n")
            
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True
            )
            
            stdout_lines = []
            stderr_lines = []
            
            def read_stdout():
                for line in iter(process.stdout.readline, ''):
                    stdout_lines.append(line)
                    with open(task_log_file, 'a', encoding='utf-8') as log_f:
                        log_f.write(f"STDOUT: {line}")
                    logger.debug(f"[{quality.upper()} #{task_id}] STDOUT: {line.strip()}")
            
            def read_stderr():
                for line in iter(process.stderr.readline, ''):
                    stderr_lines.append(line)
                    with open(task_log_file, 'a', encoding='utf-8') as log_f:
                        log_f.write(f"STDERR: {line}")
                    logger.debug(f"[{quality.upper()} #{task_id}] STDERR: {line.strip()}")
            
            stdout_thread = threading.Thread(target=read_stdout)
            stderr_thread = threading.Thread(target=read_stderr)
            stdout_thread.daemon = True
            stderr_thread.daemon = True
            stdout_thread.start()
            stderr_thread.start()
            
            try:
                process.wait(timeout=1200)
                timeout_occurred = False
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
                timeout_occurred = True
                logger.warning(f"[{quality.upper()} #{task_id}] Task timeout (1200 seconds)")
            
            stdout_thread.join(timeout=5)
            stderr_thread.join(timeout=5)
            
            end_time = time.time()
            end_resources = self.get_system_resources()
            
            stdout_content = ''.join(stdout_lines)
            stderr_content = ''.join(stderr_lines)
            
            success = process.returncode == 0 and not timeout_occurred
            
            video_info = None
            if success:
                video_file = self.find_rendered_video(output_path)
                if video_file:
                    video_info = self.get_video_info(video_file)
                    logger.info(f"[{quality.upper()} #{task_id}] Video: {video_file.name}, "
                              f"Size: {video_info.file_size_mb:.2f}MB, "
                              f"Duration: {video_info.duration_seconds:.2f}s")
            
            estimated_cpu_usage = (start_resources['cpu_percent'] + end_resources['cpu_percent']) / 2
            
            with open(task_log_file, 'a', encoding='utf-8') as log_f:
                log_f.write("-" * 80 + "\n")
                log_f.write(f"End time: {datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')}\n")
                log_f.write(f"Duration: {end_time - start_time:.2f} seconds\n")
                log_f.write(f"Return code: {process.returncode}\n")
                log_f.write(f"Timeout: {timeout_occurred}\n")
                log_f.write(f"Success: {success}\n")
                log_f.write(f"Estimated CPU usage: {estimated_cpu_usage:.1f}%\n")
                if video_info:
                    log_f.write(f"File size: {video_info.file_size_mb:.2f} MB\n")
                    log_f.write(f"Video duration: {video_info.duration_seconds:.2f} seconds\n")
                    log_f.write(f"Resolution: {video_info.resolution}\n")
                log_f.write(f"Final resources: CPU={end_resources['cpu_percent']:.1f}%, "
                           f"Memory={end_resources['memory_percent']:.1f}%, "
                           f"Available memory={end_resources['memory_available_gb']:.2f}GB\n")
            
            if success:
                logger.info(f"[{quality.upper()} #{task_id}] Task completed successfully "
                          f"(Duration: {end_time - start_time:.2f}s, CPU: {estimated_cpu_usage:.1f}%)")
            else:
                error_msg = stderr_content if stderr_content else "Unknown error"
                logger.error(f"[{quality.upper()} #{task_id}] Task failed - Return code: {process.returncode}, "
                           f"Timeout: {timeout_occurred}, Error: {error_msg[:200]}...")
            
            render_result = RenderResult(
                file_name=file_path.name,
                quality=quality,
                task_id=task_id,
                start_time=start_time,
                end_time=end_time,
                duration=end_time - start_time,
                success=success,
                returncode=process.returncode,
                timeout=timeout_occurred,
                cpu_usage_start=start_resources['cpu_percent'],
                cpu_usage_end=end_resources['cpu_percent'],
                memory_usage_start=start_resources['memory_percent'],
                memory_usage_end=end_resources['memory_percent'],
                memory_available_start=start_resources['memory_available_gb'],
                memory_available_end=end_resources['memory_available_gb'],
                stdout=stdout_content,
                stderr=stderr_content,
                command=cmd,
                video_info=video_info,
                estimated_cpu_usage=estimated_cpu_usage
            )
            
            return render_result
            
        except Exception as e:
            end_time = time.time()
            end_resources = self.get_system_resources()
            error_traceback = traceback.format_exc()
            
            with open(task_log_file, 'a', encoding='utf-8') as log_f:
                log_f.write(f"Exception: {str(e)}\n")
                log_f.write(f"Traceback:\n{error_traceback}\n")
            
            logger.error(f"[{quality.upper()} #{task_id}] Task execution exception: {e}")
            
            render_result = RenderResult(
                file_name=file_path.name,
                quality=quality,
                task_id=task_id,
                start_time=start_time,
                end_time=end_time,
                duration=end_time - start_time,
                success=False,
                returncode=-1,
                timeout=False,
                cpu_usage_start=start_resources['cpu_percent'],
                cpu_usage_end=end_resources['cpu_percent'],
                memory_usage_start=start_resources['memory_percent'],
                memory_usage_end=end_resources['memory_percent'],
                memory_available_start=start_resources['memory_available_gb'],
                memory_available_end=end_resources['memory_available_gb'],
                stdout="",
                stderr=str(e) + "\n" + error_traceback,
                command=cmd,
                estimated_cpu_usage=(start_resources['cpu_percent'] + end_resources['cpu_percent']) / 2
            )
            
            return render_result
    
    def can_start_new_task(self, completed_tasks: List[RenderResult], current_cpu_usage: float) -> bool:
        """Intelligent check if new task can be started"""
        if not completed_tasks:
            return True
        
        current_resources = self.get_system_resources()
        current_cpu = current_resources['cpu_percent']
        current_memory = current_resources['memory_percent']
        
        if current_cpu > 90 or current_memory > 90:
            logger.warning(f"System resources too high - CPU: {current_cpu:.1f}%, Memory: {current_memory:.1f}%, pausing new tasks")
            return False
        
        successful_tasks = [t for t in completed_tasks if t.success]
        if not successful_tasks:
            avg_cpu_usage = 20.0
        else:
            avg_cpu_usage = statistics.mean([t.estimated_cpu_usage for t in successful_tasks])
        
        remaining_cpu = 100 - current_cpu
        required_cpu = avg_cpu_usage + 5.0
        can_start = remaining_cpu >= required_cpu
        
        if not can_start:
            logger.info(f"Insufficient resources - Remaining CPU: {remaining_cpu:.1f}%, "
                       f"Required CPU: {required_cpu:.1f}% (Average: {avg_cpu_usage:.1f}%), "
                       f"pausing new tasks")
        
        return can_start
    
    def test_quality_level(self, quality: str, max_test_duration: int = 1800) -> QualityTestResult:
        """Test specified quality level with intelligent resource management"""
        logger.info(f"\n{'='*80}")
        logger.info(f"Starting {self.quality_configs[quality]['description']} test")
        logger.info(f"Task launch interval: {self.launch_interval} seconds")
        logger.info(f"Intelligent resource management strategy enabled")
        logger.info(f"{'='*80}")
        
        self.system_monitor_data = []
        self.system_monitor_stop.clear()
        self.completed_tasks = []
        
        monitor_thread = threading.Thread(target=self.system_monitor_thread)
        monitor_thread.start()
        
        start_test_time = time.time()
        render_results = []
        task_id = 0
        consecutive_failures = 0
        max_consecutive_failures = 3
        last_task_start_time = 0
        
        try:
            while True:
                current_time = time.time()
                elapsed_time = current_time - start_test_time
                
                if elapsed_time > max_test_duration:
                    logger.info(f"Reached maximum test duration {max_test_duration} seconds, stopping test")
                    break
                
                if not self.can_start_new_task(self.completed_tasks, 
                                             self.get_system_resources()['cpu_percent']):
                    logger.info("Waiting for resource release...")
                    time.sleep(5)
                    continue
                
                if task_id >= len(self.manim_files):
                    file_to_render = self.manim_files[task_id % len(self.manim_files)]
                else:
                    file_to_render = self.manim_files[task_id]
                
                logger.info(f"[{quality.upper()}] Starting task #{task_id + 1}: {file_to_render.name}")
                
                render_thread = threading.Thread(
                    target=self._render_task_wrapper,
                    args=(file_to_render, quality, task_id, render_results)
                )
                render_thread.daemon = True
                render_thread.start()
                
                task_id += 1
                last_task_start_time = current_time
                time.sleep(self.launch_interval)
                
                self.completed_tasks = [r for r in render_results if r.end_time > 0]
                
                recent_results = [r for r in self.completed_tasks if r.end_time > current_time - 60]
                if recent_results:
                    recent_failures = sum(1 for r in recent_results if not r.success)
                    if recent_failures >= max_consecutive_failures:
                        logger.info(f"Detected {recent_failures} failed tasks in last 60 seconds, stopping test")
                        break
                
                active_tasks = len([r for r in render_results if r.end_time == 0])
                if (current_time - last_task_start_time > max(120, self.launch_interval * 10) and 
                    active_tasks > 10):
                    logger.warning("Possible system hang detected, stopping test")
                    break
            
            logger.info(f"[{quality.upper()}] Waiting for all render tasks to complete...")
            wait_start = time.time()
            max_wait_time = 600
            while time.time() - wait_start < max_wait_time:
                completed_count = sum(1 for r in render_results if r.end_time > 0)
                if completed_count == len(render_results):
                    break
                remaining = len(render_results) - completed_count
                logger.info(f"[{quality.upper()}] {remaining} tasks remaining...")
                time.sleep(10)
            
            self.system_monitor_stop.set()
            monitor_thread.join(timeout=5)
            
            successful_results = [r for r in render_results if r.success]
            durations = [r.duration for r in successful_results]
            
            video_durations = []
            file_sizes = []
            for r in successful_results:
                if r.video_info:
                    if r.video_info.duration_seconds > 0:
                        video_durations.append(r.video_info.duration_seconds)
                    if r.video_info.file_size_mb > 0:
                        file_sizes.append(r.video_info.file_size_mb)
            
            if durations:
                avg_duration = statistics.mean(durations)
                min_duration = min(durations)
                max_duration = max(durations)
                median_duration = statistics.median(durations)
                std_duration = statistics.stdev(durations) if len(durations) > 1 else 0
            else:
                avg_duration = min_duration = max_duration = median_duration = std_duration = 0
            
            if video_durations:
                avg_video_duration = statistics.mean(video_durations)
                min_video_duration = min(video_durations)
                max_video_duration = max(video_durations)
            else:
                avg_video_duration = min_video_duration = max_video_duration = 0
            
            if file_sizes:
                avg_file_size = statistics.mean(file_sizes)
                min_file_size = min(file_sizes)
                max_file_size = max(file_sizes)
            else:
                avg_file_size = min_file_size = max_file_size = 0
            
            successful_count = len(successful_results)
            failed_count = len(render_results) - successful_count
            success_rate = successful_count / len(render_results) if render_results else 0
            
            max_concurrent = self._calculate_max_concurrent(render_results)
            test_duration = time.time() - start_test_time
            tasks_per_second = len(render_results) / test_duration if test_duration > 0 else 0
            
            cpu_usage_history = [r.estimated_cpu_usage for r in successful_results if r.estimated_cpu_usage > 0]
            
            result = QualityTestResult(
                quality=quality,
                max_concurrent_tasks=max_concurrent,
                total_tasks_started=len(render_results),
                successful_tasks=successful_count,
                failed_tasks=failed_count,
                success_rate=success_rate,
                task_durations=durations,
                avg_duration=avg_duration,
                min_duration=min_duration,
                max_duration=max_duration,
                median_duration=median_duration,
                std_duration=std_duration,
                video_durations=video_durations,
                avg_video_duration=avg_video_duration,
                min_video_duration=min_video_duration,
                max_video_duration=max_video_duration,
                video_file_sizes=file_sizes,
                avg_file_size=avg_file_size,
                min_file_size=min_file_size,
                max_file_size=max_file_size,
                resource_usage=self.system_monitor_data.copy(),
                final_system_resources=self.get_system_resources(),
                test_duration=test_duration,
                tasks_per_second=tasks_per_second,
                individual_results=render_results,
                cpu_usage_history=cpu_usage_history
            )
            
            logger.info(f"{quality.upper()} test completed:")
            logger.info(f"  Total tasks: {result.total_tasks_started}")
            logger.info(f"  Successful tasks: {result.successful_tasks}")
            logger.info(f"  Max concurrent: {result.max_concurrent_tasks}")
            logger.info(f"  Avg render duration: {result.avg_duration:.2f}s")
            logger.info(f"  Avg video duration: {result.avg_video_duration:.2f}s")
            logger.info(f"  Avg file size: {result.avg_file_size:.2f}MB")
            logger.info(f"  Success rate: {result.success_rate:.2%}")
            
            return result
            
        except KeyboardInterrupt:
            logger.info(f"[{quality.upper()}] Test interrupted by user")
            self.system_monitor_stop.set()
            monitor_thread.join(timeout=5)
            raise
        except Exception as e:
            logger.error(f"[{quality.upper()}] Test error: {e}")
            logger.error(f"[{quality.upper()}] Traceback:\n{traceback.format_exc()}")
            self.system_monitor_stop.set()
            monitor_thread.join(timeout=5)
            raise
    
    def _render_task_wrapper(self, file_path: Path, quality: str, task_id: int, results_list: List[RenderResult]):
        """Wrapper for render task"""
        result = self.render_single_file(file_path, quality, task_id)
        results_list.append(result)
        status = "success" if result.success else "failed"
        logger.info(f"[{quality.upper()} #{task_id}] Task {status} (Duration: {result.duration:.2f}s)")
    
    def _calculate_max_concurrent(self, results: List[RenderResult]) -> int:
        """Calculate maximum concurrent tasks"""
        if not results:
            return 0
        
        events = []
        for result in results:
            events.append((result.start_time, 1))
            events.append((result.end_time, -1))
        
        events.sort()
        
        current_concurrent = 0
        max_concurrent = 0
        
        for _, delta in events:
            current_concurrent += delta
            max_concurrent = max(max_concurrent, current_concurrent)
        
        return max_concurrent
    
    def generate_report(self, results: Dict[str, QualityTestResult]) -> str:
        """Generate detailed test report"""
        report_lines = []
        report_lines.append("=" * 130)
        report_lines.append("MANIQ - Manim Quality Stress Testing Report")
        report_lines.append("=" * 130)
        report_lines.append(f"Test time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_lines.append(f"Test files: {len(self.manim_files)}")
        report_lines.append(f"Code directory: {self.code_dir}")
        report_lines.append(f"Task launch interval: {self.launch_interval} seconds")
        report_lines.append("")
        
        report_lines.append("System Information:")
        report_lines.append(f"  CPU cores: {psutil.cpu_count()} (Logical: {psutil.cpu_count(logical=True)})")
        report_lines.append(f"  Total memory: {psutil.virtual_memory().total / (1024**3):.2f} GB")
        report_lines.append(f"  Available disk space: {psutil.disk_usage('/').free / (1024**3):.2f} GB")
        report_lines.append("")
        
        all_qualities = ['low', 'medium', 'high', '2k', '4k']
        for quality in all_qualities:
            if quality not in results:
                continue
                
            result = results[quality]
            desc = self.quality_configs[quality]['description']
            
            report_lines.append(f"{desc.upper()} Test Results")
            report_lines.append("-" * 90)
            report_lines.append(f"Max concurrent tasks: {result.max_concurrent_tasks}")
            report_lines.append(f"Total tasks started: {result.total_tasks_started}")
            report_lines.append(f"Successful tasks: {result.successful_tasks}")
            report_lines.append(f"Failed tasks: {result.failed_tasks}")
            report_lines.append(f"Success rate: {result.success_rate:.2%}")
            report_lines.append("")
            
            if result.task_durations:
                report_lines.append("Render Task Duration Statistics (seconds):")
                report_lines.append(f"  Average: {result.avg_duration:.2f}")
                report_lines.append(f"  Minimum: {result.min_duration:.2f}")
                report_lines.append(f"  Maximum: {result.max_duration:.2f}")
                report_lines.append(f"  Median: {result.median_duration:.2f}")
                report_lines.append(f"  Standard deviation: {result.std_duration:.2f}")
                report_lines.append("")
            
            if result.video_durations:
                report_lines.append("Rendered Video Duration Statistics (seconds):")
                report_lines.append(f"  Average: {result.avg_video_duration:.2f}")
                report_lines.append(f"  Minimum: {result.min_video_duration:.2f}")
                report_lines.append(f"  Maximum: {result.max_video_duration:.2f}")
                report_lines.append("")
            
            if result.video_file_sizes:
                report_lines.append("Rendered Video File Size Statistics (MB):")
                report_lines.append(f"  Average: {result.avg_file_size:.2f}")
                report_lines.append(f"  Minimum: {result.min_file_size:.2f}")
                report_lines.append(f"  Maximum: {result.max_file_size:.2f}")
                report_lines.append("")
            
            if result.resource_usage:
                cpu_usage = [r['cpu_percent'] for r in result.resource_usage]
                memory_usage = [r['memory_percent'] for r in result.resource_usage]
                
                report_lines.append("System Resource Usage Statistics:")
                report_lines.append(f"  CPU usage - Average: {statistics.mean(cpu_usage):.1f}%, "
                                  f"Peak: {max(cpu_usage):.1f}%")
                report_lines.append(f"  Memory usage - Average: {statistics.mean(memory_usage):.1f}%, "
                                  f"Peak: {max(memory_usage):.1f}%")
                report_lines.append("")
            
            if result.cpu_usage_history:
                avg_cpu_per_task = statistics.mean(result.cpu_usage_history)
                report_lines.append(f"Average CPU usage per task: {avg_cpu_per_task:.1f}%")
                report_lines.append("")
            
            report_lines.append(f"Detailed task logs saved in: {self.log_output_dir / quality}")
            report_lines.append("")
        
        report_lines.append("Performance Comparison Summary")
        report_lines.append("-" * 110)
        report_lines.append(f"{'Quality':<15} {'Max Concurrent':<15} {'Success Rate':<15} {'Avg Render Time':<18} {'Avg Video Duration':<20} {'Avg File Size (MB)':<18}")
        report_lines.append("-" * 110)
        
        for quality in all_qualities:
            if quality not in results:
                continue
                
            result = results[quality]
            desc = quality.upper()
            
            report_lines.append(f"{desc:<15} {result.max_concurrent_tasks:<15} "
                              f"{result.success_rate:<15.2%} {result.avg_duration:<18.2f} "
                              f"{result.avg_video_duration:<20.2f} {result.avg_file_size:<18.2f}")
        
        report_lines.append("")
        report_lines.append("Intelligent Resource Management Strategy:")
        report_lines.append("• Dynamically adjusts concurrency based on historical CPU usage")
        report_lines.append("• Pauses new tasks when remaining CPU < (average CPU usage + 5%)")
        report_lines.append("• Automatically pauses when CPU or memory usage > 90%")
        report_lines.append("• Prevents server crashes due to resource exhaustion")
        report_lines.append("")
        
        report_lines.append("Recommendations:")
        if results:
            best_quality = max(results.keys(), key=lambda q: results[q].max_concurrent_tasks)
            report_lines.append(f"• Based on maximum concurrency, recommend using {best_quality.upper()} quality")
            
            qualities_with_data = [q for q in ['low', 'medium', 'high', '2k', '4k'] if q in results]
            if len(qualities_with_data) >= 2:
                first_q = qualities_with_data[0]
                last_q = qualities_with_data[-1]
                first_size = results[first_q].avg_file_size
                last_size = results[last_q].avg_file_size
                if first_size > 0 and last_size > 0:
                    size_ratio = last_size / first_size
                    report_lines.append(f"• {last_q.upper()} quality video file size is {size_ratio:.1f}x larger than {first_q.upper()}")
        
        report_lines.append("=" * 130)
        
        return "\n".join(report_lines)
    
    def run_selected_tests(self, selected_qualities: List[str], max_duration_per_test: int = 1800) -> Dict[str, QualityTestResult]:
        """Run selected quality level tests"""
        results = {}
        
        valid_qualities = set(self.quality_configs.keys())
        invalid_qualities = set(selected_qualities) - valid_qualities
        if invalid_qualities:
            logger.warning(f"Invalid quality levels: {invalid_qualities}")
            selected_qualities = [q for q in selected_qualities if q in valid_qualities]
        
        if not selected_qualities:
            logger.error("No valid quality levels selected")
            return results
        
        logger.info(f"Testing quality levels: {selected_qualities}")
        
        for quality in selected_qualities:
            try:
                logger.info(f"\n{'='*80}")
                logger.info(f"Preparing {self.quality_configs[quality]['description']} test...")
                logger.info(f"{'='*80}")
                
                logger.info("Waiting for system resource recovery (30 seconds)...")
                for i in range(30, 0, -1):
                    if i % 10 == 0:
                        resources = self.get_system_resources()
                        logger.info(f"Countdown {i} seconds... Current resources: CPU={resources['cpu_percent']:.1f}%, "
                                  f"Memory={resources['memory_percent']:.1f}%")
                    time.sleep(1)
                
                result = self.test_quality_level(quality, max_duration_per_test)
                results[quality] = result
                
            except KeyboardInterrupt:
                logger.info(f"User interrupted {quality} quality test")
                break
            except Exception as e:
                logger.error(f"{quality} quality test failed: {e}")
                continue
        
        return results

def main():
    parser = argparse.ArgumentParser(description="Maniq - Manim Quality Stress Testing Tool")
    parser.add_argument("code_dir", help="Manim code files directory")
    parser.add_argument("--output-dir", default="manim_quality_output", help="Render output directory")
    parser.add_argument("--log-output-dir", default="manim_task_logs", help="Task log output directory")
    parser.add_argument("--max-duration", type=int, default=1800, 
                       help="Maximum test duration per quality level in seconds (default: 1800)")
    parser.add_argument("--report-file", default="manim_quality_test_report.txt",
                       help="Test report filename")
    parser.add_argument("--json-report", default="manim_quality_test_results.json",
                       help="JSON report filename")
    parser.add_argument("--log-file", default="manim_quality_stress_test.log",
                       help="Main log filename")
    parser.add_argument("--launch-interval", type=float, default=1.0,
                       help="Task launch interval in seconds (default: 1.0)")
    parser.add_argument("--qualities", nargs='+', 
                       choices=['low', 'medium', 'high', '2k', '4k'],
                       default=['low', 'medium', 'high', '2k', '4k'],
                       help="Quality levels to test (default: all levels)")
    
    args = parser.parse_args()
    
    global logger
    logger = setup_logging(args.log_file)
    
    try:
        tester = ManimQualityStressTester(
            args.code_dir, 
            args.output_dir, 
            args.log_output_dir,
            args.launch_interval
        )
        
        logger.info("=" * 90)
        logger.info("Starting Maniq - Manim Quality Stress Testing")
        logger.info(f"Supported quality levels: low(480p), medium(720p), high(1080p), 2k(1440p), 4k(2160p)")
        logger.info(f"Testing quality levels: {args.qualities}")
        logger.info(f"Task launch interval: {args.launch_interval} seconds")
        logger.info("Features: Intelligent resource management + Detailed video analysis + Crash prevention")
        logger.info("=" * 90)
        
        results = tester.run_selected_tests(args.qualities, args.max_duration)
        
        if not results:
            logger.error("All tests failed!")
            sys.exit(1)
        
        report = tester.generate_report(results)
        with open(args.report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        json_results = {}
        for quality, result in results.items():
            json_results[quality] = asdict(result)
            if 'individual_results' in json_results[quality]:
                individual_results = []
                for r in json_results[quality]['individual_results']:
                    r_copy = r.copy()
                    if len(r_copy.get('stdout', '')) > 10000:
                        r_copy['stdout'] = r_copy['stdout'][:10000] + " [truncated...]"
                    if len(r_copy.get('stderr', '')) > 10000:
                        r_copy['stderr'] = r_copy['stderr'][:10000] + " [truncated...]"
                    individual_results.append(r_copy)
                json_results[quality]['individual_results'] = individual_results
            
            if 'resource_usage' in json_results[quality]:
                json_results[quality]['resource_usage'] = [
                    {k: v for k, v in r.items()} for r in json_results[quality]['resource_usage']
                ]
        
        with open(args.json_report, 'w', encoding='utf-8') as f:
            json.dump(json_results, f, indent=2, ensure_ascii=False, default=str)
        
        print("\n" + "="*130)
        print("Test completed! Detailed report below:")
        print("="*130)
        print(report)
        
        print(f"\nComplete reports saved to:")
        print(f"  📄 Text report: {args.report_file}")
        print(f"  📊 JSON report: {args.json_report}")
        print(f"  📝 Main log file: {args.log_file}")
        print(f"  📁 Task log directory: {args.log_output_dir}")
        print(f"  🎥 Render output directory: {args.output_dir}")
        
    except KeyboardInterrupt:
        logger.info("Test interrupted by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Critical error during testing: {e}")
        logger.error(f"Traceback:\n{traceback.format_exc()}")
        sys.exit(1)

if __name__ == "__main__":
    main()