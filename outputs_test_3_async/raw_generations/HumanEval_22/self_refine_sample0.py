"""Filter string values to extract only valid integers."""

from typing import List


def filter_integers(values: List[str]) -> List[int]:
    """
    Filter given list of string values only for integers.

    Example:
        >>> filter_integers(['10', ' 123 ', '5.0', 'three', 'abc', '{}'])
        [10, 123]
    """
    result = []

    for value in values:
        stripped_value = value.strip()

        if not stripped_value:
            continue

        if stripped_value[0] in ('-', '+'):
            if len(stripped_value) == 1:
                continue
            numeric_part = stripped_value[1:]
        else:
            numeric_part = stripped_value

        if numeric_part.isdigit():
            result.append(int(stripped_value))

    return result