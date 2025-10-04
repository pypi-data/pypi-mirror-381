#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Video analysis utilities for Maniq
"""

import subprocess
import json
import traceback
from pathlib import Path
from typing import Optional, List

from .logging import get_logger

logger = get_logger()


class VideoAnalyzer:
    """Utilities for analyzing rendered video files"""
    
    @staticmethod
    def get_video_info(video_path: Path) -> Optional['VideoInfo']:
        """Get video file information"""
        from ..core.models import VideoInfo
        
        try:
            if not video_path.exists():
                return None
            
            # Get file size
            file_size_bytes = video_path.stat().st_size
            file_size_mb = file_size_bytes / (1024**2)
            
            # Use ffprobe to get detailed video information (if available)
            try:
                cmd = [
                    'ffprobe', '-v', 'quiet', '-print_format', 'json',
                    '-show_format', '-show_streams', str(video_path)
                ]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                
                if result.returncode == 0:
                    probe_data = json.loads(result.stdout)
                    
                    # Get video duration
                    duration = float(probe_data.get('format', {}).get('duration', 0))
                    
                    # Get resolution and FPS
                    resolution = "unknown"
                    fps = 0.0
                    for stream in probe_data.get('streams', []):
                        if stream.get('codec_type') == 'video':
                            width = stream.get('width', 0)
                            height = stream.get('height', 0)
                            if width and height:
                                resolution = f"{width}x{height}"
                            # Try to get FPS
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
            
            # Fallback: return basic file information
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
    
    @staticmethod
    def find_rendered_video(output_dir: Path) -> Optional[Path]:
        """Find rendered video file in output directory"""
        try:
            # Common video file extensions
            video_extensions = ['.mp4', '.mov', '.avi', '.mkv', '.webm']
            for ext in video_extensions:
                video_files = list(output_dir.rglob(f"*{ext}"))
                if video_files:
                    # Return the most recently modified file
                    return max(video_files, key=lambda f: f.stat().st_mtime)
        except Exception as e:
            logger.warning(f"Failed to find video file {output_dir}: {e}")
        return None
        