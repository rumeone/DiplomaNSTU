def decimal_to_binary(decimal: int) -> str:
    """
    Convert a positive decimal integer to binary string with 'db' prefix and suffix.
    """
    if decimal == 0:
        return "db0db"
    
    binary_digits = []
    num = decimal
    
    while num > 0:
        binary_digits.append(str(num % 2))
        num //= 2
    
    binary_str = ''.join(reversed(binary_digits))
    return f"db{binary_str}db"