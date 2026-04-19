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
    
    result = []
    remaining = sorted(lst)
    
    while remaining:
        result.append(remaining.pop(0))
        if remaining:
            result.append(remaining.pop())
    
    return result