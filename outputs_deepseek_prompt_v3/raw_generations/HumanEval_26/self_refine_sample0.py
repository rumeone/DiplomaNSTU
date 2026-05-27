from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all the elements that occur more than once.
    Keep the order of the elements the same as in the input.

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen_once = set()
    seen_multiple = set()

    for num in numbers:
        if num in seen_multiple:
            continue
        if num in seen_once:
            seen_once.remove(num)
            seen_multiple.add(num)
        else:
            seen_once.add(num)

    return [num for num in numbers if num in seen_once]