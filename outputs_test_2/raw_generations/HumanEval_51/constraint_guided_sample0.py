"""
Module for string manipulation functions.
"""


def remove_vowels(text: str) -> str:
    """
    Return the text without vowels (a, e, i, o, u).

    The function removes both lowercase and uppercase vowels.

    Args:
        text: The input string from which vowels will be removed.

    Returns:
        A new string with all vowels removed.

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