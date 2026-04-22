"""
Module for solving the fizz_buzz counting problem.

This module provides a function to count occurrences of the digit 7
in numbers less than n that are divisible by 11 or 13.
"""


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
    if n <= 0:
        return 0

    count = 0
    for num in range(1, n):
        if num % 11 == 0 or num % 13 == 0:
            count += str(num).count('7')

    return count