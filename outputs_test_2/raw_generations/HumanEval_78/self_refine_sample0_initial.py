"""
Count prime hexadecimal digits in a string representation of a hexadecimal number.
"""

from typing import Dict


def hex_key(num: str) -> int:
    """
    Count the number of hexadecimal digits in the given string that are prime numbers.

    Args:
        num: A string representing a hexadecimal number (uppercase A-F, digits 0-9).

    Returns:
        The count of prime hexadecimal digits in the input string.

    Examples:
        >>> hex_key("AB")
        1
        >>> hex_key("2020")
        2
    """
    prime_digits: Dict[str, bool] = {
        "2": True,
        "3": True,
        "5": True,
        "7": True,
        "B": True,
        "D": True,
    }

    if not num:
        return 0

    count = 0
    for digit in num:
        if digit in prime_digits:
            count += 1

    return count