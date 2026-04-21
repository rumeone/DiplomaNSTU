"""
Module for mathematical operations.
"""


def sum_to_n(n: int) -> int:
    """
    Return the sum of numbers from 1 to n inclusive.

    Args:
        n: A non-negative integer.

    Returns:
        The sum 1 + 2 + ... + n. For n = 0, returns 1.

    Examples:
        >>> sum_to_n(5)
        15
        >>> sum_to_n(10)
        55
        >>> sum_to_n(1)
        1
        >>> sum_to_n(0)
        1
    """
    if n <= 0:
        return 1
    return n * (n + 1) // 2