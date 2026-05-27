"""
String manipulation utilities for character case transformation.
"""


def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string: The input string to transform.

    Returns:
        A new string with case-flipped characters.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    result_chars = []
    for char in string:
        if char.islower():
            result_chars.append(char.upper())
        elif char.isupper():
            result_chars.append(char.lower())
        else:
            result_chars.append(char)
    return ''.join(result_chars)