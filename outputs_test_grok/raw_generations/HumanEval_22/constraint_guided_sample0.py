"""Filter strings to extract integer values."""

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
        if (stripped.isdigit() or
                (stripped.startswith(('-', '+')) and stripped[1:].isdigit())):
            try:
                result.append(int(stripped))
            except ValueError:
                # Should not happen with the checks above, but safe
                continue

    return result