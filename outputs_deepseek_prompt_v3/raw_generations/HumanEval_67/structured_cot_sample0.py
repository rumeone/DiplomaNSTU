def fruit_distribution(s: str, n: int) -> int:
    """
    Calculate the number of mango fruits in the basket.

    The basket contains apples, oranges, and mangoes.
    The string s describes the count of apples and oranges.
    The integer n is the total number of fruits in the basket.
    Return the number of mangoes.
    """
    import re
    numbers = list(map(int, re.findall(r'\d+', s)))
    return n - sum(numbers)