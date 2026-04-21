def is_multiply_prime(a: int) -> bool:
    """
    Check if the given number is the multiplication of 3 prime numbers.

    Constraints:
        The three prime numbers must be <= 100.

    Example:
        is_multiply_prime(30) == True
        30 = 2 * 3 * 5
    """
    if a <= 1:
        return False

    # Generate primes up to 100 using Sieve of Eratosthenes
    limit = 100
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    primes = [i for i, prime in enumerate(is_prime) if prime]

    # Check all combinations of three primes
    n = len(primes)
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                if primes[i] * primes[j] * primes[k] == a:
                    return True
    return False