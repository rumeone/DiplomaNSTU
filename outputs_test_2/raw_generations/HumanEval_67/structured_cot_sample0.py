def fruit_distribution(s: str, n: int) -> int:
    """
    Return the number of mango fruits in the basket.

    The input string s contains the number of apples and oranges.
    The integer n is the total number of fruits in the basket.
    Mango count is calculated as total fruits minus apples minus oranges.
    """
    # Extract all numbers from the string
    numbers = [int(word) for word in s.split() if word.isdigit()]
    # Sum the extracted numbers (apples and oranges)
    apples_and_oranges = sum(numbers)
    # Mango count = total fruits - apples - oranges
    return n - apples_and_oranges