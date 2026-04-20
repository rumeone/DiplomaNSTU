def triangle_area(a: int, b: int, c: int) -> float:
    # Check triangle inequality for all three sides
    if a + b <= c or a + c <= b or b + c <= a:
        return -1.0
    
    # Heron's formula
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    
    return round(area, 2)