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
    if not isinstance(strings, list):
        raise TypeError("strings must be a list")
    if not isinstance(prefix, str):
        raise TypeError("prefix must be a string")
    
    return [s for s in strings if isinstance(s, str) and s.startswith(prefix)]