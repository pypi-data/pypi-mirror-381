#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main testing logic for Maniq
"""

import os
import sys
import subprocess
import time
import threading
import json
import statistics
import traceback
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional, Tuple

from .models import RenderResult, QualityTestResult, VideoInfo
from .resource_monitor import SystemResourceMonitor
from ..utils.video_analyzer import VideoAnalyzer
from ..utils.logging import get_logger
from ..utils.text_utils import create_aligned_table
from ..i18n.translator import Translator


class ManimQualityStressTester:
    """Main class for Manim quality stress testing"""
    
    def __init__(self, code_dir: str, output_dir: str = "manim_quality_output", 
                 log_output_dir: str = "manim_task_logs", launch_interval: float = 1.0,
                 language: str = 'en'):
        self.code_dir = Path(code_dir)
        self.output_dir = Path(output_dir)
        self.log_output_dir = Path(log_output_dir)
        self.launch_interval = launch_interval
        self.translator = Translator(language)
        self.logger = get_logger()
        
        self.output_dir.mkdir(exist_ok=True)
        self.log_output_dir.mkdir(exist_ok=True)
        
        self.manim_files = sorted(list(self.code_dir.glob("*.py")))
        if not self.manim_files:
            raise ValueError(self.translator.get('no_py_files', code_dir=code_dir))
        
        self.logger.info(self.translator.get('found_files', count=len(self.manim_files)))
        self.logger.info(self.translator.get('sample_files', files=[f.name for f in self.manim_files[:5]]))
        self.logger.info(self.translator.get('task_interval', interval=launch_interval))
        
        self.quality_configs = {
            'low': {'flag': '-ql', 'description': self.translator.translations.get('low_desc', 'Low quality (480p)')},
            'medium': {'flag': '-qm', 'description': self.translator.translations.get('medium_desc', 'Medium quality (720p)')},
            'high': {'flag': '-qh', 'description': self.translator.translations.get('high_desc', 'High quality (1080p)')},
            '2k': {'flag': '-qp', 'description': self.translator.translations.get('2k_desc', '2K quality (1440p)')},
            '4k': {'flag': '-qk', 'description': self.translator.translations.get('4k_desc', '4K quality (2160p)')}
        }
        
        self.resource_monitor = SystemResourceMonitor()
        self.completed_tasks = []
        
        for quality in self.quality_configs:
            (self.log_output_dir / quality).mkdir(exist_ok=True)
    
    def render_single_file(self, file_path: Path, quality: str, task_id: int) -> RenderResult:
        """Render single Manim file"""
        start_time = time.time()
        quality_flag = self.quality_configs[quality]['flag']
        output_subdir = f"{quality}_{task_id}"
        output_path = self.output_dir / output_subdir
        output_path.mkdir(exist_ok=True)
        
        start_resources = self.resource_monitor.get_system_resources()
        
        cmd = [
            "manim",
            quality_flag,
            "--disable_caching",
            "--media_dir", str(output_path),
            str(file_path)
        ]
        
        task_log_file = self.log_output_dir / quality / f"task_{task_id:03d}.log"
        
        try:
            self.logger.info(self.translator.get('starting_task', quality=quality.upper(), task_id=task_id+1, filename=file_path.name))
            
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
                    self.logger.debug(f"[{quality.upper()} #{task_id}] STDOUT: {line.strip()}")
            
            def read_stderr():
                for line in iter(process.stderr.readline, ''):
                    stderr_lines.append(line)
                    with open(task_log_file, 'a', encoding='utf-8') as log_f:
                        log_f.write(f"STDERR: {line}")
                    self.logger.debug(f"[{quality.upper()} #{task_id}] STDERR: {line.strip()}")
            
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
                self.logger.warning(self.translator.get('reached_max_duration', duration=1200))
            
            stdout_thread.join(timeout=5)
            stderr_thread.join(timeout=5)
            
            end_time = time.time()
            end_resources = self.resource_monitor.get_system_resources()
            
            stdout_content = ''.join(stdout_lines)
            stderr_content = ''.join(stderr_lines)
            
            success = process.returncode == 0 and not timeout_occurred
            
            # Get video information
            video_info = None
            if success:
                video_file = VideoAnalyzer.find_rendered_video(output_path)
                if video_file:
                    video_info = VideoAnalyzer.get_video_info(video_file)
                    self.logger.info(f"[{quality.upper()} #{task_id}] Video: {video_file.name}, "
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
                self.logger.info(f"[{quality.upper()} #{task_id}] Task completed successfully "
                               f"(Duration: {end_time - start_time:.2f}s, CPU: {estimated_cpu_usage:.1f}%)")
            else:
                error_msg = stderr_content if stderr_content else "Unknown error"
                self.logger.error(f"[{quality.upper()} #{task_id}] Task failed - Return code: {process.returncode}, "
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
            end_resources = self.resource_monitor.get_system_resources()
            error_traceback = traceback.format_exc()
            
            with open(task_log_file, 'a', encoding='utf-8') as log_f:
                log_f.write(f"Exception: {str(e)}\n")
                log_f.write(f"Traceback:\n{error_traceback}\n")
            
            self.logger.error(f"[{quality.upper()} #{task_id}] Task execution exception: {e}")
            
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
        
        current_resources = self.resource_monitor.get_system_resources()
        current_cpu = current_resources['cpu_percent']
        current_memory = current_resources['memory_percent']
        
        if current_cpu > 90 or current_memory > 90:
            self.logger.warning(self.translator.get('waiting_resources'))
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
            self.logger.info(self.translator.get('waiting_resources'))
        
        return can_start
    
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
    
    def _render_task_wrapper(self, file_path: Path, quality: str, task_id: int, results_list: List[RenderResult]):
        """Wrapper for render task"""
        result = self.render_single_file(file_path, quality, task_id)
        results_list.append(result)
        status = "success" if result.success else "failed"
        self.logger.info(f"[{quality.upper()} #{task_id}] Task {status} (Duration: {result.duration:.2f}s)")
    
    def test_quality_level(self, quality: str, max_test_duration: int = 1800) -> QualityTestResult:
        """Test specified quality level with intelligent resource management"""
        self.logger.info(f"\n{'='*80}")
        self.logger.info(self.translator.get('starting_test', description=self.quality_configs[quality]['description']))
        self.logger.info(self.translator.get('task_interval', interval=self.launch_interval))
        self.logger.info(self.translator.get('intelligent_resource'))
        self.logger.info(f"{'='*80}")
        
        # Reset monitoring data
        self.resource_monitor.clear_monitor_data()
        self.resource_monitor.start_monitoring()
        self.completed_tasks = []
        
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
                    self.logger.info(self.translator.get('reached_max_duration', duration=max_test_duration))
                    break
                
                if not self.can_start_new_task(self.completed_tasks, 
                                             self.resource_monitor.get_system_resources()['cpu_percent']):
                    self.logger.info(self.translator.get('waiting_resources'))
                    time.sleep(5)
                    continue
                
                if task_id >= len(self.manim_files):
                    file_to_render = self.manim_files[task_id % len(self.manim_files)]
                else:
                    file_to_render = self.manim_files[task_id]
                
                self.logger.info(self.translator.get('starting_task', quality=quality.upper(), task_id=task_id+1, filename=file_to_render.name))
                
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
                        self.logger.info(self.translator.get('reached_max_duration', duration=max_test_duration))
                        break
                
                active_tasks = len([r for r in render_results if r.end_time == 0])
                if (current_time - last_task_start_time > max(120, self.launch_interval * 10) and 
                    active_tasks > 10):
                    self.logger.warning(self.translator.get('reached_max_duration', duration=max_test_duration))
                    break
            
            self.logger.info(self.translator.get('waiting_completion', quality=quality.upper()))
            wait_start = time.time()
            max_wait_time = 600
            while time.time() - wait_start < max_wait_time:
                completed_count = sum(1 for r in render_results if r.end_time > 0)
                if completed_count == len(render_results):
                    break
                remaining = len(render_results) - completed_count
                self.logger.info(self.translator.get('tasks_remaining', quality=quality.upper(), remaining=remaining))
                time.sleep(10)
            
            self.resource_monitor.stop_monitoring()
            
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
                resource_usage=self.resource_monitor.get_monitor_data(),
                final_system_resources=self.resource_monitor.get_system_resources(),
                test_duration=test_duration,
                tasks_per_second=tasks_per_second,
                individual_results=render_results,
                cpu_usage_history=cpu_usage_history
            )
            
            self.logger.info(self.translator.get('test_completed', quality=quality.upper()))
            self.logger.info(self.translator.get('total_tasks', count=result.total_tasks_started))
            self.logger.info(self.translator.get('successful_tasks', count=result.successful_tasks))
            self.logger.info(self.translator.get('max_concurrent', count=result.max_concurrent_tasks))
            self.logger.info(self.translator.get('avg_render_duration', duration=result.avg_duration))
            self.logger.info(self.translator.get('avg_video_duration', duration=result.avg_video_duration))
            self.logger.info(self.translator.get('avg_file_size', size=result.avg_file_size))
            self.logger.info(self.translator.get('success_rate', rate=result.success_rate))
            
            return result
            
        except KeyboardInterrupt:
            self.logger.info(self.translator.get('test_interrupted'))
            self.resource_monitor.stop_monitoring()
            raise
        except Exception as e:
            self.logger.error(self.translator.get('critical_error', error=e))
            self.logger.error(f"[{quality.upper()}] Traceback:\n{traceback.format_exc()}")
            self.resource_monitor.stop_monitoring()
            raise
    
    def run_selected_tests(self, selected_qualities: List[str], max_duration_per_test: int = 1800) -> Dict[str, QualityTestResult]:
        """Run selected quality level tests"""
        results = {}
        
        valid_qualities = set(self.quality_configs.keys())
        invalid_qualities = set(selected_qualities) - valid_qualities
        if invalid_qualities:
            self.logger.warning(f"Invalid quality levels: {invalid_qualities}")
            selected_qualities = [q for q in selected_qualities if q in valid_qualities]
        
        if not selected_qualities:
            self.logger.error(self.translator.get('all_tests_failed'))
            return results
        
        self.logger.info(self.translator.get('testing_qualities', qualities=selected_qualities))
        
        for quality in selected_qualities:
            try:
                self.logger.info(f"\n{'='*80}")
                self.logger.info(self.translator.get('preparing_test', description=self.quality_configs[quality]['description']))
                self.logger.info(f"{'='*80}")
                
                self.logger.info(self.translator.get('waiting_recovery'))
                for i in range(30, 0, -1):
                    if i % 10 == 0:
                        resources = self.resource_monitor.get_system_resources()
                        self.logger.info(self.translator.get('countdown_resources', seconds=i, cpu=resources['cpu_percent'], memory=resources['memory_percent']))
                    time.sleep(1)
                
                result = self.test_quality_level(quality, max_duration_per_test)
                results[quality] = result
                
            except KeyboardInterrupt:
                self.logger.info(self.translator.get('test_interrupted'))
                break
            except Exception as e:
                self.logger.error(f"{quality} quality test failed: {e}")
                continue
        
        return results
    
    def generate_report(self, results: Dict[str, QualityTestResult]) -> str:
        """Generate detailed test report"""
        from ..utils.system_info import get_system_info
        
        report_lines = []
        report_lines.append("=" * 130)
        report_lines.append(self.translator.get('report_title'))
        report_lines.append("=" * 130)
        report_lines.append(self.translator.get('test_time', time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        report_lines.append(self.translator.get('test_files', count=len(self.manim_files)))
        report_lines.append(self.translator.get('code_directory', path=self.code_dir))
        report_lines.append(self.translator.get('task_launch_interval', interval=self.launch_interval))
        report_lines.append("")
        
        # System information
        system_info = get_system_info()
        report_lines.append(self.translator.get('system_information'))
        report_lines.append(self.translator.get('cpu_cores', physical=system_info['cpu_physical'], logical=system_info['cpu_logical']))
        report_lines.append(self.translator.get('total_memory', memory=system_info['total_memory_gb']))
        report_lines.append(self.translator.get('available_disk', disk=system_info['available_disk_gb']))
        report_lines.append("")
        
        all_qualities = ['low', 'medium', 'high', '2k', '4k']
        quality_names = {
            'low': self.translator.translations.get('low_name', 'LOW'),
            'medium': self.translator.translations.get('medium_name', 'MEDIUM'),
            'high': self.translator.translations.get('high_name', 'HIGH'),
            '2k': self.translator.translations.get('2k_name', '2K'),
            '4k': self.translator.translations.get('4k_name', '4K'),
        }
        
        for quality in all_qualities:
            if quality not in results:
                continue
                
            result = results[quality]
            desc = self.quality_configs[quality]['description']
            
            report_lines.append(self.translator.get('test_results', description=desc))
            report_lines.append("-" * 90)
            report_lines.append(self.translator.get('max_concurrent_tasks', count=result.max_concurrent_tasks))
            report_lines.append(self.translator.get('total_tasks_started', count=result.total_tasks_started))
            report_lines.append(self.translator.get('successful_tasks_report', count=result.successful_tasks))
            report_lines.append(self.translator.get('failed_tasks', count=result.failed_tasks))
            report_lines.append(self.translator.get('success_rate_report', rate=result.success_rate))
            report_lines.append("")
            
            if result.task_durations:
                report_lines.append(self.translator.get('render_duration_stats'))
                report_lines.append(self.translator.get('average', value=result.avg_duration))
                report_lines.append(self.translator.get('minimum', value=result.min_duration))
                report_lines.append(self.translator.get('maximum', value=result.max_duration))
                report_lines.append(self.translator.get('median', value=result.median_duration))
                report_lines.append(self.translator.get('std_dev', value=result.std_duration))
                report_lines.append("")
            
            if result.video_durations:
                report_lines.append(self.translator.get('video_duration_stats'))
                report_lines.append(self.translator.get('average', value=result.avg_video_duration))
                report_lines.append(self.translator.get('minimum', value=result.min_video_duration))
                report_lines.append(self.translator.get('maximum', value=result.max_video_duration))
                report_lines.append("")
            
            if result.video_file_sizes:
                report_lines.append(self.translator.get('file_size_stats'))
                report_lines.append(self.translator.get('average', value=result.avg_file_size))
                report_lines.append(self.translator.get('minimum', value=result.min_file_size))
                report_lines.append(self.translator.get('maximum', value=result.max_file_size))
                report_lines.append("")
            
            if result.resource_usage:
                cpu_usage = [r['cpu_percent'] for r in result.resource_usage]
                memory_usage = [r['memory_percent'] for r in result.resource_usage]
                
                report_lines.append(self.translator.get('resource_usage_stats'))
                report_lines.append(self.translator.get('cpu_usage_stats', avg=statistics.mean(cpu_usage), peak=max(cpu_usage)))
                report_lines.append(self.translator.get('memory_usage_stats', avg=statistics.mean(memory_usage), peak=max(memory_usage)))
                report_lines.append("")
            
            if result.cpu_usage_history:
                avg_cpu_per_task = statistics.mean(result.cpu_usage_history)
                report_lines.append(self.translator.get('avg_cpu_per_task', usage=avg_cpu_per_task))
                report_lines.append("")
            
            report_lines.append(self.translator.get('detailed_logs_saved', path=self.log_output_dir / quality))
            report_lines.append("")
        
        report_lines.append(self.translator.get('performance_comparison'))
        
        # Create properly aligned table using the new utility
        headers = [
            self.translator.get('quality'),
            self.translator.get('max_concurrent_col'),
            self.translator.get('success_rate_col'),
            self.translator.get('avg_render_time_col'),
            self.translator.get('avg_video_duration_col'),
            self.translator.get('avg_file_size_col')
        ]
        
        # Prepare data rows
        data_rows = []
        for quality in all_qualities:
            if quality not in results:
                continue
            result = results[quality]
            quality_name = quality_names[quality]
            row = [
                quality_name,
                str(result.max_concurrent_tasks),
                f"{result.success_rate:.2%}",
                f"{result.avg_duration:.2f}",
                f"{result.avg_video_duration:.2f}",
                f"{result.avg_file_size:.2f}"
            ]
            data_rows.append(row)
        
        # Create aligned table (this will handle CJK characters properly)
        table = create_aligned_table(headers, data_rows)
        report_lines.append(table)
        report_lines.append("")
        
        report_lines.append(self.translator.get('resource_strategy'))
        report_lines.append(self.translator.get('strategy_point1'))
        report_lines.append(self.translator.get('strategy_point2'))
        report_lines.append(self.translator.get('strategy_point3'))
        report_lines.append(self.translator.get('strategy_point4'))
        report_lines.append("")
        
        report_lines.append(self.translator.get('recommendations'))
        if results:
            best_quality = max(results.keys(), key=lambda q: results[q].max_concurrent_tasks)
            best_quality_name = quality_names[best_quality]
            report_lines.append(self.translator.get('recommend_best_quality', quality=best_quality_name))
            
            qualities_with_data = [q for q in ['low', 'medium', 'high', '2k', '4k'] if q in results]
            if len(qualities_with_data) >= 2:
                first_q = qualities_with_data[0]
                last_q = qualities_with_data[-1]
                first_size = results[first_q].avg_file_size
                last_size = results[last_q].avg_file_size
                if first_size > 0 and last_size > 0:
                    size_ratio = last_size / first_size
                    first_name = quality_names[first_q]
                    last_name = quality_names[last_q]
                    report_lines.append(self.translator.get('recommend_file_size', 
                                                          high_quality=last_name, 
                                                          low_quality=first_name, 
                                                          ratio=size_ratio))
        
        report_lines.append("=" * 130)
        
        return "\n".join(report_lines)
    
    def generate_json_report(self, results: Dict[str, QualityTestResult]) -> str:
        """Generate JSON report"""
        from dataclasses import asdict
        
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
        
        return json.dumps(json_results, indent=2, ensure_ascii=False, default=str)
        