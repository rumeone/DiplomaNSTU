from typing import List


def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Example:
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)