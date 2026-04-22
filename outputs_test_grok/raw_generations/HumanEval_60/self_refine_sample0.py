"""
Module providing utility functions for mathematical computations.

This module contains the sum_to_n function which calculates the sum
of integers from 1 to n (inclusive).
"""


def sum_to_n(n: int) -> int:
    """
    sum_to_n is a function that sums numbers from 1 to n.

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
    if n < 1:
        return 1

    total = 0
    for i in range(1, n + 1):
        total += i
    return total