"""
Module providing an efficient implementation of the fib4 sequence.
The fib4 sequence is defined as:
    fib4(0) = 0
    fib4(1) = 0
    fib4(2) = 2
    fib4(3) = 0
    fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n > 3
This implementation uses dynamic programming with O(n) time and O(1) space.
"""


def fib4(n: int) -> int:
    """
    Return the n-th element of the fib4 number sequence.

    This function computes the result iteratively to avoid recursion
    and excessive memory usage. It uses constant space by only tracking
    the four most recent values.

    Examples:
        >>> fib4(5)
        4
        >>> fib4(6)
        8
        >>> fib4(7)
        14
    """
    if n == 0 or n == 1 or n == 3:
        return 0
    if n == 2:
        return 2
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Initialize the first four values
    a, b, c, d = 0, 0, 2, 0

    for _ in range(4, n + 1):
        a, b, c, d = b, c, d, a + b + c + d

    return d