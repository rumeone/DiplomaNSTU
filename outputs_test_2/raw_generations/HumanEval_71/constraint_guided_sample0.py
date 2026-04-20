"""
Module for calculating triangle area given side lengths.
"""


def triangle_area(a: int, b: int, c: int) -> float:
    """
    Calculate the area of a triangle given its three side lengths.

    Args:
        a: Length of first side.
        b: Length of second side.
        c: Length of third side.

    Returns:
        Area of the triangle rounded to 2 decimal places if sides form a valid
        triangle, otherwise -1.
    """
    if a <= 0 or b <= 0 or c <= 0:
        return -1.0

    if a + b <= c or a + c <= b or b + c <= a:
        return -1.0

    semi_perimeter = (a + b + c) / 2
    area = (semi_perimeter * (semi_perimeter - a) *
            (semi_perimeter - b) * (semi_perimeter - c)) ** 0.5

    return round(area, 2)