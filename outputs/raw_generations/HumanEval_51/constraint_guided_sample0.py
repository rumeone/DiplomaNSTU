def remove_vowels(text: str) -> str:
    """
    Return the text without vowels (a, e, i, o, u).
    """
    vowels = "aeiou"
    # Use a list comprehension to filter out vowels (case-sensitive)
    result_chars = [char for char in text if char not in vowels]
    return "".join(result_chars)