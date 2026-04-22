def count_distinct_characters(string: str) -> int:
    if not string:
        return 0
    lower_string = string.lower()
    unique_chars = set(lower_string)
    return len(unique_chars)