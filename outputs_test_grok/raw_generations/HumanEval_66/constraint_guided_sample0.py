"""
Module providing a function to calculate the sum of ASCII values
for uppercase characters in a given string.
"""


def digitSum(s: str) -> int:
    """
    Take a string as input and return the sum of the ASCII codes
    from upper characters only.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    if not s:
        return 0

    total = 0
    for char in s:
        if char.isupper():
            total += ord(char)

    return total