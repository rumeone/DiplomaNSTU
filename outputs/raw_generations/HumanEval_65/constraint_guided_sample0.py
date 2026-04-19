def circular_shift(x: int, shift: int) -> str:
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    """
    digits = str(x)
    n = len(digits)
    
    if shift > n:
        return digits[::-1]
    
    split_point = n - shift
    return digits[split_point:] + digits[:split_point]