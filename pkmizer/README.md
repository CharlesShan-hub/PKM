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

## Available Tools

### 1. Markdown Splitter (`markdown_splitter.py`)
A powerful tool for splitting large markdown files into smaller, organized notes.

**Features:**
- Splits markdown files by level-1 headings (`# Title`)
- Handles code blocks correctly (ignores `#` inside code)
- AI-powered filename generation using DeepSeek API (optional)
- Creates organized directory structure with `/notes` subfolder
- Automatically generates README.md with relative path links
- Supports both AI-generated and fallback filenames

**Usage:**
```bash
uv run python scripts/markdown_splitter.py <input_file> <output_dir> [api_key]
```

**Parameters:**
- `input_file`: Path to the markdown file to split
- `output_dir`: Output directory (will create `/notes` subfolder)
- `api_key`: DeepSeek API key (optional, for AI filename generation)

### 2. Image Downloader (`image_downloader.py`)
A tool for downloading images from URLs.

**Features:**
- Downloads images from provided URLs
- Saves images to specified directory
- Handles various image formats
- Provides download progress and status

## Markdown Splitter Detailed Example

### Basic Usage (Without AI)

```bash
# Split a markdown file without AI filename generation
uv run python scripts/markdown_splitter.py "D:/path/to/input.md" "./output"
```

This will:
1. Read the input markdown file
2. Find all level-1 headings (`# Title`)
3. Split the content at each heading
4. Generate fallback filenames based on headings
5. Save each section as a separate file in `./output/notes/`
6. Create `README.md` in `./output/` with links to all files

### Advanced Usage (With AI)

```bash
# Split a markdown file with AI filename generation
uv run python scripts/markdown_splitter.py "D:/path/to/input.md" "./output" "your-deepseek-api-key"
```

This will:
1. Do everything from the basic usage
2. Use DeepSeek API to generate meaningful filenames for each section
3. Create more descriptive and organized filenames

### Output Structure

After running the tool, you'll get:

```
output/
├── README.md                    # Index file with links to all notes
└── notes/                       # All split files go here
    ├── introduction.md          # First section
    ├── technical-overview.md    # Second section
    ├── api-integration.md       # Third section
    ├── testing-strategy.md      # Fourth section
    └── conclusion.md            # Last section
```

### Features in Detail

1. **Smart Heading Detection**: Only detects `# Title` (not `## Subtitle`) and ignores `#` inside code blocks
2. **Code Block Handling**: Preserves code blocks intact, doesn't split inside them
3. **AI Filename Generation**: Uses DeepSeek API to create meaningful, English filenames
4. **Fallback Mechanism**: If AI fails or no API key provided, uses heading-based filenames
5. **Directory Organization**: Automatically creates `/notes` subfolder for clean organization
6. **README Generation**: Creates index file with relative path links for easy navigation

## Project Structure

```
PKM/
 ├── main.py # Main GUI application
 ├── pyproject.toml # Project configuration and dependencies
 ├── README.md # Project documentation (this file)
 ├── scripts/ # Tool scripts directory
 │ ├── __init__.py # Makes scripts a Python package
 │ ├── markdown_splitter.py # Markdown file splitter tool
 │ └── image_downloader.py # Image downloader tool
 └── tests/ # Test files (optional)
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
