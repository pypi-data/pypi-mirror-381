#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Text utilities for proper alignment with CJK characters
"""

import unicodedata


def get_display_width(text: str) -> int:
    """
    Calculate the display width of text, considering CJK characters as double width.
    
    Args:
        text: Input text string
        
    Returns:
        Display width in terminal columns
    """
    if not text:
        return 0
    
    width = 0
    for char in text:
        # Check if character is CJK (Chinese, Japanese, Korean)
        if unicodedata.east_asian_width(char) in 'WF':
            width += 2
        else:
            width += 1
    return width


def pad_string(text: str, width: int, align: str = 'left', pad_char: str = ' ') -> str:
    """
    Pad string to specified display width with proper CJK handling.
    
    Args:
        text: Text to pad
        width: Target display width
        align: 'left', 'right', or 'center'
        pad_char: Character to use for padding
        
    Returns:
        Padded string with correct display width
    """
    if not text:
        text = ""
    
    current_width = get_display_width(text)
    if current_width >= width:
        return text
    
    pad_width = width - current_width
    
    if align == 'right':
        return pad_char * pad_width + text
    elif align == 'center':
        left_pad = pad_width // 2
        right_pad = pad_width - left_pad
        return pad_char * left_pad + text + pad_char * right_pad
    else:  # left
        return text + pad_char * pad_width


def create_aligned_table(headers: list, data_rows: list, alignments: list = None) -> str:
    """
    Create a properly aligned table that handles CJK characters correctly.
    
    Args:
        headers: List of header strings
        data_rows: List of data rows (each row is a list of strings)
        alignments: List of alignments ('left', 'right', 'center') for each column
        
    Returns:
        Formatted table as string
    """
    if not headers:
        return ""
    
    if alignments is None:
        # Default: headers left-aligned, data right-aligned except for text columns
        alignments = ['left'] * len(headers)
        # For data, right-align numeric columns (columns 1, 2, 3, 4, 5 in our case)
        if data_rows:
            alignments = ['left'] + ['right'] * (len(headers) - 1)
    
    # Calculate column widths based on display width
    col_widths = []
    for i, header in enumerate(headers):
        max_width = get_display_width(str(header))
        for row in data_rows:
            if i < len(row):
                cell_width = get_display_width(str(row[i]))
                max_width = max(max_width, cell_width)
        col_widths.append(max_width)
    
    # Create separator line
    separator = "+" + "+".join("-" * (width + 2) for width in col_widths) + "+"
    
    # Create header row
    header_row = "|"
    for i, header in enumerate(headers):
        padded_header = pad_string(str(header), col_widths[i], alignments[i])
        header_row += f" {padded_header} |"
    
    # Create data rows
    data_rows_formatted = []
    for row in data_rows:
        data_row = "|"
        for i, cell in enumerate(row):
            if i < len(alignments):
                alignment = alignments[i]
            else:
                alignment = 'right' if i > 0 else 'left'
            padded_cell = pad_string(str(cell), col_widths[i], alignment)
            data_row += f" {padded_cell} |"
        data_rows_formatted.append(data_row)
    
    # Combine all parts
    table_lines = [separator, header_row, separator]
    table_lines.extend(data_rows_formatted)
    table_lines.append(separator)
    
    return "\n".join(table_lines)
    