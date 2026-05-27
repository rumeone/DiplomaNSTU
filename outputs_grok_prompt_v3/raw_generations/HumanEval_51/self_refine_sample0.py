"""Module providing vowel removal functionality."""

def remove_vowels(text: str) -> str:
    """Return the text without vowels (a, e, i, o, u).

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
    vowel_characters = set("aeiouAEIOU")
    return "".join(
        character for character in text if character not in vowel_characters
    )