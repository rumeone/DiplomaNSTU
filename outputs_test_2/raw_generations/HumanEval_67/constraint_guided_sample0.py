"""
This module provides a function to calculate the number of mango fruits in a basket
given a string describing apples and oranges and the total number of fruits.
"""


def fruit_distribution(s: str, n: int) -> int:
    """
    Calculate the number of mango fruits in a basket.

    The basket contains apples, oranges, and mangoes. The string `s` describes
    the number of apples and oranges. The integer `n` is the total number of
    fruits. The number of mangoes is the total minus apples and oranges.

    Args:
        s: A string describing the number of apples and oranges.
        n: The total number of fruits in the basket.

    Returns:
        The number of mango fruits in the basket.

    Examples:
        >>> fruit_distribution("5 apples and 6 oranges", 19)
        8
        >>> fruit_distribution("0 apples and 1 orange", 3)
        2
    """
    words = s.split()
    apples = int(words[0])
    oranges = int(words[-2])
    return n - apples - oranges