def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if not numbers:
        return []
    result = []
    for num in numbers[:-1]:
        result.append(num)
        result.append(delimeter)
    result.append(numbers[-1])
    return result