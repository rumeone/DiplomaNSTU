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
    return pow(2, n, p)