"""Find the longest string in a list of strings."""

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
    max_length = len(longest_string)

    for string in strings[1:]:
        current_length = len(string)
        if current_length > max_length:
            longest_string = string
            max_length = current_length

    return longest_string