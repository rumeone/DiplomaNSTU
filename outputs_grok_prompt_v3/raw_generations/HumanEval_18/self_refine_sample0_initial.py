"""Utility for counting substring occurrences with overlap support."""

def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Example:
        >>> how_many_times('aaaa', 'aa')
        3
    """
    if not substring:
        return 0
    count = 0
    current_position = 0
    while True:
        current_position = string.find(substring, current_position)
        if current_position == -1:
            break
        count += 1
        current_position += 1
    return count