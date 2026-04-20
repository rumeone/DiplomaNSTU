def iscube(a: int) -> bool:
    if a < 0:
        a = -a
        sign = -1
    else:
        sign = 1
    
    for i in range(int(a ** (1/3)) + 2):
        if i ** 3 == a:
            return True
        if i ** 3 > a:
            break
    return False