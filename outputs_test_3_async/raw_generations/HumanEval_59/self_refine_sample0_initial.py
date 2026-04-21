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
    # Start with the smallest prime factor
    factor = 2
    
    # Divide n by factor as many times as possible
    while factor * factor <= n:
        while n % factor == 0:
            n //= factor
        factor += 1 if factor == 2 else 2  # Check only odd numbers after 2
    
    # If n is still greater than 1, it's the largest prime factor
    return n