"""Utility for comparing character sets of strings."""

def same_chars(s0: str, s1: str) -> bool:
    """Check if two words have the same characters.

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