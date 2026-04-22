"""Module providing the pluck function to find the smallest even value node in a tree branch array."""

from typing import List


def pluck(arr: List[int]) -> List[int]:
    """
    Given an array representing a branch of a tree that has integer nodes,
    pluck the node with the smallest even value. If multiple nodes share
    the same smallest even value, return the one with the smallest index.

    The result is returned as [smallest_even_value, index]. Returns an empty
    list if the array is empty or contains no even values.

    Args:
        arr: List of integers representing tree nodes.

    Returns:
        List containing [value, index] or empty list if no even value exists.
    """
    if not arr:
        return []

    min_value = float('inf')
    min_index = -1

    for index, value in enumerate(arr):
        if value % 2 == 0 and value < min_value:
            min_value = value
            min_index = index

    if min_index == -1:
        return []

    return [min_value, min_index]