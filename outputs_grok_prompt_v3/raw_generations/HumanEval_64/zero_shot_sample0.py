def vowels_count(s: str) -> int:
    if not s:
        return 0
    vowels = 'aeiou'
    count = 0
    last_alpha = None
    for char in s:
        c = char.lower()
        if c.isalpha():
            last_alpha = c
            if c in vowels:
                count += 1
    if last_alpha == 'y':
        count += 1
    return count