def fruit_distribution(s: str, n: int) -> int:
    """
    Calculate the number of mango fruits in a basket.

    The basket contains apples, oranges, and mangoes. The string `s` describes
    the number of apples and oranges. The integer `n` is the total number of
    fruits. The mango count is the total minus the apples and oranges.

    Args:
        s: A string like "X apples and Y oranges".
        n: Total number of fruits in the basket.

    Returns:
        Number of mango fruits.
    """
    # Split the string into words
    words = s.split()
    # Extract the numbers: first token and the token before "oranges"
    apples = int(words[0])
    oranges = int(words[words.index("oranges") - 1])
    # Mangoes = total - apples - oranges
    return n - apples - oranges