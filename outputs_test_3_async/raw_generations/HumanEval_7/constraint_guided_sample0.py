"""Filter strings by substring presence.

This module provides a function to filter a list of strings,
keeping only those that contain a specified substring.
"""

from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """Filter an input list of strings only for ones that contain given substring.

    Args:
        strings: A list of strings to filter.
        substring: The substring to search for in each string.

    Returns:
        A new list containing only the strings from the input list
        that contain the specified substring.

    Example:
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    if not strings or not substring:
        return []

    filtered_strings = []
    for string in strings:
        if substring in string:
            filtered_strings.append(string)

    return filtered_strings