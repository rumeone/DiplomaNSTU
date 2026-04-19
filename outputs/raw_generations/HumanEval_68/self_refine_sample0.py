from typing import List


def pluck(arr: List[int]) -> List[int]:
    if not arr:
        return []

    smallest_even = None
    smallest_index = None

    for i, value in enumerate(arr):
        if value % 2 == 0:
            if smallest_even is None or value < smallest_even or (value == smallest_even and i < smallest_index):
                smallest_even = value
                smallest_index = i

    if smallest_even is None:
        return []
    return [smallest_even, smallest_index]