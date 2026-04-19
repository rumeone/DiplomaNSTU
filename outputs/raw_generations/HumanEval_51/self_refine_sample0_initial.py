def remove_vowels(text: str) -> str:
    """
    Return the text without vowels (a, e, i, o, u).
    """
    vowels = "aeiou"
    # Use a list comprehension to filter out vowels (case-insensitive)
    result_chars = [char for char in text if char.lower() not in vowels]
    # Join the list back into a string
    return "".join(result_chars)