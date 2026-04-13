from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Example:
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []
    
    result = []
    # Add first element
    result.append(numbers[0])
    
    # For each subsequent element, add delimeter then the element
    for num in numbers[1:]:
        result.append(delimeter)
        result.append(num)
    
    return result