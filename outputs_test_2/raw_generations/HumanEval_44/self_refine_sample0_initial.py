"""
Module for converting integers to string representations in different bases.
"""


def change_base(x: int, base: int) -> str:
    """
    Convert an integer to its string representation in a given base.

    The base must be less than 10. The function handles positive integers
    and returns the appropriate string representation.

    Args:
        x: The integer to convert.
        base: The target base (must be less than 10).

    Returns:
        A string representing the number in the given base.

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

    digits = []
    while x > 0:
        digits.append(str(x % base))
        x //= base

    return ''.join(reversed(digits))