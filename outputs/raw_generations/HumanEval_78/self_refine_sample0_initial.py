def hex_key(num: str) -> int:
    """
    Counts the number of hexadecimal digits that are primes.
    """
    prime_digits = {'2', '3', '5', '7', 'B', 'D'}
    count = 0
    for digit in num:
        if digit in prime_digits:
            count += 1
    return count