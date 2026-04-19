def digitSum(s: str) -> int:
    """
    Take a string as input and return the sum of the the ASCII codes from upper characters only.
    """
    total = 0
    for ch in s:
        if ch.isupper():
            total += ord(ch)
    return total