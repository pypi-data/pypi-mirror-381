# PPTX to Video

Convert PowerPoint presentations (`.pptx`) into narrated videos with automatic translation and speech synthesis.

## Features

- Converts each slide of a PPTX file into a video segment
- Extracts and translates slide notes into multiple languages
- Synthesizes speech from translated notes using Google Text-to-Speech
- Assembles narrated video for each language
- Supports Linux, macOS, and Windows (with appropriate dependencies)
- Command-line interface

## Requirements

- Python 3.8+
- [moviepy](https://github.com/Zulko/moviepy)
- [gtts](https://pypi.org/project/gTTS/)
- [deep-translator](https://pypi.org/project/deep-translator/)
- [python-pptx](https://python-pptx.readthedocs.io/)
- LibreOffice (for Linux/macOS slide rendering)
- PowerPoint (for Windows slide rendering)

Install dependencies:
```bash
pip install .
```

## Usage

```bash
python pptx-to-video.py path/to/presentation.pptx --languages English Spanish French --output_dir output_videos
```

- `pptx_path`: Path to the input PPTX file (required)
- `--languages`: List of languages for translation (default: `en`)
- `--output_dir`: Directory to save output videos (default: `output_videos`)

## Example

```bash
python main.py slides.pptx --languages English French --output_dir my_videos
```

## Project Structure

```
ppt-to-video/
├── pptx-to-video.py
├── src/
│   ├── cli.py
│   ├── logger.py
│   ├── language_codes.py
│   ├── powerpoint.py
│   ├── powerpoint_engine.py
│   └── video_constructer.py
├── tests/
│   └── test_language_codes.py
|   └── test_powerpoint_engine.py
|   └── test_powerpoint.py
|   └── test_video_constructor.py
├── pyproject.toml
└── README.md
```

## Development

- Run tests with [pytest](https://docs.pytest.org/):
  ```bash
  pytest
  ```
- Lint and type-check with [ruff](https://github.com/astral-sh/ruff) and [mypy](http://mypy-lang.org/).

## License

MIT License

---

**Note:**
- On Linux/macOS, LibreOffice must be installed and available in your PATH for slide-to-image conversion.
- On Windows, Microsoft PowerPoint is required for slide rendering.