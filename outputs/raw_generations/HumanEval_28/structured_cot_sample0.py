from typing import List


def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Example:
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    result = ""
    for s in strings:
        result += s
    return result