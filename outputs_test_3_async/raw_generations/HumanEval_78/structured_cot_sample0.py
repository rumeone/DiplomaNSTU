def hex_key(num: str) -> int:
    """
    Count the number of hexadecimal digits in the given string that are prime.

    The input is a valid hexadecimal string (empty string allowed). Digits A-F
    are uppercase. Prime hexadecimal digits: 2, 3, 5, 7, B, D (11 and 13 in decimal).

    Args:
        num: Hexadecimal number as a string.

    Returns:
        Number of prime hexadecimal digits in the string.
    """
    primes = {'2', '3', '5', '7', 'B', 'D'}
    return sum(1 for digit in num if digit in primes)