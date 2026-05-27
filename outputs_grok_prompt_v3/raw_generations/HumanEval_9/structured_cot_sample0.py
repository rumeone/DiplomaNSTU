"""Compute rolling maximums over sequences."""

from itertools import accumulate
from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found
    until given moment in the sequence.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    return list(accumulate(numbers, max))