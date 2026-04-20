def vowels_count(s: str) -> int:
    vowels = set('aeiou')
    count = 0
    s_lower = s.lower()
    for i, ch in enumerate(s_lower):
        if ch in vowels:
            count += 1
        elif ch == 'y' and i == len(s) - 1:
            count += 1
    return count