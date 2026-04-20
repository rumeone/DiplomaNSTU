def count_distinct_characters(string: str) -> int:
    """
    Find out how many distinct characters (regardless of case) are in the string.
    """
    if not isinstance(string, str):
        return 0
    distinct_chars = {char.lower() for char in string}
    return len(distinct_chars)