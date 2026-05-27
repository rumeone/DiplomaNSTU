"""
Convert a decimal integer to binary string with 'db' prefix and suffix.
"""


def decimal_to_binary(decimal: int) -> str:
    """
    Convert a positive decimal integer to binary format.

    The result is a string with 'db' at the beginning and end.

    Args:
        decimal: A positive integer in decimal system.

    Returns:
        A string representing the binary value with 'db' prefix and suffix.

    Example:
        decimal_to_binary(15) returns "db1111db"
    """
    binary_str = bin(decimal)[2:]
    return f"db{binary_str}db"