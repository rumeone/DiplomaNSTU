def remove_vowels(text: str) -> str:
    """
    Return the text without vowels (a, e, i, o, u).
    """
    vowels = set('aeiouAEIOU')
    result = []
    for char in text:
        if char not in vowels:
            result.append(char)
    return ''.join(result)