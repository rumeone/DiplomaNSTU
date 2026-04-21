"""
Module for counting prime hexadecimal digits in a given hex string.
"""


def hex_key(num: str) -> int:
    """
    Based on a hexadecimal number, received as a string,
    counts the number of hexadecimal digits that are primes.

    You may assume the input is always correct or empty string,
    and symbols A,B,C,D,E,F are always uppercase.

    Examples:
        For num = "AB" the output should be 1.
        For num = "2020" the output should be 2.
    """
    if not num:
        return 0

    # Hex digits that represent prime numbers:
    # 2 (2), 3 (3), 5 (5), 7 (7), B (11), D (13)
    prime_hex_digits = {'2', '3', '5', '7', 'B', 'D'}

    count = 0
    for char in num:
        if char in prime_hex_digits:
            count += 1

    return count