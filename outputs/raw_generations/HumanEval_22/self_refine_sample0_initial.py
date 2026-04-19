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
        # Strip whitespace to handle cases like ' 123 '
        stripped = value.strip()
        # Check if string consists only of digits (with optional leading sign)
        if stripped and (stripped.isdigit() or 
                        (stripped[0] in '+-' and stripped[1:].isdigit())):
            result.append(int(stripped))
    return result