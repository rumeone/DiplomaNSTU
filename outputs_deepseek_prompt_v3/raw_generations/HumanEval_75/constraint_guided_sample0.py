"""
Check if a number is the product of exactly three prime numbers ≤ 100.
"""


def is_multiply_prime(a: int) -> bool:
    """
    Return True if the given number is the multiplication of exactly three
    prime numbers, each ≤ 100.

    Args:
        a: The integer to check.

    Returns:
        True if a can be expressed as the product of three primes ≤ 100,
        False otherwise.
    """
    if a <= 0:
        return False

    # Generate primes up to 100 using the Sieve of Eratosthenes
    sieve = [True] * 101
    sieve[0] = sieve[1] = False
    for i in range(2, int(101 ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, 101, i):
                sieve[j] = False
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]

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