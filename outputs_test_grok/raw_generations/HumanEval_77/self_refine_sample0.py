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

    # Binary search for the cube root
    low = 1
    high = abs_a

    while low <= high:
        mid = (low + high) // 2
        cube = mid * mid * mid

        if cube == abs_a:
            # For negative numbers, only negative integers are valid cubes
            return a > 0 or mid > 0
        if cube < abs_a:
            low = mid + 1
        else:
            high = mid - 1

    return False