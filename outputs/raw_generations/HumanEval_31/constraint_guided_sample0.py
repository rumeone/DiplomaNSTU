def is_prime(n: int) -> bool:
    """
    Check if given number is considered to be prime.
    
    A prime number is a natural number greater than 1 that has no positive
    divisors other than 1 and itself.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check for factors from 5 to sqrt(n)
    # All primes greater than 3 can be written as 6k ± 1
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True