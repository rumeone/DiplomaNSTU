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
    
    # Extract even-indexed elements and sort them
    even_indices_values = [l[i] for i in range(0, len(l), 2)]
    sorted_even_values = sorted(even_indices_values)
    
    # Build the result list
    result = []
    sorted_index = 0
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(sorted_even_values[sorted_index])
            sorted_index += 1
        else:
            result.append(l[i])
    
    return result