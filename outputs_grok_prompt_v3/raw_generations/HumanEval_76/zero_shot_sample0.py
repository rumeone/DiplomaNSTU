def is_simple_power(x: int, n: int) -> bool:
    if x == 1:
        return True
    if n == 1 or n == 0:
        return False
    power = 1
    while power < x:
        try:
            power *= n
        except OverflowError:
            return False
        if power == x:
            return True
    return False