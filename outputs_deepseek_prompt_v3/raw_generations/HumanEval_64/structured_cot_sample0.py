def vowels_count(s: str) -> int:
    """
    Count vowels in a word. Vowels are 'a', 'e', 'i', 'o', 'u'.
    'y' is also a vowel, but only when it is at the end of the word.
    Trailing special characters or spaces are ignored.
    """
    vowels = set('aeiou')
    word = s.strip().rstrip('!?., ')
    count = sum(1 for ch in word.lower() if ch in vowels)
    if word and word[-1].lower() == 'y':
        count += 1
    return count