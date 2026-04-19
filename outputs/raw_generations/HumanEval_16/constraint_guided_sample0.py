def count_distinct_characters(string: str) -> int:
    """
    Find out how many distinct characters (regardless of case) are in the string.
    """
    # Convert all characters to lower case to ignore case differences,
    # then create a set to keep only distinct characters.
    distinct_chars = {char.lower() for char in string}
    return len(distinct_chars)