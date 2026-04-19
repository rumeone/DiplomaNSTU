def modp(n: int, p: int) -> int:
    """
    Compute 2^n modulo p efficiently using binary exponentiation.
    Returns the least non-negative residue.
    """
    if p == 1:
        return 0
    result = 1
    base = 2 % p
    exp = n
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % p
        base = (base * base) % p
        exp //= 2
    return result