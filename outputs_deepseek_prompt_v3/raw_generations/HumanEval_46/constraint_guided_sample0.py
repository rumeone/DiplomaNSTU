"""
Module for computing the Fib4 number sequence.
"""


def fib4(n: int) -> int:
    """
    Compute the n-th element of the Fib4 number sequence.

    The sequence is defined as:
        fib4(0) = 0
        fib4(1) = 0
        fib4(2) = 2
        fib4(3) = 0
        fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n >= 4

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
        raise ValueError("n must be a non-negative integer")

    base_cases = [0, 0, 2, 0]
    if n < 4:
        return base_cases[n]

    a, b, c, d = base_cases
    for _ in range(4, n + 1):
        a, b, c, d = b, c, d, a + b + c + d

    return d