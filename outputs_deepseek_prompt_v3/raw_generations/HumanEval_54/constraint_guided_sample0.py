"""
Module for checking if two strings have the same characters.
"""


def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.

    The function returns True if both strings contain exactly the same set of
    characters (ignoring duplicates and order), otherwise False.

    Examples:
        >>> same_chars('abcd', 'dddddddabc')
        True
        >>> same_chars('dddddddabc', 'abcd')
        True
        >>> same_chars('eabcd', 'dddddddabc')
        False
        >>> same_chars('abcd', 'dddddddabce')
        False
    """
    return set(s0) == set(s1)