"""
Implementation of the Fib4 sequence defined by:
fib4(0) = 0
fib4(1) = 0
fib4(2) = 2
fib4(3) = 0
fib4(n) = fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4) for n >= 4
"""


def fib4(n: int) -> int:
    """
    Compute the n-th element of the fib4 number sequence efficiently without recursion.

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
        raise ValueError("n must be a non-negative integer")

    base_sequence = [0, 0, 2, 0]
    if n < 4:
        return base_sequence[n]

    a, b, c, d = base_sequence
    for _ in range(4, n + 1):
        a, b, c, d = b, c, d, a + b + c + d

    return d