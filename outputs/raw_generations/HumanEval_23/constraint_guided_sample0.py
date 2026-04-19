def strlen(string: str) -> int:
    """
    Return the length of the given string.

    Example:
        >>> strlen('abc')
        3
    """
    length = 0
    for _ in string:
        length += 1
    return length