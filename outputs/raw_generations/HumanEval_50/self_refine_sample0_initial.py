def decode_shift(s: str) -> str:
    """
    Decodes a string where each letter was shifted forward by 5 positions.
    To decode, shift each letter backward by 5 positions in the alphabet.
    """
    result = []
    for char in s:
        if 'a' <= char <= 'z':
            # Shift backward by 5, wrapping around the alphabet
            decoded_char = chr((ord(char) - ord('a') - 5) % 26 + ord('a'))
            result.append(decoded_char)
        else:
            # Non-lowercase letters are kept unchanged (though not expected per spec)
            result.append(char)
    return ''.join(result)