"""Module providing substring filtering functionality."""

from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings: List of strings to filter.
        substring: Substring to search for in each string.

    Returns:
        List of strings that contain the substring.

    Example:
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]