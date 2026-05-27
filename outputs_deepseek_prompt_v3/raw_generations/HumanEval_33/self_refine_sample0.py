from typing import List


def sort_third(l: List[int]) -> List[int]:
    """
    Return a list where values at indices divisible by three are sorted,
    while other indices remain unchanged.

    Args:
        l: A list of integers.

    Returns:
        A new list with the described transformation.

    Examples:
        >>> sort_third([1, 2, 3])
        [1, 2, 3]
        >>> sort_third([5, 6, 3, 4, 8, 9, 2])
        [2, 6, 3, 4, 8, 9, 5]
    """
    result = l.copy()
    divisible_by_three_indices = [i for i in range(len(l)) if i % 3 == 0]
    values_at_divisible_indices = [l[i] for i in divisible_by_three_indices]
    sorted_values = sorted(values_at_divisible_indices)

    for idx, sorted_val in zip(divisible_by_three_indices, sorted_values):
        result[idx] = sorted_val

    return result