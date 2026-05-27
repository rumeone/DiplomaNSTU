"""
Module for string manipulation functions.
"""


def remove_vowels(text: str) -> str:
    """
    Return the text without vowels (a, e, i, o, u).

    Args:
        text: The input string.

    Returns:
        The input string with all vowels removed.

    Examples:
        >>> remove_vowels('abcdef')
        'bcdf'
        >>> remove_vowels('aaaaa')
        ''
        >>> remove_vowels('aaBAA')
        'B'
        >>> remove_vowels('zbcd')
        'zbcd'
    """
    vowels = "aeiouAEIOU"
    return "".join(char for char in text if char not in vowels)