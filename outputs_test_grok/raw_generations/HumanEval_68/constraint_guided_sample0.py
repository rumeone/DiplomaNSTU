"""Module for plucking the smallest even node from a tree branch array."""

from typing import List


def pluck(arr: List[int]) -> List[int]:
    """
    Given an array representing a branch of a tree that has integer nodes,
    pluck one of the nodes and return it as [smallest_even_value, index].
    The plucked node is the one with the smallest even value.
    If multiple nodes share the same smallest even value, return the one
    with the smallest index.

    If there are no even values or the array is empty, return [].

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

    min_even = float("inf")
    min_index = -1

    for i, value in enumerate(arr):
        if value % 2 == 0 and value < min_even:
            min_even = value
            min_index = i

    if min_index == -1:
        return []

    return [min_even, min_index]