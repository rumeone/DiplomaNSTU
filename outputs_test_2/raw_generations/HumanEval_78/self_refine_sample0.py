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
    prime_digits = {"2", "3", "5", "7", "B", "D"}
    count = 0
    for digit in num:
        if digit in prime_digits:
            count += 1
    return count