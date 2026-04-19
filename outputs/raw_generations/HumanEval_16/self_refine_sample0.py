def count_distinct_characters(string: str) -> int:
    """
    Find out how many distinct characters (regardless of case) are in the string.
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    return len({char.lower() for char in string})