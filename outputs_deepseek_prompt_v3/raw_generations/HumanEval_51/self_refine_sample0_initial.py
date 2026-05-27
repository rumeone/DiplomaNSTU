"""
Module for text processing utilities.
"""


def remove_vowels(text: str) -> str:
    """
    Return the text without vowels (a, e, i, o, u).

    Vowel removal is case-insensitive: both uppercase and lowercase
    vowels are removed.

    Args:
        text: The input string to process.

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