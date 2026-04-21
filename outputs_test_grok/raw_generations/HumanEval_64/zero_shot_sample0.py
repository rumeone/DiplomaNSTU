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
    if last_char == 'y' and (cleaned[-1].isalpha() or not any(c.isalpha() for c in cleaned[:-1])):
        if not any(c.isdigit() for c in cleaned[:-1]) and not any(c.isalpha() for c in cleaned[:-1] if c.lower() != 'y'):
            count += 1
        elif cleaned[:-1].strip(' \t\n\r!@#$%^&*()_+-=[]{}|;:,.<>/?`~').endswith('y') or not any(c.isalnum() for c in cleaned[:-1]):
            count += 1
        else:
            if not any(c.isalnum() for c in cleaned[:-1]):
                count += 1
            elif cleaned.rstrip(' \t\n\r!@#$%^&*()_+-=[]{}|;:,.<>/?`~')[-1].lower() == 'y':
                count += 1
    if last_char == 'y':
        prefix = cleaned[:-1].rstrip(' \t\n\r!@#$%^&*()_+-=[]{}|;:,.<>/?`~')
        if not prefix or not any(c.isalnum() for c in prefix):
            count += 1
        elif prefix[-1].isalpha() and prefix[-1].lower() != 'y':
            pass
        elif not any(c.isalpha() or c.isdigit() for c in prefix):
            count += 1
    return count