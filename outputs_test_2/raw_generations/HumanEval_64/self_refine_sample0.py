"""
Module for counting vowels in words with special handling for the letter 'y'.
"""


def vowels_count(s: str) -> int:
    """
    Count vowels in a word.

    Vowels are 'a', 'e', 'i', 'o', 'u'. The letter 'y' is considered a vowel
    only when it appears at the end of the word. Trailing special characters
    and spaces are ignored, but numbers and letters affect whether 'y' is
    considered the last letter.

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
    vowels = set('aeiou')
    count = 0

    # Find the last alphanumeric character
    last_alpha_index = -1
    for i, char in enumerate(s):
        if char.isalnum():
            last_alpha_index = i

    # If no alphanumeric characters exist, return 0
    if last_alpha_index == -1:
        return 0

    # Count vowels
    for i, char in enumerate(s):
        if i > last_alpha_index:
            break
        if char.lower() in vowels:
            count += 1
        elif i == last_alpha_index and char.lower() == 'y':
            count += 1

    return count