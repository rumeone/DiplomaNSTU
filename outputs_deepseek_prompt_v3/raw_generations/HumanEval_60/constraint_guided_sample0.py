"""
Module providing mathematical summation functions.
"""


def sum_to_n(n: int) -> int:
    """
    Return the sum of all integers from 1 to n inclusive.

    For n <= 0, returns 1 as specified in the examples.

    Args:
        n: The upper bound of the summation range.

    Returns:
        The sum of integers from 1 to n, or 1 if n <= 0.

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