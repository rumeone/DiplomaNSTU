"""
Module for plucking the smallest even value from a list of integers.
"""

from typing import List


def pluck(arr: List[int]) -> List[int]:
    """
    Pluck the smallest even value from a list of integers.

    Returns a list containing the smallest even value and its index.
    If multiple nodes have the same smallest even value, returns the one
    with the smallest index. Returns an empty list if no even values exist
    or the input list is empty.

    Args:
        arr: List of integers representing tree branch nodes.

    Returns:
        List containing [smallest_even_value, index] or [] if no even values.
    """
    if not arr:
        return []

    smallest_even = None
    smallest_index = None

    for index, value in enumerate(arr):
        if value % 2 == 0:
            if smallest_even is None or value < smallest_even:
                smallest_even = value
                smallest_index = index
            elif value == smallest_even and index < smallest_index:
                smallest_index = index

    if smallest_even is None:
        return []

    return [smallest_even, smallest_index]