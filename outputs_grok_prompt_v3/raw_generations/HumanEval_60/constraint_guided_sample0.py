"""Utility functions for numeric computations."""

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
    return n * (n + 1) // 2