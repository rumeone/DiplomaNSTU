def fruit_distribution(s: str, n: int) -> int:
    """
    Calculate the number of mango fruits in the basket.
    The string s contains the count of apples and oranges.
    n is the total number of all fruits (apples, oranges, mangoes).
    """
    # Split the string into words
    words = s.split()
    # Initialize counts
    apple_count = 0
    orange_count = 0
    
    # Iterate through words to find numbers followed by 'apples' or 'oranges'
    for i, word in enumerate(words):
        if word == "apples" and i > 0:
            try:
                apple_count = int(words[i-1])
            except ValueError:
                apple_count = 0
        elif word == "oranges" and i > 0:
            try:
                orange_count = int(words[i-1])
            except ValueError:
                orange_count = 0
        elif word == "orange" and i > 0:  # Handle singular "orange"
            try:
                orange_count = int(words[i-1])
            except ValueError:
                orange_count = 0
    
    # Mango count = total fruits - apples - oranges
    mango_count = n - apple_count - orange_count
    return mango_count