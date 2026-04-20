def fib(n: int) -> int:
    """
    Return the n-th Fibonacci number.

    The Fibonacci sequence is defined as:
        F(0) = 0, F(1) = 1
        F(n) = F(n-1) + F(n-2) for n > 1

    Args:
        n: The index of the Fibonacci number to compute.

    Returns:
        The n-th Fibonacci number.

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

    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr