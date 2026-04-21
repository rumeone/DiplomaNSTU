"""
Prime number checking utility.
"""

from typing import Optional


def is_prime(n: int) -> bool:
    """
    Check if given number is considered to be prime.

    A prime number is a natural number greater than 1 that has no positive
    divisors other than 1 and itself.

    Args:
        n: The integer to check.

    Returns:
        True if n is prime, False otherwise.

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

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True