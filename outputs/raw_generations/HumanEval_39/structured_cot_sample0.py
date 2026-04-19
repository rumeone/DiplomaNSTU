def prime_fib(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 2
    
    def is_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        i = 3
        while i * i <= num:
            if num % i == 0:
                return False
            i += 2
        return True
    
    count = 1
    a, b = 1, 1
    
    while count < n:
        a, b = b, a + b
        if is_prime(b):
            count += 1
            if count == n:
                return b
    return b