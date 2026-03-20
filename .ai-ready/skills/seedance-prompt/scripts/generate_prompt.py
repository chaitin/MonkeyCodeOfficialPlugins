#!/usr/bin/env python3
"""
Seedance 2.0 Prompt Generator CLI

Usage:
    python generate_prompt.py --input script.txt --output prompts.md
    python generate_prompt.py --input script.txt --aspect 16:9 --model seedance_2.0
"""

import argparse
import re
from pathlib import Path


def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate Seedance 2.0 prompts from scripts')
    parser.add_argument('--input', '-i', required=True, help='Input script file path')
    parser.add_argument('--output', '-o', default='prompts.md', help='Output file path')
    parser.add_argument('--aspect', default='9:16', choices=['16:9', '9:16', '1:1'], help='Video aspect ratio')
    parser.add_argument('--model', default='seedance_2.0_fast', choices=['seedance_2.0', 'seedance_2.0_fast'], help='Video model')
    parser.add_argument('--subtitle', default='off', choices=['on', 'off'], help='Enable subtitles')
    return parser.parse_args()


def segment_script(script: str) -> list:
    """
    Segment script into shots.
    Returns list of (duration, description) tuples.
    """
    lines = [l.strip() for l in script.split('\n') if l.strip()]
    segments = []
    
    for line in lines:
        duration = 5
        segments.append((duration, line))
    
    return segments


def generate_prompt(segment: tuple, index: int, aspect: str) -> str:
    """Generate a Seedance prompt from a segment."""
    duration, description = segment
    
    vertical_note = "vertical composition, centered or lower third composition, background layers" if aspect == "9:16" else ""
    
    prompt = f"片段{index+1} [{duration}s]\n"
    prompt += f"[{duration}s] {description}, {vertical_note}, cinematic, 8k, film grain, shallow depth of field, high contrast lighting, professional color grading"
    
    return prompt


def main():
    args = parse_arguments()
    
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file '{args.input}' not found")
        return 1
    
    script = input_path.read_text(encoding='utf-8')
    segments = segment_script(script)
    
    output = "视觉风格 现代都市, 电影感\n\n"
    
    for i, segment in enumerate(segments):
        output += generate_prompt(segment, i, args.aspect) + "\n\n"
    
    output_path = Path(args.output)
    output_path.write_text(output, encoding='utf-8')
    
    print(f"Generated {len(segments)} segments")
    print(f"Output written to: {args.output}")
    
    return 0


if __name__ == '__main__':
    exit(main())
