def digitSum(s: str) -> int:
    """
    Take a string as input and return the sum of the ASCII codes from upper characters only.
    """
    total = 0
    for char in s:
        if char.isupper():
            total += ord(char)
    return total