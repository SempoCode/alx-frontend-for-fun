# Markdown to HTML Converter

This project is a Python script that converts Markdown files into HTML. It provides basic Markdown parsing, including headings, lists, paragraphs, bold, emphasis, and other common Markdown elements.

## Project Overview

The `markdown2html.py` script reads a Markdown file and converts its content into HTML format. The project supports various Markdown syntax features like:

- Headings (`#`, `##`, `###`, etc.)
- Unordered lists (`- item`)
- Ordered lists (`* item`)
- Simple text (paragraphs)
- Bold and emphasis (`**bold**`, `__italic__`)
- Custom MD5 and text transformations

## Requirements

- Python 3.7 or higher
- Ubuntu 18.04 LTS
- The script must be executable and follow PEP 8 style guidelines.

## Usage

The script requires two arguments:
1. **Markdown file**: The input file containing Markdown syntax.
2. **HTML file**: The output file where the converted HTML will be written.

### Example:

```bash
./markdown2html.py README.md README.html
```

Error Handling:

If fewer than two arguments are provided:

Usage: ```bash ./markdown2html.py README.md README.html```

If the Markdown file does not exist:

Missing <filename>


Features

1. Headings: Convert Markdown headings (`#`, `##`, etc.) into corresponding HTML headings (`<h1>`, `<h2>`, etc.).


2. Unordered Lists: Convert unordered lists (- item) into HTML <ul> and <li> elements.


3. Ordered Lists: Convert ordered lists (* item) into HTML <ol> and <li> elements.


4. Paragraphs: Convert simple text into HTML <p> elements with support for line breaks.


5. Bold and Emphasis: Parse bold (**text**) and emphasis (__text__) into <b> and <em> tags, respectively.


6. Custom Transformations: Handle MD5 transformations and remove specific characters as defined.



Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/alx-frontend-for-fun.git
```

2. Make the script executable:
```bash
chmod +x markdown2html.py
```

3. Run the script:
```bash
./markdown2html.py input.md output.html
```
License

This project is licensed under the MIT License. See the LICENSE file for details.
