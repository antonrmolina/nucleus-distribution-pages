"""
Extract content under '# Protocol' heading and remove MyST directive blocks.
"""

import re
import sys
import os
import subprocess

def extract_protocol_section(content):
    """Extract everything under the '# Protocol' heading."""
    lines = content.split('\n')
    protocol_lines = []
    in_protocol = False
    
    for line in lines:
        # Check if we've reached the Protocol heading
        if line.strip() == '# Protocol':
            in_protocol = True
            protocol_lines.append(line)
            continue
        
        # Stop if we hit another level 1 heading
        if in_protocol and line.startswith('# ') and line.strip() != '# Protocol':
            break
        
        # Collect lines if we're in the Protocol section
        if in_protocol:
            protocol_lines.append(line)
    
    return '\n'.join(protocol_lines)

def remove_myst_directives(content):
    """Remove MyST directive blocks matching :::{} ... ::: or ::::{} ... ::::"""
    # Pattern to match both ::: and :::: style directives
    # Matches ::::{anything on this line} through closing ::::
    # or :::{anything on this line} through closing :::
    
    # First remove 4-colon directives (need to do this first to avoid conflicts)
    pattern_4 = r'::::\{[^}]*\}[^\n]*\n.*?\n::::'
    content = re.sub(pattern_4, '', content, flags=re.DOTALL)
    
    # Then remove 3-colon directives
    pattern_3 = r':::\{[^}]*\}[^\n]*\n.*?\n:::'
    content = re.sub(pattern_3, '', content, flags=re.DOTALL)
    
    # Clean up multiple consecutive blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content

def extract_title_from_filename(filename):
    """Extract title from filename pattern: process-Make_tRNAs.md -> Make tRNAs"""
    # Get basename without extension
    basename = os.path.splitext(os.path.basename(filename))[0]
    
    # Remove the 'process-' or 'process_' prefix
    if basename.startswith('process-'):
        title_raw = basename[8:]  # Remove 'process-'
    elif basename.startswith('process_'):
        title_raw = basename[8:]  # Remove 'process_'
    else:
        title_raw = basename
    
    # Replace underscores and hyphens with spaces
    title_raw = title_raw.replace('_', ' ').replace('-', ' ')
    
    # Smart capitalize: only capitalize words that are all lowercase
    words = title_raw.split()
    title_words = []
    
    for word in words:
        if word.lower() == word:  # All lowercase
            title_words.append(word.capitalize())
        else:  # Has mixed case, preserve it
            title_words.append(word)
    
    return ' '.join(title_words)

def create_output_filename(input_filename):
    """Convert input filename to output filename pattern.
    
    Examples:
        process-some_file_name.md -> protocol-some_file_name.md
        process_Make-tRNAs.md -> protocol_Make-tRNAs.md
    """
    basename = os.path.basename(input_filename)
    
    # Replace 'process' prefix with 'protocol'
    if basename.startswith('process-'):
        output_basename = basename.replace('process-', 'protocol-', 1)
    elif basename.startswith('process_'):
        output_basename = basename.replace('process_', 'protocol_', 1)
    else:
        # If no 'process' prefix, just add 'protocol-' prefix
        output_basename = 'protocol-' + basename
    
    # Get the directory of the input file
    input_dir = os.path.dirname(input_filename)
    
    # Create full output path
    if input_dir:
        output_filename = os.path.join(input_dir, output_basename)
    else:
        output_filename = output_basename
    
    return output_filename

def create_frontmatter(filename):
    """Create YAML frontmatter based on filename."""
    title = extract_title_from_filename(filename)
    
    # Extract the raw title for output filename (remove process- prefix, keep underscores/hyphens)
    basename = os.path.splitext(os.path.basename(filename))[0]
    
    # Remove 'process-' or 'process_' prefix to get the raw output name
    if basename.startswith('process-'):
        title_raw = basename[8:]  # Remove 'process-'
    elif basename.startswith('process_'):
        title_raw = basename[8:]  # Remove 'process_'
    else:
        title_raw = basename
    
    frontmatter = f"""---
title: {title}
exports:
  - format: typst
    template: https://github.com/antonrmolina/nucleus-typst-test/archive/refs/heads/main.zip
    output: protocol-{title_raw}.pdf
---

"""
    return frontmatter
    
# def fix_url_underscores(content):
#     """URL-encode underscores in links."""
#     def encode_underscores(match):
#         text = match.group(1)
#         url = match.group(2)
        
#         # Replace underscores with %5F (URL encoding)
#         url = url.replace('_', '%5F')
#         return f'[{text}]({url})'
    
#     content = re.sub(r'\[([^\]]+)\]\((https?://[^\)]+)\)', encode_underscores, content)
#     return content

# def convert_to_typst_links(content):
#     """Convert markdown links to Typst link() syntax for URLs with underscores."""
#     def to_typst_link(match):
#         text = match.group(1)
#         url = match.group(2)
        
#         # Only convert http/https links
#         if url.startswith('http://') or url.startswith('https://'):
#             # Use Typst's link function: #link("url")[text]
#             return f'#link("{url}")[{text}]'
#         return match.group(0)
    
#     content = re.sub(r'\[([^\]]+)\]\((https?://[^\)]+)\)', to_typst_link, content)
#     return content

def remove_links(content):
    """Remove all markdown links with http/https URLs, keeping only the display text."""
    # Pattern matches [text](http://url) or [text](https://url)
    # Replaces with just the text
    content = re.sub(r'\[([^\]]+)\]\(https?://[^\)]+\)', r'\1', content)
    return content

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <markdown_file>")
        sys.exit(1)
    
    input_filename = sys.argv[1]
    
    try:
        with open(input_filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract Protocol section
        protocol_section = extract_protocol_section(content)
        
        if not protocol_section:
            print("Warning: No '# Protocol' heading found in the file.")
            sys.exit(1)
        
        # Remove MyST directives
        cleaned_content = remove_myst_directives(protocol_section)

        # Remove all HTTP/HTTPS links
        cleaned_content = remove_links(cleaned_content)
        
        # Create frontmatter
        frontmatter = create_frontmatter(input_filename)
        
        # Combine frontmatter and cleaned content
        output_content = frontmatter + cleaned_content
        
        # Generate output filename
        output_filename = create_output_filename(input_filename)
        
        # Write to output file
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(output_content)
        
        print(f"✓ Successfully processed: {input_filename}")
        print(f"  Output written to: {output_filename}")
        print(f"\nTo build PDF, run:")
        print(f"  myst build {output_filename} --pdf")
        
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()