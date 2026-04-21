"""
Module for converting decimal numbers to binary strings with formatting.
"""


def decimal_to_binary(decimal: int) -> str:
    """
    Convert a positive decimal integer to binary string format.

    The binary representation is surrounded by 'db' characters at both ends.

    Args:
        decimal: Positive integer in decimal system.

    Returns:
        Binary representation of the decimal number with 'db' prefix and suffix.

    Example:
        >>> decimal_to_binary(15)
        'db1111db'
    """
    if decimal == 0:
        return "db0db"

    binary_digits = []
    current_number = decimal

    while current_number > 0:
        remainder = current_number % 2
        binary_digits.append(str(remainder))
        current_number //= 2

    binary_digits.reverse()
    binary_string = "".join(binary_digits)

    return f"db{binary_string}db"