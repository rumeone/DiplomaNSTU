"""
Check if two strings contain the same set of characters.
"""

from collections import Counter


def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.

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
    return Counter(s0) == Counter(s1)