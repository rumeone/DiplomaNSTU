"""
Module for performing circular shift operations on integer digits.
"""


def circular_shift(x: int, shift: int) -> str:
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Examples:
        >>> circular_shift(12, 1)
        "21"
        >>> circular_shift(12, 2)
        "12"
    """
    digits = str(x)
    digit_count = len(digits)

    if shift > digit_count:
        return digits[::-1]

    split_point = digit_count - shift
    right_part = digits[split_point:]
    left_part = digits[:split_point]
    return right_part + left_part