"""
String concatenation utilities.

This module provides functions for concatenating strings from collections.
"""

from typing import List


def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings: A list of strings to concatenate.

    Returns:
        A single string containing all input strings concatenated together.

    Example:
        >>> concatenate(['a', 'b', 'c'])
        'abc'
        >>> concatenate([])
        ''
    """
    if not strings:
        return ''
    
    return ''.join(strings)