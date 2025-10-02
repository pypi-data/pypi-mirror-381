#!/usr/bin/env python3
"""
Scene Detection and Keyframe Extraction
Extracts a keyframe from each scene change in a video file.
"""

import argparse
import os
from pathlib import Path
from scenedetect import VideoManager, SceneManager
from scenedetect.detectors import ContentDetector
from scenedetect.frame_timecode import FrameTimecode
import cv2


def extract_keyframes(video_path, output_dir, threshold=27.0):
    """
    Detect scenes in a video and extract keyframes.

    Args:
        video_path: Path to input video file
        output_dir: Directory to save keyframe images
        threshold: Scene detection threshold (lower = more sensitive)

    Returns:
        List of tuples (scene_number, frame_path, timecode)
    """
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Initialize video manager and scene manager
    video_manager = VideoManager([video_path])
    scene_manager = SceneManager()
    scene_manager.add_detector(ContentDetector(threshold=threshold))

    # Start video processing
    video_manager.set_downscale_factor()
    video_manager.start()

    print(f"Processing video: {video_path}")
    print(f"Detecting scenes with threshold: {threshold}")

    # Detect scenes
    scene_manager.detect_scenes(frame_source=video_manager)
    scene_list = scene_manager.get_scene_list()

    print(f"\nDetected {len(scene_list)} scenes")

    # Extract keyframes
    video_cap = cv2.VideoCapture(video_path)
    fps = video_cap.get(cv2.CAP_PROP_FPS)

    keyframes = []

    for i, scene in enumerate(scene_list):
        scene_num = i + 1
        # Get the start frame of the scene
        start_frame = scene[0].get_frames()
        start_time = scene[0].get_seconds()

        # Set video to the frame
        video_cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
        ret, frame = video_cap.read()

        if ret:
            # Save keyframe
            filename = f"scene_{scene_num:04d}_frame_{start_frame:06d}.jpg"
            filepath = output_path / filename
            cv2.imwrite(str(filepath), frame)

            keyframes.append((scene_num, str(filepath), start_time))
            print(f"Scene {scene_num}: {filename} @ {start_time:.2f}s")

    video_cap.release()
    video_manager.release()

    print(f"\nExtracted {len(keyframes)} keyframes to {output_dir}")

    # Save metadata
    metadata_path = output_path / "scenes_metadata.txt"
    with open(metadata_path, 'w') as f:
        f.write(f"Video: {video_path}\n")
        f.write(f"Scenes detected: {len(scene_list)}\n")
        f.write(f"Threshold: {threshold}\n\n")
        for scene_num, filepath, timecode in keyframes:
            f.write(f"Scene {scene_num}: {Path(filepath).name} @ {timecode:.2f}s\n")

    print(f"Metadata saved to {metadata_path}")

    return keyframes


def main():
    parser = argparse.ArgumentParser(
        description="Extract keyframes from scene changes in a video"
    )
    parser.add_argument(
        "video",
        help="Path to input video file"
    )
    parser.add_argument(
        "-o", "--output",
        default="keyframes",
        help="Output directory for keyframes (default: keyframes)"
    )
    parser.add_argument(
        "-t", "--threshold",
        type=float,
        default=27.0,
        help="Scene detection threshold, lower = more sensitive (default: 27.0)"
    )

    args = parser.parse_args()

    # Check if video exists
    if not os.path.exists(args.video):
        print(f"Error: Video file not found: {args.video}")
        return 1

    # Extract keyframes
    try:
        extract_keyframes(args.video, args.output, args.threshold)
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    exit(main())
