def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.
    Assume n > 1 and is not a prime.
    """
    largest = 1
    
    # Factor out 2
    while n % 2 == 0:
        largest = 2
        n //= 2
    
    # Check odd factors
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest = factor
            n //= factor
        factor += 2
    
    # If remaining n > 1, it's prime
    if n > 1:
        largest = n
    
    return largest