"""
This module provides a function to calculate the number of mango fruits in a basket
given a string describing apples and oranges, and the total number of fruits.
"""


def fruit_distribution(s: str, n: int) -> int:
    """
    Calculate the number of mango fruits in the basket.

    The input string describes the number of apples and oranges.
    The total number of fruits (apples, oranges, and mangoes) is given as n.
    The number of mangoes is computed by subtracting apples and oranges from n.

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
    numbers = [int(word) for word in words if word.isdigit()]
    apples_and_oranges_sum = sum(numbers)
    mango_count = n - apples_and_oranges_sum
    return mango_count