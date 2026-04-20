def vowels_count(s: str) -> int:
    vowels = set('aeiou')
    s_lower = s.lower()
    count = 0
    length = len(s_lower)

    for i, char in enumerate(s_lower):
        if char in vowels:
            count += 1
        elif char == 'y' and i == length - 1:
            count += 1
    return count