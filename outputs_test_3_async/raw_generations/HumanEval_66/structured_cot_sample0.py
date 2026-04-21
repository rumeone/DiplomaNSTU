def digitSum(s: str) -> int:
    """
    Take a string as input and return the sum of the ASCII codes from upper characters only.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    return sum(ord(ch) for ch in s if ch.isupper())