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
    if len(l) <= 2:
        return True

    # Determine direction by comparing first two distinct elements
    i = 0
    while i < len(l) - 1 and l[i] == l[i + 1]:
        i += 1

    # If all elements are equal or list has 0-2 elements
    if i >= len(l) - 1:
        return True

    # Determine expected direction
    increasing = l[i] < l[i + 1]

    # Check remaining elements maintain the direction
    for j in range(i, len(l) - 1):
        if increasing:
            if l[j] > l[j + 1]:
                return False
        else:
            if l[j] < l[j + 1]:
                return False

    return True