"""
Module providing vowel counting functionality for strings.
"""


def vowels_count(s: str) -> int:
    """
    Return the number of vowels in the given string.

    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel, but only
    when it is at the end of the word (i.e. the last alphanumeric
    character). Trailing special characters or spaces are ignored when
    determining the end of the word, but numbers and other letters
    affect whether 'y' counts as a trailing vowel.

    Examples:
        >>> vowels_count("abcde")
        2
        >>> vowels_count(" ACEDY!")
        3
    """
    if not s:
        return 0

    # Convert to lowercase for case-insensitive matching
    lower_s = s.lower()

    # Count standard vowels
    vowel_count = sum(1 for char in lower_s if char in "aeiou")

    # Check if 'y' should be counted as a vowel (only at the end of the word)
    # Find the last alphanumeric character
    last_alphanumeric = None
    for char in reversed(lower_s):
        if char.isalnum():
            last_alphanumeric = char
            break

    if last_alphanumeric == "y":
        vowel_count += 1

    return vowel_count