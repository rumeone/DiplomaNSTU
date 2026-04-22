"""
Module for fruit distribution calculations.

This module provides a function to determine the number of mangoes
in a fruit basket given a description of apples and oranges along
with the total number of fruits.
"""


def fruit_distribution(s: str, n: int) -> int:
    """
    Return the number of mango fruits in the basket.

    Given a string describing the number of apples and oranges
    and the total number of fruits in the basket, calculates
    the number of mangoes by subtracting the apples and oranges
    from the total.

    Args:
        s: A string in the format "X apples and Y oranges" (or similar).
        n: The total number of fruits in the basket.

    Returns:
        The number of mango fruits in the basket.

    Examples:
        >>> fruit_distribution("5 apples and 6 oranges", 19)
        8
        >>> fruit_distribution("0 apples and 1 orange", 3)
        2
        >>> fruit_distribution("2 apples and 3 oranges", 100)
        95
        >>> fruit_distribution("100 apples and 1 orange", 120)
        19
    """
    words = s.split()
    apples = 0
    oranges = 0

    for i, word in enumerate(words):
        if word.isdigit():
            num = int(word)
            if i + 1 < len(words):
                fruit_type = words[i + 1].lower()
                if fruit_type.startswith("apple"):
                    apples = num
                elif fruit_type.startswith("orange"):
                    oranges = num

    mangoes = n - apples - oranges
    return mangoes