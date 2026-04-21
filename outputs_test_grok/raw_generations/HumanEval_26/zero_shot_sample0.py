from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all the elements that occur more than once.
    Keep the order of the elements the same as in the input.

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen = set()
    duplicates = set()
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return [num for num in numbers if num not in duplicates]