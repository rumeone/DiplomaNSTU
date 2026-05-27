def is_prime(n: int) -> bool:
    """
    Check if given number is considered to be prime.

    Examples:
        >>> is_prime(6)
        False
        >>> is_prime(100)
        False
        >>> is_prime(11)
        True
    """
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True