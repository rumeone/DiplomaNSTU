"""
String length calculation utility.

This module provides a function to calculate the length of a string.
"""


def strlen(string: str) -> int:
    """
    Return the length of the given string.

    Args:
        string: The input string whose length is to be calculated.

    Returns:
        The length of the input string.

    Example:
        >>> strlen('abc')
        3
        >>> strlen('')
        0
        >>> strlen('hello world')
        11
    """
    return len(string)