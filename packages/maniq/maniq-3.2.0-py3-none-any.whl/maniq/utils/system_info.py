#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
System information utilities for Maniq
"""

import psutil


def get_system_info():
    """Get comprehensive system information"""
    return {
        'cpu_physical': psutil.cpu_count(logical=False) or psutil.cpu_count(),
        'cpu_logical': psutil.cpu_count(logical=True),
        'total_memory_gb': psutil.virtual_memory().total / (1024**3),
        'available_disk_gb': psutil.disk_usage('/').free / (1024**3),
        'platform': sys.platform if 'sys' in globals() else 'unknown'
    }
    