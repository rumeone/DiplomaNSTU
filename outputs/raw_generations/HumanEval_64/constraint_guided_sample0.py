def vowels_count(s: str) -> int:
    vowels = set("aeiou")
    s_lower = s.lower()
    count = 0
    for i, ch in enumerate(s_lower):
        if ch in vowels:
            count += 1
        elif ch == 'y' and i == len(s_lower) - 1:
            count += 1
    return count