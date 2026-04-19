def iscube(a: int) -> bool:
    if a == 0:
        return True
    sign = 1 if a > 0 else -1
    abs_a = abs(a)
    for i in range(1, int(abs_a ** (1/3)) + 2):
        if i * i * i == abs_a:
            return True
    return False