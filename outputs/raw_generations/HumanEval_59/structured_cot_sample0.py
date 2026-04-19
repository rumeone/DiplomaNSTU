def largest_prime_factor(n: int) -> int:
    original = n
    factor = 2
    largest = 2
    
    while factor * factor <= original:
        while n % factor == 0:
            largest = factor
            n //= factor
        factor += 1 if factor == 2 else 2
    
    if n > 1:
        largest = n
    
    return largest