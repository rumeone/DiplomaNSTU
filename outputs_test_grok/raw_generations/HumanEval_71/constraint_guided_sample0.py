"""
Module providing a function to calculate the area of a triangle
given its three side lengths, or -1 if the sides do not form a valid triangle.
"""


def triangle_area(a: int, b: int, c: int) -> float:
    """
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle.
    Otherwise return -1.
    Three sides make a valid triangle when the sum of any two sides is greater
    than the third side.

    Examples:
        triangle_area(3, 4, 5) == 6.00
        triangle_area(1, 2, 10) == -1
    """
    # Guard clause: check triangle inequality
    if a + b <= c or a + c <= b or b + c <= a:
        return -1.0

    # Calculate semi-perimeter
    semi_perimeter = (a + b + c) / 2.0

    # Heron's formula for area
    area = (semi_perimeter * (semi_perimeter - a) *
            (semi_perimeter - b) * (semi_perimeter - c)) ** 0.5

    # Round to 2 decimal places and return as float
    return round(area, 2)