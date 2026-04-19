def iscube(a: int) -> bool:
    if a < 0:
        a = -a
        return round(a ** (1/3)) ** 3 == a
    return round(a ** (1/3)) ** 3 == a