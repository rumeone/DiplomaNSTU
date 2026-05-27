"""Fizz buzz digit counting utility."""

def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n
    which are divisible by 11 or 13.

    Examples:
        >>> fizz_buzz(50)
        0
        >>> fizz_buzz(78)
        2
        >>> fizz_buzz(79)
        3
    """
    total_sevens = 0
    for number in range(n):
        if number % 11 == 0 or number % 13 == 0:
            digit_string = str(number)
            total_sevens += digit_string.count("7")
    return total_sevens