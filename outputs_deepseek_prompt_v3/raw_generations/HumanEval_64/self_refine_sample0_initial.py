"""
Module for counting vowels in a word, with special handling for 'y' at the end.
"""


def vowels_count(s: str) -> int:
    """
    Count vowels in a word.

    Vowels are 'a', 'e', 'i', 'o', 'u'. Additionally, 'y' is considered a vowel
    only when it appears at the end of the word. Trailing special characters
    or spaces are ignored, but letters and numbers affect whether 'y' is at the end.

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

    # Process each character in the string
    for i, ch in enumerate(s):
        ch_lower = ch.lower()
        if ch_lower in vowels:
            count += 1
        elif ch_lower == 'y':
            # Check if this 'y' is at the end of the word
            # Look ahead to see if only non-letter/non-digit characters follow
            rest = s[i + 1:]
            if not rest or not any(c.isalnum() for c in rest):
                count += 1

    return count