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
    if not numbers:
        return []
    
    count_map = Counter(numbers)
    return [num for num in numbers if count_map[num] == 1]