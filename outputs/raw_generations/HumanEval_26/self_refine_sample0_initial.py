from typing import List
from collections import Counter


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all the elements that occur more than once.
    Keep the order of the elements the same as in the input.

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    # Count occurrences of each number
    frequency = Counter(numbers)
    # Filter numbers that appear exactly once, preserving original order
    return [num for num in numbers if frequency[num] == 1]