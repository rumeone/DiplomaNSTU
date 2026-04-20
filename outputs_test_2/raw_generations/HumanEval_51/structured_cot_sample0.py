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
    vowels = "aeiouAEIOU"
    return "".join(char for char in text if char not in vowels)