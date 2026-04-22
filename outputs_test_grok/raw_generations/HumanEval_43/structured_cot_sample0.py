from typing import List, Set


def pairs_sum_to_zero(l: List[int]) -> bool:
    """
    Check if there are two distinct elements
    in the list that sum to zero.

    Examples:
        >>> pairs_sum_to_zero([1, 3, 5, 0])
        False
        >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
        True
    """
    seen: Set[int] = set()
    for num in l:
        if -num in seen:
            return True
        seen.add(num)
    return False