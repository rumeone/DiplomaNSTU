from typing import List


def pluck(arr: List[int]) -> List[int]:
    """
    Given an array representing a branch of a tree that has integer nodes,
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found return the node that has smallest index.

    The plucked node should be returned in a list, [ smallest_value, its index ],
    If there are no even values or the given array is empty, return [].
    """
    smallest_even = None
    smallest_index = None
    
    for i, value in enumerate(arr):
        if value % 2 == 0:  # Check if the value is even
            if smallest_even is None or value < smallest_even or (value == smallest_even and i < smallest_index):
                smallest_even = value
                smallest_index = i
    
    if smallest_even is None:
        return []
    return [smallest_even, smallest_index]