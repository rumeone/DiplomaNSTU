"""
Module for calculating geometric shapes areas.
"""


def triangle_area(a: float, h: float) -> float:
    """
    Calculate the area of a triangle given side length and height.

    Args:
        a: Length of the base side of the triangle.
        h: Height of the triangle perpendicular to the base.

    Returns:
        The area of the triangle.

    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h