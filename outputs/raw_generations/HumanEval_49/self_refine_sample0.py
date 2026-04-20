def modp(n: int, p: int) -> int:
    """
    Solve 2^n modulo p (be aware of numerics).
    Return the least non-negative residue.

    Examples:
        >>> modp(3, 5)
        3
        >>> modp(100, 101)
        1
    """
    if p <= 1:
        return 0
    
    result = 1
    base = 2 % p
    exponent = n
    
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % p
        base = (base * base) % p
        exponent >>= 1
    
    return result