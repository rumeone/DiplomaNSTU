"""
Module for fruit distribution calculations.

This module provides a function to determine the number of mangoes
in a fruit basket given a description of apples and oranges along
with the total number of fruits.
"""


def fruit_distribution(s: str, n: int) -> int:
    """
    Return the number of mango fruits in the basket.

    Given a string describing the number of apples and oranges and
    the total number of fruits in the basket, calculates the number
    of mangoes by subtracting the apples and oranges from the total.

    Args:
        s: String describing apples and oranges (e.g. "5 apples and 6 oranges")
        n: Total number of fruits in the basket

    Returns:
        Number of mango fruits in the basket

    Examples:
        >>> fruit_distribution("5 apples and 6 oranges", 19)
        8
        >>> fruit_distribution("0 apples and 1 orange", 3)
        2
    """
    words = s.split()

    apples = 0
    oranges = 0

    if words and words[0].isdigit():
        apples = int(words[0])

    if len(words) >= 4 and words[3].isdigit():
        oranges = int(words[3])
    elif len(words) >= 2 and words[1].isdigit():
        oranges = int(words[1])

    mangoes = n - apples - oranges
    return max(0, mangoes)