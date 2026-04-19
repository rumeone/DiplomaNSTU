def is_happy(s: str) -> bool:
    """
    Check if the string is happy or not:
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.
    """
    if len(s) < 3:
        return False

    for i in range(len(s) - 2):
        # Check if three consecutive characters are all different
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
            return False

    return True