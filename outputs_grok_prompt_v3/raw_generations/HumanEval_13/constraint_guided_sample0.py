"""Utility module for mathematical functions including GCD computation."""

def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b

    Examples:
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    first = abs(a)
    second = abs(b)
    while second != 0:
        first, second = second, first % second
    return first