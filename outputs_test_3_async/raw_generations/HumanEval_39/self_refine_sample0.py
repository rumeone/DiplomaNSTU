"""
Module for generating prime Fibonacci numbers.
"""

import math


def prime_fib(n: int) -> int:
    """
    Return the n-th number that is both a Fibonacci number and prime.

    Args:
        n: Positive integer indicating the position in the sequence of prime
           Fibonacci numbers.

    Returns:
        The n-th prime Fibonacci number.

    Examples:
        >>> prime_fib(1)
        2
        >>> prime_fib(2)
        3
        >>> prime_fib(3)
        5
        >>> prime_fib(4)
        13
        >>> prime_fib(5)
        89
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")

    count = 0
    a, b = 0, 1

    while True:
        a, b = b, a + b
        if a < 2:
            continue

        if is_prime(a):
            count += 1
            if count == n:
                return a


def is_prime(num: int) -> bool:
    """
    Check if a number is prime.

    Args:
        num: Integer to check for primality.

    Returns:
        True if num is prime, False otherwise.
    """
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    limit = int(math.sqrt(num)) + 1
    for divisor in range(3, limit, 2):
        if num % divisor == 0:
            return False
    return True