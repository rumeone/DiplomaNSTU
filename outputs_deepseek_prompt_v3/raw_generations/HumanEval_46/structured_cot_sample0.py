def fib4(n: int) -> int:
    """
    Compute the n-th element of the fib4 number sequence.

    The sequence is defined as:
        fib4(0) = 0
        fib4(1) = 0
        fib4(2) = 2
        fib4(3) = 0
        fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n >= 4

    Args:
        n: The index of the fib4 number to compute.

    Returns:
        The n-th fib4 number.

    Examples:
        >>> fib4(5)
        4
        >>> fib4(6)
        8
        >>> fib4(7)
        14
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 4:
        return [0, 0, 2, 0][n]

    a, b, c, d = 0, 0, 2, 0  # fib4(0), fib4(1), fib4(2), fib4(3)
    for _ in range(4, n + 1):
        a, b, c, d = b, c, d, a + b + c + d
    return d