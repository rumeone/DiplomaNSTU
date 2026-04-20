def largest_prime_factor(n: int) -> int:
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
        i += 1 if i == 2 else 2
    return n