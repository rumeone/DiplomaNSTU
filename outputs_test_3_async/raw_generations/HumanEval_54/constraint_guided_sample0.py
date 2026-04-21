"""
Module for checking if two strings contain the same set of characters.
"""


def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.

    This function determines whether two strings contain exactly the same
    set of characters, regardless of character frequency or order.

    Examples:
        >>> same_chars('abcd', 'dddddddabc')
        True
        >>> same_chars('dddddddabc', 'abcd')
        True
        >>> same_chars('eabcd', 'dddddddabc')
        False
        >>> same_chars('abcd', 'dddddddabce')
        False

    Args:
        s0: First string to compare.
        s1: Second string to compare.

    Returns:
        True if both strings contain the same set of characters, False otherwise.
    """
    return set(s0) == set(s1)