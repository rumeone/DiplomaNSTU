"""
Count occurrences of digit 7 in qualifying integers.
"""

def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n
    which are divisible by 11 or 13.
    """
    if n <= 0:
        return 0

    total_sevens = 0
    for candidate in range(1, n):
        if candidate % 11 == 0 or candidate % 13 == 0:
            total_sevens += str(candidate).count("7")
    return total_sevens