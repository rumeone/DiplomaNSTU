def triangle_area(a: float, h: float) -> float:
    """
    Given length of a side and height, return area for a triangle.

    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    if a <= 0 or h <= 0:
        return 0.0
    return 0.5 * a * h