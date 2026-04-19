def strlen(string: str) -> int:
    """
    Return the length of the given string.

    Example:
        >>> strlen('abc')
        3
    """
    count = 0
    for _ in string:
        count += 1
    return count