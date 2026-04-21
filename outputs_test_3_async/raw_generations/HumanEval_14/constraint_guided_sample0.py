"""Functions for working with string prefixes."""

from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string: The input string to generate prefixes from.

    Returns:
        A list of all prefixes from shortest to longest.

    Examples:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
        >>> all_prefixes('')
        []
        >>> all_prefixes('x')
        ['x']
    """
    if not string:
        return []

    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])

    return prefixes