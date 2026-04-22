"""
Compute 2^n modulo p efficiently using exponentiation by squaring.

The function returns the least non-negative residue of 2^n modulo p.
It handles the computation safely to avoid overflow issues with large exponents.
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
    if n == 0:
        return 1 % p
    if p == 1:
        return 0

    # Initialize result to 1 (which represents 2^0)
    result = 1
    # Start with base = 2
    base = 2 % p

    # Use exponentiation by squaring
    exponent = n
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % p
        base = (base * base) % p
        exponent //= 2

    return result