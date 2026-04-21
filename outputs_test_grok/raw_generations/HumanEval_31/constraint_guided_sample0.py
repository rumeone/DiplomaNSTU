"""Prime number checking utility.

This module provides a function to determine whether a given integer
is a prime number.
"""


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
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    divisor = 5
    while divisor * divisor <= n:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor += 6

    return True