def iscube(a: int) -> bool:
    """
    Check if number a is a cube of some integer number.

    Examples:
        iscube(2) == False
        iscube(64) == True
        iscube(-180) == False
    """
    if a < 0:
        return -(-a) ** (1/3) % 1 < 1e-12
    return a ** (1/3) % 1 < 1e-12