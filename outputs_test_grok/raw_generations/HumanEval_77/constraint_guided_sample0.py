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

    # Handle negative numbers by working with absolute value
    abs_a = abs(a)

    # Find the integer cube root by checking possible candidates
    # We can limit the search to numbers up to the cube root of abs_a
    root = 1
    while root * root * root < abs_a:
        root += 1

    # Check if we found an exact cube
    cube = root * root * root
    if cube == abs_a:
        return True

    # Also check one less in case of floating point edge cases, though
    # with integers this is rarely needed but adds robustness
    prev_cube = (root - 1) * (root - 1) * (root - 1)
    if prev_cube == abs_a:
        return True

    return False