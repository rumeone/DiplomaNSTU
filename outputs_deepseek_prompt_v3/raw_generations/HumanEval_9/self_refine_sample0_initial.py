from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements from a given list of integers.
    
    For each position in the input list, the output contains the maximum value
    seen up to that point in the sequence.
    
    Args:
        numbers: List of integers to process.
    
    Returns:
        List of rolling maximum values.
    
    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    
    result = []
    current_max = numbers[0]
    
    for num in numbers:
        if num > current_max:
            current_max = num
        result.append(current_max)
    
    return result