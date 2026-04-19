def strlen(string: str) -> int:
    """
    Return the length of the given string.

    Example:
        >>> strlen('abc')
        3
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    return len(string)