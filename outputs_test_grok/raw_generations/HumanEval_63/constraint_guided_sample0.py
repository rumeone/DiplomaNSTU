"""
Module providing an efficient implementation for computing the n-th FibFib number.
The FibFib sequence is defined as:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3) for n > 2
"""


def fibfib(n: int) -> int:
    """
    Returns the n-th element of the FibFib number sequence.

    This implementation uses dynamic programming with O(n) time and O(1) space
    by maintaining only the last three values at each step.

    Examples:
        >>> fibfib(1)
        0
        >>> fibfib(5)
        4
        >>> fibfib(8)
        24
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1

    # Initialize the last three values
    prev3 = 0  # fibfib(n-3)
    prev2 = 0  # fibfib(n-2)
    prev1 = 1  # fibfib(n-1)

    for _ in range(3, n + 1):
        current = prev1 + prev2 + prev3
        prev3 = prev2
        prev2 = prev1
        prev1 = current

    return prev1