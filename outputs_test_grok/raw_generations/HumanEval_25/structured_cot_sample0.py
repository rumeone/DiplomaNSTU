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
    factors = []
    # Handle factor 2 separately to make the loop only odd numbers
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Check for odd factors
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    # If n is a prime number greater than 2
    if n > 1:
        factors.append(n)
    return factors