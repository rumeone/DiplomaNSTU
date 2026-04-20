"""
Compute modular exponentiation of powers of two efficiently.
"""


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
    if p == 1:
        return 0

    result = 1
    base = 2 % p

    while n > 0:
        if n % 2 == 1:
            result = (result * base) % p
        base = (base * base) % p
        n //= 2

    return result