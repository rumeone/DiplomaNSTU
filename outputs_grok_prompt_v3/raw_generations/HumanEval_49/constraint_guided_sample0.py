"""Compute modular exponentiation for 2^n mod p."""

def modp(n: int, p: int) -> int:
    """Solve 2^n modulo p (be aware of numerics).

    Return the least non-negative residue.
    """
    if p == 1:
        return 0
    return pow(2, n, p)