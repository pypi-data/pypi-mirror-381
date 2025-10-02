#!/usr/bin/env python3
"""
Run complete video analysis pipeline
"""

import argparse
import sys
from pathlib import Path


def run_pipeline(url, output_dir="output", skip_download=False, video_file=None):
    """Run complete analysis pipeline."""
    from .download_video import download_video
    from .extract_keyframes import extract_keyframes
    from .get_transcript import download_transcript
    from .make_grid import create_thumbnail_sheet
    from .analyze_visuals import analyze_grid
    from .summarize import create_comprehensive_summary

    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    print("=" * 80)
    print("DBBASIC VIDEO ANALYSIS PIPELINE")
    print("=" * 80)

    # Step 1: Download video
    if not skip_download:
        print("\n[1/6] Downloading video...")
        video_file = str(output_path / "video.mp4")
        if not download_video(url, video_file):
            return 1
    else:
        print(f"\n[1/6] Using existing video: {video_file}")

    # Step 2: Extract keyframes
    print("\n[2/6] Extracting keyframes...")
    keyframes_dir = str(output_path / "keyframes")
    extract_keyframes(video_file, keyframes_dir)

    # Step 3: Create thumbnail grid
    print("\n[3/6] Creating thumbnail grid...")
    grid_file = str(output_path / "thumbnail_grid.jpg")
    create_thumbnail_sheet(keyframes_dir, grid_file)

    # Step 4: Download transcript
    print("\n[4/6] Downloading transcript...")
    video_id = url.split('v=')[-1].split('&')[0] if 'v=' in url else url.split('/')[-1]
    transcript_file = str(output_path / "transcript.json")
    download_transcript(video_id, transcript_file)

    # Step 5: Analyze visuals
    print("\n[5/6] Analyzing visuals with AI...")
    visual_analysis = str(output_path / "visual_analysis.txt")
    analyze_grid(grid_file, visual_analysis)

    # Step 6: Create comprehensive summary
    print("\n[6/6] Creating comprehensive summary...")
    summary_file = str(output_path / "comprehensive_summary.txt")
    create_comprehensive_summary(transcript_file, visual_analysis, summary_file)

    print("\n" + "=" * 80)
    print("PIPELINE COMPLETE")
    print("=" * 80)
    print(f"\nOutput directory: {output_path}")
    print(f"  - Video: video.mp4")
    print(f"  - Keyframes: keyframes/")
    print(f"  - Thumbnail grid: thumbnail_grid.jpg")
    print(f"  - Transcript: transcript.json, transcript.txt")
    print(f"  - Visual analysis: visual_analysis.txt")
    print(f"  - Summary: comprehensive_summary.txt")

    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Run complete video analysis pipeline"
    )
    parser.add_argument(
        "url",
        help="YouTube URL"
    )
    parser.add_argument(
        "-o", "--output",
        default="output",
        help="Output directory (default: output)"
    )
    parser.add_argument(
        "--skip-download",
        action="store_true",
        help="Skip download step (use existing video)"
    )
    parser.add_argument(
        "--video",
        help="Path to existing video file (requires --skip-download)"
    )

    args = parser.parse_args()

    if args.skip_download and not args.video:
        print("Error: --video required when using --skip-download", file=sys.stderr)
        return 1

    return run_pipeline(args.url, args.output, args.skip_download, args.video)


if __name__ == "__main__":
    sys.exit(main())
