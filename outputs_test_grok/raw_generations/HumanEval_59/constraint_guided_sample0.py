"""
Module providing functions for finding prime factors of integers.
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
    # Start by dividing out all factors of 2
    while n % 2 == 0:
        largest_factor = 2
        n //= 2

    # n is now odd; try odd factors from 3 up to sqrt(n)
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest_factor = factor
            n //= factor
        factor += 2

    # If n is a prime number greater than 2, it is the largest prime factor
    if n > 2:
        largest_factor = n

    return largest_factor