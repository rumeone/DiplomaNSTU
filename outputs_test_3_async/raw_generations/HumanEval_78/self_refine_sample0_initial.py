"""
Count prime digits in a hexadecimal number.
"""


def hex_key(num: str) -> int:
    """
    Count the number of hexadecimal digits that are prime numbers.

    Args:
        num: A string representing a hexadecimal number (uppercase A-F).

    Returns:
        The count of prime hexadecimal digits in the number.
    """
    prime_digits = {'2', '3', '5', '7', 'B', 'D'}
    count = 0
    for digit in num:
        if digit in prime_digits:
            count += 1
    return count