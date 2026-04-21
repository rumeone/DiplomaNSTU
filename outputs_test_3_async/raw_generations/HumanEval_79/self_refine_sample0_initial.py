"""
Module for converting decimal numbers to binary format with special formatting.
"""


def decimal_to_binary(decimal: int) -> str:
    """
    Convert a positive decimal integer to binary format with 'db' prefix and suffix.

    Args:
        decimal: A positive integer in decimal form.

    Returns:
        A string representing the binary equivalent of the input number,
        prefixed and suffixed with 'db'.

    Example:
        >>> decimal_to_binary(15)
        'db1111db'
    """
    if decimal == 0:
        return "db0db"

    binary_digits = []
    current = decimal

    while current > 0:
        binary_digits.append(str(current % 2))
        current //= 2

    binary_str = ''.join(reversed(binary_digits))
    return f"db{binary_str}db"