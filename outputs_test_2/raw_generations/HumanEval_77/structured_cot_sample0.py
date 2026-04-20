def iscube(a: int) -> bool:
    """
    Check if number a is a cube of some integer number.

    Examples:
        iscube(2) == False
        iscube(64) == True
        iscube(-180) == False
    """
    # Edge case: 0 is a cube of 0
    if a == 0:
        return True

    # Handle negative numbers correctly
    sign = 1 if a >= 0 else -1
    abs_a = abs(a)

    # Check if the cubic root of the absolute value is an integer
    cube_root = round(abs_a ** (1/3))
    
    # Test both rounding directions to account for floating point precision
    return (cube_root ** 3 == abs_a or (cube_root + sign) ** 3 == abs_a) and (
        cube_root ** 3 * sign == a or (cube_root + sign) ** 3 * sign == a
    )