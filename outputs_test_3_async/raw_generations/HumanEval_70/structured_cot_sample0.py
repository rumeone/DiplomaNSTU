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
    sorted_lst = sorted(lst)
    result = []
    while sorted_lst:
        result.append(sorted_lst.pop(0))
        if sorted_lst:
            result.append(sorted_lst.pop(-1))
    return result