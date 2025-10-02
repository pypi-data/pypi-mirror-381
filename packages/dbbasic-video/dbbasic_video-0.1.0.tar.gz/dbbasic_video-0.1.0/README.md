# DBBasic Video

AI-powered video analysis toolkit for extracting, analyzing, and summarizing video content.

## Features

- 📥 **Download** videos from YouTube
- 🎬 **Extract keyframes** using scene detection
- 📝 **Get transcripts** automatically
- 🖼️ **Create thumbnail grids** from keyframes
- 🤖 **AI analysis** of visual content using GPT-4 Vision
- 📊 **Comprehensive summaries** combining visuals and transcripts

## Installation

```bash
pip install dbbasic-video
```

Or install from source:

```bash
git clone https://github.com/askrobots/dbbasic-video.git
cd dbbasic-video
pip install -e .
```

## Requirements

- Python 3.8+
- OpenAI API key (set as `OPENAI_API_KEY` environment variable or in `.env` file)
- yt-dlp (for downloading videos)

## Quick Start

### Complete Pipeline

Run the entire analysis pipeline on a YouTube video:

```bash
dbbasic-video pipeline "https://www.youtube.com/watch?v=VIDEO_ID"
```

This will:
1. Download the video
2. Extract keyframes from scene changes
3. Create a thumbnail grid
4. Download the transcript
5. Analyze visuals with AI
6. Generate a comprehensive summary

### Individual Commands

**Download a video:**
```bash
dbbasic-video download "https://www.youtube.com/watch?v=VIDEO_ID" -o video.mp4
```

**Extract keyframes:**
```bash
dbbasic-video extract video.mp4 -o keyframes/
```

**Get transcript:**
```bash
dbbasic-video transcript VIDEO_ID
```

**Create thumbnail grid:**
```bash
dbbasic-video grid keyframes/ -o thumbnail_grid.jpg
```

**Analyze visuals:**
```bash
dbbasic-video analyze thumbnail_grid.jpg -o analysis.txt
```

**Find best thumbnail:**
```bash
dbbasic-video find-thumbnail keyframes/ -t 120.5
```

**Create comprehensive summary:**
```bash
dbbasic-video summarize transcript.json analysis.txt -o summary.txt
```

## Environment Variables

Create a `.env` file in your working directory:

```
OPENAI_API_KEY=your_api_key_here
```

## Output Structure

When running the pipeline, output is organized as:

```
output/
├── video.mp4                    # Downloaded video
├── keyframes/                   # Extracted keyframes
│   ├── scene_0001_*.jpg
│   ├── scene_0002_*.jpg
│   └── scenes_metadata.txt
├── thumbnail_grid.jpg           # Grid of all keyframes
├── transcript.json              # Raw transcript
├── transcript.txt               # Readable transcript
├── visual_analysis.txt          # AI visual analysis
└── comprehensive_summary.txt    # Final summary
```

## API Usage

```python
from dbbasic_video.extract_keyframes import extract_keyframes
from dbbasic_video.make_grid import create_thumbnail_sheet
from dbbasic_video.analyze_visuals import analyze_grid

# Extract keyframes
extract_keyframes("video.mp4", "keyframes/")

# Create thumbnail grid
create_thumbnail_sheet("keyframes/", "grid.jpg")

# Analyze with AI
analyze_grid("grid.jpg", "analysis.txt")
```

## Cost Considerations

- Scene detection and keyframe extraction: **Free** (local processing)
- Transcript download: **Free** (from YouTube)
- AI visual analysis: **~$0.01-0.02** per image with GPT-4 Vision
- Using thumbnail grid: **1 API call** instead of analyzing each frame individually

## License

MIT

## Future: DBBasic Core Integration

This package is designed to be part of the larger **DBBasic** ecosystem. In the future, a unified `db-basic` CLI will provide:

```bash
# Unified configuration
db-basic config set output_dir ~/analysis

# Plugin-based architecture
db-basic video extract video.mp4     # uses dbbasic-video
db-basic audio transcribe audio.mp3  # uses dbbasic-audio
db-basic image analyze photo.jpg     # uses dbbasic-image

# Plugin discovery
db-basic list
  ✓ video  (dbbasic-video 0.1.0)
  ✓ audio  (dbbasic-audio 0.2.1)
  ✗ image  (not installed - pip install dbbasic-image)
```

**Planned shared infrastructure:**
- Global config: `~/.config/dbbasic/config.toml`
- Shared cache and output structure
- Unified logging and error handling
- Plugin registry and version management
- Common utilities for AI, media processing, and data handling

For now, `dbbasic-video` works as a standalone tool. When `db-basic` core is released, it will automatically integrate while maintaining backwards compatibility.

## Contributing

Contributions welcome! Please open an issue or PR.
