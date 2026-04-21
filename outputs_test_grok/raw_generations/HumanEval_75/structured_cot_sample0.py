"""Module providing function to check if a number is a product of three primes <= 100."""

from itertools import product


def is_multiply_prime(a: int) -> bool:
    """
    Check if the given number is the multiplication of 3 prime numbers.

    Constraints:
        The three prime numbers must be <= 100.

    Example:
        is_multiply_prime(30) == True
        30 = 2 * 3 * 5
    """
    if a < 8:
        return False

    primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
        71, 73, 79, 83, 89, 97
    ]

    for p1, p2, p3 in product(primes, repeat=3):
        if p1 * p2 * p3 == a:
            return True
    return False