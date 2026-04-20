def iscube(a: int) -> bool:
    """
    Check if number a is a cube of some integer number.
    """
    if a == 0:
        return True

    # Find the integer cube root candidate
    root = int(round(abs(a) ** (1 / 3)))
    if a < 0:
        root = -root

    # Check candidates around the approximation
    candidates = {root - 1, root, root + 1}
    for candidate in candidates:
        if candidate ** 3 == a:
            return True

    return False