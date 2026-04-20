from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all the elements that occur more than once.
    Keep the order of the elements the same as in the input.

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen = {}
    for num in numbers:
        seen[num] = seen.get(num, 0) + 1
    return [num for num in numbers if seen[num] == 1]