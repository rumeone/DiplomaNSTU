"""
Module providing base conversion utilities for integers.
"""


def change_base(x: int, base: int) -> str:
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Examples:
        >>> change_base(8, 3)
        '22'
        >>> change_base(8, 2)
        '1000'
        >>> change_base(7, 2)
        '111'
    """
    if x == 0:
        return '0'

    digits = []
    current = abs(x)

    while current > 0:
        digits.append(str(current % base))
        current //= base

    digits.reverse()
    result = ''.join(digits)

    return result if x >= 0 else '-' + result