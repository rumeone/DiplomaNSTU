"""Module providing the prime_fib function to find the n-th prime Fibonacci number."""

from typing import Iterator


def is_prime(num: int) -> bool:
    """Check if a number is prime using trial division up to sqrt(n)."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_fibonacci() -> Iterator[int]:
    """Generate Fibonacci numbers indefinitely."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and also prime.

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
    if n < 1:
        raise ValueError("n must be a positive integer")

    count = 0
    for fib in generate_fibonacci():
        if fib > 1 and is_prime(fib):
            count += 1
            if count == n:
                return fib
    # This line is unreachable for valid positive n
    raise RuntimeError("Failed to find enough prime Fibonacci numbers")