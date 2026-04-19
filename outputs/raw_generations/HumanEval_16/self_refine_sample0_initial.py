def count_distinct_characters(string: str) -> int:
    """
    Find out how many distinct characters (regardless of case) are in the string.
    """
    distinct_chars = set()
    for char in string:
        distinct_chars.add(char.lower())
    return len(distinct_chars)