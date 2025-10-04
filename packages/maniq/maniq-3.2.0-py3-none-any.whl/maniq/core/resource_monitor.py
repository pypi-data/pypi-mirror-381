#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
System resource monitoring for Maniq
"""

import psutil
import threading
import time
from typing import Dict, List

class SystemResourceMonitor:
    """Monitor system resources during testing"""
    
    def __init__(self):
        self.monitor_data: List[Dict] = []
        self.stop_event = threading.Event()
        self.monitor_thread: Optional[threading.Thread] = None
    
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
    
    def _monitor_loop(self):
        """Internal monitoring loop"""
        while not self.stop_event.is_set():
            try:
                resources = self.get_system_resources()
                self.monitor_data.append(resources)
                time.sleep(1)
            except Exception as e:
                # Use basic logging since we don't have access to the main logger
                print(f"System monitor thread error: {e}")
                time.sleep(1)
    
    def start_monitoring(self):
        """Start the resource monitoring thread"""
        self.stop_event.clear()
        self.monitor_thread = threading.Thread(target=self._monitor_loop)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()
    
    def stop_monitoring(self, timeout: float = 5.0):
        """Stop the resource monitoring thread"""
        self.stop_event.set()
        if self.monitor_thread:
            self.monitor_thread.join(timeout=timeout)
    
    def get_monitor_data(self) -> List[Dict]:
        """Get a copy of the monitoring data"""
        return self.monitor_data.copy()
    
    def clear_monitor_data(self):
        """Clear the monitoring data"""
        self.monitor_data.clear()
        