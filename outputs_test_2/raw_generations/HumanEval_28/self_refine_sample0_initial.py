"""String concatenation utilities."""

from typing import List


def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings: List of strings to concatenate.

    Returns:
        Concatenated string.

    Example:
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    if not strings:
        return ''
    
    return ''.join(strings)