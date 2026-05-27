def filter_integers(values: List[str]) -> List[int]:
    result = []
    for v in values:
        try:
            result.append(int(v))
        except ValueError:
            pass
    return result