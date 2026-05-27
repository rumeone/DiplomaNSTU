"""
Module providing a function to find the longest string in a list.
"""

from typing import List


def longest(strings: List[str]) -> str:
    """
    Out of a list of strings, return the longest one.
    Return the first one in case of multiple strings of the same length.
    Return an empty string for edge cases.

    Examples:
        >>> longest(['a', 'b', 'c'])
        'a'
        >>> longest(['a', 'bb', 'ccc'])
        'ccc'
    """
    if not strings:
        return ""

    current_longest = strings[0]
    for candidate in strings[1:]:
        if len(candidate) > len(current_longest):
            current_longest = candidate
    return current_longest