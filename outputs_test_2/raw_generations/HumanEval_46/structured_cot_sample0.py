def fib4(n: int) -> int:
    """
    Compute the n-th element of the fib4 number sequence.
    fib4(0) = 0
    fib4(1) = 0
    fib4(2) = 2
    fib4(3) = 0
    fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n >= 4
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    sequence = [0, 0, 2, 0]
    if n < 4:
        return sequence[n]
    for i in range(4, n + 1):
        next_value = sum(sequence)
        sequence.pop(0)
        sequence.append(next_value)
    return sequence[-1]