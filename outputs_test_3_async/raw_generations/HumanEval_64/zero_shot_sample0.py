def vowels_count(s: str) -> int:
    vowels = set('aeiou')
    s = s.strip().lower()
    if not s:
        return 0
    count = 0
    for i, ch in enumerate(s):
        if ch in vowels:
            count += 1
        elif ch == 'y' and i == len(s) - 1 and s[i].isalpha():
            count += 1
    return count