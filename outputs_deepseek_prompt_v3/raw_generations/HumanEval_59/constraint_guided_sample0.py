"""
Module for finding the largest prime factor of a given integer.
"""


def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.
    Assume n > 1 and is not a prime.

    Examples:
        >>> largest_prime_factor(13195)
        29
        >>> largest_prime_factor(2048)
        2
    """
    original_n = n
    largest_factor = 1

    # Handle factor 2
    while n % 2 == 0:
        largest_factor = 2
        n //= 2

    # Handle odd factors
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest_factor = factor
            n //= factor
        factor += 2

    # If n is still greater than 1, it's a prime factor
    if n > 1:
        largest_factor = n

    return largest_factor