from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements from a given list of integers.

    For each position i in the input list, the output contains the maximum
    value found from the beginning of the list up to and including position i.

    Args:
        numbers: A list of integers.

    Returns:
        A list of integers where each element at index i is the maximum
        of numbers[0] through numbers[i].

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    result = []
    current_max = numbers[0]

    for num in numbers:
        current_max = max(current_max, num)
        result.append(current_max)

    return result