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
    
    # First pass: count occurrences
    for num in numbers:
        seen_counts[num] = seen_counts.get(num, 0) + 1
    
    # Second pass: collect elements that appear exactly once
    result = []
    for num in numbers:
        if seen_counts[num] == 1:
            result.append(num)
    
    return result