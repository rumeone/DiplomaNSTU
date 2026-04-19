def is_multiply_prime(a: int) -> bool:
    if a <= 1:
        return False
    
    primes = []
    for num in range(2, 101):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    
    n = len(primes)
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                if primes[i] * primes[j] * primes[k] == a:
                    return True
    return False