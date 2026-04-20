from typing import Generator
import math


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

    limit = int(math.isqrt(num)) + 1
    for divisor in range(3, limit, 2):
        if num % divisor == 0:
            return False
    return True


def fibonacci_generator() -> Generator[int, None, None]:
    """
    Generate Fibonacci numbers indefinitely.

    Yields:
        Fibonacci numbers starting from 1, 1, 2, ...
    """
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def prime_fib(n: int) -> int:
    """
    Return the n-th number that is both a Fibonacci number and prime.

    Args:
        n: Positive integer indicating the position in the sequence.

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
        raise ValueError("n must be positive")

    count = 0
    fib_gen = fibonacci_generator()

    while True:
        fib_num = next(fib_gen)
        if is_prime(fib_num):
            count += 1
            if count == n:
                return fib_num