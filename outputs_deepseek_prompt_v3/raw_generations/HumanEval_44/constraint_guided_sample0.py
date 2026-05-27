"""
Module for converting integers to string representations in different bases.
"""


def change_base(x: int, base: int) -> str:
    """
    Convert an integer to its string representation in a given base.

    Args:
        x: The integer to convert.
        base: The target base (must be less than 10).

    Returns:
        String representation of x in the specified base.

    Examples:
        >>> change_base(8, 3)
        '22'
        >>> change_base(8, 2)
        '1000'
        >>> change_base(7, 2)
        '111'
    """
    if base < 2 or base >= 10:
        raise ValueError("Base must be between 2 and 9 inclusive")

    if x == 0:
        return "0"

    result = []
    negative = x < 0
    x = abs(x)

    while x > 0:
        remainder = x % base
        result.append(str(remainder))
        x //= base

    if negative:
        result.append("-")

    return "".join(reversed(result))