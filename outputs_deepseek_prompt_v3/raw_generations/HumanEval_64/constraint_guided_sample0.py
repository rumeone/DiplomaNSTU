"""
Module for counting vowels in words with special handling for 'y' at word endings.
"""


def vowels_count(s: str) -> int:
    """
    Count vowels in a word string.

    Vowels are 'a', 'e', 'i', 'o', 'u'. Additionally, 'y' is considered
    a vowel only when it appears at the end of the word. Trailing special
    characters and spaces are ignored when determining the end position.

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
    vowels = set("aeiou")
    count = 0

    # Find the last alphabetic character to determine if 'y' at end is a vowel
    last_alpha_index = -1
    for i, char in enumerate(s):
        if char.isalpha():
            last_alpha_index = i

    for i, char in enumerate(s):
        lower_char = char.lower()
        if lower_char in vowels:
            count += 1
        elif lower_char == 'y' and i == last_alpha_index:
            count += 1

    return count