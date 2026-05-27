"""
Count prime hexadecimal digits in a given string representation of a hexadecimal number.
"""


def hex_key(num: str) -> int:
    """
    Count the number of hexadecimal digits in the given string that are prime numbers.

    Hexadecimal digits are: 0-9 and A-F (uppercase).
    Prime hexadecimal digits are: 2, 3, 5, 7, B, D.

    Parameters:
    num (str): The hexadecimal number as a string.

    Returns:
    int: The count of prime hexadecimal digits.
    """
    prime_digits = {'2', '3', '5', '7', 'B', 'D'}
    count = 0
    for digit in num:
        if digit in prime_digits:
            count += 1
    return count