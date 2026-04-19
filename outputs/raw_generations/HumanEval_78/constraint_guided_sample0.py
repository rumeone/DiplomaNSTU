def hex_key(num: str) -> int:
    prime_digits = {'2', '3', '5', '7', 'B', 'D'}
    count = 0
    for ch in num:
        if ch in prime_digits:
            count += 1
    return count