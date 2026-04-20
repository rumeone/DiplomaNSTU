def vowels_count(s: str) -> int:
    vowels = set('aeiou')
    count = 0
    s_lower = s.lower()
    length = len(s)
    
    for i, ch in enumerate(s_lower):
        if ch in vowels:
            count += 1
        elif ch == 'y' and i == length - 1:
            count += 1
        elif ch == 'y' and i < length - 1:
            next_char = s_lower[i + 1]
            if not next_char.isalpha():
                j = i + 1
                while j < length and not s_lower[j].isalpha():
                    j += 1
                if j == length:
                    count += 1
    
    return count