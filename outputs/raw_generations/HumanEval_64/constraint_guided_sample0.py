def vowels_count(s: str) -> int:
    vowels = set("aeiou")
    count = 0
    stripped = s.strip()
    if not stripped:
        return 0
    for i, ch in enumerate(stripped):
        lower_ch = ch.lower()
        if lower_ch in vowels:
            count += 1
        elif lower_ch == 'y' and i == len(stripped) - 1:
            count += 1
    return count