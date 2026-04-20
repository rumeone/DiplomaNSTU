def remove_vowels(text: str) -> str:
    """
    Return the text without vowels (a, e, i, o, u).
    """
    vowels = "aeiouAEIOU"
    result_chars = []
    for char in text:
        if char not in vowels:
            result_chars.append(char)
    return "".join(result_chars)