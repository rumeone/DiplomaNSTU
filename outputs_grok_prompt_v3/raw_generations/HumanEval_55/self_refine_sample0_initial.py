"""Module providing Fibonacci number calculation."""

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
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 0
    previous = 0
    current = 1
    for _ in range(1, n):
        previous, current = current, previous + current
    return current