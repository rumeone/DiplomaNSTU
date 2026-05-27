"""Prime factorization utility."""

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
    if n < 2:
        return []

    prime_factors = []

    # Extract all factors of 2
    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2

    # Check odd divisors up to sqrt(n)
    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            prime_factors.append(divisor)
            n //= divisor
        divisor += 2

    # Remaining prime factor
    if n > 1:
        prime_factors.append(n)

    return prime_factors