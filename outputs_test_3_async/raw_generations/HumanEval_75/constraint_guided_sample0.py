"""
Module containing functions related to prime number operations.
"""

from typing import List


def is_multiply_prime(a: int) -> bool:
    """
    Check if the given number is the multiplication of 3 prime numbers.

    The three prime numbers must be <= 100.

    Args:
        a: The integer to check.

    Returns:
        True if `a` is the product of exactly three prime numbers ≤ 100,
        False otherwise.

    Example:
        >>> is_multiply_prime(30)
        True
        # 30 = 2 * 3 * 5
    """
    if a <= 0:
        return False

    # Generate all primes ≤ 100
    primes: List[int] = []
    for num in range(2, 101):
        is_prime = True
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

    # Try all combinations of three primes
    prime_count = len(primes)
    for i in range(prime_count):
        for j in range(i, prime_count):
            product_ij = primes[i] * primes[j]
            if product_ij > a:
                break
            for k in range(j, prime_count):
                product = product_ij * primes[k]
                if product == a:
                    return True
                if product > a:
                    break

    return False