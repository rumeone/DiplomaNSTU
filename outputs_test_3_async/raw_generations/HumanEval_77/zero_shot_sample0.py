def iscube(a: int) -> bool:
    if a == 0:
        return True
    if a > 0:
        return round(a ** (1/3)) ** 3 == a
    else:
        return round((-a) ** (1/3)) ** 3 == -a