"""String concatenation utilities."""

from typing import List


def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings: A list of strings to concatenate.

    Returns:
        A single string resulting from concatenating all input strings.
        Returns an empty string if the input list is empty.

    Example:
        >>> concatenate(['a', 'b', 'c'])
        'abc'
        >>> concatenate([])
        ''
    """
    if not strings:
        return ''
    
    return ''.join(strings)