"""
Vowel counting utility.
"""
def vowels_count(s: str) -> int:
    """
    Write a function vowels_count which takes a string representing
    a single word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word. Note, trailing
    special characters or spaces do not matter, however, numbers and letters do effect
    whether 'y' is considered to be the last letter of the word.

    Examples:
        >>> vowels_count("abcde")
        2
        >>> vowels_count(" ACEDY!")
        3
    """
    lowered = s.lower()
    vowels = set("aeiou")
    count = 0
    last_letter = None
    for char in lowered:
        if char.isalpha():
            last_letter = char
            if char in vowels:
                count += 1
    if last_letter == "y":
        count += 1
    return count