"""
Module for performing circular shift operations on integer digits.
"""


def circular_shift(x: int, shift: int) -> str:
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x: The integer whose digits will be shifted.
        shift: The number of positions to shift right.

    Returns:
        The result of the circular shift as a string.

    Examples:
        >>> circular_shift(12, 1)
        "21"
        >>> circular_shift(12, 2)
        "12"
    """
    digits = str(x)
    num_digits = len(digits)

    if shift > num_digits:
        return digits[::-1]

    if shift == 0:
        return digits

    split_point = num_digits - shift
    return digits[split_point:] + digits[:split_point]