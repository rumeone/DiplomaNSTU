"""
Module providing mathematical utility functions.
"""


def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    Uses the Euclidean algorithm to compute the GCD efficiently.

    Args:
        a: First integer
        b: Second integer

    Returns:
        The greatest common divisor of a and b

    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
        >>> greatest_common_divisor(48, 18)
        6
    """
    if a == 0 and b == 0:
        return 0

    a = abs(a)
    b = abs(b)

    while b != 0:
        a, b = b, a % b

    return a