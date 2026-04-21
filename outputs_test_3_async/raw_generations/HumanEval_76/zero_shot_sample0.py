def is_simple_power(x: int, n: int) -> bool:
    if n == 1:
        return x == 1
    if x == 1:
        return True
    power = 0
    current = 1
    while current <= x:
        if current == x:
            return True
        power += 1
        current = n ** power
    return False