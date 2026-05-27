"""
String filtering utility functions.

This module provides functions for filtering lists of strings based on
various criteria, such as substring presence.
"""

from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings: List of strings to filter.
        substring: Substring to search for within each string.

    Returns:
        List of strings from the input that contain the specified substring.

    Example:
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    if not strings:
        return []

    if not substring:
        return strings

    return [s for s in strings if substring in s]