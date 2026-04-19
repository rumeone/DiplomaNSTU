def filter_integers(values: List[str]) -> List[int]:
    result = []
    for value in values:
        stripped = value.strip()
        if stripped.startswith('-'):
            numeric_part = stripped[1:]
            if numeric_part.isdigit():
                result.append(int(stripped))
        else:
            if stripped.isdigit():
                result.append(int(stripped))
    return result