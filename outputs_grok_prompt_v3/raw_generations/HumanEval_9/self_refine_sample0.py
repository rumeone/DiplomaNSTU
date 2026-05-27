"""Compute rolling maximum values from a sequence of numbers."""

from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found
    until given moment in the sequence.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_maxima = []
    current_max = float("-inf")
    for number in numbers:
        current_max = max(current_max, number)
        rolling_maxima.append(current_max)
    return rolling_maxima