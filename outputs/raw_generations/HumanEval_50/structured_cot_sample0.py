def decode_shift(s: str) -> str:
    result = []
    for ch in s:
        if 'a' <= ch <= 'z':
            shifted = ord(ch) - 5
            if shifted < ord('a'):
                shifted += 26
            result.append(chr(shifted))
        else:
            result.append(ch)
    return ''.join(result)