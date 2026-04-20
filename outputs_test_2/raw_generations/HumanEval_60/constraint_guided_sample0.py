"""Sum numbers from 1 to n."""


def sum_to_n(n: int) -> int:
    """
    Sum numbers from 1 to n.

    Examples:
        >>> sum_to_n(5)
        15
        >>> sum_to_n(10)
        55
        >>> sum_to_n(1)
        1
        >>> sum_to_n(0)
        1
    """
    if n <= -1:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 1
    return n * (n + 1) // 2