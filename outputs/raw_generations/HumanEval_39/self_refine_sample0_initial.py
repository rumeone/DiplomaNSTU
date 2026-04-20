def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and also prime.
    """
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        limit = int(num ** 0.5) + 1
        for i in range(3, limit, 2):
            if num % i == 0:
                return False
        return True

    if n <= 0:
        return 0

    count = 0
    a, b = 0, 1
    while count < n:
        a, b = b, a + b
        if a > 1 and is_prime(a):
            count += 1
            if count == n:
                return a
    return 0