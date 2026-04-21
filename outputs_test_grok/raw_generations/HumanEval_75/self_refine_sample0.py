"""
Module to check if a number is a product of exactly three primes (each <= 100).
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
    if a < 8:  # 2*2*2 is the smallest possible product
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
            for k in range(j, len(primes)):
                p3 = primes[k]
                product = p1 * p2 * p3
                if product == a:
                    return True
                if product > a:
                    break

    return False