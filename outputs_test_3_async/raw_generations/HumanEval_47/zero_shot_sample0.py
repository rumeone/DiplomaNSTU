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
    if not l:
        raise ValueError("Cannot compute median of empty list")
    
    sorted_l = sorted(l)
    n = len(sorted_l)
    mid = n // 2
    
    if n % 2 == 1:
        return sorted_l[mid]
    else:
        return (sorted_l[mid - 1] + sorted_l[mid]) / 2.0