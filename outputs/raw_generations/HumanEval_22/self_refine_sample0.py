from typing import List


def filter_integers(values: List[str]) -> List[int]:
    """
    Filter given list of string values only for integers.
    """
    result = []
    for value in values:
        stripped = value.strip()
        # Check if it's a valid integer (allows negative numbers)
        if stripped.lstrip('-').isdigit() and stripped.count('-') <= 1:
            # Ensure it's not just a minus sign
            if stripped != '-' and (not stripped.startswith('-') or len(stripped) > 1):
                result.append(int(stripped))
    return result