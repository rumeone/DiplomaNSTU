"""Mathematical utilities for computing divisors and related operations."""


def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    # Use absolute values to handle negative inputs correctly
    absolute_a = abs(a)
    absolute_b = abs(b)

    # Euclidean algorithm using early return for base case
    while absolute_b != 0:
        absolute_a, absolute_b = absolute_b, absolute_a % absolute_b

    return absolute_a