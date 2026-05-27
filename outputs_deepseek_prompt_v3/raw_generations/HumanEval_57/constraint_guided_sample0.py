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
        >>> monotonic([4, 1, 0, -10])
        True
        >>> monotonic([])
        True
        >>> monotonic([5])
        True
        >>> monotonic([1, 1, 1])
        True
    """
    if len(l) <= 1:
        return True

    is_increasing = True
    is_decreasing = True

    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            is_decreasing = False
        elif l[i] < l[i - 1]:
            is_increasing = False

        if not is_increasing and not is_decreasing:
            return False

    return is_increasing or is_decreasing