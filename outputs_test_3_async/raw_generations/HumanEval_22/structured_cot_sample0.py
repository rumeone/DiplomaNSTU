from typing import List


def filter_integers(values: List[str]) -> List[int]:
    """
    Filter given list of string values only for integers.

    Example:
        >>> filter_integers(['10', ' 123 ', '5.0', three', 'abc', '{}'])
        [10]
    """
    result = []
    for value in values:
        try:
            # Strip whitespace and attempt to parse as integer
            parsed = int(value.strip())
            result.append(parsed)
        except ValueError:
            # Skip non-integer strings
            continue
    return result