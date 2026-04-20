"""Count prime hexadecimal digits in a string representation of a hexadecimal number."""


def hex_key(num: str) -> int:
    """
    Count the number of hexadecimal digits in the given string that are prime numbers.

    Hexadecimal digits are '0'-'9' and 'A'-'F' (always uppercase). The function counts
    how many of these digits represent prime numbers in decimal (2, 3, 5, 7, B=11, D=13).

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
    if not num:
        return 0

    prime_digits = {"2", "3", "5", "7", "B", "D"}
    return sum(1 for digit in num if digit in prime_digits)