def iscube(a: int) -> bool:
    if a == 0:
        return True
    # Find the cube root candidate
    root = round(abs(a) ** (1/3))
    # Check both directions due to rounding errors
    return root ** 3 == abs(a) and (a > 0 or (a < 0 and root != 0))