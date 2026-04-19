def iscube(a: int) -> bool:
    """
    Check if number a is a cube of some integer number.
    """
    if a == 0:
        return True
    if a < 0:
        candidate = -round((-a) ** (1/3))
    else:
        candidate = round(a ** (1/3))
    return candidate ** 3 == a