"""Prime factorization utilities."""

from typing import List


def factorize(n: int) -> List[int]:
    """
    Return a list of prime factors of the given integer in the order of smallest to largest.
    Each of the factors should be listed as often as it appears in the factorization.
    The input number should be equal to the product of all factors.

    Examples:
        >>> factorize(8)
        [2, 2, 2]
        >>> factorize(25)
        [5, 5]
        >>> factorize(70)
        [2, 5, 7]
    """
    if n <= 1:
        return []

    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    candidate = 3
    while candidate * candidate <= n:
        while n % candidate == 0:
            factors.append(candidate)
            n //= candidate
        candidate += 2

    if n > 1:
        factors.append(n)

    return factors