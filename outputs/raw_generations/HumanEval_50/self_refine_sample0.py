def decode_shift(s: str) -> str:
    """
    Decodes a string where each letter was shifted forward by 5 positions.
    To decode, shift each letter backward by 5 positions in the alphabet.
    """
    result = []
    for char in s:
        if 'a' <= char <= 'z':
            decoded_char = chr((ord(char) - ord('a') - 5) % 26 + ord('a'))
            result.append(decoded_char)
        else:
            result.append(char)
    return ''.join(result)