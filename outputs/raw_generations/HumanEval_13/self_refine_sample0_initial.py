def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return the greatest common divisor of two integers a and b
    """
    # Handle negative numbers by taking absolute values
    a = abs(a)
    b = abs(b)
    
    # Euclidean algorithm
    while b != 0:
        a, b = b, a % b
    
    return a