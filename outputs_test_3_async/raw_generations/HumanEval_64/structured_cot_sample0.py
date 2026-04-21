def vowels_count(s: str) -> int:
    """
    Count vowels in a word.

    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel,
    but only when it is at the end of the word (ignoring trailing
    special characters or spaces). Numbers and letters affect whether
    'y' is considered the last letter.

    Args:
        s: A string representing a single word.

    Returns:
        The number of vowels in the word.
    """
    vowels = set('aeiou')
    count = 0

    # Process the string to find the last alphanumeric character
    last_alpha_index = -1
    for i, ch in enumerate(s):
        if ch.isalnum():
            last_alpha_index = i

    for i, ch in enumerate(s):
        ch_lower = ch.lower()
        if ch_lower in vowels:
            count += 1
        elif ch_lower == 'y' and i == last_alpha_index:
            count += 1

    return count