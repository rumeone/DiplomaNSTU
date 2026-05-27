"""Utility functions for integer divisor calculations."""

def largest_divisor(n: int) -> int:
    """
    Find the largest number that divides n evenly, smaller than n.
    Return -1 if such a number does not exist.
    """
    if n <= 1:
        return -1
    for candidate in range(n // 2, 0, -1):
        if n % candidate == 0:
            return candidate
    return -1