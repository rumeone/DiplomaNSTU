"""Module providing a function to find the longest string in a list."""

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

    longest_string = strings[0]
    for string in strings[1:]:
        if len(string) > len(longest_string):
            longest_string = string

    return longest_string