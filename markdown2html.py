#!/usr/bin/python3
"""
markdown2html.py
This module converts Markdown to HTML, supporting headings, unordered lists, ordered lists, paragraphs, and line breaks.
"""

import sys
import os

def parse_markdown_line(line, inside_unordered_list, inside_ordered_list, inside_paragraph):
    """
    Parse a single line of markdown and convert it to HTML.
    Handles heading levels 1 to 6, unordered lists, ordered lists, paragraphs, and line breaks.
    Returns the HTML-converted line and updated list and paragraph states.
    """
    line = line.rstrip()

    # Handle headings
    if line.startswith("#"):
        heading_level = len(line.split()[0])  # Number of '#' before the first space
        if 1 <= heading_level <= 6:
            return f"<h{heading_level}>{line[heading_level+1:].strip()}</h{heading_level}>", inside_unordered_list, inside_ordered_list, False

    # Handle unordered lists
    if line.startswith("- "):
        list_item = f"<li>{line[2:].strip()}</li>"
        if not inside_unordered_list:
            return f"<ul>\n{list_item}", True, inside_ordered_list, False  # Start of a new unordered list
        return list_item, True, inside_ordered_list, False  # Continuing inside an unordered list
    
    # Handle ordered lists
    if line.startswith("* "):
        list_item = f"<li>{line[2:].strip()}</li>"
        if not inside_ordered_list:
            return f"<ol>\n{list_item}", inside_unordered_list, True, False  # Start of a new ordered list
        return list_item, inside_unordered_list, True, False  # Continuing inside an ordered list
    
    # Handle paragraph text
    if line != "":  # Non-empty line
        if not inside_paragraph:  # Start of a new paragraph
            return f"<p>\n{line}", inside_unordered_list, inside_ordered_list, True
        else:  # Inside a paragraph, add line break for multiline
            return f"{line}<br />", inside_unordered_list, inside_ordered_list, True

    # If we were inside a paragraph but encounter an empty line, close the paragraph
    if inside_paragraph and line == "":
        return "</p>", inside_unordered_list, inside_ordered_list, False

    # If we were inside an unordered list but encounter an empty line, close the list
    if inside_unordered_list:
        return f"</ul>\n{line}", False, inside_ordered_list, False

    # If we were inside an ordered list but encounter an empty line, close the list
    if inside_ordered_list:
        return f"</ol>\n{line}", inside_unordered_list, False, False

    # If it's an empty line, return it as is (used to separate paragraphs)
    return "", inside_unordered_list, inside_ordered_list, inside_paragraph

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]
    
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    inside_unordered_list = False
    inside_ordered_list = False
    inside_paragraph = False

    # Read the Markdown file and convert it to HTML
    try:
        with open(markdown_file, 'r') as md_file, open(output_file, 'w') as html_file:
            for line in md_file:
                # Parse each line of the markdown file and write the corresponding HTML
                html_line, inside_unordered_list, inside_ordered_list, inside_paragraph = parse_markdown_line(
                    line, inside_unordered_list, inside_ordered_list, inside_paragraph
                )
                if html_line:  # Only write non-empty lines
                    html_file.write(html_line + "\n")
            
            # Ensure we close any open lists or paragraphs at the end of the file
            if inside_unordered_list:
                html_file.write("</ul>\n")
            if inside_ordered_list:
                html_file.write("</ol>\n")
            if inside_paragraph:
                html_file.write("</p>\n")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    
    sys.exit(0)
