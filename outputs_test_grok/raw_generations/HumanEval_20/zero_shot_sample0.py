from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return 
    the last two elements that are the closest to each other and return them
    in order (smaller number, larger number).
    """
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[1])
    
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            diff = abs(numbers[i] - numbers[j])
            if diff < min_diff or (diff == min_diff and j > numbers.index(closest_pair[1])):
                min_diff = diff
                a, b = numbers[i], numbers[j]
                closest_pair = (min(a, b), max(a, b))
    
    return closest_pair