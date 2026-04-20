def decode_shift(s: str) -> str:
    result = []
    for char in s:
        if 'a' <= char <= 'z':
            shifted = chr((ord(char) - ord('a') - 5) % 26 + ord('a'))
            result.append(shifted)
        else:
            result.append(char)
    return ''.join(result)