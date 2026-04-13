from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    """
    if not numbers:
        return []
    
    result = []
    # Add first element without preceding delimiter
    result.append(numbers[0])
    
    # For each subsequent element, add delimiter then the element
    for num in numbers[1:]:
        result.append(delimeter)
        result.append(num)
    
    return result