"""
String case manipulation utilities.

This module provides functions for transforming the case of strings.
"""


def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    if not string:
        return string

    result = []
    for char in string:
        if char.islower():
            result.append(char.upper())
        elif char.isupper():
            result.append(char.lower())
        else:
            result.append(char)

    return ''.join(result)