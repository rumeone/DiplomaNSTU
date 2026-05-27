"""Utility for counting substring occurrences allowing overlaps."""

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
    start = 0
    while True:
        pos = string.find(substring, start)
        if pos == -1:
            break
        count += 1
        start = pos + 1
    return count