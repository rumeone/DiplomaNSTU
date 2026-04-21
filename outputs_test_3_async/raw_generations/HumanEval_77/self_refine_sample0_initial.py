"""
Module for checking if a number is a perfect cube.
"""


def iscube(a: int) -> bool:
    """
    Check if number a is a cube of some integer number.

    Examples:
        iscube(2) == False
        iscube(64) == True
        iscube(-180) == False
    """
    if a < 0:
        candidate = -round((-a) ** (1/3))
    else:
        candidate = round(a ** (1/3))
    
    return candidate ** 3 == a