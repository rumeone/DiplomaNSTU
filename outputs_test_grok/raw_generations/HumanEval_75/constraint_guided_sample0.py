"""
Module for checking if a number is a product of exactly three primes (each <= 100).
"""


def is_multiply_prime(a: int) -> bool:
    """
    Check if the given number is the multiplication of 3 prime numbers.

    Constraints:
        The three prime numbers must be <= 100.

    Example:
        is_multiply_prime(30) == True
        30 = 2 * 3 * 5
    """
    if a < 8:  # Smallest product is 2*2*2
        return False

    # Generate all primes <= 100 using Sieve of Eratosthenes
    is_prime = [True] * 101
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(100**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, 101, i):
                is_prime[j] = False

    primes = [i for i in range(2, 101) if is_prime[i]]

    # Check all combinations of three primes (allowing duplicates)
    for i, p1 in enumerate(primes):
        if p1 * p1 * p1 > a:
            break
        for j in range(i, len(primes)):
            p2 = primes[j]
            if p1 * p2 * p2 > a:
                break
            product_two = p1 * p2
            if product_two > a:
                break
            # Check if the remaining factor is also a prime <= 100
            if a % product_two == 0:
                p3 = a // product_two
                if p3 <= 100 and is_prime[p3]:
                    return True

    return False