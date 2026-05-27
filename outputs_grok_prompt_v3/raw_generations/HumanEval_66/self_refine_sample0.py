"""Utility for summing ASCII values of uppercase characters."""

def digitSum(s: str) -> int:
    """
    Take a string as input and return the sum of the the ASCII codes from upper characters only.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    ascii_sum = 0
    for char in s:
        if char.isupper():
            ascii_sum += ord(char)
    return ascii_sum