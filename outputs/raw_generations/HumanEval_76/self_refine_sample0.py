def is_simple_power(x: int, n: int) -> bool:
    """
    Check if number x is a simple power of n.
    x is a simple power of n if n to the power of some integer equals x.
    """
    if n == 1:
        return x == 1
    if x == 1:
        return True
    if x < 1 or n < 1:
        return False
    
    current = 1
    while current <= x:
        if current == x:
            return True
        current *= n
        if current == 0:  # Handle overflow
            break
    return False