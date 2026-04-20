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
    sieve = [True] * 101
    sieve[0:2] = [False, False]
    for i in range(2, int(100**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, 101, i):
                sieve[j] = False
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]

    # Check all combinations of three primes
    n = len(primes)
    for i in range(n):
        for j in range(i, n):
            product = primes[i] * primes[j]
            if product > a:
                break
            for k in range(j, n):
                total = product * primes[k]
                if total == a:
                    return True
                if total > a:
                    break
    return False