"""Utilities for prime factorization."""

def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n.

    Assume n > 1 and is not a prime.
    """
    largest_factor = 1

    while n % 2 == 0:
        largest_factor = 2
        n //= 2

    candidate = 3
    while candidate * candidate <= n:
        while n % candidate == 0:
            largest_factor = candidate
            n //= candidate
        candidate += 2

    if n > 1:
        largest_factor = n

    return largest_factor