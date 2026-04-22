"""Module for plucking the smallest even node from a tree branch array."""

from typing import List


def pluck(arr: List[int]) -> List[int]:
    """
    Given an array representing a branch of a tree that has integer nodes,
    pluck one of the nodes and return it as [smallest_even_value, index].
    The plucked node is the one with the smallest even value.
    If multiple nodes share the same smallest even value, return the one
    with the smallest index.

    If the array is empty or contains no even values, return [].

    Examples:
        >>> pluck([4, 2, 3])
        [2, 1]
        >>> pluck([1, 2, 3])
        [2, 1]
        >>> pluck([])
        []
        >>> pluck([5, 0, 3, 0, 4, 2])
        [0, 1]
    """
    if not arr:
        return []

    min_even = None
    min_index = -1

    for i, value in enumerate(arr):
        if value % 2 == 0:
            if min_even is None or value < min_even:
                min_even = value
                min_index = i
            elif value == min_even and i < min_index:
                min_index = i

    if min_even is None:
        return []

    return [min_even, min_index]