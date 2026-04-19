def largest_divisor(n: int) -> int:
    if n <= 1:
        return -1
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return -1