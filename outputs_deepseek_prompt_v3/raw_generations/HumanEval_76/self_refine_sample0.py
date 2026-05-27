def is_simple_power(x: int, n: int) -> bool:
    """
    Check if number x is a simple power of n.
    x is a simple power of n if n to the power of some integer equals x.
    """
    if n == 0:
        return x == 0
    if n == 1:
        return x == 1
    if x == 1:
        return True
    if n == -1:
        return x == 1 or x == -1

    exponent = 0
    power = 1
    while True:
        if power == x:
            return True
        exponent += 1
        power *= n
        if abs(power) > abs(x) and exponent > 0:
            break
    return False