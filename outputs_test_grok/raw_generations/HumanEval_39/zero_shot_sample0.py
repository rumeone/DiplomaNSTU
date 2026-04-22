def is_prime(x: int) -> bool:
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_fib(n: int) -> int:
    if n == 1:
        return 2
    a, b = 2, 3
    count = 1
    while True:
        if is_prime(b):
            count += 1
            if count == n:
                return b
        a, b = b, a + b