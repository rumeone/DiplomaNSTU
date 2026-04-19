def remove_vowels(text: str) -> str:
    """
    Return the text without vowels (a, e, i, o, u).
    """
    vowels = "aeiou"
    return "".join(char for char in text if char.lower() not in vowels)