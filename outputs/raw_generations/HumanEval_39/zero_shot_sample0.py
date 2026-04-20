def prime_fib(n: int) -> int:
    def is_prime(num: int) -> bool:
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

    if n <= 0:
        return 0

    count = 0
    a, b = 0, 1
    while True:
        a, b = b, a + b
        if is_prime(a):
            count += 1
            if count == n:
                return a