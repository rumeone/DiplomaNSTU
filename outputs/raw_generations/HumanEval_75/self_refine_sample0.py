def is_multiply_prime(a: int) -> bool:
    """
    Check if the given number is the multiplication of 3 prime numbers.
    Constraints:
        The three prime numbers must be <= 100.
    """
    if a <= 0:
        return False

    # Generate all primes <= 100 using sieve
    limit = 100
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    primes = [i for i, prime in enumerate(is_prime) if prime]

    # Try all combinations of three primes (allow repeats)
    n = len(primes)
    for i in range(n):
        p1 = primes[i]
        if p1 * p1 * p1 > a:
            break
        for j in range(i, n):
            p2 = primes[j]
            if p1 * p2 * p2 > a:
                break
            for k in range(j, n):
                p3 = primes[k]
                product = p1 * p2 * p3
                if product == a:
                    return True
                if product > a:
                    break
    return False