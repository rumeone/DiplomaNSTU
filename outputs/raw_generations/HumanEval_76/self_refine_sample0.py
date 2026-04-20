def is_simple_power(x: int, n: int) -> bool:
    """
    Check if number x is a simple power of n.
    x is a simple power of n if n to the power of some integer equals x.
    """
    # Handle special cases
    if n == 0:
        return x == 0 or x == 1
    if n == 1:
        return x == 1
    if x == 0:
        return n == 0
    if x == 1:
        return True  # n^0 = 1 for any n != 0
    
    # Check if x is a power of n by repeatedly dividing by n
    current = x
    while current % n == 0:
        current //= n
    return current == 1