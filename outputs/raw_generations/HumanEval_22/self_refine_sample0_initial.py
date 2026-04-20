from typing import List


def filter_integers(values: List[str]) -> List[int]:
    """
    Filter given list of string values only for integers.
    """
    result = []
    for value in values:
        stripped = value.strip()
        if stripped.isdigit():
            result.append(int(stripped))
    return result