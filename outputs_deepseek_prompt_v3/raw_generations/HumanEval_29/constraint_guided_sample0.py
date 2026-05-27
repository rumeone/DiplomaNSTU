"""
Module for filtering strings based on prefix matching.
"""

from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings: List of strings to filter.
        prefix: The prefix to match against.

    Returns:
        List of strings that start with the given prefix.

    Examples:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    if not strings:
        return []

    return [s for s in strings if s.startswith(prefix)]