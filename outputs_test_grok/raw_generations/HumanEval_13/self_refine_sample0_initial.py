"""Module providing a function to compute the greatest common divisor of two integers."""


def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b.

    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    # Use absolute values to handle negative numbers correctly
    absolute_a = abs(a)
    absolute_b = abs(b)

    # Early return if either number is zero
    if absolute_a == 0:
        return absolute_b
    if absolute_b == 0:
        return absolute_a

    # Euclidean algorithm using flat control flow
    while absolute_b != 0:
        absolute_a, absolute_b = absolute_b, absolute_a % absolute_b

    return absolute_a