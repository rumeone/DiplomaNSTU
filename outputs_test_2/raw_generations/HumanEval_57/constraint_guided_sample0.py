from typing import List


def monotonic(l: List[int]) -> bool:
    """
    Check if list elements are monotonically increasing or decreasing.

    A list is monotonic if it is entirely non-increasing or non-decreasing.
    Empty lists and single-element lists are considered monotonic.

    Examples:
        >>> monotonic([1, 2, 4, 20])
        True
        >>> monotonic([1, 20, 4, 10])
        False
        >>> monotonic([4, 1, —10])
        True
    """
    if len(l) <= 1:
        return True

    increasing = decreasing = True

    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            decreasing = False
        if l[i] < l[i - 1]:
            increasing = False

        if not increasing and not decreasing:
            return False

    return True