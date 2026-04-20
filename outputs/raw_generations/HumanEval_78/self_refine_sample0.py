def hex_key(num: str) -> int:
    """
    Counts the number of hexadecimal digits that are primes.
    """
    prime_digits = {'2', '3', '5', '7', 'B', 'D'}
    return sum(1 for digit in num if digit in prime_digits)