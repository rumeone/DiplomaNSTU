"""Prime number checking utilities."""

def is_prime(n: int) -> bool:
    """Check if given number is considered to be prime.

    Examples:
        >>> is_prime(6)
        False
        >>> is_prime(100)
        False
        >>> is_prime(11)
        True
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for divisor in range(3, int(n**0.5) + 1, 2):
        if n % divisor == 0:
            return False
    return True