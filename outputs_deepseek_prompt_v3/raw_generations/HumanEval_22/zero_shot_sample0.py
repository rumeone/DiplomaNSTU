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
        value = value.strip()
        try:
            num = int(value)
            result.append(num)
        except ValueError:
            continue
    return result