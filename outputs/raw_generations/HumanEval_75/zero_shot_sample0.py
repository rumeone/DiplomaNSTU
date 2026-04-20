def is_multiply_prime(a: int) -> bool:
    """
    Check if the given number is the multiplication of 3 prime numbers.
    
    Constraints:
        The three prime numbers must be <= 100.
    
    Example:
        is_multiply_prime(30) == True
        30 = 2 * 3 * 5
    """
    if a <= 0:
        return False
    
    # Generate primes up to 100
    primes = []
    for num in range(2, 101):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    
    # Check all combinations of 3 primes
    n = len(primes)
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                if primes[i] * primes[j] * primes[k] == a:
                    return True
    return False