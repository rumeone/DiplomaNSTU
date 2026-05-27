"""
Module for calculating geometric shapes areas.
"""


def triangle_area(a: float, h: float) -> float:
    """
    Calculate the area of a triangle given the length of a side and its height.

    Args:
        a: Length of the triangle's base side.
        h: Height of the triangle corresponding to the given side.

    Returns:
        The area of the triangle.

    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h