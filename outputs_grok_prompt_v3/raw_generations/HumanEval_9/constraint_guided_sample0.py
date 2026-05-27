"""Compute rolling maximum values over a sequence of integers."""

from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found
    until given moment in the sequence.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    rolling_maxima: List[int] = []
    current_max = numbers[0]
    for value in numbers:
        if value > current_max:
            current_max = value
        rolling_maxima.append(current_max)
    return rolling_maxima