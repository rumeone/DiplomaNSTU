from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Examples:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    if not prefix:
        return strings.copy()

    if not strings:
        return []

    filtered = []
    for string in strings:
        if string.startswith(prefix):
            filtered.append(string)

    return filtered