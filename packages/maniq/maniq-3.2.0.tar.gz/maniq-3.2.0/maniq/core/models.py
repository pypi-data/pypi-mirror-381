#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data models for Maniq
"""

from dataclasses import dataclass
from typing import List, Dict, Optional

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