def decimal_to_binary(decimal: int) -> str:
    if decimal == 0:
        return "db0db"
    
    binary_digits = []
    n = decimal
    
    while n > 0:
        binary_digits.append(str(n % 2))
        n //= 2
    
    binary_digits.reverse()
    binary_str = ''.join(binary_digits)
    
    return f"db{binary_str}db"