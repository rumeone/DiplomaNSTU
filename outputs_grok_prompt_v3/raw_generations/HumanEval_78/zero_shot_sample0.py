def hex_key(num: str) -> int:
    primes = set("2357BD")
    return sum(1 for c in num if c in primes)