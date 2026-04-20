def fruit_distribution(s: str, n: int) -> int:
    """
    Return the number of mango fruits given a string describing apples and oranges,
    and the total number of fruits.
    """
    import re
    pattern = r'(\d+)\s+(apples?|oranges?)'
    matches = re.findall(pattern, s)
    apples = 0
    oranges = 0
    for num_str, fruit in matches:
        num = int(num_str)
        if fruit.startswith('apple'):
            apples = num
        elif fruit.startswith('orange'):
            oranges = num
    mangoes = n - apples - oranges
    return mangoes