"""This module provides utility functions for list manipulation.

The primary function, sort_third, modifies a list by sorting values
at indices divisible by three while leaving other elements unchanged.
"""


from typing import List


def sort_third(l: List[int]) -> List[int]:
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the indices that are not divisible by three, while its values at the indices that are divisible by three are equal
    to the values of the corresponding indices of l, but sorted.

    Examples:
        >>> sort_third([1, 2, 3])
        [1, 2, 3]
        >>> sort_third([5, 6, 3, 4, 8, 9, 2])
        [5, 6, 3, 4, 8, 9, 2]
    """
    if not l:
        return []

    # Extract values at indices divisible by 3
    third_indices_values = [l[i] for i in range(0, len(l), 3)]

    # Sort these values
    third_indices_values.sort()

    # Create result list, copying original and replacing every third element
    result = l[:]
    for i, value in enumerate(third_indices_values):
        result[i * 3] = value

    return result