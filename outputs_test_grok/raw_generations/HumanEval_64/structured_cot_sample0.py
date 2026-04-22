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
    if not s:
        return 0
    cleaned = s.strip()
    if not cleaned:
        return 0
    lower = cleaned.lower()
    count = sum(1 for c in lower if c in "aeiou")
    if lower.endswith("y") and (len(lower) == 1 or not lower[-2].isalnum() or lower[-2].isalpha()):
        count += 1
    return count