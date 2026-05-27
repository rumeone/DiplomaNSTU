"""Utility for prime product checks."""

def is_multiply_prime(a: int) -> bool:
    """Check if the given number is the multiplication of 3 prime numbers.

    Constraints:
        The three prime numbers must be <= 100.

    Example:
        is_multiply_prime(30) == True
        30 = 2 * 3 * 5
    """
    if a < 8:
        return False

    def generate_primes(limit: int) -> set:
        if limit < 2:
            return set()
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        for num in range(2, int(limit ** 0.5) + 1):
            if sieve[num]:
                for multiple in range(num * num, limit + 1, num):
                    sieve[multiple] = False
        return {i for i, is_prime in enumerate(sieve) if is_prime}

    primes = generate_primes(100)
    prime_set = primes

    for p in primes:
        if p > a:
            break
        for q in primes:
            if p * q > a:
                break
            remainder = a // (p * q)
            if p * q * remainder == a and remainder in prime_set:
                return True
    return False