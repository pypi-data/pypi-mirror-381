#!/usr/bin/env python3
"""
Download video from YouTube
"""

import argparse
import subprocess
import sys


def download_video(url, output="video.mp4", format_spec="bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"):
    """Download video using yt-dlp."""
    print(f"Downloading video from: {url}")

    cmd = [
        "yt-dlp",
        "-f", format_spec,
        "-o", output,
        url
    ]

    try:
        result = subprocess.run(cmd, check=True, capture_output=False)
        print(f"\nVideo downloaded to: {output}")
        return output
    except subprocess.CalledProcessError as e:
        print(f"Error downloading video: {e}", file=sys.stderr)
        return None
    except FileNotFoundError:
        print("Error: yt-dlp not found. Install with: pip install yt-dlp", file=sys.stderr)
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Download video from YouTube"
    )
    parser.add_argument(
        "url",
        help="YouTube URL"
    )
    parser.add_argument(
        "-o", "--output",
        default="video.mp4",
        help="Output filename (default: video.mp4)"
    )
    parser.add_argument(
        "-f", "--format",
        default="bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        help="Format specification for yt-dlp"
    )

    args = parser.parse_args()

    result = download_video(args.url, args.output, args.format)
    return 0 if result else 1


if __name__ == "__main__":
    sys.exit(main())
