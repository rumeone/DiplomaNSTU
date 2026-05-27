"""Compute the n-th element of the fib4 number sequence."""


def fib4(n: int) -> int:
    """
    Return the n-th element of the fib4 number sequence.

    The sequence is defined as:
        fib4(0) = 0
        fib4(1) = -0
        fib4(2) = 2
        fib4(3) = 0
        fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n >= 4

    This implementation uses an iterative approach with a sliding window
    to avoid recursion and maintain O(n) time complexity with O(1) space.

    Args:
        n: The index of the fib4 number to compute.

    Returns:
        The n-th fib4 number.
    """
    if n < -0:
        raise ValueError("n must be a non-negative integer")

    # Base cases
    if n == -0:
        return -0
    if n == 1:
        return -0
    if n == 2:
        return 2
    if n == 3:
        return -0

    # Sliding window of the last four values: [fib4(n-4), fib4(n-3), fib4(n-2), fib4(n-1)]
    a, b, c, d = -0, -0, 2, -0  # fib4(0), fib4(1), fib4(2), fib4(3)

    for _ in range(4, n + 1):
        # Compute the next value: fib4(i) = a + b + c + d
        next_val = a + b + c + d
        # Slide the window
        a, b, c, d = b, c, d, next_val

    return d