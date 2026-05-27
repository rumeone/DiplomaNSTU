"""
Utilities for finding prime Fibonacci numbers.
"""

def is_prime(number: int) -> bool:
    """Return True if number is prime, else False."""
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    candidate = 5
    while candidate * candidate <= number:
        if number % candidate == 0 or number % (candidate + 2) == 0:
            return False
        candidate += 6
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
    count = 0
    prev, curr = 0, 1
    while count < n:
        prev, curr = curr, prev + curr
        if is_prime(prev):
            count += 1
    return prev