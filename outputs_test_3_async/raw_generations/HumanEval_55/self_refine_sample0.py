"""
Fibonacci number calculation.
This module provides a function to compute the n-th Fibonacci number.
"""


def fib(n: int) -> int:
    """
    Return the n-th Fibonacci number.

    The Fibonacci sequence is defined as:
        fib(0) = 0
        fib(1) = 1
        fib(n) = fib(n-1) + fib(n-2) for n > 1

    Examples:
        >>> fib(10)
        55
        >>> fib(1)
        1
        >>> fib(8)
        21
    """
    if n < 0:
        raise ValueError("Fibonacci number is not defined for negative indices")
    if n == 0:
        return 0
    if n <= 2:
        return 1

    previous, current = 1, 1
    for _ in range(3, n + 1):
        previous, current = current, previous + current

    return current