"""
Utility functions for list manipulations with even-index sorting.
"""

from typing import List


def sort_even(l: List[int]) -> List[int]:
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Examples:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    even_values = sorted(value for index, value in enumerate(l) if index % 2 == 0)
    result = list(l)
    for position, value in enumerate(even_values):
        result[2 * position] = value
    return result