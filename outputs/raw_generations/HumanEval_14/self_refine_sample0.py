from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    
    return [string[:i] for i in range(1, len(string) + 1)]