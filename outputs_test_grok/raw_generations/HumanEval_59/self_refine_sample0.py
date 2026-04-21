"""
Module providing a function to find the largest prime factor of an integer.
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

    # n is now odd; try odd factors from 3 upwards
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest_factor = factor
            n //= factor
        factor += 2

    # If n is still greater than 2, it is a prime factor
    if n > 2:
        largest_factor = n

    return largest_factor