"""
Conversion utilities between decimal and binary representations.
"""


def decimal_to_binary(decimal: int) -> str:
    """
    Convert a positive decimal integer to a binary string with 'db' prefix and suffix.

    Example:
        decimal_to_binary(15) == "db1111db"
    """
    if decimal == 0:
        return "db0db"

    binary_digits = []
    number = decimal

    while number > 0:
        binary_digits.append(str(number % 2))
        number //= 2

    # Reverse the digits to get the correct binary representation
    binary_string = ''.join(reversed(binary_digits))
    return f"db{binary_string}db"