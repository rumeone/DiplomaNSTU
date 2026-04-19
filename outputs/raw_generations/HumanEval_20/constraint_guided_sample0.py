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
    # Initialize with the first two elements
    min_distance = abs(numbers[0] - numbers[1])
    best_pair = (min(numbers[0], numbers[1]), max(numbers[0], numbers[1]))
    
    # Check all pairs, preferring later ones when distances are equal
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            current_distance = abs(numbers[i] - numbers[j])
            # Update if we found a strictly smaller distance
            # or equal distance (to prefer later pairs)
            if current_distance <= min_distance:
                min_distance = current_distance
                best_pair = (min(numbers[i], numbers[j]), max(numbers[i], numbers[j]))
    
    return best_pair