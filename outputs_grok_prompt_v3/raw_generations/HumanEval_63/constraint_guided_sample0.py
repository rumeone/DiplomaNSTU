"""Compute elements of the FibFib sequence."""

def fibfib(n: int) -> int:
    """Compute the n-th element of the FibFib sequence efficiently."""
    if n < 2:
        return 0
    if n == 2:
        return 1

    prev3 = 0
    prev2 = 0
    prev1 = 1
    for _ in range(3, n + 1):
        current = prev1 + prev2 + prev3
        prev3 = prev2
        prev2 = prev1
        prev1 = current
    return prev1