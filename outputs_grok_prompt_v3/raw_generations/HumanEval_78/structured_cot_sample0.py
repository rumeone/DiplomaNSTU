"""Count prime hexadecimal digits in a given string."""

def hex_key(num: str) -> int:
    """Count prime hexadecimal digits (2, 3, 5, 7, B, D) in num."""
    primes = set("2357BD")
    return sum(d in primes for d in num)