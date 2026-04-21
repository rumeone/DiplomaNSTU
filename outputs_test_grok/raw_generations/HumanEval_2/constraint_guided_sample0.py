"""
This module provides utility functions for working with floating-point numbers,
including decomposition into integer and fractional parts.
"""


def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Return the decimal part of the number.

    Example:
        >>> truncate_number(3.5)
        0.5
    """
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part