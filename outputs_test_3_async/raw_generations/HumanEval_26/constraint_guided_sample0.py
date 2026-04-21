from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all the elements that occur more than once.
    Keep the order of the elements the same as in the input.

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen_counts = {}
    for number in numbers:
        seen_counts[number] = seen_counts.get(number, 0) + 1

    result = []
    for number in numbers:
        if seen_counts[number] == 1:
            result.append(number)

    return result