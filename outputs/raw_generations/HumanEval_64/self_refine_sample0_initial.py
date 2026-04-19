def vowels_count(s: str) -> int:
    vowels = set('aeiou')
    count = 0
    s_lower = s.lower()
    length = len(s_lower)
    
    for i, ch in enumerate(s_lower):
        if ch in vowels:
            count += 1
        elif ch == 'y' and i == length - 1:
            count += 1
    return count