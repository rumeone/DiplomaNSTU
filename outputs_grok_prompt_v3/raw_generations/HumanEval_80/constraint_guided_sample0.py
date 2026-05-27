"""Utility to determine if strings are happy."""

def is_happy(s: str) -> bool:
    """
    Check if the string is happy or not:
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.

    Examples:
      is_happy(a) => False
      is_happy(aa) => False
      is_happy(abcd) => True
      is_happy(aabb) => False
    """
    if len(s) < 3:
        return False
    for index in range(len(s) - 2):
        triplet = s[index:index + 3]
        if len(set(triplet)) != 3:
            return False
    return True