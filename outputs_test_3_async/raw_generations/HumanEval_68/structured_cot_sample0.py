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
    even_values = [(value, index) for index, value in enumerate(arr) if value % 2 == 0]
    if not even_values:
        return []
    smallest_value, smallest_index = min(even_values, key=lambda x: (x[0], x[1]))
    return [smallest_value, smallest_index]