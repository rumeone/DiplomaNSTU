"""Filter strings by prefix.

This module provides a function to filter a list of strings based on whether
they start with a given prefix.
"""


from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Examples:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    if not prefix:
        return strings[:]

    if not strings:
        return []

    filtered = []
    for s in strings:
        if s.startswith(prefix):
            filtered.append(s)

    return filtered