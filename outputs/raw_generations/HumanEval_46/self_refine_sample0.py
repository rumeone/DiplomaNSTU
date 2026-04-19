def fib4(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0

    a, b, c, d = 0, 0, 2, 0
    for _ in range(4, n + 1):
        next_val = a + b + c + d
        a, b, c, d = b, c, d, next_val
    return d