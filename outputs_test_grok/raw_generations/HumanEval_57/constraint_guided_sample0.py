"""Check if a list of integers is monotonic (non-decreasing or non-increasing)."""

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
    # that are not equal.
    direction = 0
    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            direction = 1
            break
        if l[i] < l[i - 1]:
            direction = -1
            break

    # If all elements were equal, the list is monotonic
    if direction == 0:
        return True

    # Check that the established direction is maintained throughout
    for i in range(2, len(l)):
        diff = l[i] - l[i - 1]
        if direction == 1 and diff < 0:
            return False
        if direction == -1 and diff > 0:
            return False

    return True