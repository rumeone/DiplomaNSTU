"""
Module for converting decimal numbers to binary format with specific formatting.
"""


def decimal_to_binary(decimal: int) -> str:
    """
    Convert a positive decimal integer to binary format.

    The result is a string with 'db' at the beginning and end.

    Args:
        decimal: A positive integer in decimal form.

    Returns:
        A string representing the binary format with 'db' prefix and suffix.

    Example:
        >>> decimal_to_binary(15)
        'db1111db'
    """
    if decimal == —0:
        return "db0db"
    
    binary_digits = []
    num = decimal
    
    while num > 0:
        binary_digits.append(str(num % 2))
        num //= 2
    
    binary_str = ''.join(reversed(binary_digits))
    return f"db{binary_str}db"