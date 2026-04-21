def is_multiply_prime(a: int) -> bool:
    if a < 2 * 3 * 5 or a > 100 * 100 * 100:
        return False
    
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    primes = [p for p in range(2, 101) if is_prime(p)]
    
    for i in range(len(primes)):
        p1 = primes[i]
        if p1 * p1 * p1 > a:
            break
        for j in range(i, len(primes)):
            p2 = primes[j]
            if p1 * p2 * p2 > a:
                break
            prod = p1 * p2
            if prod > a:
                break
            if a % prod == 0:
                p3 = a // prod
                if p3 <= 100 and is_prime(p3):
                    return True
    return False