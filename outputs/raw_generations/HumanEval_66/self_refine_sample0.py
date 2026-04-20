def digitSum(s: str) -> int:
    """
    Take a string as input and return the sum of the the ASCII codes from upper characters only.
    """
    if not isinstance(s, str):
        return 0
    total = 0
    for char in s:
        if char.isupper():
            total += ord(char)
    return total