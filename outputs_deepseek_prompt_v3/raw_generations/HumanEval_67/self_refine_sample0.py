"""
This module provides a function to calculate the number of mango fruits in a basket
given the count of apples and oranges and the total number of fruits.
"""


def fruit_distribution(s: str, n: int) -> int:
    """
    Calculate the number of mango fruits in a basket.

    The function takes a string describing the number of apples and oranges,
    and the total number of fruits in the basket. It returns the number of
    mango fruits, which is the total minus the apples and oranges.

    Args:
        s: A string describing the number of apples and oranges.
           Example: "5 apples and 6 oranges"
        n: The total number of fruits in the basket.

    Returns:
        The number of mango fruits in the basket.
    """
    words = s.split()
    apples = 0
    oranges = 0

    for i, word in enumerate(words):
        if word.isdigit():
            if i + 1 < len(words) and words[i + 1] == "apples":
                apples = int(word)
            elif i + 1 < len(words) and words[i + 1] == "oranges":
                oranges = int(word)

    mangoes = n - apples - oranges
    return mangoes