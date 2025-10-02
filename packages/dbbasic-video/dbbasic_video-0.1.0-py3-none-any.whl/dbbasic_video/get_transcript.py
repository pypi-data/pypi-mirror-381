#!/usr/bin/env python3
"""
Download YouTube transcript
"""

import argparse
import json
from youtube_transcript_api import YouTubeTranscriptApi as yt_api


def download_transcript(video_id, output_file=None):
    """Download transcript for a YouTube video."""
    print(f"Fetching transcript for video ID: {video_id}")

    try:
        # Get transcript
        fetched = yt_api().fetch(video_id)
        transcript = [{'start': s.start, 'duration': s.duration, 'text': s.text} for s in fetched]

        if not output_file:
            output_file = f"{video_id}_transcript.json"

        # Save JSON version
        with open(output_file, 'w') as f:
            json.dump(transcript, f, indent=2)

        print(f"Transcript saved to {output_file}")

        # Save readable text version
        text_file = output_file.replace('.json', '.txt')
        with open(text_file, 'w') as f:
            for entry in transcript:
                timestamp = entry['start']
                text = entry['text']
                f.write(f"[{timestamp:.2f}s] {text}\n")

        print(f"Text version saved to {text_file}")

        # Print summary
        total_duration = transcript[-1]['start'] + transcript[-1]['duration']
        print(f"\nTranscript stats:")
        print(f"  - Entries: {len(transcript)}")
        print(f"  - Duration: {total_duration:.2f}s ({total_duration/60:.2f} min)")
        print(f"  - Total text length: {sum(len(e['text']) for e in transcript)} characters")

        return transcript

    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Download YouTube video transcript"
    )
    parser.add_argument(
        "video_id",
        help="YouTube video ID (e.g., 'xAji90wPgec') or URL"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output JSON file (default: {video_id}_transcript.json)"
    )

    args = parser.parse_args()

    # Extract video ID from URL if needed
    video_id = args.video_id
    if 'youtube.com' in video_id or 'youtu.be' in video_id:
        if 'v=' in video_id:
            video_id = video_id.split('v=')[1].split('&')[0]
        elif 'youtu.be/' in video_id:
            video_id = video_id.split('youtu.be/')[1].split('?')[0]

    download_transcript(video_id, args.output)


if __name__ == "__main__":
    main()
