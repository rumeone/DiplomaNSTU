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
    # Work with absolute values to handle negative numbers correctly
    absolute_a = abs(a)
    absolute_b = abs(b)

    # Use Euclidean algorithm with early return for zero cases
    if absolute_b == 0:
        return absolute_a

    while absolute_b != 0:
        absolute_a, absolute_b = absolute_b, absolute_a % absolute_b

    return absolute_a