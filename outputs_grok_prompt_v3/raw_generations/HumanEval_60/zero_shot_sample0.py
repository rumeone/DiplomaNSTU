def sum_to_n(n: int) -> int:
    if n == 0:
        return 1
    return n * (n + 1) // 2