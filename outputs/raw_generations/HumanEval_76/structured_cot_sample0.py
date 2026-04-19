def is_simple_power(x: int, n: int) -> bool:
    if n == 1:
        return x == 1
    if x == 1:
        return True
    if x < n:
        return False
    power = 0
    result = 1
    while result <= x:
        if result == x:
            return True
        power += 1
        result = n ** power
    return False