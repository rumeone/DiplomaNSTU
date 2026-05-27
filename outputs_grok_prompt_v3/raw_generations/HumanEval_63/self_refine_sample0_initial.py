"""Compute FibFib sequence numbers efficiently."""

def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
        fibfib(0) == 0
        fibfib(1) == 0
        fibfib(2) == 1
        fibfib(n) == fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    """
    if n < 2:
        return 0
    if n == 2:
        return 1

    prev3, prev2, prev1 = 0, 0, 1
    for _ in range(3, n + 1):
        current = prev1 + prev2 + prev3
        prev3, prev2, prev1 = prev2, prev1, current
    return prev1