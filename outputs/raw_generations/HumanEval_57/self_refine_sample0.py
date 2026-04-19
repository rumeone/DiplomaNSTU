from typing import List


def monotonic(l: List[int]) -> bool:
    """
    Check if list elements are monotonically increasing or decreasing.

    Examples:
        >>> monotonic([1, 2, 4, 20])
        True
        >>> monotonic([1, 20, 4, 10])
        False
        >>> monotonic([4, 1, 0, -10])
        True
    """
    if len(l) <= 1:
        return True

    increasing = None
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            if increasing is False:
                return False
            increasing = True
        elif l[i] > l[i + 1]:
            if increasing is True:
                return False
            increasing = False

    return True