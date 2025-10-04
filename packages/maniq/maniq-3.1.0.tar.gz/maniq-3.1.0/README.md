# Maniq - Manim Quality Stress Testing Tool

Maniq is a comprehensive stress testing tool for Manim that helps you determine the maximum concurrent rendering capacity of your server across different quality levels.

## Features

- **Multi-quality support**: Test low (480p), medium (720p), high (1080p), 2K (1440p), and 4K (2160p) quality levels
- **Intelligent resource management**: Dynamically adjusts concurrency based on CPU usage to prevent server crashes
- **Detailed video analysis**: Measures render time, video duration, and file sizes
- **Flexible configuration**: Customizable task launch intervals and quality selection
- **Comprehensive reporting**: Generates detailed text and JSON reports with performance statistics

## Installation

```bash
pip install -U maniq
```

## Usage

```bash
# Test all quality levels with default settings
maniq /path/to/manim/code

# Test specific quality levels with custom interval
maniq /path/to/manim/code --qualities high 4k --launch-interval 2.0

# Custom output directories and test duration
maniq /path/to/manim/code --output-dir my_output --max-duration 1200
```

## Command Line Options

- `--qualities`: Select quality levels to test (low, medium, high, 2k, 4k)
- `--launch-interval`: Time interval between task launches (default: 1.0 seconds)
- `--max-duration`: Maximum test duration per quality level in seconds (default: 1800)
- `--output-dir`: Render output directory (default: manim_quality_output)
- `--log-output-dir`: Task log directory (default: manim_task_logs)
- `--report-file`: Text report filename (default: manim_quality_test_report.txt)
- `--json-report`: JSON report filename (default: manim_quality_test_results.json)
- `--log-file`: Main log filename (default: manim_quality_stress_test.log)

## Requirements

- Python 3.10+
- Manim
- psutil
- ffprobe (optional, for detailed video analysis)

## License

Apache2.0 License
