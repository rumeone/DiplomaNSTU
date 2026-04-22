"""
Circular shift implementation for integer digits.

This module provides a function to perform circular shifts on the digits
of an integer and return the result as a string.
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
    if x == 0:
        return "0"

    # Convert to string for digit manipulation
    digits = str(abs(x))
    num_digits = len(digits)

    # If shift is greater than number of digits, return reversed
    if shift > num_digits:
        reversed_digits = digits[::-1]
        return reversed_digits if x >= 0 else "-" + reversed_digits

    # Normalize shift to be within 0 to num_digits
    effective_shift = shift % num_digits
    if effective_shift == 0:
        result = digits
    else:
        # Right circular shift: last 'effective_shift' digits move to front
        result = digits[-effective_shift:] + digits[:-effective_shift]

    # Add sign if original number was negative
    if x < 0:
        result = "-" + result

    return result