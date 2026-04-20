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
        value in numbers[0:i+1].

    Examples:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
        >>> rolling_max([5, 4, 3, 2, 1])
        [5, 5, 5, 5, 5]
        >>> rolling_max([])
        []
    """
    if not numbers:
        return []

    result = []
    current_max = numbers[0]

    for number in numbers:
        if number > current_max:
            current_max = number
        result.append(current_max)

    return result