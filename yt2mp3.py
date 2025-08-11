#!/usr/bin/env python3
"""
YouTube to MP3 Downloader
A simple script to download YouTube videos as MP3 files with embedded thumbnails using yt-dlp.
"""

import os
import sys
import argparse
from pathlib import Path
import yt_dlp


def download_youtube_as_mp3(url, output_dir="./downloads", quality="192"):
    """
    Download a YouTube video as an MP3 file with embedded thumbnail.
    
    Args:
        url (str): YouTube URL to download
        output_dir (str): Directory to save the MP3 file
        quality (str): Audio quality in kbps (default: 192)
    
    Returns:
        bool: True if successful, False otherwise
    """
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Configure yt-dlp options
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'writethumbnail': True,  # Download thumbnail
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': quality,
            },
            {
                'key': 'EmbedThumbnail',  # Embed thumbnail as album art
                'already_have_thumbnail': False,
            },
            {
                'key': 'FFmpegMetadata',  # Add metadata
                'add_metadata': True,
            },
        ],
        'postprocessor_args': [
            '-ar', '44100',  # Sample rate
        ],
        'prefer_ffmpeg': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading: {url}")
            ydl.download([url])
            print("Download completed successfully with embedded thumbnail!")
            return True
            
    except yt_dlp.utils.DownloadError as e:
        print(f"Download error: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False


def validate_url(url):
    """
    Basic validation for YouTube URLs.
    
    Args:
        url (str): URL to validate
    
    Returns:
        bool: True if URL appears to be a valid YouTube URL
    """
    youtube_domains = [
        'youtube.com',
        'youtu.be',
        'm.youtube.com',
        'www.youtube.com'
    ]
    
    return any(domain in url.lower() for domain in youtube_domains)


def main():
    """Main function to handle command line arguments and execute download."""
    parser = argparse.ArgumentParser(
        description="Download YouTube videos as MP3 files with embedded thumbnails",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python yt2mp3.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
  python yt2mp3.py "https://youtu.be/dQw4w9WgXcQ" -o ./music -q 320
        """
    )
    
    parser.add_argument(
        'url',
        help='YouTube URL to download'
    )
    
    parser.add_argument(
        '-o', '--output',
        default='./downloads',
        help='Output directory for downloaded files (default: ./downloads)'
    )
    
    parser.add_argument(
        '-q', '--quality',
        default='192',
        choices=['96', '128', '192', '256', '320'],
        help='Audio quality in kbps (default: 192)'
    )
    
    args = parser.parse_args()
    
    # Validate the URL
    if not validate_url(args.url):
        print("Error: Please provide a valid YouTube URL")
        sys.exit(1)
    
    # Check if ffmpeg is available
    try:
        import subprocess
        subprocess.run(['ffmpeg', '-version'], 
                      stdout=subprocess.DEVNULL, 
                      stderr=subprocess.DEVNULL, 
                      check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Warning: FFmpeg not found. Please install FFmpeg for audio conversion.")
        print("On macOS: brew install ffmpeg")
        print("On Ubuntu/Debian: sudo apt install ffmpeg")
        print("On Windows: Download from https://ffmpeg.org/download.html")
        sys.exit(1)
    
    # Perform the download
    success = download_youtube_as_mp3(args.url, args.output, args.quality)
    
    if not success:
        sys.exit(1)
    
    print(f"MP3 file saved to: {os.path.abspath(args.output)}")


if __name__ == "__main__":
    main()
