def fruit_distribution(s: str, n: int) -> int:
    """
    Return the number of mango fruits given a string describing apples and oranges,
    and the total number of fruits.
    """
    # Split the string into words
    words = s.split()
    # Extract the numbers for apples and oranges
    # The pattern is: number word "apples" "and" number word "oranges"
    apples = int(words[0])
    oranges = int(words[3])
    # Mango count = total fruits - apples - oranges
    return n - apples - oranges