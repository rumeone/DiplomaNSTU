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
    
    # Find the cube root candidate
    root = round(abs(a) ** (1 / 3))
    
    # Check both directions due to rounding errors
    if root ** 3 == abs(a):
        if a > 0:
            return True
        if a < 0:
            return root != 0
    return False