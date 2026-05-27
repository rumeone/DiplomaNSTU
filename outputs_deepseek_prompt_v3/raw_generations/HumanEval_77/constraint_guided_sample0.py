"""
Module for checking if a number is a perfect cube.
"""


def iscube(a: int) -> bool:
    """
    Check if number a is a cube of some integer number.

    Args:
        a: The integer to check.

    Returns:
        True if a is a perfect cube (i.e., there exists an integer n
        such that n³ = a), False otherwise.

    Examples:
        >>> iscube(2)
        False
        >>> iscube(64)
        True
        >>> iscube(-180)
        False
    """
    if a < 0:
        return False

    low = 0
    high = max(1, int(a ** (1 / 3)) + 2)

    while low <= high:
        mid = (low + high) // 2
        cube = mid * mid * mid

        if cube == a:
            return True
        elif cube < a:
            low = mid + 1
        else:
            high = mid - 1

    return False