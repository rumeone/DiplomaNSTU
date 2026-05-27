"""
Count prime hexadecimal digits in a given string representation of a hexadecimal number.
"""


def hex_key(num: str) -> int:
    """
    Count the number of hexadecimal digits that are prime numbers.

    The input is a string representing a hexadecimal number (uppercase A-F).
    Returns the count of prime digits.

    Examples:
        hex_key("AB") -> 1
        hex_key("2020") -> 2
    """
    # Prime digits in hexadecimal: 2, 3, 5, 7, B (11), D (13)
    prime_digits = {'2', '3', '5', '7', 'B', 'D'}
    count = 0
    for digit in num:
        if digit in prime_digits:
            count += 1
    return count