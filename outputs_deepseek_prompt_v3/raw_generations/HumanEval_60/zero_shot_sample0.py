def sum_to_n(n: int) -> int:
    if n <= -1:
        return 0
    if n == 0:
        return 1
    return n * (n + 1) // 2