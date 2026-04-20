def count_distinct_characters(string: str) -> int:
    """
    Find out how many distinct characters (regardless of case) are in the string.
    """
    # Convert all characters to lowercase to ignore case, then use set to get distinct characters
    distinct_chars = {char.lower() for char in string}
    return len(distinct_chars)