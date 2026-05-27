"""
Module for checking if a string is "happy" based on consecutive distinct characters.
"""


def is_happy(s: str) -> bool:
    """
    Check if the string is happy or not.

    A string is happy if its length is at least 3 and every 3 consecutive
    letters are distinct.

    Args:
        s: The input string to check.

    Returns:
        True if the string is happy, False otherwise.

    Examples:
        >>> is_happy("a")
        False
        >>> is_happy("aa")
        False
        >>> is_happy("abcd")
        True
        >>> is_happy("aabb")
        False
    """
    if len(s) < 3:
        return False

    for i in range(len(s) - 2):
        if len(set(s[i:i + 3])) != 3:
            return False

    return True