"""
helper.py - A Python module for a Helper class handling information retrieval.

Author: Wes Modes
Date: 2023
"""

import logging
import re

# Create a logger instance for the 'lookup' module
logger = logging.getLogger('helper_logger')

def super_strip(string):
    """
    Trim leading/trailing empty lines, remove leading spaces/tabs, and spaces/tabs before triple backticks.
    """

    # strip leading and trailing empty lines and spaces
    string = string.strip()

    # split string into lines
    lines = string.splitlines()

    in_code_block = False
    compiled_lines = []

    # Remove leading and trailing empty lines
    # lines = [line for line in lines if line.strip()]

    for line in lines:
        # strip line to find code blocks
        stripped_line = line.strip()
        # flag when we are in a code block
        if stripped_line.startswith('```') and not in_code_block:
            in_code_block = True
            compiled_lines.append(stripped_line)
        elif stripped_line.endswith('```') and in_code_block:
            in_code_block = False
            compiled_lines.append(line)
        elif in_code_block:
            compiled_lines.append(line)
        else:
            # Remove leading spaces and tabs
            trimmed_line = line.lstrip(' \t')
            # if trimmed_line.count('"') % 2 == 1:
            #     in_code_block = True
            compiled_lines.append(trimmed_line)

    # Join trimmed lines
    trimmed_string = '\n'.join(compiled_lines)

    return trimmed_string

