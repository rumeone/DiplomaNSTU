"""
Module providing utility function to check if a number is a perfect cube.
"""


def iscube(a: int) -> bool:
    """
    Check if number a is a cube of some integer number.

    Examples:
        iscube(2) == False
        iscube(64) == True
        iscube(-180) == False
    """
    if a == 0:
        return True

    # Handle negative numbers
    if a < 0:
        return iscube(-a)

    # Find integer cube root by checking cubes up to a reasonable bound
    root = 1
    while root * root * root < a:
        root += 1

    return root * root * root == a