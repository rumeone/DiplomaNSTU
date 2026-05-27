"""
Find the largest divisor of a given integer that is smaller than the integer itself.
"""


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

    for divisor in range(n - 1, 0, -1):
        if n % divisor == 0:
            return divisor

    return -1