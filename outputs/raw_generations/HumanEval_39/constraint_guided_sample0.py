def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and also prime.
    """
    if n <= 0:
        raise ValueError("n must be positive")
    
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        limit = int(num ** 0.5) + 1
        for divisor in range(3, limit, 2):
            if num % divisor == 0:
                return False
        return True
    
    count = 0
    a, b = 0, 1
    
    while True:
        a, b = b, a + b
        if a > 1 and is_prime(a):
            count += 1
            if count == n:
                return a