"""
Module for counting vowels in a word, with special handling for 'y' at the end.
"""


def vowels_count(s: str) -> int:
    """
    Count vowels in a word.

    Vowels are 'a', 'e', 'i', 'o', 'u'. Additionally, 'y' is considered a vowel
    only when it appears at the end of the word. Trailing special characters
    or spaces are ignored, but numbers and letters affect whether 'y' is final.

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

    # Find the last alphanumeric character
    last_char = None
    for char in reversed(s):
        if char.isalnum():
            last_char = char.lower()
            break

    # Count vowels in the string
    for char in s:
        if char.lower() in vowels:
            count += 1

    # Add count for 'y' if it's the last alphanumeric character
    if last_char == 'y':
        count += 1

    return count