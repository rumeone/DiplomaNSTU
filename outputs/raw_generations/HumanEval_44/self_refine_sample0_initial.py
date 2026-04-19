def change_base(x: int, base: int) -> str:
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    if x == 0:
        return "0"
    
    digits = []
    is_negative = x < 0
    num = abs(x)
    
    while num > 0:
        remainder = num % base
        digits.append(str(remainder))
        num //= base
    
    if is_negative:
        digits.append('-')
    
    return ''.join(reversed(digits))