def vowels_count(s: str) -> int:
    if not s:
        return 0
    vowels = set('aeiouAEIOU')
    cleaned = s.strip()
    if not cleaned:
        return 0
    count = 0
    for char in cleaned:
        if char.lower() in 'aeiou':
            count += 1
    last_char = cleaned[-1].lower()
    if last_char == 'y':
        if cleaned[-1].isalpha() and (len(cleaned) == 1 or cleaned[-2].isalpha() or not cleaned[-2].isalnum()):
            count += 1
    return count