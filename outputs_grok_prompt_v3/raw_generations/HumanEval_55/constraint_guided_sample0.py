"""Module for computing Fibonacci numbers."""

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
    if n < 0:
        raise ValueError("n must be non-negative")
    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, previous + current
    return previous