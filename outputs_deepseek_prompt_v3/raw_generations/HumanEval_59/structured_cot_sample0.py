def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.
    Assume n > 1 and is not a prime.

    Examples:
        >>> largest_prime_factor(13195)
        29
        >>> largest_prime_factor(2048)
        2
    """
    factor = 2
    while factor * factor <= n:
        while n % factor == 0:
            n //= factor
        factor += 1 if factor == 2 else 2
    return n