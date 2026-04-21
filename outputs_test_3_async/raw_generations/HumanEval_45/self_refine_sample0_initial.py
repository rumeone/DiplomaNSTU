"""Calculate the area of a triangle given side length and height."""


def triangle_area(a: float, h: float) -> float:
    """
    Return the area of a triangle.

    The area is computed as (side * height) / 2.

    Args:
        a: Length of a side of the triangle.
        h: Height corresponding to that side.

    Returns:
        The area of the triangle.

    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    return (a * h) / 2.0