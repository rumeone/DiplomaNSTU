"""Happy string checker module."""

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
    return len(s) >= 3 and all(len(set(s[i:i+3])) == 3 for i in range(len(s) - 2))