#!/usr/bin/env python3
"""
Analyze the thumbnail grid image using OpenAI Vision API
"""

import base64
import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI


def encode_image(image_path):
    """Encode image to base64."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def analyze_grid(image_path, output_file="grid_analysis.txt"):
    """Analyze the thumbnail grid image."""
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment or .env file")

    client = OpenAI(api_key=api_key)

    print(f"Analyzing grid image: {image_path}")
    base64_image = encode_image(image_path)

    prompt = """This is a grid of 193 video keyframes from scene changes in a video.

Please analyze this thumbnail sheet and provide:

1. **Overall Summary**: What type of video is this? What's the main content?
2. **Main Themes/Topics**: What are the key themes or topics covered?
3. **Visual Patterns**: What visual patterns do you notice across the scenes?
4. **Scene Categories**: Group the scenes into major categories (e.g., interviews, outdoor shots, graphics, etc.)
5. **Notable Moments**: Any particularly interesting or significant frames?

Be detailed and thorough in your analysis."""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        max_tokens=2000
    )

    analysis = response.choices[0].message.content

    # Save results
    with open(output_file, 'w') as f:
        f.write(analysis)

    print(f"\nAnalysis saved to {output_file}\n")
    print("=" * 80)
    print(analysis)
    print("=" * 80)

    return analysis


if __name__ == "__main__":
    import sys
    image_path = sys.argv[1] if len(sys.argv) > 1 else "thumbnail_sheet.jpg"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "grid_analysis.txt"

    analyze_grid(image_path, output_file)
