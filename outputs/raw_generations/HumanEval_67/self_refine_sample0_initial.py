def fruit_distribution(s: str, n: int) -> int:
    """
    Return the number of mango fruits in the basket.
    s: string describing number of apples and oranges.
    n: total number of fruits in the basket.
    """
    # Split the string into words
    words = s.split()
    # Extract numbers: they are at positions 0 and 3 in the standard format
    apples = int(words[0])
    oranges = int(words[3])
    # Mango count = total fruits - apples - oranges
    return n - apples - oranges