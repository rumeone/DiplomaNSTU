"""Vowel counting utility for words with special 'y' handling."""

def vowels_count(s: str) -> int:
    """
    Write a function vowels_count which takes a string representing
    a single word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word. Note, trailing
    special characters or spaces do not matter, however, numbers and letters do effect
    whether 'y' is considered to be the last letter of the word.
    """
    vowels = set("aeiouAEIOU")
    count = sum(1 for char in s if char in vowels)

    last_letter = None
    for char in reversed(s):
        if char.isalpha():
            last_letter = char.lower()
            break

    if last_letter == "y":
        count += 1

    return count