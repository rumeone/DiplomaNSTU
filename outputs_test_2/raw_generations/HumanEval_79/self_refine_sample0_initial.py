"""
Module for converting decimal numbers to binary strings with a special format.
"""


def decimal_to_binary(decimal: int) -> str:
    """
    Convert a positive decimal integer to binary format with 'db' prefix and suffix.

    Args:
        decimal: A positive integer in decimal form.

    Returns:
        A string representing the binary equivalent of the decimal number,
        prefixed and suffixed with 'db'.

    Example:
        >>> decimal_to_binary(15)
        'db1111db'
    """
    if decimal == 0:
        return "db0db"

    binary_digits = []
    while decimal > 0:
        binary_digits.append(str(decimal & 1))
        decimal >>= 1

    binary_digits.reverse()
    return "db" + "".join(binary_digits) + "db"