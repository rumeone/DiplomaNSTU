"""
Module for counting vowels in a word, with special handling for 'y'.
"""


def vowels_count(s: str) -> int:
    """
    Count the vowels in a given word.

    Vowels are 'a', 'e', 'i', 'o', 'u'. Additionally, 'y' is considered
    a vowel only when it appears at the end of the word. Trailing special
    characters or spaces are ignored, but numbers and letters affect whether
    'y' is considered the last letter.

    Args:
        s: A string representing a single word.

    Returns:
        The number of vowels in the word.

    Examples:
        >>> vowels_count("abcde")
        2
        >>> vowels_count(" ACEDY!")
        3
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0

    # Remove trailing spaces and special characters
    stripped = s.rstrip(' !?.,;:')

    for i, char in enumerate(stripped):
        lower_char = char.lower()
        if lower_char in vowels:
            count += 1
        elif lower_char == 'y' and i == len(stripped) - 1:
            count += 1

    return count