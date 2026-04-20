def iscube(a: int) -> bool:
    if a < 0:
        return False
    root = round(a ** (1/3))
    return root ** 3 == a