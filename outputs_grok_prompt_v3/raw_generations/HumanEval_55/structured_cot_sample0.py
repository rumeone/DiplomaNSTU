"""
Module providing Fibonacci number computation.
"""


def fib(n: int) -> int:
    """
    Return the n-th Fibonacci number.

    Examples:
        >>> fib(10)
        55
        >>> fib(1)
        1
        >>> fib(8)
        21
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a