def triangle_area(a: float, h: float) -> float:
    """
    Given length of a side and height, return area for a triangle.
    """
    if a <= 0 or h <= 0:
        return 0.0
    return 0.5 * a * h