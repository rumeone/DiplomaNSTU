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
    vowels = set('aeiou')
    count = 0
    s_lower = s.lower()
    
    # Process all characters except the last one
    for ch in s_lower[:-1]:
        if ch in vowels:
            count += 1
    
    # Process the last character
    if s_lower:
        last_char = s_lower[-1]
        if last_char in vowels or last_char == 'y':
            count += 1
    
    return count