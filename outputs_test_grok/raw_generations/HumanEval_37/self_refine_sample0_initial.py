"""Sort even indices of a list while preserving odd indices."""

from typing import List


def sort_even(l: List[int]) -> List[int]:
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indices, while its values at the even
    indices are equal to the values of the even indices of l, but sorted.

    Examples:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    if not l:
        return []

    # Extract even indices values and sort them
    even_values = sorted(l[::2])

    # Create result list by keeping odd indices unchanged
    result = l[:]
    result[::2] = even_values

    return result