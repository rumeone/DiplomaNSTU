from typing import List


def pluck(arr: List[int]) -> List[int]:
    """
    Pluck the node with the smallest even value from an array.

    Returns a list containing [smallest_even_value, its_index].
    If no even values exist or the array is empty, returns an empty list.
    If multiple nodes have the same smallest even value, returns the one with the smallest index.

    Args:
        arr: List of integers representing tree branch nodes.

    Returns:
        List containing the smallest even value and its index, or empty list if no even values.
    """
    if not arr:
        return []

    smallest_even = None
    smallest_index = None

    for index, value in enumerate(arr):
        if value % 2 == 0:
            if smallest_even is None or value < smallest_even or (
                    value == smallest_even and index < smallest_index):
                smallest_even = value
                smallest_index = index

    if smallest_even is None:
        return []

    return [smallest_even, smallest_index]