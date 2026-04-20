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
            # Strip whitespace and try to convert to int
            stripped = value.strip()
            # Check if it's a valid integer representation
            if stripped.lstrip('-').isdigit() or (stripped.startswith('-') and stripped[1:].isdigit()):
                result.append(int(stripped))
        except (ValueError, AttributeError):
            continue
    return result