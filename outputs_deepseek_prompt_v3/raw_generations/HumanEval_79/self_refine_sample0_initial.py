"""
Module for converting decimal numbers to binary format with special formatting.
"""


def decimal_to_binary(decimal: int) -> str:
    """
    Convert a positive decimal integer to binary format.

    The result is formatted with 'db' at both the beginning and end.

    Args:
        decimal: A positive integer in decimal form.

    Returns:
        A string containing the binary representation of the decimal number,
        prefixed and suffixed with 'db'.

    Example:
        >>> decimal_to_binary(15)
        'db1111db'
    """
    binary_str = bin(decimal)[2:]
    return f"db{binary_str}db"