"""Module providing a function to find the n-th prime Fibonacci number."""

def is_prime(num: int) -> bool:
    """Check if a number is prime."""
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

    # First two prime Fibonacci numbers
    if n == 1:
        return 2
    if n == 2:
        return 3

    # Start from the third Fibonacci number (5)
    a, b = 2, 3
    count = 2  # We already have two prime fibs: 2 and 3

    while True:
        a, b = b, a + b
        if is_prime(b):
            count += 1
            if count == n:
                return b