"""Utility for finding largest proper divisors."""

def largest_divisor(n: int) -> int:
    """
    Find the largest number that divides n evenly, smaller than n.
    Return -1 if such a number does not exist.

    Example:
        >>> largest_divisor(15)
        5
    """
    if n <= 1:
        return -1
    for candidate in range(n // 2, 0, -1):
        if n % candidate == 0:
            return candidate
    return -1