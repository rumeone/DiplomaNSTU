from typing import List


def sort_third(l: List[int]) -> List[int]:
    """
    Return a list where elements at indices divisible by three are sorted,
    while other elements remain in their original positions.

    Args:
        l: A list of integers.

    Returns:
        A new list with the same elements as l, but with elements at indices
        divisible by three sorted in ascending order.

    Examples:
        >>> sort_third([1, 2, 3])
        [1, 2, 3]
        >>> sort_third([5, 6, 3, 4, 8, 9, 2])
        [2, 6, 3, 4, 8, 9, 5]
    """
    result = l[:]
    divisible_by_three_indices = [i for i in range(len(l)) if i % 3 == 0]
    divisible_values = sorted([l[i] for i in divisible_by_three_indices])

    for idx, sorted_value in zip(divisible_by_three_indices, divisible_values):
        result[idx] = sorted_value

    return result