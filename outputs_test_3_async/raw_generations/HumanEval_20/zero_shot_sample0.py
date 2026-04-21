from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return 
    the last two elements that are the closest to each other and return them
    in order (smaller number, larger number).

    Examples:
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    min_diff = float('inf')
    result = (0.0, 0.0)
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            diff = abs(numbers[i] - numbers[j])
            if diff < min_diff or (diff == min_diff and max(i, j) > max(result[0], result[1])):
                min_diff = diff
                if numbers[i] <= numbers[j]:
                    result = (numbers[i], numbers[j])
                else:
                    result = (numbers[j], numbers[i])
    
    return result