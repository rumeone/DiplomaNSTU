from typing import List


def sort_third(l: List[int]) -> List[int]:
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.

    Examples:
        >>> sort_third([1, 2, 3])
        [1, 2, 3]
        >>> sort_third([5, 6, 3, 4, 8, 9, 2])
        [2, 6, 3, 4, 8, 9, 5]
    """
    indices = [i for i in range(len(l)) if i % 3 == 0]
    values = [l[i] for i in indices]
    values.sort()
    result = l[:]
    for idx, val in zip(indices, values):
        result[idx] = val
    return result