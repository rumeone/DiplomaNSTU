"""
Return the n-th Fibonacci number that is also prime.
"""

import math
from typing import Generator


def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    limit = int(math.isqrt(num)) + 1
    for divisor in range(3, limit, 2):
        if num % divisor == 0:
            return False
    return True


def fibonacci_generator() -> Generator[int, None, None]:
    """Generate Fibonacci numbers indefinitely."""
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a


def prime_fib(n: int) -> int:
    """Return the n-th Fibonacci number that is also prime.

    Args:
        n: The position in the sequence of prime Fibonacci numbers (1-indexed).

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
    fib_gen = fibonacci_generator()

    while True:
        candidate = next(fib_gen)
        if is_prime(candidate):
            count += 1
            if count == n:
                return candidate