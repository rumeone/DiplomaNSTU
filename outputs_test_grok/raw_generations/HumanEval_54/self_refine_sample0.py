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
    if not s0 and not s1:
        return True
    if not s0 or not s1:
        return False

    return set(s0) == set(s1)