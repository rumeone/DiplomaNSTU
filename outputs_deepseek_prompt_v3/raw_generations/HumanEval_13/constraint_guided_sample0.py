"""Module providing a function to compute the greatest common divisor of two integers."""


def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    Uses the Euclidean algorithm to compute the GCD efficiently.

    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)