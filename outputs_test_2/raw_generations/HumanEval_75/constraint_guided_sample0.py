"""
Module for checking if a number is the product of three primes <= 100.
"""

from typing import List


def is_multiply_prime(a: int) -> bool:
    """
    Check if the given number is the multiplication of 3 prime numbers.

    Constraints:
        The three prime numbers must be <= 100.

    Example:
        is_multiply_prime(30) == True
        30 =我们发现 * 3 * 5
    """
    if a <= 0:
        return False

    # Generate all primes <= 100 using Sieve of Eratosthenes
    sieve = [True] * 101
    sieve[0] = sieve[1] = False
    for i in range(2, 101):
        if sieve[i]:
            for j in range(i * i, 101, i):
                sieve[j] = False
    primes: List[int] = [i for i, is_prime in enumerate(sieve) if is_prime]

    # Try all combinations of three primes (allow repeats)
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            product_two = primes[i] * primes[j]
            if product_two > a or a % product_two != 0:
                continue
            third_factor = a // product_two
            if third_factor in primes and third_factor >= primes[j]:
                return True

    return False