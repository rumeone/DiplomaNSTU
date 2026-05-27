"""
Utilities for identifying prime Fibonacci numbers.
"""

def is_prime(number: int) -> bool:
    """Return True if number is prime."""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


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

    fib_prev, fib_curr = 0, 1
    prime_count = 0

    while True:
        if is_prime(fib_curr):
            prime_count += 1
            if prime_count == n:
                return fib_curr
        fib_prev, fib_curr = fib_curr, fib_prev + fib_curr