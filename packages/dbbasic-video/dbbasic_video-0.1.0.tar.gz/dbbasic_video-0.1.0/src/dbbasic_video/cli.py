#!/usr/bin/env python3
"""
Main CLI entry point for dbbasic-video
"""

import sys
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="DBBasic Video - AI-powered video analysis toolkit",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Available commands:
  download        Download video from YouTube
  extract         Extract keyframes from video using scene detection
  transcript      Download video transcript
  grid            Create thumbnail grid from keyframes
  analyze         Analyze visuals with AI
  summarize       Create comprehensive summary
  find-thumbnail  Find best thumbnail candidates
  pipeline        Run complete analysis pipeline

Use 'dbbasic-video <command> --help' for more information on a command.
"""
    )

    parser.add_argument(
        'command',
        nargs='?',
        help='Command to run'
    )

    # Parse just the command
    args, remaining = parser.parse_known_args()

    if not args.command:
        parser.print_help()
        return 1

    # Route to appropriate module
    if args.command == 'download':
        from .download_video import main as cmd_main
    elif args.command == 'extract':
        from .extract_keyframes import main as cmd_main
    elif args.command == 'transcript':
        from .get_transcript import main as cmd_main
    elif args.command == 'grid':
        from .make_grid import main as cmd_main
    elif args.command == 'analyze':
        from .analyze_visuals import main as cmd_main
    elif args.command == 'summarize':
        from .summarize import main as cmd_main
    elif args.command == 'find-thumbnail':
        from .find_thumbnail import main as cmd_main
    elif args.command == 'pipeline':
        from .pipeline import main as cmd_main
    else:
        print(f"Unknown command: {args.command}", file=sys.stderr)
        parser.print_help()
        return 1

    # Replace argv with remaining args and run command
    sys.argv = [f'dbbasic-video {args.command}'] + remaining
    return cmd_main()


if __name__ == "__main__":
    sys.exit(main())
