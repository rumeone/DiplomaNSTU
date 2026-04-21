"""
String filtering utilities.

This module provides functions for filtering strings based on various criteria.
"""

from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings: A list of strings to filter.
        substring: The substring to search for within each string.

    Returns:
        A new list containing only the strings from the input list that contain
        the specified substring.

    Example:
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]