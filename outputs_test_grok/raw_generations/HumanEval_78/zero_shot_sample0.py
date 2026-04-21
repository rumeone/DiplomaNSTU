def hex_key(num: str) -> int:
    if not num:
        return 0
    primes = {'2', '3', '5', '7', 'B', 'D'}
    count = 0
    for char in num:
        if char in primes:
            count += 1
    return count