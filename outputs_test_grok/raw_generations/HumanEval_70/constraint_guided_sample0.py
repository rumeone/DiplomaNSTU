"""Module providing the strange_sort_list function for alternating min-max sorting."""

from typing import List


def strange_sort_list(lst: List[int]) -> List[int]:
    """
    Given a list of integers, return the list in a 'strange' order.
    Strange sorting, is when you start with the minimum value,
    then the maximum value from the remaining integers, then the minimum and so on.

    Examples:
        strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
        strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
        strange_sort_list([]) == []
    """
    if not lst:
        return []

    sorted_list = sorted(lst)
    result = []
    left = 0
    right = len(sorted_list) - 1
    take_min = True

    while left <= right:
        if take_min:
            result.append(sorted_list[left])
            left += 1
        else:
            result.append(sorted_list[right])
            right -= 1
        take_min = not take_min

    return result