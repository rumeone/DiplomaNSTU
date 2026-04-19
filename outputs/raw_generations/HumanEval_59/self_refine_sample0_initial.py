def largest_prime_factor(n: int) -> int:
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1 if factor == 2 else 2  # skip even numbers after 2
    return n