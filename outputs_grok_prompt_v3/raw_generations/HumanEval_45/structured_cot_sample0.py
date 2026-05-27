"""Triangle area calculation module."""


def triangle_area(a: float, h: float) -> float:
    """Given length of a side and height, return area for a triangle.

    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    return (a * h) / 2