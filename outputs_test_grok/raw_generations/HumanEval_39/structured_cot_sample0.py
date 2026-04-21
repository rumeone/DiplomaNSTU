def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and also prime.
    """
    a, b = 0, 1
    count = 0
    while True:
        if a > 1 and is_prime(a):
            count += 1
            if count == n:
                return a
        a, b = b, a + b