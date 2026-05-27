"""Determine whether an integer is a perfect cube."""

def iscube(a: int) -> bool:
    """Check if number a is a cube of some integer number.

    Examples:
        iscube(2) == False
        iscube(64) == True
        iscube(-180) == False
    """
    if a == 0:
        return True
    x = abs(a)
    left, right = 1, x
    while left <= right:
        mid = (left + right) // 2
        cube = mid * mid * mid
        if cube == x:
            return True
        if cube < x:
            left = mid + 1
        else:
            right = mid - 1
    return False