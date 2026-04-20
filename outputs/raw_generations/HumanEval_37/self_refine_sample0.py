from typing import List


def sort_even(l: List[int]) -> List[int]:
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Examples:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    if not l:
        return []

    # Extract and sort even-indexed elements
    even_elements = sorted(l[i] for i in range(0, len(l), 2))
    
    # Build result list
    result = l.copy()
    for i, sorted_val in zip(range(0, len(l), 2), even_elements):
        result[i] = sorted_val
    
    return result