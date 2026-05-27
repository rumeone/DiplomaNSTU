def remove_vowels(text: str) -> str:
    vowels = 'aeiouAEIOU'
    return ''.join(c for c in text if c not in vowels)