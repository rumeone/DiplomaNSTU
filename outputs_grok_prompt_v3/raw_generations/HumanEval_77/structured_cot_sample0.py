"""Check whether an integer is a perfect cube."""

def iscube(a: int) -> bool:
    """Check if number a is a cube of some integer number.

    Examples:
        iscube(2) == False
        iscube(64) == True
        iscube(-180) == False
    """
    if a < 0:
        return iscube(-a)
    root = round(a ** (1 / 3))
    return root ** 3 == a