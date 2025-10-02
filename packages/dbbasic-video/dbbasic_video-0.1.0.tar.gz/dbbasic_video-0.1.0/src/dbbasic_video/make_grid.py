#!/usr/bin/env python3
"""
Create a thumbnail sheet from all keyframes
"""

import math
from pathlib import Path
from PIL import Image


def create_thumbnail_sheet(keyframes_dir, output_file="thumbnail_sheet.jpg", thumb_width=160):
    """Create a grid of thumbnails from all keyframes."""
    keyframes_path = Path(keyframes_dir)
    image_files = sorted(keyframes_path.glob("scene_*.jpg"))

    if not image_files:
        print(f"No keyframes found in {keyframes_dir}")
        return

    print(f"Creating thumbnail sheet from {len(image_files)} keyframes...")

    # Calculate grid dimensions (roughly square)
    num_images = len(image_files)
    cols = math.ceil(math.sqrt(num_images))
    rows = math.ceil(num_images / cols)

    # Load first image to get aspect ratio
    first_img = Image.open(image_files[0])
    aspect_ratio = first_img.height / first_img.width
    thumb_height = int(thumb_width * aspect_ratio)
    first_img.close()

    # Create blank canvas
    canvas_width = cols * thumb_width
    canvas_height = rows * thumb_height
    canvas = Image.new('RGB', (canvas_width, canvas_height), (0, 0, 0))

    # Place thumbnails
    for idx, img_path in enumerate(image_files):
        row = idx // cols
        col = idx % cols

        img = Image.open(img_path)
        img.thumbnail((thumb_width, thumb_height), Image.Resampling.LANCZOS)

        x = col * thumb_width
        y = row * thumb_height
        canvas.paste(img, (x, y))
        img.close()

        if (idx + 1) % 20 == 0:
            print(f"  Processed {idx + 1}/{num_images}...")

    # Save
    canvas.save(output_file, "JPEG", quality=85, optimize=True)
    print(f"\nThumbnail sheet saved to {output_file}")
    print(f"Grid: {cols} columns × {rows} rows")
    print(f"Thumbnail size: {thumb_width}×{thumb_height}px")
    print(f"Total size: {canvas_width}×{canvas_height}px")


if __name__ == "__main__":
    import sys

    keyframes_dir = sys.argv[1] if len(sys.argv) > 1 else "keyframes"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "thumbnail_sheet.jpg"
    thumb_width = int(sys.argv[3]) if len(sys.argv) > 3 else 160

    create_thumbnail_sheet(keyframes_dir, output_file, thumb_width)
