"""Solution to the fruit distribution problem."""

def fruit_distribution(s: str, n: int) -> int:
    """
    In this task, you will be given a string that represents a number of apples and oranges
    that are distributed in a basket of fruit this basket contains
    apples, oranges, and mango fruits. Given the string, that represents the total number of
    the oranges and apples, and an integer that represent the total number of the fruits
    in the basket, return the number of the mango fruits in the basket.

    For example:
        fruit_distribution("5 apples and 6 oranges", 19) -> 19 - 5 - 6 = 8
        fruit_distribution("0 apples and 1 orange", 3) -> 3 - 0 - 1 = 2
        fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
        fruit_distribution("100 apples and 1 orange", 120) -> 120 - 100 - 1 = 19
    """
    words = s.split()
    apples_count = int(words[0])
    oranges_count = int(words[3])
    mangoes_count = n - apples_count - oranges_count
    return mangoes_count