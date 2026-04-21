def vowels_count(s: str) -> int:
    """
    Write a function vowels_count which takes a string representing
    a single word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word. Note, trailing
    special characters or spaces do not matter, however, numbers and letters do effect
    whether 'y' is considered to be the last letter of the word.
    """
    cleaned = s.strip().lower()
    if not cleaned:
        return 0
    count = sum(1 for c in cleaned if c in "aeiou")
    if cleaned.endswith("y") and not cleaned[-2:].isalnum() or cleaned[-1] == "y":
        # y at end after stripping trailing non-letters, but only if last letter
        # is actually y (i.e. no trailing non-letters after y)
        if cleaned.rstrip("!@#$%^&*()_+-=[]{}|;':\",./<>?`~ ").endswith("y"):
            count += 1
    elif cleaned.endswith("y"):
        count += 1
    return count