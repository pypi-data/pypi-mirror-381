#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Maniq CLI - Command Line Interface
"""

import argparse
import sys
import traceback
from pathlib import Path

from . import __version__
from .core.tester import ManimQualityStressTester
from .utils.logging import setup_logging


def main():
    parser = argparse.ArgumentParser(description="Maniq - Manim Quality Stress Testing Tool")
    
    # Add version argument
    parser.add_argument('--version', action='version', version=f'maniq {__version__}')
    
    parser.add_argument("code_dir", nargs='?', help="Manim code files directory")
    
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
    
    # If no code_dir provided and not just checking version, show help
    if not args.code_dir:
        if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1] in ['--version', '-h', '--help']):
            parser.print_help()
            return
        else:
            parser.error("the following arguments are required: code_dir")
    
    # Setup logging
    logger = setup_logging(args.log_file)
    
    try:
        tester = ManimQualityStressTester(
            code_dir=args.code_dir,
            output_dir=args.output_dir,
            log_output_dir=args.log_output_dir,
            launch_interval=args.launch_interval,
            language=args.lang
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
        
        # Generate and save reports
        report = tester.generate_report(results)
        with open(args.report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        json_results = tester.generate_json_report(results)
        with open(args.json_report, 'w', encoding='utf-8') as f:
            f.write(json_results)
        
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
    