"""
Module for finding the largest divisor of a given integer.
"""


def largest_divisor(n: int) -> int:
    """
    Find the largest number that divides n evenly, smaller than n.
    Return -1 if such a number does not exist.

    Args:
        n: The integer to find the largest divisor for.

    Returns:
        The largest divisor of n that is less than n, or -1 if none exists.

    Examples:
        >>> largest_divisor(15)
        5
        >>> largest_divisor(7)
        -1
        >>> largest_divisor(1)
        -1
    """
    if n <= 1:
        return -1

    # Start from n//2 and go downwards
    for divisor in range(n // 2, 0, -1):
        if n % divisor == 0:
            return divisor

    # This line should never be reached for n > 1,
    # but return -1 as a fallback
    return -1