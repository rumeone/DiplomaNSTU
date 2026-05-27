"""Calculate the median of a list of numbers."""

from typing import List


def median(l: List[float]) -> float:
    """
    Return median of elements in the list l.

    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        8.0
    """
    s = sorted(l)
    n = len(s)
    m = n // 2
    if n % 2:
        return s[m]
    return (s[m - 1] + s[m]) / 2