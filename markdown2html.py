#!/usr/bin/python3
"""
markdown2html.py
This module provides functionality to convert Markdown to HTML, including parsing headings and unordered lists.
"""

import sys
import os

def parse_markdown_line(line, inside_list):
    """
    Parse a single line of markdown and convert it to HTML.
    Handles heading levels 1 to 6 and unordered lists.
    Returns the HTML-converted line and a boolean indicating if it's inside a list.
    """
    line = line.strip()

    # Handle headings
    if line.startswith("#"):
        heading_level = len(line.split()[0])  # Number of '#' before the first space
        if 1 <= heading_level <= 6:
            return f"<h{heading_level}>{line[heading_level+1:].strip()}</h{heading_level}>", inside_list

    # Handle unordered lists
    if line.startswith("- "):
        list_item = f"<li>{line[2:].strip()}</li>"
        if not inside_list:
            return f"<ul>\n{list_item}", True  # Start of a new list
        return list_item, True  # Continuing inside a list
    
    # If we were inside a list but encounter a non-list item, close the list
    if inside_list:
        return f"</ul>\n{line}", False

    # If it's not a heading or a list item, return the line as a paragraph or as is
    return line, inside_list

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]
    
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    inside_list = False

    # Read the Markdown file and convert it to HTML
    try:
        with open(markdown_file, 'r') as md_file, open(output_file, 'w') as html_file:
            for line in md_file:
                # Parse each line of the markdown file and write the corresponding HTML
                html_line, inside_list = parse_markdown_line(line, inside_list)
                html_file.write(html_line + "\n")
            
            # Ensure we close any open lists at the end of the file
            if inside_list:
                html_file.write("</ul>\n")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    
    sys.exit(0)
