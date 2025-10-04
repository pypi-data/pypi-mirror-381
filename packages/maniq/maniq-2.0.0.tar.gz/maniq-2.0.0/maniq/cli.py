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

# Translation dictionary
TRANSLATIONS = {
    'en': {
        # Logging messages
        'no_py_files': "No .py files found in directory {code_dir}",
        'found_files': "Found {count} Manim code files",
        'sample_files': "Sample files: {files}",
        'task_interval': "Task launch interval: {interval} seconds",
        'starting_test': "Starting {description} test",
        'intelligent_resource': "Intelligent resource management strategy enabled",
        'reached_max_duration': "Reached maximum test duration {duration} seconds, stopping test",
        'waiting_resources': "Waiting for resource release...",
        'starting_task': "[{quality}] Starting task #{task_id}: {filename}",
        'waiting_completion': "[{quality}] Waiting for all render tasks to complete...",
        'tasks_remaining': "[{quality}] {remaining} tasks remaining...",
        'test_completed': "{quality} test completed:",
        'total_tasks': "  Total tasks: {count}",
        'successful_tasks': "  Successful tasks: {count}",
        'max_concurrent': "  Max concurrent: {count}",
        'avg_render_duration': "  Avg render duration: {duration:.2f}s",
        'avg_video_duration': "  Avg video duration: {duration:.2f}s",
        'avg_file_size': "  Avg file size: {size:.2f}MB",
        'success_rate': "  Success rate: {rate:.2%}",
        'testing_qualities': "Testing quality levels: {qualities}",
        'preparing_test': "Preparing {description} test...",
        'waiting_recovery': "Waiting for system resource recovery (30 seconds)...",
        'countdown_resources': "Countdown {seconds} seconds... Current resources: CPU={cpu:.1f}%, Memory={memory:.1f}%",
        'all_tests_failed': "All tests failed!",
        'test_interrupted': "Test interrupted by user",
        'critical_error': "Critical error during testing: {error}",
        
        # Report headers
        'report_title': "MANIQ - Manim Quality Stress Testing Report",
        'test_time': "Test time: {time}",
        'test_files': "Test files: {count}",
        'code_directory': "Code directory: {path}",
        'task_launch_interval': "Task launch interval: {interval} seconds",
        'system_information': "System Information:",
        'cpu_cores': "  CPU cores: {physical} (Logical: {logical})",
        'total_memory': "  Total memory: {memory:.2f} GB",
        'available_disk': "  Available disk space: {disk:.2f} GB",
        'test_results': "{description} Test Results",
        'max_concurrent_tasks': "Max concurrent tasks: {count}",
        'total_tasks_started': "Total tasks started: {count}",
        'successful_tasks_report': "Successful tasks: {count}",
        'failed_tasks': "Failed tasks: {count}",
        'success_rate_report': "Success rate: {rate:.2%}",
        'render_duration_stats': "Render Task Duration Statistics (seconds):",
        'average': "  Average: {value:.2f}",
        'minimum': "  Minimum: {value:.2f}",
        'maximum': "  Maximum: {value:.2f}",
        'median': "  Median: {value:.2f}",
        'std_dev': "  Standard deviation: {value:.2f}",
        'video_duration_stats': "Rendered Video Duration Statistics (seconds):",
        'file_size_stats': "Rendered Video File Size Statistics (MB):",
        'resource_usage_stats': "System Resource Usage Statistics:",
        'cpu_usage_stats': "  CPU usage - Average: {avg:.1f}%, Peak: {peak:.1f}%",
        'memory_usage_stats': "  Memory usage - Average: {avg:.1f}%, Peak: {peak:.1f}%",
        'avg_cpu_per_task': "Average CPU usage per task: {usage:.1f}%",
        'detailed_logs_saved': "Detailed task logs saved in: {path}",
        'performance_comparison': "Performance Comparison Summary",
        'quality': "Quality",
        'max_concurrent_col': "Max Concurrent",
        'success_rate_col': "Success Rate",
        'avg_render_time_col': "Avg Render Time",
        'avg_video_duration_col': "Avg Video Duration",
        'avg_file_size_col': "Avg File Size (MB)",
        'resource_strategy': "Intelligent Resource Management Strategy:",
        'strategy_point1': "• Dynamically adjusts concurrency based on historical CPU usage",
        'strategy_point2': "• Pauses new tasks when remaining CPU < (average CPU usage + 5%)",
        'strategy_point3': "• Automatically pauses when CPU or memory usage > 90%",
        'strategy_point4': "• Prevents server crashes due to resource exhaustion",
        'recommendations': "Recommendations:",
        'recommend_best_quality': "• Based on maximum concurrency, recommend using {quality} quality",
        'recommend_file_size': "• {high_quality} quality video file size is {ratio:.1f}x larger than {low_quality}",
        
        # Quality descriptions
        'low_desc': "Low quality (480p)",
        'medium_desc': "Medium quality (720p)",
        'high_desc': "High quality (1080p)",
        '2k_desc': "2K quality (1440p)",
        '4k_desc': "4K quality (2160p)",
        
        # Quality names for display
        'low_name': "LOW",
        'medium_name': "MEDIUM", 
        'high_name': "HIGH",
        '2k_name': "2K",
        '4k_name': "4K",
    },
    'zh': {
        # Simplified Chinese
        'no_py_files': "在目录 {code_dir} 中没有找到 .py 文件",
        'found_files': "找到 {count} 个 Manim 代码文件",
        'sample_files': "示例文件: {files}",
        'task_interval': "任务启动间隔: {interval} 秒",
        'starting_test': "开始 {description} 测试",
        'intelligent_resource': "已启用智能资源管理策略",
        'reached_max_duration': "达到最大测试时间 {duration} 秒，停止测试",
        'waiting_resources': "等待资源释放...",
        'starting_task': "[{quality}] 启动任务 #{task_id}: {filename}",
        'waiting_completion': "[{quality}] 等待所有渲染任务完成...",
        'tasks_remaining': "[{quality}] 还有 {remaining} 个任务未完成...",
        'test_completed': "{quality} 测试完成:",
        'total_tasks': "  总任务数: {count}",
        'successful_tasks': "  成功任务: {count}",
        'max_concurrent': "  最大并发: {count}",
        'avg_render_duration': "  平均渲染耗时: {duration:.2f}s",
        'avg_video_duration': "  平均视频时长: {duration:.2f}s",
        'avg_file_size': "  平均文件大小: {size:.2f}MB",
        'success_rate': "  成功率: {rate:.2%}",
        'testing_qualities': "测试质量级别: {qualities}",
        'preparing_test': "准备 {description} 测试...",
        'waiting_recovery': "等待系统资源恢复 (30秒)...",
        'countdown_resources': "倒计时 {seconds} 秒... 当前资源: CPU={cpu:.1f}%, 内存={memory:.1f}%",
        'all_tests_failed': "所有测试都失败了！",
        'test_interrupted': "测试被用户中断",
        'critical_error': "测试过程中发生严重错误: {error}",
        
        'report_title': "MANIQ - Manim 质量压力测试报告",
        'test_time': "测试时间: {time}",
        'test_files': "测试文件: {count}",
        'code_directory': "代码目录: {path}",
        'task_launch_interval': "任务启动间隔: {interval} 秒",
        'system_information': "系统信息:",
        'cpu_cores': "  CPU 核心数: {physical} (逻辑核心: {logical})",
        'total_memory': "  总内存: {memory:.2f} GB",
        'available_disk': "  可用磁盘空间: {disk:.2f} GB",
        'test_results': "{description} 测试结果",
        'max_concurrent_tasks': "最大并发任务数: {count}",
        'total_tasks_started': "总启动任务数: {count}",
        'successful_tasks_report': "成功任务数: {count}",
        'failed_tasks': "失败任务数: {count}",
        'success_rate_report': "成功率: {rate:.2%}",
        'render_duration_stats': "渲染任务耗时统计 (秒):",
        'average': "  平均值: {value:.2f}",
        'minimum': "  最小值: {value:.2f}",
        'maximum': "  最大值: {value:.2f}",
        'median': "  中位数: {value:.2f}",
        'std_dev': "  标准差: {value:.2f}",
        'video_duration_stats': "渲染视频时长统计 (秒):",
        'file_size_stats': "渲染视频文件大小统计 (MB):",
        'resource_usage_stats': "系统资源使用统计:",
        'cpu_usage_stats': "  CPU 使用率 - 平均: {avg:.1f}%, 峰值: {peak:.1f}%",
        'memory_usage_stats': "  内存使用率 - 平均: {avg:.1f}%, 峰值: {peak:.1f}%",
        'avg_cpu_per_task': "每个任务平均CPU使用率: {usage:.1f}%",
        'detailed_logs_saved': "详细任务日志保存在: {path}",
        'performance_comparison': "性能对比总结",
        'quality': "质量级别",
        'max_concurrent_col': "最大并发",
        'success_rate_col': "成功率",
        'avg_render_time_col': "平均渲染耗时",
        'avg_video_duration_col': "平均视频时长",
        'avg_file_size_col': "平均文件大小(MB)",
        'resource_strategy': "智能资源管理策略:",
        'strategy_point1': "• 基于历史CPU使用率动态调整并发",
        'strategy_point2': "• 当剩余CPU资源 < (平均CPU使用率 + 5%) 时暂停启动新任务",
        'strategy_point3': "• CPU或内存使用率 > 90% 时自动暂停",
        'strategy_point4': "• 防止服务器因资源耗尽而崩溃",
        'recommendations': "建议:",
        'recommend_best_quality': "• 基于最大并发能力，推荐使用 {quality} 质量级别",
        'recommend_file_size': "• {high_quality} 质量视频平均文件大小是 {low_quality} 的 {ratio:.1f} 倍",
        
        'low_desc': "低质量 (480p)",
        'medium_desc': "中质量 (720p)",
        'high_desc': "高质量 (1080p)",
        '2k_desc': "2K质量 (1440p)",
        '4k_desc': "4K质量 (2160p)",
        
        'low_name': "低质量",
        'medium_name': "中质量",
        'high_name': "高质量",
        '2k_name': "2K",
        '4k_name': "4K",
    },
    'zh_tw': {
        # Traditional Chinese
        'no_py_files': "在目錄 {code_dir} 中沒有找到 .py 檔案",
        'found_files': "找到 {count} 個 Manim 程式碼檔案",
        'sample_files': "範例檔案: {files}",
        'task_interval': "任務啟動間隔: {interval} 秒",
        'starting_test': "開始 {description} 測試",
        'intelligent_resource': "已啟用智慧資源管理策略",
        'reached_max_duration': "達到最大測試時間 {duration} 秒，停止測試",
        'waiting_resources': "等待資源釋放...",
        'starting_task': "[{quality}] 啟動任務 #{task_id}: {filename}",
        'waiting_completion': "[{quality}] 等待所有渲染任務完成...",
        'tasks_remaining': "[{quality}] 還有 {remaining} 個任務未完成...",
        'test_completed': "{quality} 測試完成:",
        'total_tasks': "  總任務數: {count}",
        'successful_tasks': "  成功任務: {count}",
        'max_concurrent': "  最大並行: {count}",
        'avg_render_duration': "  平均渲染耗時: {duration:.2f}s",
        'avg_video_duration': "  平均影片時長: {duration:.2f}s",
        'avg_file_size': "  平均檔案大小: {size:.2f}MB",
        'success_rate': "  成功率: {rate:.2%}",
        'testing_qualities': "測試品質等級: {qualities}",
        'preparing_test': "準備 {description} 測試...",
        'waiting_recovery': "等待系統資源恢復 (30秒)...",
        'countdown_resources': "倒數 {seconds} 秒... 目前資源: CPU={cpu:.1f}%, 記憶體={memory:.1f}%",
        'all_tests_failed': "所有測試都失敗了！",
        'test_interrupted': "測試被使用者中斷",
        'critical_error': "測試過程中發生嚴重錯誤: {error}",
        
        'report_title': "MANIQ - Manim 品質壓力測試報告",
        'test_time': "測試時間: {time}",
        'test_files': "測試檔案: {count}",
        'code_directory': "程式碼目錄: {path}",
        'task_launch_interval': "任務啟動間隔: {interval} 秒",
        'system_information': "系統資訊:",
        'cpu_cores': "  CPU 核心數: {physical} (邏輯核心: {logical})",
        'total_memory': "  總記憶體: {memory:.2f} GB",
        'available_disk': "  可用磁碟空間: {disk:.2f} GB",
        'test_results': "{description} 測試結果",
        'max_concurrent_tasks': "最大並行任務數: {count}",
        'total_tasks_started': "總啟動任務數: {count}",
        'successful_tasks_report': "成功任務數: {count}",
        'failed_tasks': "失敗任務數: {count}",
        'success_rate_report': "成功率: {rate:.2%}",
        'render_duration_stats': "渲染任務耗時統計 (秒):",
        'average': "  平均值: {value:.2f}",
        'minimum': "  最小值: {value:.2f}",
        'maximum': "  最大值: {value:.2f}",
        'median': "  中位數: {value:.2f}",
        'std_dev': "  標準差: {value:.2f}",
        'video_duration_stats': "渲染影片時長統計 (秒):",
        'file_size_stats': "渲染影片檔案大小統計 (MB):",
        'resource_usage_stats': "系統資源使用統計:",
        'cpu_usage_stats': "  CPU 使用率 - 平均: {avg:.1f}%, 峰值: {peak:.1f}%",
        'memory_usage_stats': "  記憶體使用率 - 平均: {avg:.1f}%, 峰值: {peak:.1f}%",
        'avg_cpu_per_task': "每個任務平均CPU使用率: {usage:.1f}%",
        'detailed_logs_saved': "詳細任務日誌保存在: {path}",
        'performance_comparison': "效能對比總結",
        'quality': "品質等級",
        'max_concurrent_col': "最大並行",
        'success_rate_col': "成功率",
        'avg_render_time_col': "平均渲染耗時",
        'avg_video_duration_col': "平均影片時長",
        'avg_file_size_col': "平均檔案大小(MB)",
        'resource_strategy': "智慧資源管理策略:",
        'strategy_point1': "• 基於歷史CPU使用率動態調整並行",
        'strategy_point2': "• 當剩餘CPU資源 < (平均CPU使用率 + 5%) 時暫停啟動新任務",
        'strategy_point3': "• CPU或記憶體使用率 > 90% 時自動暫停",
        'strategy_point4': "• 防止伺服器因資源耗盡而崩潰",
        'recommendations': "建議:",
        'recommend_best_quality': "• 基於最大並行能力，推薦使用 {quality} 品質等級",
        'recommend_file_size': "• {high_quality} 品質影片平均檔案大小是 {low_quality} 的 {ratio:.1f} 倍",
        
        'low_desc': "低品質 (480p)",
        'medium_desc': "中品質 (720p)",
        'high_desc': "高品質 (1080p)",
        '2k_desc': "2K品質 (1440p)",
        '4k_desc': "4K品質 (2160p)",
        
        'low_name': "低品質",
        'medium_name': "中品質",
        'high_name': "高品質",
        '2k_name': "2K",
        '4k_name': "4K",
    },
    'ko': {
        # Korean
        'no_py_files': "디렉토리 {code_dir}에서 .py 파일을 찾을 수 없습니다",
        'found_files': "Manim 코드 파일 {count}개를 찾았습니다",
        'sample_files': "샘플 파일: {files}",
        'task_interval': "작업 시작 간격: {interval}초",
        'starting_test': "{description} 테스트 시작",
        'intelligent_resource': "지능형 리소스 관리 전략 활성화됨",
        'reached_max_duration': "최대 테스트 시간 {duration}초에 도달하여 테스트 중지",
        'waiting_resources': "리소스 해제 대기 중...",
        'starting_task': "[{quality}] 작업 #{task_id} 시작: {filename}",
        'waiting_completion': "[{quality}] 모든 렌더 작업 완료 대기 중...",
        'tasks_remaining': "[{quality}] {remaining}개의 작업이 남았습니다...",
        'test_completed': "{quality} 테스트 완료:",
        'total_tasks': "  총 작업 수: {count}",
        'successful_tasks': "  성공한 작업: {count}",
        'max_concurrent': "  최대 동시 작업: {count}",
        'avg_render_duration': "  평균 렌더 시간: {duration:.2f}s",
        'avg_video_duration': "  평균 비디오 길이: {duration:.2f}s",
        'avg_file_size': "  평균 파일 크기: {size:.2f}MB",
        'success_rate': "  성공률: {rate:.2%}",
        'testing_qualities': "테스트 품질 수준: {qualities}",
        'preparing_test': "{description} 테스트 준비 중...",
        'waiting_recovery': "시스템 리소스 복구 대기 중 (30초)...",
        'countdown_resources': "카운트다운 {seconds}초... 현재 리소스: CPU={cpu:.1f}%, 메모리={memory:.1f}%",
        'all_tests_failed': "모든 테스트가 실패했습니다!",
        'test_interrupted': "사용자에 의해 테스트가 중단되었습니다",
        'critical_error': "테스트 중 심각한 오류 발생: {error}",
        
        'report_title': "MANIQ - Manim 품질 스트레스 테스트 보고서",
        'test_time': "테스트 시간: {time}",
        'test_files': "테스트 파일: {count}",
        'code_directory': "코드 디렉토리: {path}",
        'task_launch_interval': "작업 시작 간격: {interval}초",
        'system_information': "시스템 정보:",
        'cpu_cores': "  CPU 코어 수: {physical} (논리 코어: {logical})",
        'total_memory': "  총 메모리: {memory:.2f} GB",
        'available_disk': "  사용 가능한 디스크 공간: {disk:.2f} GB",
        'test_results': "{description} 테스트 결과",
        'max_concurrent_tasks': "최대 동시 작업 수: {count}",
        'total_tasks_started': "총 시작 작업 수: {count}",
        'successful_tasks_report': "성공한 작업 수: {count}",
        'failed_tasks': "실패한 작업 수: {count}",
        'success_rate_report': "성공률: {rate:.2%}",
        'render_duration_stats': "렌더 작업 시간 통계 (초):",
        'average': "  평균: {value:.2f}",
        'minimum': "  최소: {value:.2f}",
        'maximum': "  최대: {value:.2f}",
        'median': "  중앙값: {value:.2f}",
        'std_dev': "  표준 편차: {value:.2f}",
        'video_duration_stats': "렌더된 비디오 길이 통계 (초):",
        'file_size_stats': "렌더된 비디오 파일 크기 통계 (MB):",
        'resource_usage_stats': "시스템 리소스 사용 통계:",
        'cpu_usage_stats': "  CPU 사용률 - 평균: {avg:.1f}%, 최고: {peak:.1f}%",
        'memory_usage_stats': "  메모리 사용률 - 평균: {avg:.1f}%, 최고: {peak:.1f}%",
        'avg_cpu_per_task': "작업당 평균 CPU 사용률: {usage:.1f}%",
        'detailed_logs_saved': "상세 작업 로그 저장 위치: {path}",
        'performance_comparison': "성능 비교 요약",
        'quality': "품질",
        'max_concurrent_col': "최대 동시 작업",
        'success_rate_col': "성공률",
        'avg_render_time_col': "평균 렌더 시간",
        'avg_video_duration_col': "평균 비디오 길이",
        'avg_file_size_col': "평균 파일 크기(MB)",
        'resource_strategy': "지능형 리소스 관리 전략:",
        'strategy_point1': "• 과거 CPU 사용률을 기반으로 동시 작업을 동적으로 조정",
        'strategy_point2': "• 남은 CPU < (평균 CPU 사용률 + 5%)일 때 새 작업 일시 중지",
        'strategy_point3': "• CPU 또는 메모리 사용률이 90%를 초과하면 자동 일시 중지",
        'strategy_point4': "• 리소스 고갈로 인한 서버 충돌 방지",
        'recommendations': "권장 사항:",
        'recommend_best_quality': "• 최대 동시 작업 기준으로 {quality} 품질 사용 권장",
        'recommend_file_size': "• {high_quality} 품질 비디오 파일 크기는 {low_quality}의 {ratio:.1f}배입니다",
        
        'low_desc': "저품질 (480p)",
        'medium_desc': "중품질 (720p)",
        'high_desc': "고품질 (1080p)",
        '2k_desc': "2K 품질 (1440p)",
        '4k_desc': "4K 품질 (2160p)",
        
        'low_name': "저품질",
        'medium_name': "중품질",
        'high_name': "고품질",
        '2k_name': "2K",
        '4k_name': "4K",
    },
    'ja': {
        # Japanese
        'no_py_files': "ディレクトリ {code_dir} に .py ファイルが見つかりません",
        'found_files': "Manim コードファイルを {count} 個見つけました",
        'sample_files': "サンプルファイル: {files}",
        'task_interval': "タスク起動間隔: {interval} 秒",
        'starting_test': "{description} テストを開始",
        'intelligent_resource': "インテリジェントリソース管理戦略を有効化",
        'reached_max_duration': "最大テスト時間 {duration} 秒に到達したため、テストを停止",
        'waiting_resources': "リソース解放を待機中...",
        'starting_task': "[{quality}] タスク #{task_id} を開始: {filename}",
        'waiting_completion': "[{quality}] すべてのレンダリングタスクの完了を待機中...",
        'tasks_remaining': "[{quality}] {remaining} 個のタスクが残っています...",
        'test_completed': "{quality} テスト完了:",
        'total_tasks': "  合計タスク数: {count}",
        'successful_tasks': "  成功したタスク: {count}",
        'max_concurrent': "  最大同時実行数: {count}",
        'avg_render_duration': "  平均レンダリング時間: {duration:.2f}s",
        'avg_video_duration': "  平均ビデオ時間: {duration:.2f}s",
        'avg_file_size': "  平均ファイルサイズ: {size:.2f}MB",
        'success_rate': "  成功率: {rate:.2%}",
        'testing_qualities': "テスト品質レベル: {qualities}",
        'preparing_test': "{description} テストを準備中...",
        'waiting_recovery': "システムリソースの回復を待機中 (30秒)...",
        'countdown_resources': "カウントダウン {seconds} 秒... 現在のリソース: CPU={cpu:.1f}%, メモリ={memory:.1f}%",
        'all_tests_failed': "すべてのテストが失敗しました！",
        'test_interrupted': "ユーザーによってテストが中断されました",
        'critical_error': "テスト中に重大なエラーが発生しました: {error}",
        
        'report_title': "MANIQ - Manim 品質ストレステストレポート",
        'test_time': "テスト時間: {time}",
        'test_files': "テストファイル: {count}",
        'code_directory': "コードディレクトリ: {path}",
        'task_launch_interval': "タスク起動間隔: {interval} 秒",
        'system_information': "システム情報:",
        'cpu_cores': "  CPUコア数: {physical} (論理コア: {logical})",
        'total_memory': "  合計メモリ: {memory:.2f} GB",
        'available_disk': "  利用可能なディスク容量: {disk:.2f} GB",
        'test_results': "{description} テスト結果",
        'max_concurrent_tasks': "最大同時タスク数: {count}",
        'total_tasks_started': "合計開始タスク数: {count}",
        'successful_tasks_report': "成功したタスク数: {count}",
        'failed_tasks': "失敗したタスク数: {count}",
        'success_rate_report': "成功率: {rate:.2%}",
        'render_duration_stats': "レンダリングタスク時間統計 (秒):",
        'average': "  平均: {value:.2f}",
        'minimum': "  最小: {value:.2f}",
        'maximum': "  最大: {value:.2f}",
        'median': "  中央値: {value:.2f}",
        'std_dev': "  標準偏差: {value:.2f}",
        'video_duration_stats': "レンダリングされたビデオ時間統計 (秒):",
        'file_size_stats': "レンダリングされたビデオファイルサイズ統計 (MB):",
        'resource_usage_stats': "システムリソース使用統計:",
        'cpu_usage_stats': "  CPU使用率 - 平均: {avg:.1f}%, ピーク: {peak:.1f}%",
        'memory_usage_stats': "  メモリ使用率 - 平均: {avg:.1f}%, ピーク: {peak:.1f}%",
        'avg_cpu_per_task': "タスクあたりの平均CPU使用率: {usage:.1f}%",
        'detailed_logs_saved': "詳細タスブログ保存先: {path}",
        'performance_comparison': "パフォーマンス比較サマリー",
        'quality': "品質",
        'max_concurrent_col': "最大同時実行",
        'success_rate_col': "成功率",
        'avg_render_time_col': "平均レンダリング時間",
        'avg_video_duration_col': "平均ビデオ時間",
        'avg_file_size_col': "平均ファイルサイズ(MB)",
        'resource_strategy': "インテリジェントリソース管理戦略:",
        'strategy_point1': "• 履歴CPU使用率に基づいて同時実行を動的に調整",
        'strategy_point2': "• 残りCPU < (平均CPU使用率 + 5%) の場合、新規タスクを一時停止",
        'strategy_point3': "• CPUまたはメモリ使用率が90%を超えると自動一時停止",
        'strategy_point4': "• リソース枯渇によるサーバークラッシュを防止",
        'recommendations': "推奨事項:",
        'recommend_best_quality': "• 最大同時実行能力に基づき、{quality} 品質の使用を推奨",
        'recommend_file_size': "• {high_quality} 品質ビデオファイルサイズは {low_quality} の {ratio:.1f}倍です",
        
        'low_desc': "低品質 (480p)",
        'medium_desc': "中品質 (720p)",
        'high_desc': "高品質 (1080p)",
        '2k_desc': "2K品質 (1440p)",
        '4k_desc': "4K品質 (2160p)",
        
        'low_name': "低品質",
        'medium_name': "中品質",
        'high_name': "高品質",
        '2k_name': "2K",
        '4k_name': "4K",
    },
    'de': {
        # German
        'no_py_files': "Keine .py-Dateien im Verzeichnis {code_dir} gefunden",
        'found_files': "{count} Manim-Code-Dateien gefunden",
        'sample_files': "Beispieldateien: {files}",
        'task_interval': "Aufgabenstartintervall: {interval} Sekunden",
        'starting_test': "{description}-Test wird gestartet",
        'intelligent_resource': "Intelligente Ressourcenverwaltungsstrategie aktiviert",
        'reached_max_duration': "Maximale Testdauer von {duration} Sekunden erreicht, Test wird gestoppt",
        'waiting_resources': "Warten auf Ressourcenfreigabe...",
        'starting_task': "[{quality}] Aufgabe #{task_id} wird gestartet: {filename}",
        'waiting_completion': "[{quality}] Warten auf Abschluss aller Render-Aufgaben...",
        'tasks_remaining': "[{quality}] {remaining} Aufgaben verbleiben...",
        'test_completed': "{quality}-Test abgeschlossen:",
        'total_tasks': "  Gesamte Aufgaben: {count}",
        'successful_tasks': "  Erfolgreiche Aufgaben: {count}",
        'max_concurrent': "  Maximale Parallelität: {count}",
        'avg_render_duration': "  Durchschn. Renderdauer: {duration:.2f}s",
        'avg_video_duration': "  Durchschn. Videolänge: {duration:.2f}s",
        'avg_file_size': "  Durchschn. Dateigröße: {size:.2f}MB",
        'success_rate': "  Erfolgsrate: {rate:.2%}",
        'testing_qualities': "Test-Qualitätsstufen: {qualities}",
        'preparing_test': "{description}-Test wird vorbereitet...",
        'waiting_recovery': "Warten auf Systemressourcenwiederherstellung (30 Sekunden)...",
        'countdown_resources': "Countdown {seconds} Sekunden... Aktuelle Ressourcen: CPU={cpu:.1f}%, Speicher={memory:.1f}%",
        'all_tests_failed': "Alle Tests sind fehlgeschlagen!",
        'test_interrupted': "Test wurde vom Benutzer unterbrochen",
        'critical_error': "Schwerwiegender Fehler während des Tests: {error}",
        
        'report_title': "MANIQ - Manim-Qualitäts-Stresstestbericht",
        'test_time': "Testzeit: {time}",
        'test_files': "Testdateien: {count}",
        'code_directory': "Code-Verzeichnis: {path}",
        'task_launch_interval': "Aufgabenstartintervall: {interval} Sekunden",
        'system_information': "Systeminformationen:",
        'cpu_cores': "  CPU-Kerne: {physical} (Logisch: {logical})",
        'total_memory': "  Gesamtspeicher: {memory:.2f} GB",
        'available_disk': "  Verfügbare Festplattenkapazität: {disk:.2f} GB",
        'test_results': "{description}-Testergebnisse",
        'max_concurrent_tasks': "Maximale parallele Aufgaben: {count}",
        'total_tasks_started': "Gesamt gestartete Aufgaben: {count}",
        'successful_tasks_report': "Erfolgreiche Aufgaben: {count}",
        'failed_tasks': "Fehlgeschlagene Aufgaben: {count}",
        'success_rate_report': "Erfolgsrate: {rate:.2%}",
        'render_duration_stats': "Render-Aufgaben-Dauerstatistik (Sekunden):",
        'average': "  Durchschnitt: {value:.2f}",
        'minimum': "  Minimum: {value:.2f}",
        'maximum': "  Maximum: {value:.2f}",
        'median': "  Median: {value:.2f}",
        'std_dev': "  Standardabweichung: {value:.2f}",
        'video_duration_stats': "Gerenderte Video-Längenstatistik (Sekunden):",
        'file_size_stats': "Gerenderte Video-Dateigrößenstatistik (MB):",
        'resource_usage_stats': "Systemressourcen-Nutzungsstatistik:",
        'cpu_usage_stats': "  CPU-Auslastung - Durchschn.: {avg:.1f}%, Spitze: {peak:.1f}%",
        'memory_usage_stats': "  Speicherauslastung - Durchschn.: {avg:.1f}%, Spitze: {peak:.1f}%",
        'avg_cpu_per_task': "Durchschn. CPU-Auslastung pro Aufgabe: {usage:.1f}%",
        'detailed_logs_saved': "Detaillierte Aufgabenprotokolle gespeichert in: {path}",
        'performance_comparison': "Leistungsvergleichsübersicht",
        'quality': "Qualität",
        'max_concurrent_col': "Max. Parallelität",
        'success_rate_col': "Erfolgsrate",
        'avg_render_time_col': "Durchschn. Renderzeit",
        'avg_video_duration_col': "Durchschn. Videolänge",
        'avg_file_size_col': "Durchschn. Dateigröße(MB)",
        'resource_strategy': "Intelligente Ressourcenverwaltungsstrategie:",
        'strategy_point1': "• Passt Parallelität dynamisch basierend auf historischer CPU-Auslastung an",
        'strategy_point2': "• Pausiert neue Aufgaben, wenn verbleibende CPU < (durchschn. CPU-Auslastung + 5%)",
        'strategy_point3': "• Pausiert automatisch bei CPU- oder Speicherauslastung > 90%",
        'strategy_point4': "• Verhindert Serverabstürze durch Ressourcenerschöpfung",
        'recommendations': "Empfehlungen:",
        'recommend_best_quality': "• Basierend auf maximaler Parallelität wird {quality}-Qualität empfohlen",
        'recommend_file_size': "• {high_quality}-Qualitäts-Videodateigröße ist {ratio:.1f}x größer als {low_quality}",
        
        'low_desc': "Niedrige Qualität (480p)",
        'medium_desc': "Mittlere Qualität (720p)",
        'high_desc': "Hohe Qualität (1080p)",
        '2k_desc': "2K-Qualität (1440p)",
        '4k_desc': "4K-Qualität (2160p)",
        
        'low_name': "NIEDRIG",
        'medium_name': "MITTEL",
        'high_name': "HOCH",
        '2k_name': "2K",
        '4k_name': "4K",
    },
    'fr': {
        # French
        'no_py_files': "Aucun fichier .py trouvé dans le répertoire {code_dir}",
        'found_files': "{count} fichiers de code Manim trouvés",
        'sample_files': "Fichiers exemples: {files}",
        'task_interval': "Intervalle de lancement des tâches: {interval} secondes",
        'starting_test': "Démarrage du test {description}",
        'intelligent_resource': "Stratégie de gestion intelligente des ressources activée",
        'reached_max_duration': "Durée maximale de test de {duration} secondes atteinte, arrêt du test",
        'waiting_resources': "En attente de libération des ressources...",
        'starting_task': "[{quality}] Démarrage de la tâche #{task_id}: {filename}",
        'waiting_completion': "[{quality}] En attente de la fin de toutes les tâches de rendu...",
        'tasks_remaining': "[{quality}] {remaining} tâches restantes...",
        'test_completed': "Test {quality} terminé:",
        'total_tasks': "  Tâches totales: {count}",
        'successful_tasks': "  Tâches réussies: {count}",
        'max_concurrent': "  Concurrence maximale: {count}",
        'avg_render_duration': "  Durée moyenne de rendu: {duration:.2f}s",
        'avg_video_duration': "  Durée moyenne vidéo: {duration:.2f}s",
        'avg_file_size': "  Taille moyenne du fichier: {size:.2f}MB",
        'success_rate': "  Taux de réussite: {rate:.2%}",
        'testing_qualities': "Niveaux de qualité testés: {qualities}",
        'preparing_test': "Préparation du test {description}...",
        'waiting_recovery': "En attente de la récupération des ressources système (30 secondes)...",
        'countdown_resources': "Compte à rebours {seconds} secondes... Ressources actuelles: CPU={cpu:.1f}%, Mémoire={memory:.1f}%",
        'all_tests_failed': "Tous les tests ont échoué !",
        'test_interrupted': "Test interrompu par l'utilisateur",
        'critical_error': "Erreur critique pendant le test: {error}",
        
        'report_title': "MANIQ - Rapport de test de stress qualité Manim",
        'test_time': "Heure du test: {time}",
        'test_files': "Fichiers de test: {count}",
        'code_directory': "Répertoire du code: {path}",
        'task_launch_interval': "Intervalle de lancement des tâches: {interval} secondes",
        'system_information': "Informations système:",
        'cpu_cores': "  Cœurs CPU: {physical} (Logiques: {logical})",
        'total_memory': "  Mémoire totale: {memory:.2f} Go",
        'available_disk': "  Espace disque disponible: {disk:.2f} Go",
        'test_results': "Résultats du test {description}",
        'max_concurrent_tasks': "Tâches simultanées maximales: {count}",
        'total_tasks_started': "Tâches totales lancées: {count}",
        'successful_tasks_report': "Tâches réussies: {count}",
        'failed_tasks': "Tâches échouées: {count}",
        'success_rate_report': "Taux de réussite: {rate:.2%}",
        'render_duration_stats': "Statistiques de durée des tâches de rendu (secondes):",
        'average': "  Moyenne: {value:.2f}",
        'minimum': "  Minimum: {value:.2f}",
        'maximum': "  Maximum: {value:.2f}",
        'median': "  Médiane: {value:.2f}",
        'std_dev': "  Écart-type: {value:.2f}",
        'video_duration_stats': "Statistiques de durée vidéo rendue (secondes):",
        'file_size_stats': "Statistiques de taille des fichiers vidéo rendus (Mo):",
        'resource_usage_stats': "Statistiques d'utilisation des ressources système:",
        'cpu_usage_stats': "  Utilisation CPU - Moyenne: {avg:.1f}%, Pic: {peak:.1f}%",
        'memory_usage_stats': "  Utilisation mémoire - Moyenne: {avg:.1f}%, Pic: {peak:.1f}%",
        'avg_cpu_per_task': "Utilisation CPU moyenne par tâche: {usage:.1f}%",
        'detailed_logs_saved': "Journaux détaillés des tâches enregistrés dans: {path}",
        'performance_comparison': "Résumé de comparaison des performances",
        'quality': "Qualité",
        'max_concurrent_col': "Concurrence Max",
        'success_rate_col': "Taux de réussite",
        'avg_render_time_col': "Temps de rendu moyen",
        'avg_video_duration_col': "Durée vidéo moyenne",
        'avg_file_size_col': "Taille fichier moyenne(Mo)",
        'resource_strategy': "Stratégie de gestion intelligente des ressources:",
        'strategy_point1': "• Ajuste dynamiquement la concurrence basée sur l'utilisation historique du CPU",
        'strategy_point2': "• Met en pause les nouvelles tâches quand CPU restant < (utilisation CPU moyenne + 5%)",
        'strategy_point3': "• Met automatiquement en pause quand utilisation CPU ou mémoire > 90%",
        'strategy_point4': "• Empêche les plantages du serveur dus à l'épuisement des ressources",
        'recommendations': "Recommandations:",
        'recommend_best_quality': "• Basé sur la concurrence maximale, recommande d'utiliser la qualité {quality}",
        'recommend_file_size': "• La taille du fichier vidéo en qualité {high_quality} est {ratio:.1f}x plus grande qu'en {low_quality}",
        
        'low_desc': "Basse qualité (480p)",
        'medium_desc': "Qualité moyenne (720p)",
        'high_desc': "Haute qualité (1080p)",
        '2k_desc': "Qualité 2K (1440p)",
        '4k_desc': "Qualité 4K (2160p)",
        
        'low_name': "BASSE",
        'medium_name': "MOYENNE",
        'high_name': "HAUTE",
        '2k_name': "2K",
        '4k_name': "4K",
    },
    'es': {
        # Spanish
        'no_py_files': "No se encontraron archivos .py en el directorio {code_dir}",
        'found_files': "Se encontraron {count} archivos de código Manim",
        'sample_files': "Archivos de ejemplo: {files}",
        'task_interval': "Intervalo de inicio de tareas: {interval} segundos",
        'starting_test': "Iniciando prueba {description}",
        'intelligent_resource': "Estrategia de gestión inteligente de recursos activada",
        'reached_max_duration': "Duración máxima de prueba de {duration} segundos alcanzada, deteniendo prueba",
        'waiting_resources': "Esperando liberación de recursos...",
        'starting_task': "[{quality}] Iniciando tarea #{task_id}: {filename}",
        'waiting_completion': "[{quality}] Esperando a que todas las tareas de renderizado se completen...",
        'tasks_remaining': "[{quality}] {remaining} tareas restantes...",
        'test_completed': "Prueba {quality} completada:",
        'total_tasks': "  Tareas totales: {count}",
        'successful_tasks': "  Tareas exitosas: {count}",
        'max_concurrent': "  Concurrencia máxima: {count}",
        'avg_render_duration': "  Duración promedio de renderizado: {duration:.2f}s",
        'avg_video_duration': "  Duración promedio del video: {duration:.2f}s",
        'avg_file_size': "  Tamaño promedio del archivo: {size:.2f}MB",
        'success_rate': "  Tasa de éxito: {rate:.2%}",
        'testing_qualities': "Niveles de calidad de prueba: {qualities}",
        'preparing_test': "Preparando prueba {description}...",
        'waiting_recovery': "Esperando recuperación de recursos del sistema (30 segundos)...",
        'countdown_resources': "Cuenta regresiva {seconds} segundos... Recursos actuales: CPU={cpu:.1f}%, Memoria={memory:.1f}%",
        'all_tests_failed': "¡Todas las pruebas fallaron!",
        'test_interrupted': "Prueba interrumpida por el usuario",
        'critical_error': "Error crítico durante la prueba: {error}",
        
        'report_title': "MANIQ - Informe de prueba de estrés de calidad Manim",
        'test_time': "Hora de la prueba: {time}",
        'test_files': "Archivos de prueba: {count}",
        'code_directory': "Directorio de código: {path}",
        'task_launch_interval': "Intervalo de inicio de tareas: {interval} segundos",
        'system_information': "Información del sistema:",
        'cpu_cores': "  Núcleos CPU: {physical} (Lógicos: {logical})",
        'total_memory': "  Memoria total: {memory:.2f} GB",
        'available_disk': "  Espacio en disco disponible: {disk:.2f} GB",
        'test_results': "Resultados de la prueba {description}",
        'max_concurrent_tasks': "Tareas concurrentes máximas: {count}",
        'total_tasks_started': "Tareas totales iniciadas: {count}",
        'successful_tasks_report': "Tareas exitosas: {count}",
        'failed_tasks': "Tareas fallidas: {count}",
        'success_rate_report': "Tasa de éxito: {rate:.2%}",
        'render_duration_stats': "Estadísticas de duración de tareas de renderizado (segundos):",
        'average': "  Promedio: {value:.2f}",
        'minimum': "  Mínimo: {value:.2f}",
        'maximum': "  Máximo: {value:.2f}",
        'median': "  Mediana: {value:.2f}",
        'std_dev': "  Desviación estándar: {value:.2f}",
        'video_duration_stats': "Estadísticas de duración de video renderizado (segundos):",
        'file_size_stats': "Estadísticas de tamaño de archivo de video renderizado (MB):",
        'resource_usage_stats': "Estadísticas de uso de recursos del sistema:",
        'cpu_usage_stats': "  Uso de CPU - Promedio: {avg:.1f}%, Pico: {peak:.1f}%",
        'memory_usage_stats': "  Uso de memoria - Promedio: {avg:.1f}%, Pico: {peak:.1f}%",
        'avg_cpu_per_task': "Uso promedio de CPU por tarea: {usage:.1f}%",
        'detailed_logs_saved': "Registros detallados de tareas guardados en: {path}",
        'performance_comparison': "Resumen de comparación de rendimiento",
        'quality': "Calidad",
        'max_concurrent_col': "Concurrencia Máx",
        'success_rate_col': "Tasa de éxito",
        'avg_render_time_col': "Tiempo de renderizado promedio",
        'avg_video_duration_col': "Duración de video promedio",
        'avg_file_size_col': "Tamaño de archivo promedio(MB)",
        'resource_strategy': "Estrategia de gestión inteligente de recursos:",
        'strategy_point1': "• Ajusta dinámicamente la concurrencia basada en el uso histórico de CPU",
        'strategy_point2': "• Pausa nuevas tareas cuando CPU restante < (uso promedio de CPU + 5%)",
        'strategy_point3': "• Pausa automáticamente cuando uso de CPU o memoria > 90%",
        'strategy_point4': "• Previene bloqueos del servidor debido al agotamiento de recursos",
        'recommendations': "Recomendaciones:",
        'recommend_best_quality': "• Basado en concurrencia máxima, recomienda usar calidad {quality}",
        'recommend_file_size': "• El tamaño del archivo de video en calidad {high_quality} es {ratio:.1f}x mayor que en {low_quality}",
        
        'low_desc': "Baja calidad (480p)",
        'medium_desc': "Calidad media (720p)",
        'high_desc': "Alta calidad (1080p)",
        '2k_desc': "Calidad 2K (1440p)",
        '4k_desc': "Calidad 4K (2160p)",
        
        'low_name': "BAJA",
        'medium_name': "MEDIA",
        'high_name': "ALTA",
        '2k_name': "2K",
        '4k_name': "4K",
    },
    'ru': {
        # Russian
        'no_py_files': "В директории {code_dir} не найдено файлов .py",
        'found_files': "Найдено {count} файлов кода Manim",
        'sample_files': "Примеры файлов: {files}",
        'task_interval': "Интервал запуска задач: {interval} секунд",
        'starting_test': "Запуск теста {description}",
        'intelligent_resource': "Стратегия интеллектуального управления ресурсами включена",
        'reached_max_duration': "Достигнута максимальная продолжительность теста {duration} секунд, остановка теста",
        'waiting_resources': "Ожидание освобождения ресурсов...",
        'starting_task': "[{quality}] Запуск задачи #{task_id}: {filename}",
        'waiting_completion': "[{quality}] Ожидание завершения всех задач рендеринга...",
        'tasks_remaining': "[{quality}] Осталось {remaining} задач...",
        'test_completed': "Тест {quality} завершен:",
        'total_tasks': "  Всего задач: {count}",
        'successful_tasks': "  Успешных задач: {count}",
        'max_concurrent': "  Максимальная параллельность: {count}",
        'avg_render_duration': "  Средняя длительность рендеринга: {duration:.2f}с",
        'avg_video_duration': "  Средняя длительность видео: {duration:.2f}с",
        'avg_file_size': "  Средний размер файла: {size:.2f}МБ",
        'success_rate': "  Процент успеха: {rate:.2%}",
        'testing_qualities': "Тестируемые уровни качества: {qualities}",
        'preparing_test': "Подготовка теста {description}...",
        'waiting_recovery': "Ожидание восстановления системных ресурсов (30 секунд)...",
        'countdown_resources': "Обратный отсчет {seconds} секунд... Текущие ресурсы: CPU={cpu:.1f}%, Память={memory:.1f}%",
        'all_tests_failed': "Все тесты завершились неудачно!",
        'test_interrupted': "Тест прерван пользователем",
        'critical_error': "Критическая ошибка во время теста: {error}",
        
        'report_title': "MANIQ - Отчет о стресс-тестировании качества Manim",
        'test_time': "Время теста: {time}",
        'test_files': "Тестовые файлы: {count}",
        'code_directory': "Директория кода: {path}",
        'task_launch_interval': "Интервал запуска задач: {interval} секунд",
        'system_information': "Информация о системе:",
        'cpu_cores': "  Ядра CPU: {physical} (Логические: {logical})",
        'total_memory': "  Общая память: {memory:.2f} ГБ",
        'available_disk': "  Доступное место на диске: {disk:.2f} ГБ",
        'test_results': "Результаты теста {description}",
        'max_concurrent_tasks': "Максимальное количество параллельных задач: {count}",
        'total_tasks_started': "Всего запущено задач: {count}",
        'successful_tasks_report': "Успешных задач: {count}",
        'failed_tasks': "Неудачных задач: {count}",
        'success_rate_report': "Процент успеха: {rate:.2%}",
        'render_duration_stats': "Статистика длительности задач рендеринга (секунды):",
        'average': "  Среднее: {value:.2f}",
        'minimum': "  Минимум: {value:.2f}",
        'maximum': "  Максимум: {value:.2f}",
        'median': "  Медиана: {value:.2f}",
        'std_dev': "  Стандартное отклонение: {value:.2f}",
        'video_duration_stats': "Статистика длительности отрендеренного видео (секунды):",
        'file_size_stats': "Статистика размера файлов отрендеренного видео (МБ):",
        'resource_usage_stats': "Статистика использования системных ресурсов:",
        'cpu_usage_stats': "  Использование CPU - Среднее: {avg:.1f}%, Пик: {peak:.1f}%",
        'memory_usage_stats': "  Использование памяти - Среднее: {avg:.1f}%, Пик: {peak:.1f}%",
        'avg_cpu_per_task': "Среднее использование CPU на задачу: {usage:.1f}%",
        'detailed_logs_saved': "Подробные логи задач сохранены в: {path}",
        'performance_comparison': "Сводка сравнения производительности",
        'quality': "Качество",
        'max_concurrent_col': "Макс. параллельность",
        'success_rate_col': "Процент успеха",
        'avg_render_time_col': "Среднее время рендеринга",
        'avg_video_duration_col': "Средняя длительность видео",
        'avg_file_size_col': "Средний размер файла(МБ)",
        'resource_strategy': "Стратегия интеллектуального управления ресурсами:",
        'strategy_point1': "• Динамически регулирует параллельность на основе исторического использования CPU",
        'strategy_point2': "• Приостанавливает новые задачи, когда оставшийся CPU < (среднее использование CPU + 5%)",
        'strategy_point3': "• Автоматически приостанавливает при использовании CPU или памяти > 90%",
        'strategy_point4': "• Предотвращает сбои сервера из-за исчерпания ресурсов",
        'recommendations': "Рекомендации:",
        'recommend_best_quality': "• На основе максимальной параллельности рекомендуется использовать качество {quality}",
        'recommend_file_size': "• Размер файла видео в качестве {high_quality} в {ratio:.1f} раз больше, чем в {low_quality}",
        
        'low_desc': "Низкое качество (480p)",
        'medium_desc': "Среднее качество (720p)",
        'high_desc': "Высокое качество (1080p)",
        '2k_desc': "Качество 2K (1440p)",
        '4k_desc': "Качество 4K (2160p)",
        
        'low_name': "НИЗКОЕ",
        'medium_name': "СРЕДНЕЕ",
        'high_name': "ВЫСОКОЕ",
        '2k_name': "2K",
        '4k_name': "4K",
    }
}

class Translator:
    def __init__(self, language: str = 'en'):
        self.language = language
        self.translations = TRANSLATIONS.get(language, TRANSLATIONS['en'])
    
    def get(self, key: str, **kwargs) -> str:
        """Get translated string with formatting"""
        template = self.translations.get(key, key)
        try:
            return template.format(**kwargs)
        except KeyError:
            return template

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
                 log_output_dir: str = "manim_task_logs", launch_interval: float = 1.0,
                 language: str = 'en'):
        self.code_dir = Path(code_dir)
        self.output_dir = Path(output_dir)
        self.log_output_dir = Path(log_output_dir)
        self.launch_interval = launch_interval
        self.translator = Translator(language)
        self.output_dir.mkdir(exist_ok=True)
        self.log_output_dir.mkdir(exist_ok=True)
        
        self.manim_files = sorted(list(self.code_dir.glob("*.py")))
        if not self.manim_files:
            raise ValueError(self.translator.get('no_py_files', code_dir=code_dir))
        
        logger.info(self.translator.get('found_files', count=len(self.manim_files)))
        logger.info(self.translator.get('sample_files', files=[f.name for f in self.manim_files[:5]]))
        logger.info(self.translator.get('task_interval', interval=launch_interval))
        
        self.quality_configs = {
            'low': {'flag': '-ql', 'description': self.translator.translations.get('low_desc', 'Low quality (480p)')},
            'medium': {'flag': '-qm', 'description': self.translator.translations.get('medium_desc', 'Medium quality (720p)')},
            'high': {'flag': '-qh', 'description': self.translator.translations.get('high_desc', 'High quality (1080p)')},
            '2k': {'flag': '-qp', 'description': self.translator.translations.get('2k_desc', '2K quality (1440p)')},
            '4k': {'flag': '-qk', 'description': self.translator.translations.get('4k_desc', '4K quality (2160p)')}
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
            logger.info(self.translator.get('starting_task', quality=quality.upper(), task_id=task_id+1, filename=file_path.name))
            
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
                logger.warning(self.translator.get('starting_task', quality=quality.upper(), task_id=task_id+1, filename=f"Task timeout (1200 seconds)"))
            
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
            logger.warning(self.translator.get('waiting_resources'))
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
            logger.info(self.translator.get('waiting_resources'))
        
        return can_start
    
    def test_quality_level(self, quality: str, max_test_duration: int = 1800) -> QualityTestResult:
        """Test specified quality level with intelligent resource management"""
        logger.info(f"\n{'='*80}")
        logger.info(self.translator.get('starting_test', description=self.quality_configs[quality]['description']))
        logger.info(self.translator.get('task_interval', interval=self.launch_interval))
        logger.info(self.translator.get('intelligent_resource'))
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
                    logger.info(self.translator.get('reached_max_duration', duration=max_test_duration))
                    break
                
                if not self.can_start_new_task(self.completed_tasks, 
                                             self.get_system_resources()['cpu_percent']):
                    logger.info(self.translator.get('waiting_resources'))
                    time.sleep(5)
                    continue
                
                if task_id >= len(self.manim_files):
                    file_to_render = self.manim_files[task_id % len(self.manim_files)]
                else:
                    file_to_render = self.manim_files[task_id]
                
                logger.info(self.translator.get('starting_task', quality=quality.upper(), task_id=task_id+1, filename=file_to_render.name))
                
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
                        logger.info(self.translator.get('reached_max_duration', duration=max_test_duration))
                        break
                
                active_tasks = len([r for r in render_results if r.end_time == 0])
                if (current_time - last_task_start_time > max(120, self.launch_interval * 10) and 
                    active_tasks > 10):
                    logger.warning(self.translator.get('reached_max_duration', duration=max_test_duration))
                    break
            
            logger.info(self.translator.get('waiting_completion', quality=quality.upper()))
            wait_start = time.time()
            max_wait_time = 600
            while time.time() - wait_start < max_wait_time:
                completed_count = sum(1 for r in render_results if r.end_time > 0)
                if completed_count == len(render_results):
                    break
                remaining = len(render_results) - completed_count
                logger.info(self.translator.get('tasks_remaining', quality=quality.upper(), remaining=remaining))
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
            
            logger.info(self.translator.get('test_completed', quality=quality.upper()))
            logger.info(self.translator.get('total_tasks', count=result.total_tasks_started))
            logger.info(self.translator.get('successful_tasks', count=result.successful_tasks))
            logger.info(self.translator.get('max_concurrent', count=result.max_concurrent_tasks))
            logger.info(self.translator.get('avg_render_duration', duration=result.avg_duration))
            logger.info(self.translator.get('avg_video_duration', duration=result.avg_video_duration))
            logger.info(self.translator.get('avg_file_size', size=result.avg_file_size))
            logger.info(self.translator.get('success_rate', rate=result.success_rate))
            
            return result
            
        except KeyboardInterrupt:
            logger.info(self.translator.get('test_interrupted'))
            self.system_monitor_stop.set()
            monitor_thread.join(timeout=5)
            raise
        except Exception as e:
            logger.error(self.translator.get('critical_error', error=e))
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
        report_lines.append(self.translator.get('report_title'))
        report_lines.append("=" * 130)
        report_lines.append(self.translator.get('test_time', time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        report_lines.append(self.translator.get('test_files', count=len(self.manim_files)))
        report_lines.append(self.translator.get('code_directory', path=self.code_dir))
        report_lines.append(self.translator.get('task_launch_interval', interval=self.launch_interval))
        report_lines.append("")
        
        report_lines.append(self.translator.get('system_information'))
        report_lines.append(self.translator.get('cpu_cores', physical=psutil.cpu_count(), logical=psutil.cpu_count(logical=True)))
        report_lines.append(self.translator.get('total_memory', memory=psutil.virtual_memory().total / (1024**3)))
        report_lines.append(self.translator.get('available_disk', disk=psutil.disk_usage('/').free / (1024**3)))
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
        
        # Create aligned table
        headers = [
            self.translator.get('quality'),
            self.translator.get('max_concurrent_col'),
            self.translator.get('success_rate_col'),
            self.translator.get('avg_render_time_col'),
            self.translator.get('avg_video_duration_col'),
            self.translator.get('avg_file_size_col')
        ]
        
        # Calculate column widths
        col_widths = [len(header) for header in headers]
        
        # Get data rows
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
            # Update column widths
            for i, cell in enumerate(row):
                col_widths[i] = max(col_widths[i], len(cell))
        
        # Create separator line
        separator = "+" + "+".join("-" * (width + 2) for width in col_widths) + "+"
        
        # Add table to report
        report_lines.append(separator)
        # Header row
        header_row = "|"
        for i, header in enumerate(headers):
            header_row += f" {header:<{col_widths[i]}} |"
        report_lines.append(header_row)
        report_lines.append(separator)
        # Data rows
        for row in data_rows:
            data_row = "|"
            for i, cell in enumerate(row):
                if i == 2:  # Success rate column
                    data_row += f" {cell:<{col_widths[i]}} |"
                else:
                    data_row += f" {cell:>{col_widths[i]}} |"
            report_lines.append(data_row)
        report_lines.append(separator)
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
    
    def run_selected_tests(self, selected_qualities: List[str], max_duration_per_test: int = 1800) -> Dict[str, QualityTestResult]:
        """Run selected quality level tests"""
        results = {}
        
        valid_qualities = set(self.quality_configs.keys())
        invalid_qualities = set(selected_qualities) - valid_qualities
        if invalid_qualities:
            logger.warning(f"Invalid quality levels: {invalid_qualities}")
            selected_qualities = [q for q in selected_qualities if q in valid_qualities]
        
        if not selected_qualities:
            logger.error(self.translator.get('all_tests_failed'))
            return results
        
        logger.info(self.translator.get('testing_qualities', qualities=selected_qualities))
        
        for quality in selected_qualities:
            try:
                logger.info(f"\n{'='*80}")
                logger.info(self.translator.get('preparing_test', description=self.quality_configs[quality]['description']))
                logger.info(f"{'='*80}")
                
                logger.info(self.translator.get('waiting_recovery'))
                for i in range(30, 0, -1):
                    if i % 10 == 0:
                        resources = self.get_system_resources()
                        logger.info(self.translator.get('countdown_resources', seconds=i, cpu=resources['cpu_percent'], memory=resources['memory_percent']))
                    time.sleep(1)
                
                result = self.test_quality_level(quality, max_duration_per_test)
                results[quality] = result
                
            except KeyboardInterrupt:
                logger.info(self.translator.get('test_interrupted'))
                break
            except Exception as e:
                logger.error(f"{quality} quality test failed: {e}")
                continue
        
        return results

def main():
    parser = argparse.ArgumentParser(description="Maniq - Manim Quality Stress Testing Tool")
    parser.add_argument("code_dir", help="Manim code files directory")
    
    # Short options
    parser.add_argument("-o", "--output-dir", default="manim_quality_output", help="Render output directory")
    parser.add_argument("-l", "--log-output-dir", default="manim_task_logs", help="Task log output directory")
    parser.add_argument("-d", "--max-duration", type=int, default=1800, 
                       help="Maximum test duration per quality level in seconds (default: 1800)")
    parser.add_argument("-r", "--report-file", default="manim_quality_test_report.txt",
                       help="Test report filename")
    parser.add_argument("-j", "--json-report", default="manim_quality_test_results.json",
                       help="JSON report filename")
    parser.add_argument("--log-file", default="manim_quality_stress_test.log",
                       help="Main log filename")
    parser.add_argument("-i", "--launch-interval", type=float, default=1.0,
                       help="Task launch interval in seconds (default: 1.0)")
    parser.add_argument("-q", "--qualities", nargs='+', 
                       choices=['low', 'medium', 'high', '2k', '4k'],
                       default=['low', 'medium', 'high', '2k', '4k'],
                       help="Quality levels to test (default: all levels)")
    parser.add_argument("--lang", "--language", choices=['en', 'zh', 'zh_tw', 'ko', 'ja', 'de', 'fr', 'es', 'ru'],
                       default='en', help="Report and log language (default: en)")
    
    args = parser.parse_args()
    
    global logger
    logger = setup_logging(args.log_file)
    
    try:
        tester = ManimQualityStressTester(
            args.code_dir, 
            args.output_dir, 
            args.log_output_dir,
            args.launch_interval,
            args.lang
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
    