def digitSum(s: str) -> int:
    """
    Take a string as input and return the sum of the the ASCII codes from upper characters only.
    """
    return sum(ord(c) for c in s if c.isupper())