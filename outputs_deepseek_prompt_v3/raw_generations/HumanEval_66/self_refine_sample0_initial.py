"""
Module for calculating the sum of ASCII codes of uppercase characters in a string.
"""


def digitSum(s: str) -> int:
    """
    Return the sum of ASCII codes of uppercase characters in the given string.

    Args:
        s: Input string.

    Returns:
        Sum of ASCII codes of uppercase characters. Returns 0 for empty string.
    """
    total = 0
    for char in s:
        if char.isupper():
            total += ord(char)
    return total