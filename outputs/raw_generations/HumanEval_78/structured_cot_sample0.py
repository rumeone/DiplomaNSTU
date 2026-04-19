def hex_key(num: str) -> int:
    primes = {'2', '3', '5', '7', 'B', 'D'}
    count = 0
    for digit in num:
        if digit in primes:
            count += 1
    return count