def is_simple_power(x: int, n: int) -> bool:
    if x == 1:
        return True
    if n == 1:
        return x == 1
    if x <= 0 or n <= 0:
        return False
    current = n
    while current < x:
        if current > x // n:
            return False
        current *= n
    return current == x