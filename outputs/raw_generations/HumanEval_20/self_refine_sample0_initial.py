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
    min_distance = float('inf')
    result = (0.0, 0.0)
    
    # We need to find the last pair with minimal distance
    # Iterate through all pairs, tracking the minimal distance and the pair index
    last_min_pair_index = -1
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            distance = abs(numbers[i] - numbers[j])
            # If we found a smaller distance or equal distance at a later position
            if distance < min_distance or (distance == min_distance and j > last_min_pair_index):
                min_distance = distance
                last_min_pair_index = j
                # Store in order (smaller, larger)
                if numbers[i] <= numbers[j]:
                    result = (numbers[i], numbers[j])
                else:
                    result = (numbers[j], numbers[i])
    
    return result