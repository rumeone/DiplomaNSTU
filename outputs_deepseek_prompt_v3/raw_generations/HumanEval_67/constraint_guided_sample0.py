"""
This module provides a function to calculate the number of mango fruits in a basket
given a string describing apples and oranges, and the total number of fruits.
"""


def fruit_distribution(s: str, n: int) -> int:
    """
    Calculate the number of mango fruits in a basket.

    The basket contains apples, oranges, and mangoes. The input string describes
    the number of apples and oranges, and the total number of fruits is given.
    The number of mangoes is the total minus the apples and oranges.

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
        >>> fruit_distribution("2 apples and 3 oranges", 100)
        95
        >>> fruit_distribution("100 apples and 1 orange", 120)
        19
    """
    total_apples_oranges = 0
    current_number = ""

    for char in s:
        if char.isdigit():
            current_number += char
        elif current_number:
            total_apples_oranges += int(current_number)
            current_number = ""

    if current_number:
        total_apples_oranges += int(current_number)

    return n - total_apples_oranges