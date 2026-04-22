from typing import List


def filter_integers(values: List[str]) -> List[int]:
    """
    Filter given list of string values only for integers.

    Example:
        >>> filter_integers(['10', ' 123 ', '5.0', three', 'abc', '{}'])
        [10]
    """
    result = []
    for val in values:
        stripped = val.strip()
        if stripped and stripped.isdigit():
            result.append(int(stripped))
        elif stripped.startswith('-') and stripped[1:].isdigit():
            result.append(int(stripped))
    return result