from typing import List


def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings: A list of strings to concatenate.

    Returns:
        A single string formed by concatenating all input strings.

    Example:
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)