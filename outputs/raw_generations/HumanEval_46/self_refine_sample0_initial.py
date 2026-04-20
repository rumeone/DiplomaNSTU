def fib4(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 4:
        return [0, 0, 2, 0][n]
    
    a, b, c, d = 0, 0, 2, 0  # fib4(0), fib4(1), fib4(2), fib4(3)
    for _ in range(4, n + 1):
        next_val = a + b + c + d
        a, b, c, d = b, c, d, next_val
    
    return d