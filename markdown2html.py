#!/usr/bin/python3
"""
markdown2html.py
This module provides functionality to convert Markdown to HTML, including parsing headings.
"""

import sys
import os

def parse_markdown_line(line):
    """
    Parse a single line of markdown and convert it to HTML.
    Handles heading levels 1 to 6.
    """
    heading_level = 0
    if line.startswith("#"):
        # Count the number of '#' symbols to determine the heading level
        heading_level = len(line.split()[0])  # Number of '#' before the first space
        if 1 <= heading_level <= 6:  # Valid heading levels are from 1 to 6
            return f"<h{heading_level}>{line[heading_level+1:].strip()}</h{heading_level}>"
    
    # If it's not a heading, return the line as is (for now)
    return line.strip()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]
    
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Read the Markdown file and convert it to HTML
    try:
        with open(markdown_file, 'r') as md_file, open(output_file, 'w') as html_file:
            for line in md_file:
                # Parse each line of the markdown file and write the corresponding HTML
                html_line = parse_markdown_line(line)
                html_file.write(html_line + "\n")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    
    sys.exit(0)
