def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and also prime.

    Examples:
        >>> prime_fib(1)
        2
        >>> prime_fib(2)
        3
        >>> prime_fib(3)
        5
        >>> prime_fib(4)
        13
        >>> prime_fib(5)
        89
    """
    from math import isqrt

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        if num % 2 == 0:
            return num == 2
        for i in range(3, isqrt(num) + 1, 2):
            if num % i == 0:
                return False
        return True

    fib_primes = []
    a, b = 0, 1
    while len(fib_primes) < n:
        a, b = b, a + b
        if is_prime(b):
            fib_primes.append(b)
    return fib_primes[-1]