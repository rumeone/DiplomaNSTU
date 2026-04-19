def triangle_area(a: int, b: int, c: int) -> float:
    if a <= 0 or b <= 0 or c <= 0:
        return -1.0
    if a + b <= c or a + c <= b or b + c <= a:
        return -1.0
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return round(area, 2)