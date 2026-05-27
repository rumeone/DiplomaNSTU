"""
Utility to determine whether an integer is the product of exactly three primes
each no larger than 100.
"""

def is_multiply_prime(a: int) -> bool:
    """
    Check if the given number is the multiplication of 3 prime numbers.

    Constraints:
        The three prime numbers must be <= 100.

    Example:
        is_multiply_prime(30) == True
        30 = 2 * 3 * 5
    """
    if a < 2:
        return False

    def _is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for divisor in range(3, int(n ** 0.5) + 1, 2):
            if n % divisor == 0:
                return False
        return True

    prime_factors = []
    candidate = 2
    while candidate * candidate <= a:
        while a % candidate == 0:
            if candidate > 100:
                return False
            prime_factors.append(candidate)
            a //= candidate
        candidate += 1 if candidate == 2 else 2

    if a > 1:
        if a > 100 or not _is_prime(a):
            return False
        prime_factors.append(a)

    return len(prime_factors) == 3