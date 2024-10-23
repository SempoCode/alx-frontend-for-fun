#!/usr/bin/python3
"""
markdown2html.py
This module converts Markdown to HTML, supporting headings, unordered lists, and ordered lists.
"""

import sys
import os

def parse_markdown_line(line, inside_unordered_list, inside_ordered_list):
    """
    Parse a single line of markdown and convert it to HTML.
    Handles heading levels 1 to 6, unordered lists, and ordered lists.
    Returns the HTML-converted line and updated list states (inside_unordered_list, inside_ordered_list).
    """
    line = line.strip()

    # Handle headings
    if line.startswith("#"):
        heading_level = len(line.split()[0])  # Number of '#' before the first space
        if 1 <= heading_level <= 6:
            return f"<h{heading_level}>{line[heading_level+1:].strip()}</h{heading_level}>", inside_unordered_list, inside_ordered_list

    # Handle unordered lists
    if line.startswith("- "):
        list_item = f"<li>{line[2:].strip()}</li>"
        if not inside_unordered_list:
            return f"<ul>\n{list_item}", True, inside_ordered_list  # Start of a new unordered list
        return list_item, True, inside_ordered_list  # Continuing inside an unordered list
    
    # Handle ordered lists
    if line.startswith("* "):
        list_item = f"<li>{line[2:].strip()}</li>"
        if not inside_ordered_list:
            return f"<ol>\n{list_item}", inside_unordered_list, True  # Start of a new ordered list
        return list_item, inside_unordered_list, True  # Continuing inside an ordered list
    
    # If we were inside an unordered list but encounter a non-list item, close the list
    if inside_unordered_list:
        return f"</ul>\n{line}", False, inside_ordered_list

    # If we were inside an ordered list but encounter a non-list item, close the list
    if inside_ordered_list:
        return f"</ol>\n{line}", inside_unordered_list, False

    # If it's not a heading or a list item, return the line as is
    return line, inside_unordered_list, inside_ordered_list

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

    # Read the Markdown file and convert it to HTML
    try:
        with open(markdown_file, 'r') as md_file, open(output_file, 'w') as html_file:
            for line in md_file:
                # Parse each line of the markdown file and write the corresponding HTML
                html_line, inside_unordered_list, inside_ordered_list = parse_markdown_line(
                    line, inside_unordered_list, inside_ordered_list
                )
                html_file.write(html_line + "\n")
            
            # Ensure we close any open lists at the end of the file
            if inside_unordered_list:
                html_file.write("</ul>\n")
            if inside_ordered_list:
                html_file.write("</ol>\n")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    
    sys.exit(0)
