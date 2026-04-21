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
    # Divide out all factors of 2
    while n % 2 == 0:
        n //= 2
    if n == 1:
        return 2

    # Try odd factors up to sqrt(n)
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            n //= factor
        factor += 2

    # If n is a prime number greater than 2
    return n if n > 1 else factor - 2