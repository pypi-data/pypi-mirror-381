#!/usr/bin/env python3
"""
Create a comprehensive video summary using both transcript and visual analysis
"""

import json
import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI


def load_transcript(transcript_file):
    """Load and format transcript."""
    with open(transcript_file, 'r') as f:
        transcript = json.load(f)

    # Create full text version
    full_text = ' '.join([entry['text'] for entry in transcript])
    return full_text, transcript


def load_visual_analysis(analysis_file):
    """Load visual analysis."""
    with open(analysis_file, 'r') as f:
        return f.read()


def create_comprehensive_summary(transcript_file, visual_analysis_file, output_file="comprehensive_summary.txt"):
    """Create comprehensive summary combining transcript and visual analysis."""
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment or .env file")

    client = OpenAI(api_key=api_key)

    print("Loading transcript...")
    full_transcript, transcript_entries = load_transcript(transcript_file)

    print("Loading visual analysis...")
    visual_analysis = load_visual_analysis(visual_analysis_file)

    print(f"Transcript: {len(full_transcript)} characters, {len(transcript_entries)} segments")
    print("Creating comprehensive summary...")

    prompt = f"""You are analyzing a video using two sources of information:

1. VISUAL ANALYSIS (from analyzing 193 keyframes):
{visual_analysis}

2. FULL TRANSCRIPT:
{full_transcript}

Based on both the visual content and the spoken words, provide a comprehensive analysis:

## Executive Summary
Provide a 2-3 paragraph overview of what this video is about.

## Main Topics & Key Points
List the main topics covered and key points made (use bullet points).

## Visual & Content Alignment
How do the visuals support or enhance the spoken content? Are there any interesting patterns?

## Target Audience & Purpose
Who is this video for and what is its primary purpose?

## Notable Quotes or Moments
Any particularly interesting or important quotes from the transcript.

## Overall Assessment
Your overall assessment of the video's quality, effectiveness, and key takeaways.

Be thorough and insightful. Use specific details from both sources."""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=3000,
        temperature=0.7
    )

    summary = response.choices[0].message.content

    # Save results
    with open(output_file, 'w') as f:
        f.write("=" * 80 + "\n")
        f.write("COMPREHENSIVE VIDEO ANALYSIS\n")
        f.write("=" * 80 + "\n\n")
        f.write(summary)
        f.write("\n\n" + "=" * 80 + "\n")
        f.write(f"Analysis based on:\n")
        f.write(f"  - Transcript: {len(transcript_entries)} segments\n")
        f.write(f"  - Visual analysis: 193 keyframes\n")
        f.write("=" * 80 + "\n")

    print(f"\nComprehensive summary saved to {output_file}\n")
    print("=" * 80)
    print(summary)
    print("=" * 80)

    return summary


if __name__ == "__main__":
    import sys

    transcript_file = sys.argv[1] if len(sys.argv) > 1 else "xAji90wPgec_transcript.json"
    visual_file = sys.argv[2] if len(sys.argv) > 2 else "grid_analysis.txt"
    output_file = sys.argv[3] if len(sys.argv) > 3 else "comprehensive_summary.txt"

    create_comprehensive_summary(transcript_file, visual_file, output_file)
