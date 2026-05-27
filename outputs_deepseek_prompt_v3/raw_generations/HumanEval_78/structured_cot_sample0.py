def hex_key(num: str) -> int:
    """
    Count the number of hexadecimal digits in the given string that are prime numbers.

    The function interprets each character as a hexadecimal digit (0-9, A-F) and
    counts how many of these digits represent prime numbers. The primes among
    hexadecimal digits are: 2, 3, 5, 7, 11 (B), 13 (D).

    Args:
        num: A string representing a hexadecimal number. Assumed to be valid
             (only digits 0-9 and uppercase letters A-F) or empty.

    Returns:
        The count of prime hexadecimal digits in the input string.

    Examples:
        >>> hex_key("AB")
        1
        >>> hex_key("2020")
        2
    """
    prime_digits = {'2', '3', '5', '7', 'B', 'D'}
    return sum(1 for digit in num if digit in prime_digits)