from typing import List


def filter_integers(values: List[str]) -> List[int]:
    """
    Filter given list of string values only for integers.

    Example:
        >>> filter_integers(['10', ' 123 ', '5.0', 'three', 'abc', '{}'])
        [10, 123]
    """
    integers = []
    for value in values:
        stripped_value = value.strip()
        if stripped_value.isdigit():
            integers.append(int(stripped_value))
    return integers