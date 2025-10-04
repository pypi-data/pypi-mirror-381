#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Logging utilities for Maniq
"""

import logging
import sys
from pathlib import Path


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


def get_logger():
    """Get the configured logger"""
    return logging.getLogger()
    