"""
Module providing a function to count vowels in a word according to specific rules.
Vowels are 'a', 'e', 'i', 'o', 'u' and 'y' only when it appears at the end of the word.
"""


def vowels_count(s: str) -> int:
    """
    Return the number of vowels in the input string.

    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word. Note, trailing
    special characters or spaces do not matter, however, numbers and letters do
    effect whether 'y' is considered to be the last letter of the word.

    Examples:
        >>> vowels_count("abcde")
        2
        >>> vowels_count(" ACEDY!")
        3
    """
    if not s:
        return 0

    # Convert to lowercase for case-insensitive comparison
    lower_s = s.lower()

    # Count standard vowels
    vowel_count = sum(1 for char in lower_s if char in "aeiou")

    # Check if 'y' should be counted as a vowel (only at the end of the word)
    # Find the last alphanumeric character to determine the true end of the word
    for char in reversed(lower_s):
        if char.isalnum():
            if char == "y":
                vowel_count += 1
            break

    return vowel_count