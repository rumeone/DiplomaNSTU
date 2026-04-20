def change_base(x: int, base: int) -> str:
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9 inclusive")
    
    if x == 0:
        return "0"
    
    result = ""
    is_negative = x < 0
    x = abs(x)
    
    while x > 0:
        remainder = x % base
        result = str(remainder) + result
        x //= base
    
    if is_negative:
        result = "-" + result
    
    return result