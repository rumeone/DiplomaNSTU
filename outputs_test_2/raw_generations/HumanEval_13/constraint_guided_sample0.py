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
        The greatest common divisor of a and b.

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
    # Handle the case where both numbers are zero
    if a == 0 and b == 0:
        return 0

    # Ensure both numbers are non-negative for the Euclidean algorithm
    a = abs(a)
    b = abs(b)

    # Euclidean algorithm
    while b != 0:
        a, b = b, a % b

    return a