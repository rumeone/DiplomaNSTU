"""
Check if a number is the product of exactly three prime numbers, each <= 100.
"""

from typing import List


def is_multiply_prime(a: int) -> bool:
    """
    Check if the given number is the multiplication of 3 prime numbers.

    Constraints:
        The three prime numbers must be <= 100.

    Example:
        is_multiply_prime(30) == True
        30 = 2 * 3 * 5
    """
    if a <= 1:
        return False

    # Generate primes up to 100 using Sieve of Eratosthenes
    sieve = [True] * 101
    sieve[0] = sieve[1] = False
    for i in range(2, int(101 ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, 101, i):
                sieve[j] = False
    primes: List[int] = [i for i, is_prime in enumerate(sieve) if is_prime]

    # Try all combinations of three primes
    n_primes = len(primes)
    for i in range(n_primes):
        p1 = primes[i]
        if p1 * p1 * p1 > a:
            break
        for j in range(i, n_primes):
            p2 = primes[j]
            if p1 * p2 * p2 > a:
                break
            for k in range(j, n_primes):
                p3 = primes[k]
                product = p1 * p2 * p3
                if product > a:
                    break
                if product == a:
                    return True
    return False