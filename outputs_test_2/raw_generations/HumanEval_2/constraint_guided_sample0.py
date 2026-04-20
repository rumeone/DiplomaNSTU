"""
Module for truncating floating point numbers to their decimal parts.
"""


def truncate_number(number: float) -> float:
    """
    Return the decimal part of a positive floating point number.

    The function decomposes a positive floating point number into its integer
    part (largest integer smaller than the given number) and its decimal part
    (leftover part always smaller than 1). Only the decimal part is returned.

    Parameters
    ----------
    number : float
        A positive floating point number.

    Returns
    -------
    float
        The decimal part of the input number.

    Examples
    --------
    >>> truncate_number(3.5)
    0.5
    >>> truncate_number(7.0)
    0.0
    >>> truncate_number(12.345)
    0.345
    """
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part