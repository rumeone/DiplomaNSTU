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

    # Determine initial direction from first two distinct elements
    i = 0
    while i < len(l) - 1 and l[i] == l[i + 1]:
        i += 1

    if i == len(l) - 1:
        return True  # All elements are equal

    # Found first two distinct elements
    increasing = l[i] < l[i + 1]

    # Check remaining elements maintain the same monotonic direction
    for j in range(i + 1, len(l) - 1):
        if l[j] == l[j + 1]:
            continue
        if (l[j] < l[j + 1]) != increasing:
            return False

    return True