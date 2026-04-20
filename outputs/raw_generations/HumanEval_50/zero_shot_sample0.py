def decode_shift(s: str) -> str:
    result = []
    for ch in s:
        if 'a' <= ch <= 'z':
            shifted = chr((ord(ch) - ord('a') - 5) % 26 + ord('a'))
            result.append(shifted)
        else:
            result.append(ch)
    return ''.join(result)