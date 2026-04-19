def rescale_to_unit(numbers: List[float]) -> List[float]:
    if not numbers or len(numbers) < 2:
        return []
    
    min_val = min(numbers)
    max_val = max(numbers)
    
    # If all numbers are equal, scaling is undefined
    if min_val == max_val:
        return []
    
    scale = max_val - min_val
    return [(x - min_val) / scale for x in numbers]