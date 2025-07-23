# YouTube Video Downloader

A Python-based YouTube video downloader that allows you to download videos in different resolutions and audio files in MP3 format.

## Features

- Download YouTube videos in various resolutions
- Download audio-only in MP3 format
- Select specific FPS for video downloads
- Progress bar during download
- File size information before download
- Error handling for invalid URLs

## Requirements

```text
pytubefix>=2.2.0
```

## Installation

1. Clone this repository:
```sh
git clone https://github.com/h3nxis/yt-downloader.git
cd yt-downloader
```

2. Install the required packages:
```sh
pip install -r requirements.txt
```

## Usage
```sh
python src/main.py
```
### Run the script
Run the script using Python:

```sh
python src/main.py
```

### Steps:
1. Enter the YouTube URL when prompted
2. Choose between video ('v') or audio ('a') download
3. For video downloads:
   - Select from available resolutions
   - Select from available FPS options
4. Wait for download to complete

## Example

```python
Enter YouTube URL: https://www.youtube.com/watch?v=example
for audio enter a - for video enter v: v
Available resolutions:
- 144p
- 360p
- 720p
- 1080p
```

## License

[MIT License](LICENSE)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgments

- Built using [pytube](https://github.com/pytube/pytube) - The Python YouTube Library