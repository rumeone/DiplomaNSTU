def iscube(a: int) -> bool:
    if a == 0:
        return True
    if a > 0:
        root = round(a ** (1/3))
        return root ** 3 == a
    else:
        root = round((-a) ** (1/3))
        return (-root) ** 3 == a