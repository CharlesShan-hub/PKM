# PKM Tools - GUI Tool Collection

A PySide6-based GUI application for managing and automating tasks in the PKM (Personal Knowledge Map) project.

## Features

- **Modular Design**: Each tool is a separate Python script in the `scripts/` directory
- **Easy to Extend**: Add new tools by creating Python files in the `scripts/` folder
- **Threaded Execution**: Tools run in separate threads to keep the GUI responsive
- **Clean Output**: Results are displayed in a dedicated output panel

## Installation

1. Make sure you have Python 3.8+ installed
2. Install uv (if not already installed):
   ```bash
   pip install uv
   ```

3. Install dependencies:
   ```bash
   uv sync
   ```

## Usage

1. Run the application:
   ```bash
   uv run python main.py
   ```

2. The GUI will show:
   - Left panel: List of available tools
   - Right panel: Output display

3. To use a tool:
   - Select a tool from the list
   - Click "Run Selected Tool"
   - View results in the output panel

## Adding New Tools

To add a new tool:

1. Create a new Python file in the `scripts/` directory
2. The file must contain:
   - A `DESCRIPTION` variable (string)
   - A `run()` function that returns a string result
   - Optional arguments for the `run()` function

Example template:
```python
"""
Tool Name
Brief description of what the tool does
"""

DESCRIPTION = "Detailed description of the tool's functionality"

def run(arg1=None, arg2=None):
    # Your tool logic here
    result = "Tool execution result"
    return result
```

## Demo Tool: Markdown Formatter

The included demo tool (`markdown_formatter.py`) demonstrates:
- Finding all markdown files in the PKM project
- Formatting markdown files (cleaning whitespace, standardizing headers)
- Providing a summary of changes

## Project Structure

```
PKM/
 ├── main.py # Main GUI application
 ├── pyproject.toml # Project configuration and dependencies
 ├── scripts/ # Tool scripts directory
 │ ├── init.py # Makes scripts a Python package
 │ └── markdown_formatter.py # Demo tool
 └── TOOLS_README.md # This file
```


## Dependencies

- **PySide6**: GUI framework
- **markdown**: Markdown processing (for future tools)
- **beautifulsoup4**: HTML parsing (for future tools)

## Development

Install development dependencies:
```bash
uv sync --group dev
```

Run tests:
```bash
uv run pytest
```

Format code:
```bash
uv run black .
```

Check code style:
```bash
uv run flake8
```

## Future Ideas for Tools

1. **HTML Exporter**: Convert markdown notes to HTML
2. **Link Checker**: Verify internal and external links
3. **Image Optimizer**: Compress and optimize images
4. **Content Analyzer**: Analyze note structure and completeness
5. **Backup Tool**: Create backups of important notes
6. **Search Indexer**: Create search index for notes
