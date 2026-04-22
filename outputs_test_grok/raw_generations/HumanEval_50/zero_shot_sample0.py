def decode_shift(s: str) -> str:
    result = []
    for char in s:
        if 'a' <= char <= 'z':
            # Shift back by 5: (ord(char) - ord('a') - 5) % 26 + ord('a')
            shifted = (ord(char) - ord('a') - 5) % 26 + ord('a')
            result.append(chr(shifted))
        else:
            result.append(char)
    return ''.join(result)