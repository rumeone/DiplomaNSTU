"""Module providing functions for finding the longest string in a list."""

from typing import List


def longest(strings: List[str]) -> str:
    """
    Return the longest string from a list of strings.

    If multiple strings have the same maximum length, return the first one.
    For empty lists or other edge cases, return an empty string.

    Args:
        strings: A list of strings to search through.

    Returns:
        The longest string from the list, or an empty string if no valid string is found.

    Examples:
        >>> longest(['a', 'b', 'c'])
        'a'
        >>> longest(['a', 'bb', 'ccc'])
        'ccc'
        >>> longest([])
        ''
        >>> longest(['same', 'size', 'word'])
        'same'
    """
    if not strings:
        return ''

    longest_string = strings[0]
    max_length = len(longest_string)

    for current_string in strings[1:]:
        current_length = len(current_string)
        if current_length > max_length:
            longest_string = current_string
            max_length = current_length

    return longest_string