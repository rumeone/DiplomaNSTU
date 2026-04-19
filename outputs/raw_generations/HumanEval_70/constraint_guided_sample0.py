from typing import List


def strange_sort_list(lst: List[int]) -> List[int]:
    """
    Given a list of integers, return the list in a 'strange' order.
    Strange sorting, is when you start with the minimum value,
    then the maximum value from the remaining integers, then the minimum and so on.
    """
    result = []
    remaining = sorted(lst)
    
    while remaining:
        # Take the smallest element
        result.append(remaining.pop(0))
        # Take the largest element if any remain
        if remaining:
            result.append(remaining.pop())
    
    return result