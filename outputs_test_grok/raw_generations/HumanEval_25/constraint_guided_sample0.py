"""Factorization utilities for positive integers.

This module provides a function to compute the prime factorization
of a given integer, returning each prime factor with its multiplicity.
"""


from typing import List


def factorize(n: int) -> List[int]:
    """
    Return a list of prime factors of the given integer in the order of smallest to largest.
    Each of the factors should be listed as often as it appears in the factorization.
    The input number should be equal to the product of all factors.

    Examples:
        >>> factorize(8)
        [2, 2, 2]
        >>> factorize(25)
        [5, 5]
        >>> factorize(70)
        [2, 5, 7]
    """
    if n <= 1:
        return []

    factors: List[int] = []
    # Handle factor 2 separately to simplify the loop
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Check for odd factors
    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 2

    # If n is a prime number greater than 2
    if n > 1:
        factors.append(n)

    return factors