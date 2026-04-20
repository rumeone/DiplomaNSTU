def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.
    Assume n > 1 and is not a prime.
    """
    original_n = n
    largest_factor = 1
    
    # Check for factor 2
    while n % 2 == 0:
        largest_factor = 2
        n //= 2
    
    # Check for odd factors
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest_factor = factor
            n //= factor
        factor += 2
    
    # If n is still greater than 1, it's a prime factor
    if n > 1:
        largest_factor = n
    
    return largest_factor