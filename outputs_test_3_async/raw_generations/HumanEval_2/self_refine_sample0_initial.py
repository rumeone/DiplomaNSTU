"""
Module for truncating floating point numbers to their decimal parts.
"""


def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, return its decimal part.

    The decimal part is defined as the leftover part after removing the
    integer part (largest integer smaller than the given number).

    Args:
        number: A positive floating point number.

    Returns:
        The decimal part of the number, which is always smaller than 1.

    Example:
        >>> truncate_number(3.5)
        0.5
    """
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part