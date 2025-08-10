# YouTube to MP3 Downloader

A simple Python script to download YouTube videos as MP3 files using `yt-dlp`.

## Features

- Download YouTube videos as high-quality MP3 files
- Configurable audio quality (96-320 kbps)
- Custom output directory support
- URL validation
- Error handling and user-friendly messages
- Command-line interface

## Prerequisites

- Python 3.6 or higher
- FFmpeg (required for audio conversion)

### Installing FFmpeg

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**Windows:**
Download from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html) and add to your PATH.

## Installation

1. Clone or download this repository
2. Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
python yt2mp3.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Advanced Usage

```bash
# Specify output directory
python yt2mp3.py "https://youtu.be/VIDEO_ID" -o ./music

# Specify audio quality (96, 128, 192, 256, or 320 kbps)
python yt2mp3.py "https://youtu.be/VIDEO_ID" -q 320

# Combine options
python yt2mp3.py "https://youtu.be/VIDEO_ID" -o ./downloads -q 256
```

### Command Line Options

- `url` (required): YouTube URL to download
- `-o, --output`: Output directory for downloaded files (default: `./downloads`)
- `-q, --quality`: Audio quality in kbps - options: 96, 128, 192, 256, 320 (default: 192)
- `-h, --help`: Show help message

## Examples

```bash
# Download with default settings (192 kbps to ./downloads/)
python yt2mp3.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Download high quality to music folder
python yt2mp3.py "https://youtu.be/dQw4w9WgXcQ" -o ./music -q 320

# Download multiple videos (run separately for each)
python yt2mp3.py "https://www.youtube.com/watch?v=VIDEO_ID_1"
python yt2mp3.py "https://www.youtube.com/watch?v=VIDEO_ID_2"
```

## Output

- Downloaded MP3 files are saved with the video title as the filename
- Files are saved to the specified output directory (default: `./downloads/`)
- Audio is converted to MP3 format with the specified quality
- Sample rate is set to 44.1 kHz for optimal compatibility

## Error Handling

The script includes robust error handling for:
- Invalid YouTube URLs
- Network connectivity issues
- Missing FFmpeg installation
- Download failures
- File system errors

## Legal Notice

Please respect copyright laws and YouTube's Terms of Service when using this tool. Only download content that you have the right to download or that is available under appropriate licenses.

## Dependencies

- `yt-dlp`: Modern YouTube downloader (fork of youtube-dl)

## License

This project is provided as-is for educational and personal use.
