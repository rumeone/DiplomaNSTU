"""
Module for calculating the number of mango fruits in a basket given the counts of apples and oranges.
"""


def fruit_distribution(s: str, n: int) -> int:
    """
    Calculate the number of mango fruits in a basket.

    The basket contains apples, oranges, and mangoes. The string `s` describes the number
    of apples and oranges, and `n` is the total number of fruits in the basket.

    Args:
        s: A string describing the number of apples and oranges (e.g., "5 apples and 6 oranges").
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