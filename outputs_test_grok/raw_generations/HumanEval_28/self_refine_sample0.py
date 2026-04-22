"""Utility functions for string operations."""

from typing import List


def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Example:
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    if not strings:
        return ""

    return "".join(strings)