"""
Count prime hexadecimal digits in a string representation of a hexadecimal number.
"""


def hex_key(num: str) -> int:
    """
    Count the number of hexadecimal digits in the given string that are prime numbers.

    The function considers hexadecimal digits 0-9 and A-F (always uppercase).
    Prime hexadecimal digits are: 2, 3, 5, 7, B, D.

    Args:
        num: A string representing a hexadecimal number. May be empty.

    Returns:
        The count of prime hexadecimal digits in the input string.

    Examples:
        >>> hex_key("AB")
        1
        >>> hex_key("2020")
        2
    """
    prime_digits = {'2', '3', '5', '7', 'B', 'D'}
    count = 0

    for digit in num:
        if digit in prime_digits:
            count += 1

    return count