"""
Pluck the smallest even value from an array along with its index.
"""

from typing import List


def pluck(arr: List[int]) -> List[int]:
    """
    Return the smallest even value and its index from the given array.

    Args:
        arr: List of integers representing tree branch nodes.

    Returns:
        List containing [smallest_even_value, index] if found, otherwise [].
    """
    if not arr:
        return []

    smallest_value = None
    smallest_index = None

    for i, value in enumerate(arr):
        if value % 2 == 0:
            if smallest_value is None or value < smallest_value:
                smallest_value = value
                smallest_index = i
            elif value == smallest_value and i < smallest_index:
                smallest_index = i

    if smallest_value is None:
        return []

    return [smallest_value, smallest_index]