"""Compute the area of a triangle given one side and the corresponding height."""

def triangle_area(a: float, h: float) -> float:
    """
    Given length of a side and height, return area for a triangle.

    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    base = a
    height = h
    return (base * height) / 2