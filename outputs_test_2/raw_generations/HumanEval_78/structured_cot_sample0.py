def hex_key(num: str) -> int:
    """
    Count the number of hexadecimal digits in the given string that are prime numbers.

    Args:
        num: A string representing a hexadecimal number (digits 0-9 and A-F uppercase).

    Returns:
        The count of hexadecimal digits that are prime numbers.

    Examples:
        >>> hex_key("AB")
        1
        >>> hex_key("2020")
        2
    """
    prime_digits = {'2', '3', '5', '7', 'B', 'D'}
    return sum(1 for digit in num if digit in prime_digits)