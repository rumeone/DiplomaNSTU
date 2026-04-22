"""
Module providing utility function to check if two strings contain exactly the same characters
(with the same frequencies, ignoring order).
"""


def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.

    Returns True if both strings contain exactly the same characters with the same
    frequencies (order does not matter). Returns False otherwise.

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
    if len(s0) != len(s1):
        return False

    # Use sorted strings for comparison - simple and clear
    return sorted(s0) == sorted(s1)