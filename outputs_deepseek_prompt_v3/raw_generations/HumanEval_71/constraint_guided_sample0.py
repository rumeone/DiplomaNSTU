"""
Module for calculating triangle area from side lengths.
"""


def triangle_area(a: int, b: int, c: int) -> float:
    """
    Calculate the area of a triangle given its three side lengths.

    Args:
        a: Length of first side.
        b: Length of second side.
        c: Length of third side.

    Returns:
        Area of the triangle rounded to 2 decimal places if valid,
        otherwise -1.
    """
    if not (a + b > c and a + c > b and b + c > a):
        return -1

    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return round(area, 2)