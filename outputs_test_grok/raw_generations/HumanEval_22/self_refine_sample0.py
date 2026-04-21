from typing import List


def filter_integers(values: List[str]) -> List[int]:
    """
    Filter given list of string values only for integers.

    Example:
        >>> filter_integers(['10', ' 123 ', '5.0', 'three', 'abc', '{}'])
        [10, 123]
    """
    result: List[int] = []

    for value in values:
        stripped = value.strip()
        if not stripped:
            continue

        # Check if the string represents a valid integer
        if stripped[0] in ('-', '+'):
            if len(stripped) == 1:
                continue
            number_part = stripped[1:]
        else:
            number_part = stripped

        if number_part.isdigit():
            result.append(int(stripped))

    return result