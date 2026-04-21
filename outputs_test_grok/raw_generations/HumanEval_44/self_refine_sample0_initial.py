"""
Convert a number to a different base (less than 10) and return as string.
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
    current = x
    while current > 0:
        digits.append(str(current % base))
        current //= base

    # Reverse the digits to get the correct order
    return ''.join(reversed(digits))