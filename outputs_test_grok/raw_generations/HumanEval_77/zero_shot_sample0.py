def iscube(a: int) -> bool:
    if a == 0:
        return True
    if a < 0:
        return iscube(-a)
    lo = 1
    hi = a
    while lo <= hi:
        mid = (lo + hi) // 2
        cube = mid * mid * mid
        if cube == a:
            return True
        elif cube < a:
            lo = mid + 1
        else:
            hi = mid - 1
    return False