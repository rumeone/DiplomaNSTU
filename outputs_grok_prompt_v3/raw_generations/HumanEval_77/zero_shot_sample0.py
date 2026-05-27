def iscube(a: int) -> bool:
    root = round(abs(a) ** (1 / 3))
    return root ** 3 == abs(a)