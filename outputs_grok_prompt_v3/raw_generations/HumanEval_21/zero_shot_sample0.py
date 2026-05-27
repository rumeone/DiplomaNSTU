def rescale_to_unit(numbers: List[float]) -> List[float]:
    if len(numbers) < 2:
        return []
    min_val = min(numbers)
    max_val = max(numbers)
    if min_val == max_val:
        return []
    range_val = max_val - min_val
    return [(x - min_val) / range_val for x in numbers]