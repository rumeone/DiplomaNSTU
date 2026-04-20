"""
Check if a given integer is the product of three prime numbers (each ≤ 100).
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
    if a <= 0:
        return False

    # Generate list of primes ≤ 100
    primes: List[int] = []
    for num in range(2, 101):
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

    # Try all combinations of three primes
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            for k in range(j, len(primes)):
                if primes[i] * primes[j] * primes[k] == a:
                    return True

    return False