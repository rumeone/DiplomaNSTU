"""Module providing a function to compute Fibonacci numbers."""


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
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1

    previous: int = 1
    current: int = 1

    for _ in range(3, n + 1):
        previous, current = current, previous + current

    return current