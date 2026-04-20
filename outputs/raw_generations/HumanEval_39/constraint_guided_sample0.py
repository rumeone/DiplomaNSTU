def prime_fib(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 2
    
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
    
    count = 1
    a, b = 1, 1
    
    while count < n:
        a, b = b, a + b
        if is_prime(b):
            count += 1
    
    return b