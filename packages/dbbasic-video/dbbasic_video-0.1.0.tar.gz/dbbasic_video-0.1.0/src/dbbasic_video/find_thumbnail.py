#!/usr/bin/env python3
"""
Find and display best thumbnail candidates
"""

import argparse
import subprocess
import sys
from pathlib import Path


def find_by_timestamp(keyframes_dir, timestamp, window=5):
    """Find keyframes near a timestamp."""
    keyframes_path = Path(keyframes_dir)
    metadata_file = keyframes_path / "scenes_metadata.txt"

    if not metadata_file.exists():
        print(f"Error: {metadata_file} not found", file=sys.stderr)
        return []

    matches = []
    with open(metadata_file, 'r') as f:
        for line in f:
            if '@' in line and 'Scene' in line:
                parts = line.split('@')
                if len(parts) == 2:
                    time_str = parts[1].strip().replace('s', '')
                    try:
                        time = float(time_str)
                        if abs(time - timestamp) <= window:
                            filename = parts[0].split(':')[1].strip()
                            matches.append((filename, time))
                    except ValueError:
                        continue

    return sorted(matches, key=lambda x: abs(x[1] - timestamp))


def open_images(keyframes_dir, filenames):
    """Open images in default viewer."""
    keyframes_path = Path(keyframes_dir)
    paths = [str(keyframes_path / f) for f in filenames]

    if sys.platform == 'darwin':  # macOS
        subprocess.run(['open'] + paths)
    elif sys.platform == 'linux':
        subprocess.run(['xdg-open'] + paths)
    else:  # Windows
        for p in paths:
            subprocess.run(['start', p], shell=True)


def main():
    parser = argparse.ArgumentParser(
        description="Find and display thumbnail candidates"
    )
    parser.add_argument(
        "keyframes_dir",
        help="Directory containing keyframes"
    )
    parser.add_argument(
        "-t", "--timestamp",
        type=float,
        help="Find keyframes near this timestamp (seconds)"
    )
    parser.add_argument(
        "-w", "--window",
        type=float,
        default=5.0,
        help="Time window in seconds (default: 5)"
    )
    parser.add_argument(
        "-n", "--count",
        type=int,
        default=5,
        help="Number of matches to show (default: 5)"
    )
    parser.add_argument(
        "--no-open",
        action="store_true",
        help="Don't open images, just list them"
    )

    args = parser.parse_args()

    if args.timestamp is None:
        print("Error: --timestamp is required", file=sys.stderr)
        return 1

    print(f"Searching for keyframes near {args.timestamp}s (±{args.window}s)...")
    matches = find_by_timestamp(args.keyframes_dir, args.timestamp, args.window)

    if not matches:
        print("No matches found")
        return 1

    matches = matches[:args.count]

    print(f"\nFound {len(matches)} keyframes:")
    for filename, time in matches:
        print(f"  {filename} @ {time:.2f}s (Δ{abs(time-args.timestamp):.2f}s)")

    if not args.no_open:
        filenames = [m[0] for m in matches]
        open_images(args.keyframes_dir, filenames)
        print(f"\nOpened {len(filenames)} images")

    return 0


if __name__ == "__main__":
    sys.exit(main())
