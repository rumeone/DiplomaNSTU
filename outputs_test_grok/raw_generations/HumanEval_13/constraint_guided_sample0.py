"""
Module providing mathematical utility functions, including
greatest common divisor calculation using the Euclidean algorithm.
"""


def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    # Handle negative numbers by working with absolute values
    a = abs(a)
    b = abs(b)

    # Use Euclidean algorithm with early return for zero cases
    while b != 0:
        a, b = b, a % b

    return a