def triangle_area(a: float, h: float) -> float:
    """
    Given length of a side and height, return area for a triangle.

    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("Side length and height must be positive numbers")
    return 0.5 * a * h