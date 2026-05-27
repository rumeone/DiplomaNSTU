"""
Module for converting numbers between different bases.
"""


def change_base(x: int, base: int) -> str:
    """
    Convert an integer to its string representation in a given base.

    Args:
        x: The integer to convert.
        base: The target base (must be less than 10).

    Returns:
        String representation of x in the given base.

    Examples:
        >>> change_base(8, 3)
        '22'
        >>> change_base(8, 2)
        '1000'
        >>> change_base(7, 2)
        '111'
    """
    if x == 0:
        return "0"

    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9 inclusive")

    is_negative = x < 0
    x = abs(x)

    digits = []
    while x > 0:
        remainder = x % base
        digits.append(str(remainder))
        x //= base

    if is_negative:
        digits.append("-")

    return "".join(reversed(digits))