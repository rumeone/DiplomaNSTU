"""Module providing a function to remove vowels from text."""

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
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return ''.join(char for char in text if char not in vowels)