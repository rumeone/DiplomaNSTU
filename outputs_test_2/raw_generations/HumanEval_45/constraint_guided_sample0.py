"""
Module for calculating geometric properties of triangles.
"""


def triangle_area(a: float, h: float) -> float:
    """
    Calculate the area of a triangle given the length of a side and its height.

    The area is computed using the formula: area = (base * height) / 2

    Args:
        a: Length of the base side of the triangle.
        h: Height of the triangle corresponding to the given base.

    Returns:
        The area of the triangle.

    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    return (a * h) / 2