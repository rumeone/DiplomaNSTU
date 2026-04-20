def fib4(n: int) -> int:
    """
    Compute the n-th element of the Fib4 number sequence.

    Args:
        n: The index of the Fib4 number to compute.

    Returns:
        The n-th Fib4 number.

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

    base_cases = [0, 0, 2, 0]
    if n < 4:
        return base_cases[n]

    a, b, c, d = base_cases
    for _ in range(4, n + 1):
        a, b, c, d = b, c, d, a + b + c + d

    return d