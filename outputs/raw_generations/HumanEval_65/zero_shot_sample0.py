def circular_shift(x: int, shift: int) -> str:
    digits = str(x)
    n = len(digits)
    
    if shift > n:
        return digits[::-1]
    
    shift = shift % n
    if shift == 0:
        return digits
    
    return digits[-shift:] + digits[:-shift]