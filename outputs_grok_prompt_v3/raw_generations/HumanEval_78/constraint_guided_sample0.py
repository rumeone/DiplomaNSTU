"""Count the number of prime hexadecimal digits in a given string."""

def hex_key(num: str) -> int:
    """Count prime hex digits (2, 3, 5, 7, B, D) in the input string."""
    prime_hex_digits = {"2", "3", "5", "7", "B", "D"}
    if not num:
        return 0
    return sum(1 for digit in num if digit in prime_hex_digits)