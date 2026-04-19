def digitSum(s: str) -> int:
    total = 0
    for ch in s:
        if ch.isupper():
            total += ord(ch)
    return total