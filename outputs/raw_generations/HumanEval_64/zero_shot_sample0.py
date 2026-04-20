def vowels_count(s: str) -> int:
    vowels = set('aeiou')
    s = s.strip()
    if not s:
        return 0
    count = 0
    for i, ch in enumerate(s):
        ch_lower = ch.lower()
        if ch_lower in vowels:
            count += 1
        elif ch_lower == 'y' and i == len(s) - 1 and s[-1].isalpha():
            count += 1
    return count