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
            # Check if it's a valid integer string (no decimal point)
            if stripped.isdigit():
                result.append(int(stripped))
            else:
                # Try direct conversion for cases like negative numbers
                int_val = int(stripped)
                result.append(int_val)
        except ValueError:
            continue
    return result