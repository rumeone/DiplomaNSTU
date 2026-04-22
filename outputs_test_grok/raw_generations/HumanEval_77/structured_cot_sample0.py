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
    root = round(abs(a) ** (1.0 / 3.0))
    return root**3 == abs(a) and (a > 0 or root**3 == a)