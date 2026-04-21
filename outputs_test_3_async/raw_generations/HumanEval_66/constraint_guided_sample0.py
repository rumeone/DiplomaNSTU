"""
Module for calculating the sum of ASCII codes of uppercase characters in a string.
"""


def digitSum(s: str) -> int:
    """
    Take a string as input and return the sum of the ASCII codes from uppercase characters only.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    total = 0
    for char in s:
        if char.isupper():
            total += ord(char)
    return total