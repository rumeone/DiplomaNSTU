def digitSum(s: str) -> int:
    total = 0
    for c in s:
        if c.isupper():
            total += ord(c)
    return total