"""
Module for calculating the number of mango fruits in a basket given the counts of apples and oranges.
"""


def fruit_distribution(s: str, n: int) -> int:
    """
    Return the number of mango fruits in the basket.

    The basket contains apples, oranges, and mangoes. The string `s` describes the number
    of apples and oranges, and `n` is the total number of all fruits in the basket.

    Args:
        s: A string describing the number of apples and oranges (e.g., "5 apples and 6 oranges").
        n: The total number of fruits in the basket.

    Returns:
        The number of mango fruits in the basket.
    """
    words = s.split()
    apples = int(words[0])
    oranges = int(words[-2])
    mangoes = n - apples - oranges
    return mangoes