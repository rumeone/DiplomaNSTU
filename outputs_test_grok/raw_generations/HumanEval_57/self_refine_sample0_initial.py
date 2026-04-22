"""Check if a list of integers is monotonically increasing or decreasing."""

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
    if len(l) < 2:
        return True

    # Determine the direction based on the first pair of elements
    is_increasing = l[0] <= l[1]

    for i in range(1, len(l) - 1):
        if is_increasing:
            if l[i] > l[i + 1]:
                return False
        else:
            if l[i] < l[i + 1]:
                return False

    return True