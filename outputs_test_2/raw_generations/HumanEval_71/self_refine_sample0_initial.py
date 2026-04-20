"""
Module for calculating the area of a triangle given its three side lengths.
"""

import math


def triangle_area(a: int, b: int, c: int) -> float:
    """
    Calculate the area of a triangle given its three side lengths.

    Args:
        a: Length of side a.
        b: Length of side b.
        c: Length of side c.

    Returns:
        The area of the triangle rounded to 2 decimal places if the sides
        form a valid triangle, otherwise -1.

    Examples:
        >>> triangle_area(3, 4, 5)
        6.0
        >>> triangle_area(1, 2, 10)
        -1
    """
    if a <= 0 or b <= 0 or c <= 0:
        return -1.0

    if a + b <= c or a + c <= b or b + c <= a:
        return -1.0

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return round(area, 2)