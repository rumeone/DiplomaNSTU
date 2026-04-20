def fruit_distribution(s: str, n: int) -> int:
    """
    Return the number of mango fruits given a string describing apples and oranges,
    and the total number of fruits.
    """
    # Split the string into words
    words = s.split()
    apples = 0
    oranges = 0
    
    # Iterate through words to find numbers followed by 'apples' or 'oranges'
    for i, word in enumerate(words):
        if word == "apples" and i > 0:
            try:
                apples = int(words[i-1])
            except ValueError:
                apples = 0
        elif word == "oranges" and i > 0:
            try:
                oranges = int(words[i-1])
            except ValueError:
                oranges = 0
        elif word == "orange" and i > 0:  # Handle singular "orange"
            try:
                oranges = int(words[i-1])
            except ValueError:
                oranges = 0
    
    mangoes = n - apples - oranges
    return mangoes