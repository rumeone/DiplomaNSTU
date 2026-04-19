def greatest_common_divisor(a: int, b: int) -> int:
    # Use Euclidean algorithm
    while b:
        a, b = b, a % b
    return abs(a)