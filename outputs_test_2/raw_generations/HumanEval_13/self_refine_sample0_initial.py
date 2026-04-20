"""
Module providing a function to compute the greatest common divisor of two integers.
"""


def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    Uses the Euclidean algorithm to efficiently compute the GCD.

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
        >>> greatest_common_divisor(0, 5)
        5
        >>> greatest_common_divisor(0, 0)
        0
    """
    # Handle edge case where both numbers are zero
    if a == 0 and b == 0:
        return 0

    # Ensure non-negative values for Euclidean algorithm
    x, y = abs(a), abs(b)

    # Euclidean algorithm
    while y != 0:
        x, y = y, x % y

    return x