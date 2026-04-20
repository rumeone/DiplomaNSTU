def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.
    Assume n > 1 and is not a prime.
    """
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
        i += 1 if i == 2 else 2
    return n