"""
String case manipulation utilities.
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

    result_chars = []
    for char in string:
        if char.islower():
            result_chars.append(char.upper())
        elif char.isupper():
            result_chars.append(char.lower())
        else:
            result_chars.append(char)

    return ''.join(result_chars)