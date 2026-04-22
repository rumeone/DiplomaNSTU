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

    sorted_lst = sorted(lst)
    result = []
    left, right = 0, len(sorted_lst) - 1
    while left <= right:
        if left == right:
            result.append(sorted_lst[left])
            break
        result.append(sorted_lst[left])
        result.append(sorted_lst[right])
        left += 1
        right -= 1
    return result