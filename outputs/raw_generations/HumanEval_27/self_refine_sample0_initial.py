def flip_case(string: str) -> str:
    result = []
    for ch in string:
        if ch.islower():
            result.append(ch.upper())
        elif ch.isupper():
            result.append(ch.lower())
        else:
            result.append(ch)
    return ''.join(result)