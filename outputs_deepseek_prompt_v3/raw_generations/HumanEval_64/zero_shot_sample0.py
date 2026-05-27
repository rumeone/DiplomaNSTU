def vowels_count(s: str) -> int:
    vowels = set('aeiou')
    s = s.strip()
    count = 0
    for i, ch in enumerate(s):
        if ch.lower() in vowels:
            count += 1
        elif ch.lower() == 'y' and i == len(s) - 1:
            count += 1
    return count