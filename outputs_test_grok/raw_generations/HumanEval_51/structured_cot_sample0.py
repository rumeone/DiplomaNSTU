def remove_vowels(text: str) -> str:
    """
    Return the text without vowels (a, e, i, o, u).

    Examples:
        >>> remove_vowels('abcdef')
        'bcdf'
        >>> remove_vowels('aaaaa')
        ''
        >>> remove_vowels('aaBAA')
        'B'
        >>> remove_vowels('zbcd')
        'zbcd'
    """
    vowels = set("aeiouAEIOU")
    return "".join(c for c in text if c not in vowels)