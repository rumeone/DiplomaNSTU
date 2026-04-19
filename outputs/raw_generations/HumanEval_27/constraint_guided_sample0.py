def flip_case(string: str) -> str:
    result_chars = []
    for ch in string:
        if ch.islower():
            result_chars.append(ch.upper())
        elif ch.isupper():
            result_chars.append(ch.lower())
        else:
            result_chars.append(ch)
    return ''.join(result_chars)