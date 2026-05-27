"""
Module for mathematical operations.
"""


def sum_to_n(n: int) -> int:
    """
    Sum numbers from 1 to n.

    Args:
        n: The upper bound of the summation (inclusive).

    Returns:
        The sum of integers from 1 to n. Returns 1 for n <= 0.

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