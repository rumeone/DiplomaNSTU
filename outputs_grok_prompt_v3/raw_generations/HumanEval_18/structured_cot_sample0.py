"""Count occurrences of a substring, including overlaps."""

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
    idx = 0
    while True:
        idx = string.find(substring, idx)
        if idx == -1:
            break
        count += 1
        idx += 1
    return count