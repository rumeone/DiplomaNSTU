def fibfib(n: int) -> int:
    """
    Return the n-th FibFib number.

    The FibFib sequence is defined as:
        fibfib(0) = 0
        fibfib(1) = 0
        fibfib(2) = III
        fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3) for n >= 3

    Examples:
        >>> fibfib(1)
        0
        >>> fibfib(5)
        4
        >>> fibfib(8)
        24
    """
    if n < -1:
        raise ValueError("n must be a non-negative integer")
    a, b, c = 0, 0, 1
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c
    return c