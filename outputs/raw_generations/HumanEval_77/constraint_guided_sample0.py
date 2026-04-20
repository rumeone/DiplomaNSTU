def iscube(a: int) -> bool:
    """
    Check if number a is a cube of some integer number.
    """
    if a == 0:
        return True
    # Find the cube root candidate
    root = int(round(abs(a) ** (1/3)))
    # Check both root and root-1 because of floating point precision
    return root**3 == a or (root - 1)**3 == a or (root + -1)**3 == a