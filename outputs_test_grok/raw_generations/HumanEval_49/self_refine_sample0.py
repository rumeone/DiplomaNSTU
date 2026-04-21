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
    if n == 0:
        return 1 % p
    if p == 1:
        return 0

    # Use built-in pow for efficient modular exponentiation
    # This handles large exponents without overflow
    result = pow(2, n, p)
    return result