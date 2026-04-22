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

    # Extract values at even indices and sort them
    even_values = sorted(l[i] for i in range(0, len(l), 2))

    # Create result list with original odd indices and sorted even indices
    result = l[:]
    for i, value in enumerate(even_values):
        result[i * 2] = value

    return result